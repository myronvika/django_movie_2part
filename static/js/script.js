
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

function validateFormData(formData) {
    // Перевірка на валідність даних
    if (!formData.get('rating')) {
        alert('Будь ласка, виберіть рейтинг');
        return false;
    }
    return true;
}
//функція відображення повідомлення про помилку користувачеві
function displayErrorMessage(message) {
    const errorElement = document.createElement('div');
    errorElement.classList.add('error');
    errorElement.textContent = message;
    document.body.appendChild(errorElement);
}