const errorElement = document.getElementById('error');
const button = document.querySelector('button');

// Verify elements exist before adding event listener
if (!errorElement || !button) {
    console.error('Required elements not found');
} else {
    button.addEventListener('click', () => {
        errorElement.textContent = 'An error occurred, please try again later.';
        errorElement.style.color = 'red';
    });
}