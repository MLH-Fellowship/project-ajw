/* Sending the URL-encoded string as payload using Fetch */
 
const form = document.getElementById('form');
 
form.addEventListener('submit', function(e) {
    // Prevent default behavior:
    e.preventDefault();
    console.log("test")
    // Create new FormData object:
    const formData = new FormData(form);
    // Convert formData object to URL-encoded string:
    const payload = new URLSearchParams(formData);
    // Post the payload using Fetch:
    fetch('/api/timeline_post', {
    method: 'POST',
    body: payload,
    })
    .then(res => res.json())
    .then(data => console.log(data))
})