default: 
	@echo "Comandos disponíveis"
	@echo "make build           - Cria containers caso não os tenha, ou caso modifique .env.dev"
	@echo "make makemigrations  - Cria migrations"
	@echo "make migrate         - Executa migrations"
	@echo "make createsuperuser - Criar um usuario"
	@echo "make start           - Inicializa container, e executa serviço Django"
	@echo "make stop            - Encerra execução dos containers BD e Django"
	@echo "make test            - Fazer teste com o pytest"
	@echo "make lint            - Organiza o codigo"
	@echo "make black           - Black é um formatador de código Python que segue a PEP 8,"
	@echo "make isort           - Classifica automaticamente as importações em um arquivo de código Python"
	@echo "make flake8          - O Flake8 é um linter de código Python que verifica o estilo e a qualidade do código"
	@echo "make pre             - Pre analise do codigo antes do commit, Isort, Black Flake8 e um teste de coverage"

build:
ifeq ("$(wildcard .env.dev)","") 
	cp .env.dev-example .env.dev
	@echo "#####____________________________________________________________________Novo arquivo .env.dev criado" 
endif
	docker-compose -f docker-compose-dev.yaml --env-file=.env.dev up -d --build

makemigrations:
	docker exec -ti web_soccer_sorter_dev python manage.py makemigrations

migrate:
	docker exec -ti web_soccer_sorter_dev python manage.py migrate

createsuperuser:
	docker exec -ti web_soccer_sorter_dev python manage.py createsuperuser

start:
	docker-compose -f docker-compose-dev.yaml start
	docker exec -ti web_soccer_sorter_dev python manage.py runserver 0.0.0.0:8000

stop: 
	docker-compose -f docker-compose-dev.yaml stop

test:
	docker exec -ti web_soccer_sorter_dev pytest . --cov-report term --cov=. --cov-fail-under=80

lint:
	@echo "\n########## Runs isort, black and flake8. Organizing and linting code. ###########\n"
	@echo "############################### Running isort ###################################\n"
	docker exec -ti web_soccer_sorter_dev isort .
	docker exec -ti -u root web_soccer_sorter_dev chown -R soccer_sorter:soccer_sorter /soccer_sorter
	@echo "\n################################ Running flake8. ################################\n"
	docker exec -ti web_soccer_sorter_dev flake8 .
	docker exec -ti -u root web_soccer_sorter_dev chown -R soccer_sorter:soccer_sorter /soccer_sorter

pre: 
	make lint
	make test

isort:
	@echo "\n############################### Running isort ###################################\n"
	docker exec -ti web_soccer_sorter_dev isort .
	docker exec -ti -u root web_soccer_sorter_dev chown -R soccer_sorter:soccer_sorter /soccer_sorter

flake8:
	@echo "\n################################ Running flake8. ################################\n"
	docker exec -ti web_soccer_sorter_dev flake8 .
	docker exec -ti -u root web_soccer_sorter_dev chown -R soccer_sorter:soccer_sorter /soccer_sorter