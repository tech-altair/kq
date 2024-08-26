To run the application, first clone to your local machine 

We have two methods, the manual method where you have to install everything or using  docker 

1. Using Docker
```
docker-compose up --build
```
that will start django and rabbitMQ then avail an API endpoint of :8000
to start the front-end, cd into front-end and run 
```

cp .env.example .env
npm install
npm run dev
```
		
1. Manual installation 
		we are using 
		Install celery using [this](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#using-celery-with-django)
		Install rabbitMQ using [this](https://www.architect.io/blog/2021-01-19/rabbitmq-docker-tutorial/)
		

To start all processes manaually 
```
python manage.py runserver
// starting rabitMQ
// starting schedularrabbitMQ
// start celery in connection to 
docker run --rm -it -p 15672:15672 -p 5672:5672 rabbitmq:3-management  
celery -A APIBackend worker -l INFO   
celery -A APIBackend.celery beat 
then:
npm run dev // to start local server 3000
```
