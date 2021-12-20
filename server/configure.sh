#!/bin/sh

if [ $(id -u) -ne 0 ]; then
    echo "$0: must run as root"
    exit 1
fi

# constants
database=deployment
virtual_host=deployment

# prompt for new username and password
read -p "New username: " username
stty -echo
read -p "New password: " password
stty echo

# create RabbitMQ user and virtual host
rabbitmqctl add_user $username $password
rabbitmqctl add_vhost $virtual_host
rabbitmqctl set_permissions --vhost $virtual_host $username '.*' '.*' '.*'

# create MySQL user and database
mysql << EOF
CREATE DATABASE IF NOT EXISTS $database;
CREATE USER IF NOT EXISTS '$username'@'localhost' IDENTIFIED BY '$password';
GRANT ALL PRIVILEGES ON $database.* TO '$username'@'localhost';
FLUSH PRIVILEGES;
EOF

# create initialization file
cat > config.ini << EOF
[rabbitmq]
host = "localhost"
port = 5672
user = "$username"
password = "$password"
vhost = "$virtual_host"

[mysql]
hostname = "localhost"
username = "$username"
password = "$password"
database = "$database"
EOF
