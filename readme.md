# Personal Expense Manager API

## Getting Started
These are the steps to run this project locally. It uses python, fastapi, and docker.

1. Install [Docker](https://www.docker.com/products/docker-desktop) on your machine.
2. From the below commands run the following commands in the terminal.
    ```bash
    docker build -f Dockerfile.dev -t pem-fastapi .
    docker run --name pem-api -p 8000:8000 -v $(pwd):/app -d pem-fastapi
    ```
3. You can access the API on [http://localhost:8000](http://localhost:8000)
    > Now you can make changes to the code and see the changes immediately, however you will not get any code completion. 
4. To get code completion, open the project in VSCode and install the [Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension.
5. Once the extension is installed, click on the green icon on the bottom left corner of the screen. It will prompt you to attach to the container. Click on `Attach to Running Container` and select `pem-api`.
    > Make sure your docker container is running. You can check this by running `docker ps` in the terminal.
6. When the container is attached for the first time, it will install all the dependencies and setup the environment. This will take a few minutes.
7. You can now make changes to the code and see the changes immediately. You will also get code completion.
8. To stop the container, run `docker stop pem-api` in the terminal.
9. To restart the container, run `docker start pem-api` in the terminal.


### Some Gotchas! 
1. When you make changes to the code, the devc container will ask to install certain extensions such as python, etc. 
2. When commiting code, the dev container did not have git installed. I installed it manually by running `apt-get install git` in the terminal. 
3. However, it did not pick the github credentials on my machine. I solved this opening the "Source Control" tab on the VS Code side menu and commiting from there. It automatically asked my to login to github using the browser and it worked.

### Extensions installed on Dev Container
1. [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
2. [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
3. [Github Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
4. [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
5. [isort](https://marketplace.visualstudio.com/items?itemName=pycqa.vscode-isort)

### References
- [Setup Development Environment with Docker](https://www.youtube.com/watch?v=0H2miBK_gAk&t=790s&ab_channel=PatrickLoeber)

## Docker Commands

### Create a develop docker image
```bash
docker build -f Dockerfile.dev -t pem-fastapi .
```
**Explanation**:
- `-t pem-fastapi` - Tag the image with a name
- `-f Dockerfile.dev` - Use the Dockerfile.dev file to build the image

### Run a docker container in development mode
```bash
  docker run --name pem-api -p 8000:8000 -v $(pwd):/app -d pem-fastapi
```

**Explanation**:
- `--name pem-api` - Name of the container
- `-p 8000:8000` - Port mapping. The first 8000 is the port on the host machine. The second 8000 is the port on the container.
- `-v $(pwd):/app` - Mount the current directory to the container's `/app` directory. This will allow us to make changes to the code and see the changes immediately.
- `-d` - Run the container in detached mode. This will run the container in the background. It will not block the terminal and return the id of the container.

> You can access the API on [http://localhost:8000](http://localhost:8000)

### Stop a docker container
```bash
  docker stop pem-api
```

**Explanation**:
- `pem-api` - Name of the container

### Start a docker container
```bash
  docker start pem-api
```

**Explanation**:
- `pem-api` - Name of the container

### Create a production docker image
```bash
docker build -t pem-fastapi .
```
**Explanation**:
- `-t pem-fastapi` - Tag the image with a name


### Run a docker container in production mode
```bash
  docker run --name pem-api -p 8000:8000 -d pem-fastapi
```

**Explanation**:
- `--name pem-api` - Name of the container
- `-p 8000:8000` - Port mapping. The first 8000 is the port on the host machine. The second 8000 is the port on the container.
- `-d` - Run the container in detached mode. This will run the container in the background. It will not block the terminal and return the id of the container.


### Remove a docker container
```bash
  docker rm pem-api
```

**Explanation**:
- `pem-api` - Name of the container

### Remove a docker image
```bash
  docker rmi pem-fastapi
```

**Explanation**:
- `pem-fastapi` - Name of the image