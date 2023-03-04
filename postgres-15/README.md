# Postgres v15 starter

This docker environment is designed to provide you with a pre-configured initial postgres environment.

It includes templates for postgres configuration files and initial creation scripts as well as a sample .env file for environment variables. The environment is configured to load these configurations when launching the docker compose.

## Configuration

Several things need to be configured before the first launch:

### Configuration tweak based on your system

Enter your system hardware configuration [here](https://pgtune.leopard.in.ua/) and edit the file /conf/postgres.conf accordingly. \
** Keep the line: listen_addresses = '' **

### Edit envionnement variables

This environment is pre-configured with initial environment variables, it is important to modify them. \

Copy the example file:
```bash
cp example.env .env
```

With your favorite editor, change the password (POSTGRES_PASSWORD) and if necessary the username (POSTGRES_USER) and port of the database (POSTGRES_PORT).
## Installation

Create a new directory and copy the contents from git:

```bash
mkdir postgres && cd postgres
git init
git remote add -f origin git@github.com:MathisVerstrepen/docker_templates.git
git config core.sparseCheckout true
git sparse-checkout init
git sparse-checkout set postgres-15
git pull origin master
cd postgres-15
```

Run the Docker compose using the following command:
```bash
sudo docker compose up -d
```

When you modify the database creation files you must delete the volume data:
```bash
sudo rm -r volumes/
```