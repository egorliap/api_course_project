document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');

    if (loginForm) {
        loginForm.addEventListener('submit', async function (event) {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            const response = await fetch('/auth/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, password }),
            });

            if (response.ok) {
                window.location.href = '/profile';
            } else {
                alert('Login failed');
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener('submit', async function (event) {
            event.preventDefault();
            const email = document.getElementById('reg_email').value;
            const password = document.getElementById('reg_password').value;
            const full_name = document.getElementById('full_name').value;

            const response = await fetch('/auth/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, password, full_name }),
            });

            if (response.ok) {
                window.location.href = '/profile';
            } else {
                alert('Registration failed');
            }
        });
    }
});