document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Toggle
    const mobileMenu = document.getElementById('mobile-menu');
    const navLinks = document.getElementById('nav-links');

    if (mobileMenu && navLinks) {
        mobileMenu.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // 2. Automatic AOS Animation Injection
    // Add fade-up to all cards, with a staggered delay based on their index in a grid
    const grids = document.querySelectorAll('.grid');
    grids.forEach(grid => {
        const cards = grid.querySelectorAll('.card');
        cards.forEach((card, index) => {
            card.setAttribute('data-aos', 'fade-up');
            card.setAttribute('data-aos-delay', (index * 100).toString());
        });
        
        // Also animate images inside grids
        const images = grid.querySelectorAll('img:not(.card img)');
        images.forEach(img => {
            if(!img.closest('.navbar')) {
                img.setAttribute('data-aos', 'zoom-in');
                img.setAttribute('data-aos-duration', '800');
            }
        });
    });

    // Animate all major headings
    const headings = document.querySelectorAll('h2');
    headings.forEach(h2 => {
        if (!h2.hasAttribute('data-aos') && !h2.closest('.navbar')) {
            h2.setAttribute('data-aos', 'fade-right');
        }
    });

    // Animate buttons
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(btn => {
        if (!btn.hasAttribute('data-aos') && !btn.closest('.navbar')) {
            btn.setAttribute('data-aos', 'zoom-in');
            btn.setAttribute('data-aos-offset', '50');
        }
    });

    // 3. Initialize AOS Library
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            once: true, // whether animation should happen only once
            offset: 100, // offset (in px) from the original trigger point
            easing: 'ease-out-cubic'
        });
    }
});
