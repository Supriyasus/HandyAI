document.addEventListener("DOMContentLoaded", () => {
    const startCameraBtn = document.getElementById("startCamera");
    const captureBtn = document.getElementById("capture");
    const video = document.getElementById("video");
    const canvas = document.getElementById("canvas");
    const resultDiv = document.getElementById("result");

    let stream;

    // 🎥 Start Camera
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

    // 📸 Capture Gesture
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

    // 🎭 Handle Gesture Actions
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
    }
    // 🚫 Stop Camera    
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
