const app = {
    data: {
        currentTestType: 'reading', // reading, listening, writing, speaking
        tests: [
            { id: 1, type: 'reading', title: 'Cambridge 19 - Test 1', category: 'Academic', duration: '60m' },
            { id: 2, type: 'reading', title: 'Cambridge 19 - Test 2', category: 'Academic', duration: '60m' },
            { id: 3, type: 'listening', title: 'Listening Vol 4 - Test 1', category: 'General', duration: '30m' },
            { id: 4, type: 'writing', title: 'Task 2: Education', category: 'Academic', duration: '40m' },
            { id: 5, type: 'speaking', title: 'Part 2 Cue Card: Hobbies', category: 'All', duration: '15m' },
        ]
    },
    router: {
        navigate: function(viewId, param = null) {
            // Hide all views
            document.querySelectorAll('.page-view').forEach(el => {
                el.classList.add('hidden');
                el.classList.remove('block');
            });
            // Handle params (like context data in Django)
            if (viewId === 'list' && param) {
                app.data.currentTestType = param;
                app.renderer.renderList(param);
            }
            if (viewId === 'exam') {
                app.renderer.setupExam(app.data.currentTestType);
            }
            // Show target view
            const target = document.getElementById(`view-${viewId}`);
            if(target) {
                target.classList.remove('hidden');
                target.classList.add('block');
                window.scrollTo(0,0);
            }
        }
    },
    renderer: {
        // Mimics Django ListView
        renderList: function(type) {
            document.getElementById('list-title').textContent = type.charAt(0).toUpperCase() + type.slice(1) + " Tests Library";
            
            const grid = document.getElementById('test-grid');
            grid.innerHTML = ''; // Clear
            // Filter dummy data
            const filtered = app.data.tests.filter(t => t.type === type || t.type === 'all');
            
            // Fallback if no specific dummy data
            const items = filtered.length ? filtered : app.data.tests.slice(0,3); 
            items.forEach(test => {
                const colorClass = type === 'reading' ? 'blue' : (type === 'listening' ? 'red' : (type === 'writing' ? 'yellow' : 'green'));
                const html = `
                    <div class="bg-white rounded-lg shadow-sm hover:shadow-md transition border border-gray-100 flex flex-col">
                        <div class="p-6 flex-grow">
                            <div class="flex justify-between items-start mb-4">
                                <span class="px-2 py-1 bg-${colorClass}-100 text-${colorClass}-800 text-xs rounded font-bold uppercase">${test.category}</span>
                                <span class="text-gray-400 text-xs"><i class="fa-regular fa-clock"></i> ${test.duration}</span>
                            </div>
                            <h3 class="font-bold text-gray-800 text-lg mb-2">${test.title}</h3>
                            <p class="text-gray-500 text-sm">Real exam simulation with instant band score evaluation.</p>
                        </div>
                        <div class="p-4 border-t border-gray-50 bg-gray-50 rounded-b-lg">
                            <button onclick="app.router.navigate('exam')" class="w-full bg-white border border-${colorClass}-500 text-${colorClass}-600 font-bold py-2 rounded hover:bg-${colorClass}-50 transition">
                                Take Test
                            </button>
                        </div>
                    </div>
                `;
                grid.innerHTML += html;
            });
        },
        // Sets up the Exam Interface based on type (Reading vs Listening vs Writing)
        setupExam: function(type) {
            const leftPane = document.getElementById('pane-left');
            const rightPane = document.getElementById('pane-right');
            
            // Reset visibility
            document.getElementById('content-reading').classList.add('hidden');
            document.getElementById('content-writing').classList.add('hidden');
            document.getElementById('content-speaking').classList.add('hidden');
            document.getElementById('inputs-standard').classList.add('hidden');
            document.getElementById('inputs-writing').classList.add('hidden');
            document.getElementById('exam-audio-player').classList.add('hidden');
            // Reset widths (Writing/Speaking might need different layout)
            leftPane.className = "w-1/2 overflow-y-auto test-scroll p-8 border-r bg-white";
            rightPane.className = "w-1/2 overflow-y-auto test-scroll bg-gray-50 p-8";
            if (type === 'reading') {
                document.getElementById('content-reading').classList.remove('hidden');
                document.getElementById('inputs-standard').classList.remove('hidden');
                document.getElementById('exam-header-title').textContent = "Reading Practice Test";
            } 
            else if (type === 'listening') {
                document.getElementById('exam-audio-player').classList.remove('hidden');
                document.getElementById('inputs-standard').classList.remove('hidden');
                // Listening usually doesn't have a text passage on left, maybe questions on both sides or map on left
                // For demo, we keep standard input on right, map placeholder on left
                document.getElementById('content-reading').classList.remove('hidden'); 
                document.getElementById('exam-header-title').textContent = "Listening Practice Test";
            }
            else if (type === 'writing') {
                document.getElementById('content-writing').classList.remove('hidden');
                document.getElementById('inputs-writing').classList.remove('hidden');
                document.getElementById('exam-header-title').textContent = "Writing Practice Test";
            }
            else if (type === 'speaking') {
                // Speaking is usually centered prompt
                leftPane.className = "w-full overflow-y-auto test-scroll p-8 bg-white flex flex-col items-center justify-center";
                rightPane.className = "hidden";
                document.getElementById('content-speaking').classList.remove('hidden');
                document.getElementById('exam-header-title').textContent = "Speaking Practice Test";
            }
        }
    },
    modal: {
        open: function(id) {
            document.getElementById(`modal-${id}`).classList.remove('hidden');
        },
        close: function() {
            document.querySelectorAll('[id^="modal-"]').forEach(el => el.classList.add('hidden'));
        }
    }
};
// Init
document.addEventListener('DOMContentLoaded', () => {
    app.router.navigate('home');
});
