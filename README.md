# 📚 About the project

This application is proof of concept about GIS application with Django and MongoDB

# 💻 Getting started

## Install poetry

``` curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -```

> Restart your terminal

## Create virtual env
``` python -m venv ./venv ```

## Active your virtual env
``` source ./venv/bin/activate ```


## Database

``` bash
# Create the instance of Mongo using docker

docker run --name mongo -p 27017:27017 -d -t mongo 
```

## Run command
```bash  
# Install dependencies

poetry install 
```

## Run application
``` bash
# Run server

python manage.py runserver 
 ```