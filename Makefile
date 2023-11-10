install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py

migrate:
	python3 manage.py migrate

migrations:
	python3 manage.py makemigrations

test:
	coverage run manage.py test

runserver:
	python3 manage.py runserver