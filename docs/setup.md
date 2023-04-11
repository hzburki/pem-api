# Repo Setup

This document describes how I setup this python repository to create an API for my [Personal Expense Manager]() application.

## Technologies (Backend)
1. Python 3.10.6
2. [Docker](https://www.docker.com/) - Containerization
3. [Mysql](https://www.mysql.com/) - Database
4. [FastAPI](https://fastapi.tiangolo.com/) - API server
5. [SqlAlchemy](https://www.sqlalchemy.org/) - ORM
6. [Alembic](https://alembic.sqlalchemy.org/en/latest/) - Migration tool

## General Steps
1. Create a new directory for the project and initialize a git repository.
2. Create a virtual environment for the project.
   ```bash
      python -m venv env
    ```
3. Install dependencies and create a `requirements.txt` file. 
   ```bash
      pip install {DEPENDENCIES}
      pip freeze > requirements.txt
    ```
4. Got the sample API server working from the [FastAPI docs](https://fastapi.tiangolo.com/tutorial/first-steps/).
5. Setup a Dockerfile for the FastAPI sample app.
6. Create the docker-compose file for the FastAPI sample app along with the mysql database. (reference below)
    
> I did the below step to understand the SQL models and how to use them in the application. It is not used in the final repo. 
7. Setup the database models for the application following the FastAPI SQL docs. (reference below). 
        

**In Progress**

8. Configured the alembic migration tool to create database table using the SQLAlchemy models. 

## References
1. [This](https://www.youtube.com/watch?v=NH4VZaP3_9s&t=3656s&ab_channel=VeryAcademy) Youtube video for setting up docker and mysql.
2. [SQL Relational Database](https://fastapi.tiangolo.com/tutorial/sql-databases/#create-the-database-models) from the FastAPI docs.