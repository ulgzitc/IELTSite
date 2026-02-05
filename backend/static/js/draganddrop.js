let dragged = null;
document.querySelectorAll('.opinion').forEach(item => {
    item.addEventListener('dragstart', () => dragged = item);
});
// Food trend dropzones
document.querySelectorAll('.dropzone').forEach(zone => {
    zone.addEventListener('dragover', e => {
        e.preventDefault();
        zone.classList.add('over');
    });
    zone.addEventListener('dragleave', () => {
        zone.classList.remove('over');
    });
    zone.addEventListener('drop', e => {
        e.preventDefault();
        zone.classList.remove('over');
        // If zone already has an opinion → return it
        const existing = zone.querySelector('.opinion');
        if (existing) {
            document.getElementById('opinions-zone').appendChild(existing);
        }
        zone.appendChild(dragged);
        // Remove old hidden input
        const oldInput = zone.querySelector('input');
        if (oldInput) oldInput.remove();
        // Add new hidden input
        const qid = zone.closest('.trend').dataset.question;
        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'question_' + qid;
        input.value = dragged.dataset.value;
        zone.appendChild(input);
    });
});
// Opinions return zone
const opinionsZone = document.getElementById('opinions-zone');
opinionsZone.addEventListener('dragover', e => {
    e.preventDefault();
    opinionsZone.classList.add('over');
});
opinionsZone.addEventListener('dragleave', () => {
    opinionsZone.classList.remove('over');
});
opinionsZone.addEventListener('drop', e => {
    e.preventDefault();
    opinionsZone.classList.remove('over');
    // Remove hidden input if returning
    const parentZone = dragged.parentElement;
    if (parentZone.classList.contains('dropzone')) {
        const input = parentZone.querySelector('input');
        if (input) input.remove();
    }
    opinionsZone.appendChild(dragged);
});
