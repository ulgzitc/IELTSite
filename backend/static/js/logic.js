function showView(viewId) {
    // Hide all views
    document.querySelectorAll('.view-section').forEach(el => el.classList.add('hidden'));
    // Show requested view
    const target = document.getElementById('view-' + viewId);
    if (target) {
        target.classList.remove('hidden');
        // Scroll to top
        window.scrollTo(0,0);
    }
}

// Start at home
document.addEventListener('DOMContentLoaded', () => {
    showView('home');
});