function saveToLocalQueue(data) {
    let queue = JSON.parse(localStorage.getItem("submissionQueue")) || [];
    queue.push(data);
    localStorage.setItem("submissionQueue", JSON.stringify(queue));
}

function tryResubmitQueue() {
    if (navigator.onLine) {
        let queue = JSON.parse(localStorage.getItem("submissionQueue")) || [];
        while (queue.length > 0) {
            let data = queue.shift();
            fetch('http://127.0.0.1:5000/api/submit/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });
        }
        localStorage.setItem("submissionQueue", JSON.stringify([]));
    }
}

window.addEventListener('online', tryResubmitQueue);

// 🚀 MAIN FORM SUBMIT LOGIC
document.getElementById('enumeratorForm').addEventListener('submit', function(e) {
    e.preventDefault();

    navigator.geolocation.getCurrentPosition(function(position) {
        const data = {
            latitude: position.coords.latitude,
            longitude: position.coords.longitude,
            enumeratorId: document.getElementById('enumeratorId').value,
            enumeratorName: document.getElementById('enumeratorName').value,
            regionName: document.getElementById('regionName').value,
            totalRespondents: document.getElementById('totalRespondents').value,
            supervisorName: document.getElementById('supervisorName').value,
            supervisorSignature: document.getElementById('supervisorSignature').value,
            verificationDate: document.getElementById('verificationDate').value,
            collectionDate: document.getElementById('collectionDate').value,
            surveyDate: document.getElementById('surveyDate').value,
            constituency: document.getElementById('constituency').value,
            respondents: Array.from(document.querySelectorAll('input[name="respondentName[]"]')).map((input, index) => ({
                name: input.value,
                gender: document.querySelectorAll('select[name="gender[]"]')[index].value,
                age: document.querySelectorAll('input[name="age[]"]')[index].value,
                contact: document.querySelectorAll('input[name="contact[]"]')[index].value,
                signature: document.querySelectorAll('input[name="signature[]"]')[index].value
            }))
        };

        // 🌐 Offline logic
        if (!navigator.onLine) {
            saveToLocalQueue(data);
            alert("You're offline. Data has been saved and will auto-submit once you're online.");
        } else {
            fetch('http://127.0.0.1:5000/api/submit/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                alert("Form submitted successfully!");
                console.log(data);
            })
            .catch(error => {
                alert("Submission failed.");
                console.error(error);
            });
        }
    }, function(error) {
        alert("Geolocation failed: " + error.message);
    });
});
