install:
	pip install -r requirements.txt
test:
	python manage.py test
unittest:
	python manage.py test lists
test_stage:
	STAGING_SERVER=staging.gebr.club python manage.py test functional_tests
test_live:
	STAGING_SERVER=gebr.club python manage.py test functional_tests
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
deploy_stage:
	cd deploy_tools && fab deploy:host=hayesmage@staging.gebr.club && cd -
deploy_live:
	cd deploy_tools && fab deploy:host=hayesmage@gebr.club && cd -
login:
	ssh hayesmage@gebr.club
