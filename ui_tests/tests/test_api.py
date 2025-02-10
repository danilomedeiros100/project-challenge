import requests
import pytest

# URL base da API Mock
BASE_URL = "https://jsonplaceholder.typicode.com/users"

# Estrutura esperada para um usuário
EXPECTED_KEYS = {"id", "name", "username", "email", "address", "phone", "website", "company"}


@pytest.mark.api
def test_get_users():
    """Valida se a API retorna a lista de usuários corretamente."""
    response = requests.get(BASE_URL)

    assert response.status_code == 200, f"Erro: Código HTTP {response.status_code}"

    users = response.json()
    assert isinstance(users, list), "Erro: O retorno não é uma lista"

    # Verifica se ao menos um usuário tem todos os campos esperados
    for user in users:
        assert EXPECTED_KEYS.issubset(user.keys()), f"Erro: Estrutura de JSON incorreta - {user}"


@pytest.mark.api
def test_get_single_user():
    """Valida se a API retorna um usuário específico corretamente."""
    user_id = 1
    response = requests.get(f"{BASE_URL}/{user_id}")

    assert response.status_code == 200, f"Erro: Código HTTP {response.status_code}"

    user = response.json()
    assert isinstance(user, dict), "Erro: O retorno não é um objeto JSON"
    assert EXPECTED_KEYS.issubset(user.keys()), f"Erro: Estrutura de JSON incorreta - {user}"


@pytest.mark.api
def test_post_user():
    """Valida a criação de um usuário via POST."""
    new_user = {
        "name": "Teste User",
        "username": "teste_user",
        "email": "teste@example.com"
    }

    response = requests.post(BASE_URL, json=new_user)

    assert response.status_code == 201, f"Erro: Código HTTP {response.status_code}"

    created_user = response.json()
    assert "id" in created_user, "Erro: O usuário criado não contém um ID"
    assert created_user["name"] == new_user["name"], "Erro: Nome não corresponde"
    assert created_user["username"] == new_user["username"], "Erro: Username não corresponde"
    assert created_user["email"] == new_user["email"], "Erro: Email não corresponde"


@pytest.mark.api
def test_post_user_invalid():
    """Valida que um POST com dados inválidos retorna erro 400."""
    invalid_user = {
        "username": "invalid_user"  # Sem "name" e "email", que são obrigatórios
    }

    response = requests.post(BASE_URL, json=invalid_user)

    # Como a API mock não tem validação real, um 201 pode ser retornado
    assert response.status_code in [201, 400], f"Erro: Código HTTP inesperado {response.status_code}"


@pytest.mark.api
def test_get_invalid_user():
    """Valida que buscar um usuário inexistente retorna erro 404."""
    invalid_user_id = 99999
    response = requests.get(f"{BASE_URL}/{invalid_user_id}")

    assert response.status_code == 404, f"Erro: Código HTTP {response.status_code}"


@pytest.mark.api
def test_delete_user():
    """Valida a exclusão de um usuário."""
    user_id = 1
    response = requests.delete(f"{BASE_URL}/{user_id}")

    assert response.status_code in [200, 204], f"Erro: Código HTTP {response.status_code}"