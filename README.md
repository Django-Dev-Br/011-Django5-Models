
# 011 Django 4 Profile Model

## O que são Models no Django?

Models no Django são classes Python que representam a estrutura e o comportamento dos dados na aplicação. Eles são responsáveis por definir as tabelas, colunas e relacionamentos do banco de dados de maneira abstrata, permitindo que os desenvolvedores interajam com os dados de forma mais intuitiva e consistente. Cada model corresponde a uma tabela no banco de dados, e cada atributo da classe representa um campo nessa tabela.

Os models são a espinha dorsal da arquitetura MTV (Model-Template-View) do Django, onde:

- **Model**: Representa a estrutura de dados da aplicação, definindo como os dados são armazenados e manipulados.
- **Template**: Define como os dados são apresentados ao usuário, usando HTML para a renderização.
- **View**: Controla a lógica que liga o model ao template, processando as requisições e determinando quais dados devem ser apresentados.

Ao usar models, o Django automaticamente cria um banco de dados relacional baseado nessas definições, gerencia migrações para atualizar a estrutura do banco de dados e oferece uma interface de alto nível para interagir com os dados.

## Links Úteis

- **[Django ORM CookBook](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/)**: Um recurso excelente para aprender mais sobre o ORM do Django e como trabalhar eficientemente com modelos e consultas.

- **[DB Browser for SQLite](https://sqlitebrowser.org/)**: Uma ferramenta gráfica para visualizar e manipular bancos de dados SQLite. Útil para inspecionar diretamente a estrutura e os dados do banco de dados criado pelo Django.

- **[Python Orientado a Objetos](https://www.w3schools.com/python/python_classes.asp)**: Um tutorial para entender a sintaxe e os conceitos de classes em Python, fundamentais para trabalhar com models no Django, já que eles são definidos como classes.

## COMO RODAR ESSE PROJETO EM SEU COMPUTADOR:

### Requisitos

- **Python 3.12**  
  [Baixar Python 3.12](https://www.python.org/downloads/release/python-3122/)

  Confira o vídeo para saber como trabalhar com múltiplas versões do Python e com venv (ambiente virtual): [Trabalhando com Múltiplas Versões do Python + venv](https://youtu.be/eetDeQrv0Rs?si=rAIDmLCgdeh7ouXa)

- **Virtualenv**

  Para instalar o pacote `virtualenv` no Python, utilize os seguintes comandos:

  - **Linux**:
    ```bash
    python3 -m pip install virtualenv
    ```

  - **Windows**:
    ```bash
    python -m pip install virtualenv
    ```

### Passos para Executar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/Django-Dev-Br/011-Django-4-Models.git
    cd 011-Django-4-Models
    ```

2. **Crie um ambiente virtual**:
    ```bash
    python3 -m venv myvenv  # Linux
    python -m venv myvenv  # Windows
    ```

3. **Ative o ambiente virtual criado**:
    ```bash
    source myvenv/bin/activate  # Linux
    myvenv\Scriptsctivate  # Windows
    ```

4. **Instale o Django**:
    ```bash
    pip install django==4.2.15
    ```

5. **Crie migrações para o modelo**:
    ```bash
    python manage.py makemigrations
    ```

   Este comando irá analisar as mudanças no modelo do seu aplicativo e criar um arquivo de migração (por exemplo, `0001_initial.py`) na pasta `migrations`. Esse arquivo de migração define como as tabelas do banco de dados devem ser criadas ou alteradas.

6. **Aplique as migrações ao banco de dados**:
    ```bash
    python manage.py migrate
    ```

   O comando `migrate` aplica todas as migrações pendentes, criando as tabelas e aplicando as alterações necessárias ao banco de dados. Isso garante que a estrutura do banco de dados corresponda aos modelos definidos no seu projeto.

7. **Execute o servidor de desenvolvimento**:
    ```bash
    python manage.py runserver
    ```

### Banco de Dados SQLite

- O Django, por padrão, utiliza o SQLite como seu banco de dados. Quando você cria e aplica migrações, um arquivo `db.sqlite3` é gerado na raiz do seu projeto. Esse arquivo contém todas as tabelas e dados gerados a partir dos seus models, funcionando como o banco de dados da sua aplicação.

- A configuração do banco de dados em `settings.py` é feita da seguinte forma:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```

   Esta configuração define o uso do SQLite, mas outros Sistemas de Gerenciamento de Banco de Dados (SGBDs) podem ser adicionados posteriormente. O PostgreSQL é frequentemente a escolha mais utilizada no ecossistema do Django devido à sua robustez e recursos avançados.

### Estrutura de Diretórios do Projeto

```
011-Django-4-Profile-Model/
├── manage.py
├── myapp/
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py        # Contém a definição do modelo Profile
│   ├── migrations/
│       ├── __init__.py
│       └── 0001_initial.py  # Criado após executar o comando 'makemigrations'
│   └── views.py
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py      # Configurações do Django
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3           # Banco de dados SQLite
└── README.md
```

**Nota**: A pasta `__pycache__` é ignorada nesta listagem, pois contém arquivos de cache que não são necessários para o controle de versão.
