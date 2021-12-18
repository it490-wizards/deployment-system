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

Create an initialization file `rabbitmq.ini` which contains your RabbitMQ credentials. For example:

```ini
[rabbitmq]
host = "localhost"
port = 5672
user = "guest"
password = "guest"
vhost = "/"
```
