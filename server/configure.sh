#!/bin/sh

if [ $(id -u) -ne 0 ]; then
    echo "$0: must run as root"
    exit 1
fi

# prompt for new username and password
read -p "New username: " username
stty -echo
read -p "New password: " password
stty echo
virtual_host=deployment

# create user and virtual host
rabbitmqctl add_user $username $password
rabbitmqctl add_vhost $virtual_host
rabbitmqctl set_permissions --vhost $virtual_host $username '.*' '.*' '.*'

# create initialization file
cat > rabbitmq.ini << EOF
[rabbitmq]
host = "localhost"
port = 5672
user = "$username"
password = "$password"
vhost = "$virtual_host"
EOF
