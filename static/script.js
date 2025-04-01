document.addEventListener("DOMContentLoaded", () => {
    const startCameraBtn = document.getElementById("startCamera");
    const captureBtn = document.getElementById("capture");
    const video = document.getElementById("video");
    const canvas = document.getElementById("canvas");
    const resultDiv = document.getElementById("result");

    let stream;

    // Start Camera
    startCameraBtn.addEventListener("click", async () => {
        try {
            stream = await navigator.mediaDevices.getUserMedia({ video: true });
            video.srcObject = stream;
            video.classList.remove("hidden");
            captureBtn.classList.remove("hidden");
            startCameraBtn.classList.add("hidden");
        } catch (error) {
            console.error("Error accessing the camera:", error);
            resultDiv.textContent = "⚠️ Camera access denied.";
        }
    });

    // Capture Gesture
    captureBtn.addEventListener("click", () => {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const ctx = canvas.getContext("2d");
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

        const imageData = canvas.toDataURL("image/png");

        resultDiv.textContent = "🔍 Processing gesture...";

        fetch("/detect", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ image: imageData })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                handleGestureAction(data);
            } else {
                resultDiv.textContent = "⚠️ No gesture detected.";
            }
        })
        .catch(error => {
            console.error("Error:", error);
            resultDiv.textContent = "❌ Error processing gesture.";
        });
    });

    // Handle Gesture Actions
    function handleGestureAction(data) {
        console.log("Gesture Action:", data);
        resultDiv.textContent = data.message;

        // Open URL if present
        if (data.url) {
            setTimeout(() => {
                console.log("Opening:", data.url);
                window.open(data.url, "_blank");
            }, 500);
        }

        // Fetch and display weather if the action is to fetch weather
        if (data.message.includes("Fetch Weather")) {
            fetchWeather();
        }
    }

    // Fetch the current location of the user
    function fetchWeather() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(async function (position) {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;

                try {
                    const response = await fetch(`/weather?lat=${lat}&lon=${lon}`);
                    const data = await response.json();
                    if (data.weather) {
                        resultDiv.textContent = `Weather: ${data.weather}`;
                    } else {
                        resultDiv.textContent = "⚠️ Error fetching weather.";
                    }
                } catch (error) {
                    console.error("Error fetching weather:", error);
                    resultDiv.textContent = "⚠️ Error fetching weather.";
                }
            }, function (error) {
                console.error("Error getting location:", error);
                resultDiv.textContent = "⚠️ Unable to get location.";
            });
        } else {
            resultDiv.textContent = "⚠️ Geolocation is not supported by this browser.";
        }
    }

    // Stop Camera    
    function stopCamera() {
        if (stream) {
            stream.getTracks().forEach(track => track.stop());
            video.srcObject = null;
            video.classList.add("hidden");
            captureBtn.classList.add("hidden");
            startCameraBtn.classList.remove("hidden");
        }
    }
});
