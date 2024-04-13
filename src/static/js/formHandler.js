document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('form').addEventListener('submit', function (e) {
        e.preventDefault();

        const form = document.getElementById('form');
        const formData = new FormData(form);

        const jsonData = Array.from(formData.entries()).reduce((json, [key, value]) => {
            json[key] = value;
            return json;
        }, {});

        fetch(form.action, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(jsonData)
        })

            .then(response => {
                console.log(response.status);

                if (!response.ok) {
                    return response.json().then(err => Promise.reject(err)).catch(() => Promise.reject(new Error('Server responded with an error')));
                }

                return response.json();
            })

            .then(data => {
                console.log(data);

                if (data.status === 'success') {
                    alert('Form submitted successfully');
                    form.reset();
                } else {
                    alert(`Form submission failed: ${data.message || 'Unknown error'}`);
                }
            })

            .catch(error => {
                console.error('Error:', error);
                
                alert(`Form submission failed: ${error.message || 'Unknown error'}`);
            });
    });
});
