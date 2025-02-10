# QA Automation Challenge
Este projeto contém testes automatizados para um formulário de cadastro utilizando Selenium e Pytest.

## Estrutura do Projeto
```
qa-automation-desafio/
├── app/
│   └── app.py
├── config/
│   └── pytest.ini
├── reports/
│   ├── report.html
│   ├── report.json
│   └── generate_report.py
├── static/
│   └── script.js
├── templates/
│   └── index.html
├── ui_tests/
│   ├── pages/
│   │   └── cadastro_page.py
│   └── tests/
│       └── test_cadastro.py
├── requirements.txt
├── README.md
```

---

**Descrição dos Diretórios**:
- **app/**:  
  Contém a API mock que serve os dados de teste e endpoints simulados.

- **config/**:  
  Armazena as configurações do pytest, como marcadores de teste e opções de execução.

- **reports/**:  
  Diretório onde os relatórios JSON e HTML são gerados após a execução dos testes.  
  - `generate_report.py`: Lógica adicional para manipulação ou visualização de relatórios.

- **static/**:  
  Arquivos estáticos (JS, CSS, imagens).  
  - `script.js`: Scripts para manipulação do conteúdo do relatório HTML.

- **templates/**:  
  Páginas HTML baseadas nos relatórios gerados.  
  - `index.html`: Página inicial com o relatório interativo.

- **ui_tests/**:  
  Organização dos testes de interface (UI).  
  - `pages/`: Implementações do padrão Page Object Model (POM).  
  - `tests/`: Scripts que validam a funcionalidade da interface de usuário.

---


## Instalação e Execução

### 1. Criar e ativar o ambiente virtual
No Windows:
```sh
python -m venv venv
venv\Scripts\activate
```

No Linux/macOS:
```sh
python3 -m venv venv
source venv/bin/activate
```
### 2. Atualizar o pip
```sh
pip install --upgrade pip
```

### 3. Instalar Dependências
```sh
pip install -r requirements.txt
```

### 4. Executar a API e formulário
```sh
python -m app.app & python -m http.server 8000 --directory templates & locust -f locustfile.py
```

A API estará disponível em 'http://localhost:5001/users'.

O Formulário disponível em 'http://localhost:8000'.

Teste de performance em 'http://0.0.0.0:8089/'


### 5. Executar os Testes
```sh
pytest
```

### 6. Verificar report Geraldo automaticamente 
```sh
Reports/report.html
```

### 7. Arquivos de relatórios
```sh
Os relatórios gerados estão disponíveis em:
- HTML: reports/report.html
- JSON: reports/report.json
```

🚀 Projeto pronto para automação de testes!





