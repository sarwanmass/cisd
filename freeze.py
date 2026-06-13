from flask_frozen import Freezer
from app import app

app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

@freezer.register_generator
def home():
    yield {}
    
@freezer.register_generator
def about():
    yield {}
    
@freezer.register_generator
def programmes():
    yield {}
    
@freezer.register_generator
def research():
    yield {}

@freezer.register_generator
def gallery():
    yield {}

@freezer.register_generator
def join():
    yield {}

@freezer.register_generator
def contact():
    yield {}

if __name__ == '__main__':
    freezer.freeze()
    print("Static site successfully generated in 'docs/' folder!")
