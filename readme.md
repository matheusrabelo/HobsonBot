# HobsonBot

## About

A lightweight and extensible open-source Telegram Bot.

This bot is your new personal assistant on Telegram.

## How to use
You just need to search **@HobsonBot** on Telegram and start a conversation with him.

## How to start developing
Install the following packages: flaky, nose, python-telegram-bot. Then, get a new token from Telegram Bot API. Finally, clone this repo, go to source/utils and create a **token.py** file, following the **token.example.py**.

To run, use:
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