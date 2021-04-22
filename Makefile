app_name=service
freeze:
	@rm py/requirements.txt
	@pip freeze >> py/requirements.txt
build:
	@docker-compose build
up:
	docker-compose up -d
down:
	@echo 'Killing container...'
	@docker-compose down -v
stop:
	@docker-compose stop
