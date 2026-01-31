function convert() {
    const url = document.getElementById('url').value;
    const response = document.getElementById('response');
    const spinner = document.getElementById('spinner');

    response.textContent = 'Processing...';
    spinner.style.display = 'inline-block';

    fetch('/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: url }),
    })
    .then(response => response.json())
    .then(data => {
        response.textContent = data.message;
        spinner.style.display = 'none';
    })
    .catch(error => {
        response.textContent = 'An error occurred: ' + error.message;
        spinner.style.display = 'none';
    });
}
