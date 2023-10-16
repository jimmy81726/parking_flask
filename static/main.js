function updateClock() {
    const now = new Date();
    const timeString = now.toLocaleTimeString();
    document.getElementById('clock').textContent = '現在時間 : ' + timeString;
};

window.onload = function () {
    updateClock();
    setInterval(updateClock, 1000);

};

document.getElementById('sort').addEventListener('change', function () {
    if (this.value !== '') {
        document.getElementById('sorting-form').submit()
    }
});