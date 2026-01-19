const app = {
    // Simple Router to simulate Django pages
    
    router: {
        navigate: function(viewId) {
            // Hide all views
            document.querySelectorAll('.view-section').forEach(el => {
                el.classList.add('hidden');
                el.classList.remove('block');
            });
            
            // Show target view
            const target = document.getElementById(`view-${viewId}`);
            if(target) {
                target.classList.remove('hidden');
                target.classList.add('block');
                window.scrollTo(0,0);
            }
            // Special logic: Toggle Main Nav based on view (Exam view usually hides standard nav)
            const nav = document.querySelector('nav');
            const footer = document.querySelector('footer');
            
            if (viewId === 'exam') {
                nav.style.display = 'none';
                footer.style.display = 'none';
                // Start timer if entering exam
                app.testEngine.startTimer();
            } else {
                nav.style.display = 'block';
                footer.style.display = 'block';
            }
        }
    },
    
    // Test Interface Logic
    testEngine: {
        timerInterval: null,
        timeLeft: 3600, // 60 minutes in seconds
        startTimer: function() {
            if (this.timerInterval) clearInterval(this.timerInterval);
            
            const timerEl = document.getElementById('exam-timer');
            this.timeLeft = 3600;
            this.timerInterval = setInterval(() => {
                this.timeLeft--;
                
                const minutes = Math.floor(this.timeLeft / 60);
                const seconds = this.timeLeft % 60;
                
                timerEl.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
                if (this.timeLeft <= 0) {
                    this.finishTest();
                }
            }, 1000);
        },
        markAnswered: function(qNum) {
            const btn = document.getElementById(`nav-btn-${qNum}`);
            if (btn) {
                btn.classList.add('answered');
            }
        },
        scrollToQuestion: function(qNum) {
            // Highlight nav button
            document.querySelectorAll('.q-btn').forEach(b => b.classList.remove('active'));
            const btn = document.getElementById(`nav-btn-${qNum}`);
            if (btn) btn.classList.add('active');
            // Scroll to actual question
            const qEl = document.getElementById(`q-container-${qNum}`);
            if (qEl) {
                qEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        },
        finishTest: function() {
            clearInterval(this.timerInterval);
            if(confirm("Are you sure you want to submit?")) {
                // In Django, this would be a POST request form submission
                app.router.navigate('result');
            }
        }
    }
};

// Initialize Home
document.addEventListener('DOMContentLoaded', () => {
    app.router.navigate('home');
});