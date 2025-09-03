document.getElementById('classify-button').addEventListener('click', async () => {
    const tweetInput = document.getElementById('tweet-input');
    const resultDiv = document.getElementById('result');
    const sentimentP = document.getElementById('sentiment');
    const emojiSpan = document.getElementById('emoji');

    // Clear previous results
    sentimentP.textContent = '';
    emojiSpan.textContent = '';

    const tweet = tweetInput.value.trim();
    if (!tweet) {
        sentimentP.textContent = "Please enter a tweet!";
        resultDiv.style.opacity = 1;
        return;
    }

    // Show loading state
    sentimentP.textContent = "Classifying...";
    emojiSpan.textContent = "🤖";
    resultDiv.style.opacity = 1;

    try {
        const response = await fetch('/classify', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ tweet }),
        });

        const data = await response.json();

        if (response.ok) {
            sentimentP.textContent = `Sentiment: ${data.sentiment}`;
            emojiSpan.textContent = data.emoji;
        } else {
            sentimentP.textContent = `Error: ${data.error}`;
            emojiSpan.textContent = "❌";
        }
    } catch (error) {
        sentimentP.textContent = "Network error. Please try again.";
        emojiSpan.textContent = "❌";
    }

    resultDiv.classList.remove('hidden');
    tweetInput.value = '';
});
