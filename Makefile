dev/install: 
	if [ ! -f .env ]; then cp .env.example .env; fi 
	pipenv install
	pipenv run pip freeze > requirements.txt

dev/start:
	pipenv run python app

dev/test:
	pipenv run python -m unittest discover .
	
prod/start:
	python app

prod/install:
	pip install --upgrade pip
	pip install -r requirements.txt

prod/logs:
	docker exec -ti core_api cat logs/bot.log

prod/transfer:
	docker exec -ti core_api python should_transfer.py