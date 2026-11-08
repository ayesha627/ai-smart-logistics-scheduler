document.addEventListener('DOMContentLoaded', () => {
    // Sidebar toggle functionality
    const menuToggle = document.getElementById('menu-toggle');
    const wrapper = document.getElementById('wrapper');
    
    if (menuToggle) {
        menuToggle.addEventListener('click', (e) => {
            e.preventDefault();
            wrapper.classList.toggle('toggled');
        });
    }

    // Initial GSAP Animations
    if (typeof gsap !== 'undefined') {
        // Animate Sidebar
        gsap.from("#sidebar-wrapper", {
            x: -250,
            duration: 0.8,
            ease: "power3.out"
        });

        // Animate Top Navbar
        gsap.from(".navbar", {
            y: -50,
            opacity: 0,
            duration: 0.8,
            delay: 0.2,
            ease: "power3.out"
        });

        // Animate Main Content Cards (using a class that will be added to cards)
        gsap.from(".glass-card", {
            y: 30,
            opacity: 0,
            duration: 0.8,
            stagger: 0.1,
            delay: 0.4,
            ease: "back.out(1.7)"
        });
    }
});
