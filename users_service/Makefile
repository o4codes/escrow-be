.PHONY : 
collectstatic:
	python manage.py collectstatic --noinput

.PHONY : runserver
runserver:
	python manage.py runserver 0.0.0.0:7002

.PHONY : migrate
migrate:
	python manage.py migrate


.PHONY : dev-server
dev-server:
	$(MAKE) collectstatic
	$(MAKE) migrate
	$(MAKE) runserver