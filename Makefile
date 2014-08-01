
MANAGE=python manage.py

run:
	${MANAGE} syncdb
	#${MANAGE} migrate web
	#${MANAGE} schemamigration web --auto
	${MANAGE} runserver 8000