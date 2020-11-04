build: run

run:
	docker-compose run --service-ports --rm appserver

migrations:
	docker-compose run --rm appserver python manage.py makemigrations

superuser:
	docker-compose run --rm appserver python manage.py createsuperuser

populate_books:
	docker-compose run --rm appserver python manage.py populate_books $(args)

populate_opinions:
	docker-compose run --rm appserver python manage.py populate_opinions $(args)

test:
	docker-compose run --rm appserver ./test.sh $(args)
