# deployment-system

This repository exists for the sole purpose of meeting a final presentation deliverable of creating a deployment system from scratch. Under normal conditions, I would **never** create or use something this bad; `git` would be a far more appropriate tool for deployment.

## Client Installation

Install the Python dependencies using [pip](https://pip.pypa.io/en/stable/).

```sh
python3 -m pip install -r requirements.txt
```

Create a file `.env` which contains the RabbitMQ credentials for the deployment server.

```sh
PIKA_HOST="localhost"
PIKA_USERNAME="username"
PIKA_PASSWORD="password"
```

## Server Installation

Install the PHP dependencies using [Composer](https://getcomposer.org/).

```sh
composer install
```

Run [`configure.sh`](server/configure.sh) to automatically configure RabbitMQ and MySQL. You will be prompted to choose a username and password. The configuration will be written to `config.ini`.
