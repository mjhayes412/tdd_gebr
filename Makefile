test:
	python manage.py test
unittest:
	python manage.py test lists
clean:
	find . -type f -name '*.pyc' -delete
migrations:
	python manage.py makemigrations
migrate:
	python manage.py migrate
static:
	rm -rf ../static/ && python manage.py collectstatic --noinput
serve:
	python manage.py runserver
