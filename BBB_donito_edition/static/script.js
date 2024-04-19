function getRandomLetter() {
    const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const randomIndex = Math.floor(Math.random() * alphabet.length);
    return alphabet[randomIndex];
}

function displayRandomLetter() {
    const letter = getRandomLetter();
    document.getElementById('letterDisplay').textContent = `Start with the letter ${letter}`;
}

// Display a random letter immediately when the page loads
document.addEventListener('DOMContentLoaded', displayRandomLetter);

document.getElementById('letterDisplay').addEventListener('click', function() {
    fetch('/generate-text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: 'start, give me one question from your list of categories dont repeat yourself! LOOK AT THE LIST I GAVE YOU!'}), // Adjust according to your needs
    })  
    .then(response => response.text()) // Use .text() instead of .json()
    .then(data => {
        document.getElementById('letterDisplay').textContent = data; // Directly use data
    })
    .catch(error => console.error('Error:', error));
});