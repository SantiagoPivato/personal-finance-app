# Personal finance project

## Objectives
- Create a dashboard to visualize market realted data and use this informatio to make savings/investments decisions. 
- Fetch relevant data from financial APIs like BCRA's or IOL's, and learn how to interpret this information.
- Learn financial vocabulary and strategies. 

## References
- [BCRA](https://www.bcra.gob.ar/BCRAyVos/catalogo-de-APIs-banco-central.asp) 
- [IOL](https://api.invertironline.com/)
- [django 5.1](https://docs.djangoproject.com/en/5.1/)

## Initialize project
First a *.env* file must be created based on this [example](.env.example). The the following commands have to be executed:<br> 

```bash
# Build the image
docker build -t my-finance-django .

#Run container and start server
docker compose up -d

#Open bash in container
docker exec -it my-finance-django bash

#Apply database migrations, once in container's bash
python3 manage.py makemigrations 
python3 manage.py migrate 

python3 manage.py makemigrations app
python3 manage.py migrate app

#Create superuser, this will prompt inputs for username, email and password
python3 manage.py createsuperuser 
```

If configured correctly, after executing "*docker compose up -d*" the project should be accesible at http://127.0.0.1:8000.