document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('cadastro-form');
    const emailInput = document.getElementById('email');
    const confirmEmailInput = document.getElementById('confirm-email');
    const passwordInput = document.getElementById('password');
    const successMessage = document.getElementById('success-message');

    const emailError = document.getElementById('email-error');
    const confirmEmailError = document.getElementById('confirm-email-error');
    const passwordError = document.getElementById('password-error');

    function showError(input, errorElement, message) {
        errorElement.textContent = message;
        errorElement.style.display = "block";
        input.classList.add("error-border");
    }

    function removeError(input, errorElement) {
        errorElement.textContent = "";
        errorElement.style.display = "none";
        input.classList.remove("error-border");
    }

    function validateForm() {
        let hasError = false;

        if (!emailInput.value.trim()) {
            showError(emailInput, emailError, "O e-mail é obrigatório!");
            hasError = true;
        } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value.trim())) {
            showError(emailInput, emailError, "Digite um e-mail válido!");
            hasError = true;
        } else {
            removeError(emailInput, emailError);
        }

        if (!confirmEmailInput.value.trim()) {
            showError(confirmEmailInput, confirmEmailError, "A confirmação do e-mail é obrigatória!");
            hasError = true;
        } else if (confirmEmailInput.value.trim() !== emailInput.value.trim()) {
            showError(confirmEmailInput, confirmEmailError, "Os e-mails não coincidem!");
            hasError = true;
        } else {
            removeError(confirmEmailInput, confirmEmailError);
        }

        if (!passwordInput.value.trim()) {
            showError(passwordInput, passwordError, "A senha é obrigatória!");
            hasError = true;
        } else if (!/^(?=.*[A-Z])(?=.*\d).{8,}$/.test(passwordInput.value.trim())) {
            showError(passwordInput, passwordError, "A senha deve ter pelo menos 8 caracteres, 1 letra maiúscula e 1 número.");
            hasError = true;
        } else {
            removeError(passwordInput, passwordError);
        }

        return !hasError;
    }

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Evita o envio padrão do formulário

        if (!validateForm()) {
            console.log("Formulário inválido, não será enviado.");
            return;
        }

        const userData = {
            email: emailInput.value.trim(),
            password: passwordInput.value.trim()
        };

        console.log("📤 Enviando dados para a API:", userData);

        fetch('http://localhost:5001/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userData)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Erro na requisição: ${response.statusText}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("Resposta da API:", data);
            if (data.message === "Usuário criado com sucesso") {
                successMessage.textContent = "Cadastro realizado com sucesso!";
                successMessage.style.display = "block";
                form.reset();
            } else {
                showError(emailInput, emailError, "Erro ao cadastrar usuário!");
            }
        })
        .catch(error => {
            console.error("Erro ao conectar com a API:", error);
            showError(emailInput, emailError, "Erro ao conectar com a API.");
        });
    });
});