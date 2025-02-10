from locust import HttpUser, task, between

class ApiUser(HttpUser):
    # Tempo de espera entre as requisições de cada usuário (1 a 2 segundos, ajustável)
    wait_time = between(1, 2)

    @task
    def get_users(self):
        # Substitua "/users" pelo endpoint real que deseja testar
        self.client.get("/users")