function showLogin() {
    document.getElementById('login').style.display = 'block';
    document.getElementById('register').style.display = 'none';
}

function showRegister() {
    document.getElementById('login').style.display = 'none';
    document.getElementById('register').style.display = 'block';
}

document.addEventListener('DOMContentLoaded', function () {
    const elemsSelect = document.querySelectorAll('select');
    M.FormSelect.init(elemsSelect);

    const elemsDatePicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(elemsDatePicker, {
        format: 'yyyy-mm-dd'
    });
});
