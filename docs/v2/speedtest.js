async function downloadFile(url, size) {
    const startTime = performance.now();
    // Add cache-busting query parameter
    url += (url.includes('?') ? '&' : '?') + 'cache-bust=' + Date.now();
    const response = await fetch(url);
    const blob = await response.blob();
    const endTime = performance.now();
    const duration = (endTime - startTime) / 1000; // duration in seconds
    const bitsLoaded = size * 8; // size in bits
    const speedBps = bitsLoaded / duration; // speed in bits per second
    return speedBps / (1024 * 1024); // speed in Mbps
}

async function startTest() {
    const speedElement = document.getElementById('speed');
    const testFiles = [
        { url: 'https://waste-bandwidth-webpage.chooyijie.com/testfile1', size: 1 * 1024 * 1024 }, // 1MB
        { url: 'https://waste-bandwidth-webpage.chooyijie.com/testfile2', size: 2 * 1024 * 1024 }, // 2MB
        { url: 'https://waste-bandwidth-webpage.chooyijie.com/testfile5', size: 5 * 1024 * 1024 }, // 5MB
        { url: 'https://waste-bandwidth-webpage.chooyijie.com/testfile10', size: 10 * 1024 * 1024 }, // 10MB
        { url: 'https://waste-bandwidth-webpage.chooyijie.com/testfile20', size: 20 * 1024 * 1024 }, // 20MB

    ];
    
    let totalSpeed = 0;
    for (const file of testFiles) {
        const speed = await downloadFile(file.url, file.size);
        totalSpeed += speed;
    }
    
    const averageSpeed = totalSpeed / testFiles.length;
    speedElement.textContent = `${averageSpeed.toFixed(2)} Mbps`;
}
