import pytest
from selenium import webdriver
from ui_tests.pages.cadastro_page import CadastroPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000")
    yield driver
    driver.quit()

@pytest.mark.ui
def test_campos_obrigatorios(driver):
    page = CadastroPage(driver)
    page.submeter_formulario()
    assert "O e-mail é obrigatório!" in driver.page_source

@pytest.mark.ui
def test_email_invalido(driver):
    page = CadastroPage(driver)
    page.preencher_email("email_invalido")
    page.preencher_confirmacao_email("email_invalido")
    page.preencher_senha("SenhaForte123")
    page.submeter_formulario()
    assert "Digite um e-mail válido!" in driver.page_source

@pytest.mark.ui
def test_senha_fraca(driver):
    page = CadastroPage(driver)
    page.preencher_email("teste@email.com")
    page.preencher_confirmacao_email("teste@email.com")
    page.preencher_senha("12345")
    page.submeter_formulario()
    assert "A senha deve ter pelo menos 8 caracteres, 1 letra maiúscula e 1 número." in driver.page_source

@pytest.mark.ui
def test_cadastro_sucesso(driver):
    page = CadastroPage(driver)
    page.preencher_email("usuario@teste.com")
    page.preencher_confirmacao_email("usuario@teste.com")
    page.preencher_senha("SenhaForte123")
    page.submeter_formulario()
    assert "Cadastro realizado com sucesso!" in driver.page_source
