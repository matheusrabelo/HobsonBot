# HobsonBot

[![Build Status](https://travis-ci.org/matheusrabelo/HobsonBot.svg?branch=master)](https://travis-ci.org/matheusrabelo/HobsonBot) [![Coverage Status](https://coveralls.io/repos/github/matheusrabelo/HobsonBot/badge.svg?branch=master)](https://coveralls.io/github/matheusrabelo/HobsonBot?branch=master)

## About

A lightweight and extensible open-source Telegram Bot.

This bot is your new personal assistant on Telegram.

## How to use
You just need to search **@HobsonBot** on Telegram and start a conversation with him.

## How to start developing

Ensure you have Python3 and Virtualenv installed.

Clone this repo and prepare your environment.

```bash
$ git clone https://github.com/matheusrabelo/HobsonBot.git
$ cd HobsonBot
$ virtualenv venv
$ source ./venv/bin/activate
```

Then, install all requirements.

```bash
$ pip install -r requirements.txt ; pip install -r requirements-dev.txt 
```

Then, get a new token from **@BotFather** on Telegram. Finally, go to source/utils and create a **token.py** file, following the **token.example.py**.

To start the application, use:

```bash
$ python source/main.py
```

To get test coverage, use:
```bash
$ nosetests --with-flaky --no-flaky-report --with-coverage --cover-package=source/
```

## Technologies
Python 3.6

## Contributing
Contributions are welcome

## License
MIT

## Author
Matheus Freire Rabelo