.PHONY: help install test run build up down clean logs

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install Python dependencies
	pip install -r requirements.txt

test: ## Run Django tests
	python manage.py test

run: ## Run Django development server
	python manage.py runserver

build: ## Build Docker image
	docker build -t pokedex-app .

up: ## Start application with Docker Compose
	docker-compose up -d

down: ## Stop Docker Compose services
	docker-compose down

clean: ## Clean up Docker resources
	docker system prune -f
	docker volume prune -f

logs: ## View Docker Compose logs
	docker-compose logs -f

migrate: ## Run Django migrations
	python manage.py migrate

collectstatic: ## Collect static files
	python manage.py collectstatic --noinput

shell: ## Open Django shell
	python manage.py shell

check: ## Check Django configuration
	python manage.py check --deploy

docker-test: ## Test Docker image locally
	docker run -d --name pokedex-test -p 8000:8000 pokedex-app
	sleep 10
	curl -f http://localhost:8000/pokemon/ || echo "Test failed"
	docker stop pokedex-test
	docker rm pokedex-test

production-build: ## Build production Docker image
	docker build -t pokedex-app:production --build-arg DJANGO_SETTINGS_MODULE=pokedex_project.production .

production-run: ## Run production Docker image
	docker run -d --name pokedex-prod -p 8000:8000 -e DJANGO_SETTINGS_MODULE=pokedex_project.production pokedex-app:production

