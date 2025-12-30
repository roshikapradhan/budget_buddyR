const ctx = document.getElementById('expenseChart').getContext('2d');
let expenseChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Food', 'Travel', 'Shopping', 'Bills'],
        datasets: [{
            data: [0, 0, 0, 0],
            backgroundColor: ['#FFB6C1', '#FFC0CB', '#FF69B4', '#FFB7C5']
        }]
    }
});

const form = document.getElementById('expense-form');
form.addEventListener('submit', (e) => {
    e.preventDefault();
    
    // Change Buddy's message
    const msg = document.getElementById('buddy-msg');
    const emoji = document.getElementById('buddy-emoji');
    
    msg.innerText = "Yay! Expense tracked! 🌸";
    emoji.innerText = "🐱"; // Changes from Bunny to Cat on click

    // Reset after 3 seconds
    setTimeout(() => {
        msg.innerText = "Keep it up!";
        emoji.innerText = "🐰";
    }, 3000);

    // In a real app, you would send data to Django here via fetch()
    alert("Expense Saved!");
});