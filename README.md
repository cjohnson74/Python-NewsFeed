# Python Newsfeed
I use Python to refactor an existing application that was originally built using Node.js. The app, called Just Tech News, is a website where users can post, upvote, and comment on links to news articles. Instead of using Node.js as the back-end language and Handlebars.js as the templating engine, I used Python to create the app and the Python Flask framework to create the application’s views.

## I Learned How to Do The Following:

- Build and deploy to the cloud a Flask API with correct project structure and necessary dependencies.

- Connect the application to an RDBMS database using SQL Alchemy to support the API model.

- Create a REST API that performs CRUD operations.

- Set up and configure a local virtual environment for Python Flask.

- Explain the differences between JavaScript and Python.

- Add templating to the application to allow for user interactions.

- Perform basic DevOps and deploy to a cloud infrastructure.

## Tools I Used:

- [Python](https://www.python.org/) is an interpreted, high-level, open-source, general-purpose programming language that supports procedural, object-oriented, and some functional programming constructs.
- pip is the default package manager for Python. It is distributed with Python, which means that when you install Python, pip is automatically installed on your computer!
  - [Python Package Index (PyPI)](https://pypi.org/), a repository of software for the Python programming language, to your Python applications.
- [Flask](https://palletsprojects.com/p/flask/) is a lightweight web application framework written in Python. It's designed to make getting started quick and easy, with the ability to scale up to complex applications. It has become one of the most popular Python web application frameworks.
  - [Flask PyPI Package](https://pypi.org/project/Flask/), was used for the purposes of this project.
- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and object-relational mapper that gives Python developers the full power and flexibility of SQL. It provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.
  - [SQLAlchemy PyPI Package](https://pypi.org/project/SQLAlchemy/), was used for the purposes of this project.
- [PyMySQL](https://pymysql.readthedocs.io/en/latest/) is a pure Python MySQL driver that connects a Python application to a MySQL database.
  - [PyMySQL PyPI Package](https://pypi.org/project/PyMySQL/), was used for the purposes of this project.
- [bcrypt](https://pypi.org/project/bcrypt/) is a PyPI library for Python that allows you to hash passwords. Hashing is the process of taking input and using a mathematical formula to chop and mix it up to produce an output of a specific length. Hashing is a one-way function, meaning that it can easily convert input to a fixed-size output, but it is difficult to invert, or convert in the opposite direction. This attribute allows developers to secure passwords when authenticating users for their applications.
  - [Cryptography PyPl Package](https://pypi.org/project/cryptography/) is a dependency of ``bcrypt`` that I needed to install in order to use it in my application.
- [python-dotenv](https://pypi.org/project/python-dotenv/) is a PyPI dotenv package used to manage environment variables inside Python's native virtual environment, or ``venv``. This virtual environment is a self-contained directory that can maintain its own version of Python as well as its own library dependencies so that multiple Python projects can reside on the same machine without interfering with each other.
- [Gunicorn](https://docs.gunicorn.org/en/stable/), or Green Unicorn, is a Python HTTP Server for UNIX that is broadly compatible with various web frameworks (including Python and Flask), simply implemented, light on server resources, and fast.
  - [Gunicorn PyPL Package](https://pypi.org/project/gunicorn/), was used for the purposes of this project.

## So why did I use Python when the same app can be built with Node?

Python is one of the most widely used high-level programming languages, with the [TIOBE](https://www.tiobe.com/tiobe-index/) index naming it the second most popular language out of 100 in 2020. It's an interpreted, high-level, open-source, general-purpose programming language that supports procedural, object-oriented, and some functional programming constructs. Created by Guido van Rossum between 1985 and 1990, Python is currently used in such fields as web development, data science, and DevOps.  

<p align="center">
  <img width="953" height="386" src="https://user-images.githubusercontent.com/52815609/149565520-226a9f4a-9741-496d-9861-7b7e163380f2.png">
</p>

Python has seen an increase in popularity with the rise of big data—in which extremely large datasets are analyzed computationally to reveal patterns, trends, and associations, especially relating to human behavior and interactions. Python can help us mine big data much faster than any other programming language because it can handle any data type.

Python can also be easily integrated into web applications that need to implement machine learning. Machine learning is a quickly growing branch of artificial intelligence that's based on the idea that systems can learn from data, identify patterns, and make decisions with minimal human intervention.  

Just like most other popular programming languages, Python has several frameworks that can make it easier to use. The two most popular Python frameworks are [Flask](https://flask.palletsprojects.com/en/2.0.x/) and [Django](https://www.djangoproject.com/). You’ll use Flask in this course, but you can adapt the same concepts to a Django application.

To complete the refactoring, I connected the Just Tech News application to a relational database using SQLAlchemy, provide user authentication using Flask’s built-in session functionality, and deploy my app to the cloud using Heroku.
