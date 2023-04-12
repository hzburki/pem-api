# Setup Migrations using Alembic

We are going to manage all database migrations using Alembic. Alembic is a database migration tool for usage with the SQLAlchemy Database Toolkit for Python. It provides a full suite of well known database migration patterns, designed to make it as easy as possible to manage database schema changes over time.

## Installation

Install Alembic using pip:

```bash
  pip install alembic
```

## Configuration

Run the command below to create the alembic directory and .ini file:

```bash
  alembic init alembic
```

We are going to leave everything in the `alembic.ini` file as is. We will only be changing the `script_location` to `src/migrations` so all the code for the project in encapsulated inside the `src` directory. 

We also need to change the  `sqlalchemy.url` to the database connection url. Here we will need to use envrionment variables to store the database connection url, because you should not be storing the database connection url in your code. 

```ini
  [alembic]
  script_location = src/migrations
  sqlalchemy.url = ${DATABASE_URL}
```

Once we have the `.ini` file setup. We need to provide the `declarative_base` from sqlalchemy to alembic. This is done by adding the `Base` model to the `env.py`. Alembic uses this `Base` to detect changes between the mysql database and what we have in the sqlalchemy models. 

I am import the `declarative_base` from the `src/config/database.py` file. This is where I have defined the `Base` model. 

```python
  from ..src.config.database import Base
  
  target_metadata = Base.metadata
```