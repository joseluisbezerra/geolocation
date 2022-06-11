# Geolocation
CRUD simples de pins em uma mapa

# Requisitos
- Python 3
- PostgreSQL
- PostGIS

# Instalação
1. Crie um ambiente virtual:
```
python -m venv venv
```
2. Ative o ambiente virtual;
3. Instale as dependências:
```
(venv) pip install -r requirements.txt
```
4. Em seguida você vai precisar criar um arquivo .env e colocar as credenciais que faltam:
```
(venv) python contrib/env_gen.py
```
5. Sincronize a base de dados:
```
(venv) python manage.py migrate
```
6. Teste a instalação acessando o servidor de desenvolvimento (http://127.0.0.1:8000):
```
(venv) python manage.py runserver
```