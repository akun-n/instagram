document.addEventListener('DOMContentLoaded', () => {
    const screens = document.querySelectorAll('.screen');
    let currentIndex = 0;

    function showNextScreen() {
        screens[currentIndex].classList.remove('active');
        screens[currentIndex].classList.remove('initial'); // Remove the initial class after the first transition
        currentIndex = (currentIndex + 1) % screens.length;
        screens[currentIndex].classList.add('active');
    }

    // Show the first screen initially without transition
    screens[currentIndex].classList.add('initial');

    // Change screen every 5 seconds (5000 milliseconds)
    setInterval(showNextScreen, 5000);
});
