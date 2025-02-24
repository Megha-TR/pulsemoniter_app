const ctx = document.getElementById('pulseChart').getContext('2d');
const pulseChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Pulse (BPM)',
            data: [],
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    }
});

async function fetchPulse() {
    const response = await fetch('/pulse');
    const data = await response.json();
    const pulse = data.pulse;

    if (pulse) {
        const currentTime = new Date().toLocaleTimeString();
        pulseChart.data.labels.push(currentTime);
        pulseChart.data.datasets[0].data.push(pulse);
        pulseChart.update();
    }
}

setInterval(fetchPulse, 1000);
