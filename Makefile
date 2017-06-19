test:
	python manage.py test
test_lists:
	python manage.py test lists
migrations:
	python manage.py makemigrations
migrate:
	python manage.py migrate
static:
	rm -rf ../static/ && python manage.py collectstatic --noinput
serve:
	python manage.py runserver
