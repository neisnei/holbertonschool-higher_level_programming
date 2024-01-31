// Script that toggles class (red/green) on header when clicking #toggle_header

const header = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');

toggleHeader.onclick = () => {
  header.classList.toggle('green', !header.classList.contains('green'));
  header.classList.toggle('red', !header.classList.contains('red'));
};
