# Description

This project aim to build open source network without photos.

# 🖌️ Design

The link to design in figma [https://www.figma.com/file/2gAbB7NagQDauWMLWBJdxb/Blinder?node-id=0%3A1](https://www.figma.com/file/2gAbB7NagQDauWMLWBJdxb/Blinder?node-id=0%3A1)


# 🔨 Project Folders

* API - Backend application in **Django 3**
* APP - App mobile in **Flutter**
* Web - Webpage in **React Web** 

# 🏁 Get Start

Go to api folder

```
cd api
```

Create docker-compose.override.yml for configure database credenteials

```
version: '3.5'
services: 
    postgres:
        environment: 
            - POSTGRES_PASSWORD=postgres
            - POSTGRES_USER=postgres
            - POSTGRES_DB=blinder
```

Now create .env file and configure data base 

```
cd src 
cp .env.example .env
```

Start the containers

```
docker-compose up -d
```

and enjoy