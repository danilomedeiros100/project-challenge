from selenium.webdriver.common.by import By

class CadastroPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "email")
        self.confirm_email_input = (By.ID, "confirm-email")
        self.password_input = (By.ID, "password")
        self.submit_button = (By.TAG_NAME, "button")

    def preencher_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def preencher_confirmacao_email(self, email):
        self.driver.find_element(*self.confirm_email_input).send_keys(email)

    def preencher_senha(self, senha):
        self.driver.find_element(*self.password_input).send_keys(senha)

    def submeter_formulario(self):
        self.driver.find_element(*self.submit_button).click()
