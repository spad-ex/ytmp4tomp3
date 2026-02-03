function convert() {
  const url = document.getElementById("url").value;
  const response = document.getElementById("response");
  const spinner = document.getElementById("spinner");

  response.textContent = "Processing...";
  spinner.style.display = "inline-block";

  fetch("/convert", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
      body: JSON.stringify({ url })
    })
    .then(async res => {
    const text = await res.text();
    console.log("RAW RESPONSE:", text);
    return JSON.parse(text); // this will still fail, but AFTER logging
    })
    .then(data => {
    response.textContent = data.message;
    spinner.style.display = 'none';
    })
    .catch(err => {
    console.error(err);
    response.textContent = 'ERROR — see console';
    spinner.style.display = 'none';
    });

