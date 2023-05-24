// Add star rating
const rating = document.querySelector('form[name=rating]');

rating.addEventListener("change", function (e) {
    // Получаємо дані з форми
    let data = new FormData(this);
    fetch(`${this.action}`, {
        method: 'POST',
        body: data
    })
        .then(response => alert("Рейтинг встаневлено"))
        .catch(error => alert("Помилка"))
});