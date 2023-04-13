# Personal Expense Manager API

## What is this? 

This is a personal expense manager API. I am building a clone for [moneylover](https://moneylover.me/) a personal expense tracker I use daily. I want to extend its functionalities and add some features that I want. 

It is built using Python, FastAPI, and MySQL. This API will be used to power a frontend application built with React (vite). You can find it [here](https://github.com/hzburki/pem-client).

## Motivation

This project is a way for me to learn and practice the following:

1. Python Language
2. Computer Vision and Machine Learning Libraries (with Python)

***

## Repository Setup
The general steps I took and the resources I used are [here](./docs/setup.md).

## Getting Started
These are the steps to run this project locally. It uses python, fastapi, and docker.

1. Create a virtual environment by running the following command:
```bash
python -m venv env
```

2. Activate the virtual environment:
```bash
source env/bin/activate
``` 

3. Start the docker container:
```bash
docker-compose up --build
```
> You only need to use the --build flag the first time you run the container.

4. Connect to the database.
The database should be running on your local machine on port 3306. I am using Sequel Pro to connect to the database. You can use any database client you want.

The database name is `pem-db` and the username is `root` and the password is `apples`.
> You can specify the password and database name to whatever you want.

5. Run the migrations:

### Closing Work
When you are done working on the project, you can stop the docker container by running the following command:
```bash
docker-compose down
```
