# deployment-system

## Client Installation

Install the Python dependencies using [pip](https://pip.pypa.io/en/stable/).

```sh
python3 -m pip install -r requirements.txt
```

## Server Installation

Install the PHP dependencies using [Composer](https://getcomposer.org/).

```sh
composer install
```

Run `configure.sh` to automatically configure RabbitMQ. This script will create a new user and virtual host for the deployment server. You must choose a username and password for this user.
