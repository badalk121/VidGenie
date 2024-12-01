document.getElementById('input-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const text = document.getElementById('text-input').value;
    const imageFile = document.getElementById('image-upload').files[0];
    const position = document.getElementById('position-input').value;

    const formData = new FormData();
    formData.append('text', text);
    formData.append('image', imageFile);
    formData.append('position', position);

    const response = await fetch('http://127.0.0.1:5000/generate', {
        method: 'POST',
        body: formData
    });

    const result = await response.json();
    document.getElementById('output').innerHTML = `<video src="${result.videoUrl}" controls></video>`;
});
