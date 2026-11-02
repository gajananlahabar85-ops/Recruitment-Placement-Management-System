
document.addEventListener('DOMContentLoaded', function () {

  // Login form
  document.querySelectorAll('form').forEach(function(form) {

    if (form.id === 'loginForm') {
      form.addEventListener('submit', function(e) {
        e.preventDefault();
        window.location.href = '/dashboard.html';
      });
      return;
    }

    // Filter form
    if (form.classList.contains('filters')) {
      form.addEventListener('submit', function(e) {
        e.preventDefault();
        loadCandidates();
      });
      return;
    }

    // Candidate form: Flask backend handles saving
    if (form.classList.contains('demo-form')) {
      return;
    }

    // Other prototype forms
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      alert('This feature is not connected yet.');
    });
  });

  // Load candidates from Flask API
  loadCandidates();

  function loadCandidates() {
    const table = document.querySelector('table');
    if (!table) return;

    const tbody = table.querySelector('tbody');
    if (!tbody) return;

    fetch('/api/candidates')
      .then(response => {
        if (!response.ok) throw new Error('Could not load candidates');
        return response.json();
      })
      .then(candidates => {
        tbody.innerHTML = '';

        if (candidates.length === 0) {
          tbody.innerHTML =
            '<tr><td colspan="8">No candidates found</td></tr>';
          return;
        }

        candidates.forEach(candidate => {
          const row = document.createElement('tr');

          [
  candidate.id,
  candidate.full_name,
  candidate.email,
  candidate.technology,
  candidate.qualification,
  candidate.passing_year,
  candidate.status
]
          .forEach(value => {
            const actionCell = document.createElement('td');

const deleteBtn = document.createElement('button');
deleteBtn.textContent = 'Delete';

deleteBtn.onclick = async function() {
  if (!confirm('Delete this candidate?')) return;

  const response = await fetch('/api/candidates/' + candidate.id, {
    method: 'DELETE'
  });

  if (response.ok) {
    loadCandidates();
  } else {
    alert('Delete failed');
  }
};

actionCell.appendChild(deleteBtn);
row.appendChild(actionCell);

  // Prototype links
  document.querySelectorAll('a[href="#"]').forEach(function(a) {
    a.addEventListener('click', function(e) {
      if (!a.getAttribute('onclick')) {
        e.preventDefault();
        alert('This is a prototype-only action.');
      }
    });
  });

});
