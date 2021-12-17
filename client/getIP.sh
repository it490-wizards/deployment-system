#!/bin/sh


# this is to echo out the IP address of the client 
$e =  ip -4 addr show ztc25pjfpi | grep -oP "(?<=inet ).*(?=/)"
echo 4e > file.txt