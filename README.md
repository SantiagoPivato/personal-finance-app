# Personal finance project

## Author
- Santiago Pivato - [santiagopivato@gmail.com](mailto:santiagopivato@gmail.com)

## Objectives
- Create a dashboard to visualize market realted data and use this information to make savings/investment decisions. 
- Fetch relevant data from financial APIs like BCRA's or IOL's, and learn how to interpret this information.
- Learn financial vocabulary and strategies. 

## References
- [BCRA](https://www.bcra.gob.ar/BCRAyVos/catalogo-de-APIs-banco-central.asp) 
- [IOL](https://api.invertironline.com/)
- [django 5.1](https://docs.djangoproject.com/en/5.1/)

## Initialize project
First the *.env* file must be created based on this [example](.env.example). The following commands have to be executed:<br> 

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

python3 manage.py makemigrations visualizer
python3 manage.py migrate visualizer

#Create Units from fixture
python3 manage.py loaddata Unit.json


#Create superuser, this will prompt inputs for username, email and password
python3 manage.py createsuperuser 
```

If configured correctly, after executing "*docker compose up -d*" the project should be accesible at http://127.0.0.1:8000.


## Troubleshooting
Error: "*... postgres_data permission denied ..."*
``` bash
sudo chmod a+rw postgres_data/ -R
```



## Views
### / 
Currently the main view. Implements the market variables' visualizer.

### /admin
Django administration view. Can be accessed with the superuser credentials.  


## Todo
- logging
- IOL API
- Sources and Methods model
- Investment simulator