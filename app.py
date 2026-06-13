from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from werkzeug.security import check_password_hash
import database

app = Flask(__name__)
app.secret_key = 'super_secret_key_change_in_production'

# Initialize database
database.init_db()

# --- PUBLIC ROUTES ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/programmes')
def programmes():
    return render_template('programmes.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# --- API ROUTES ---
@app.route('/api/applications', methods=['POST'])
def submit_application():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    programme = data.get('programme')
    message = data.get('message', '')
    
    if not all([name, email, phone, programme]):
        return jsonify({'error': 'All required fields must be filled.'}), 400
        
    try:
        conn = database.get_db()
        c = conn.cursor()
        c.execute('''
            INSERT INTO applications (name, email, phone, programme, message)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, email, phone, programme, message))
        conn.commit()
        conn.close()
        return jsonify({'success': 'Application submitted successfully.'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --- ADMIN ROUTES ---
@app.route('/admin')
@app.route('/admin/login')
def admin_login():
    if 'admin_logged_in' in session:
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_login.html')

@app.route('/api/admin/login', methods=['POST'])
def handle_admin_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    conn = database.get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM admins WHERE username = ?', (username,))
    admin = c.fetchone()
    conn.close()
    
    if admin and check_password_hash(admin['password_hash'], password):
        session['admin_logged_in'] = True
        return jsonify({'success': True}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin_logged_in' not in session:
        return redirect(url_for('admin_login'))
        
    conn = database.get_db()
    c = conn.cursor()
    c.execute('SELECT * FROM applications ORDER BY created_at DESC')
    applications = c.fetchall()
    conn.close()
    
    return render_template('admin_dashboard.html', applications=applications)

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

if __name__ == '__main__':
    app.run(debug=True, port=3000)
