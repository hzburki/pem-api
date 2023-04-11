# Personal Expense Manager API

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
