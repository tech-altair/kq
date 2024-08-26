fetch('/api/reviews/')
    .then(response => response.json())
    .then(data => {
        const sentiments = data.map(review => review.sentiment);
        const sentimentCounts = {
            positive: sentiments.filter(s => s === 'positive').length,
            negative: sentiments.filter(s => s === 'negative').length,
            neutral: sentiments.filter(s => s === 'neutral').length,
        };

        const ctx = document.getElementById('sentimentChart').getContext('2d');
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Positive', 'Negative', 'Neutral'],
                datasets: [{
                    data: [sentimentCounts.positive, sentimentCounts.negative, sentimentCounts.neutral],
                    backgroundColor: ['#4caf50', '#f44336', '#ffc107']
                }]
            }
        });
    });

    
    function loadReviews() {
        fetch('/api/reviews/')
            .then(response => response.json())
            .then(reviews => {
                const tableBody = document.querySelector('#reviewsTable tbody');
                tableBody.innerHTML = ''; // Clear existing rows
                reviews.forEach(review => {
                    const row = `<tr>
                                    <td>${review.review_name}</td>
                                    <td>${review.review_content}</td>
                                    <td>${review.sentiment}</td>
                                </tr>`;
                    tableBody.insertAdjacentHTML('beforeend', row);
                });
            });
    }
    
    // Call loadReviews on page load to display existing data
    document.addEventListener('DOMContentLoaded', loadReviews);
    
    document.addEventListener('DOMContentLoaded', function() {
        const scrapeBtn = document.getElementById('scrapeBtn');
        const reviewsTableBody = document.getElementById('reviewsTable').getElementsByTagName('tbody')[0];
    
        scrapeBtn.addEventListener('click', function() {
            fetch('/api/scrape/')  // Adjust the URL if necessary
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'success') {
                        reviewsTableBody.innerHTML = '';  // Clear existing rows
                        data.data.forEach(review => {
                            const row = reviewsTableBody.insertRow();
                            row.insertCell(0).textContent = review.review_name;
                            row.insertCell(1).textContent = review.review_content;
                            row.insertCell(2).textContent = review.sentiment;
                        });
                        alert('Reviews have been successfully scraped and updated.');
                    } else {
                        alert('Failed to retrieve reviews');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('An error occurred while fetching data.');
                });
        });
    });
    