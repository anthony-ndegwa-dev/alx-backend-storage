# Redis basic

## Objectives

    Use redis for basic operations
    Use redis as a simple cache

## Requirements

    All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
    All files should end with a new line
    The first line of all files should be #!/usr/bin/env python3
    Use the pycodestyle style (version 2.5)
    All modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All functions and methods should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    All functions and coroutines must be type-annotated.

## Install Redis 

$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
