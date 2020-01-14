# Bouncing Balls Game

A simple Orinted Objected Programming game that has the player dodging bouncing balls with Python, the PyGame library.

## Demo

![game](https://user-images.githubusercontent.com/34337622/72373131-f13fa400-3707-11ea-9fa0-91f9913c60b1.gif)

## Technologies

-   Python 3.7
-   PyGame

## Prerequisites

-   [Python](https://www.python.org/downloads/)
-   [pip](https://pip.pypa.io/en/stable/installing/)
-   [pipenv](https://pipenv.readthedocs.io/en/latest/install/#make-sure-you-ve-got-python-pip)

## Installation

-   [Clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this repo to your local machine using:

```
$ git clone https://github.com/tarnowski-git/Bouncing_Balls_Game.git
```

-   Setup your [local environment](https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv):

```
# Spawn a shell with the virtualenv activated
$ pipenv shell

# Install dependencies
$ pipenv install

# Run script into local environment
$ pipenv run python game.py
```

-   Compile with Pyinstaller to exectutable file:

```
# Windows
pyinstaller --onefile --windowed game.py
```

## Sources

This game is based on [wikiHow](https://www.wikihow.com/Program-a-Game-in-Python-with-Pygame#Making-a-Game-Object_sub) Tutorial.

## License

This project is licensed under the terms of the [**MIT**](https://github.com/tarnowski-git/Bouncing_Balls_Game/blob/master/LICENSE) license.
