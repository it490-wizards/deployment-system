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

Run [`configure.sh`](server/configure.sh) to automatically configure RabbitMQ and MySQL. You will be prompted to choose a username and password. The configuration will be written to `config.ini`.
