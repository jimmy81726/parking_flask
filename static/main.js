function updateClock() {
    const now = new Date();
    const timeString = now.toLocaleTimeString();
    document.getElementById('clock').textContent = timeString;
};

window.onload = function () {
    updateClock();
    setInterval(updateClock, 1000);

};