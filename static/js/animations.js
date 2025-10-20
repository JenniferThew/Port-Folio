document.addEventListener('DOMContentLoaded', () => {
    // Select all elements that have an animation class defined in animated.css
    const animatedElements = document.querySelectorAll(
        '.fade-in-up, .fade-in-left, .fade-in-right, .scale-in'
    );

    // Options for the Intersection Observer
    const observerOptions = {
        root: null, // viewport is the root
        rootMargin: '0px',
        threshold: 0.1 // Trigger when 10% of the item is visible
    };

    // Callback function to execute when targets intersect
    const observerCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add the .animate class to trigger the transition
                entry.target.classList.add('animate');
                // Stop observing once animated
                observer.unobserve(entry.target);
            }
        });
    };

    // Create the Intersection Observer
    const observer = new IntersectionObserver(observerCallback, observerOptions);

    // Start observing all targeted elements
    animatedElements.forEach(element => {
        observer.observe(element);
    });
});