# Lightrail

A simple program that accepts GTFS zip files and returns data via an API. The program allows users to upload zip file containing GTFS bundle and import it into database. It returns hyperlinked list of Stops via API and each stop should return schedule that can be filtered by weekday. The program also returns hyperlinked list of Trips with start and end time via the trips API.

## Introduction

The program is written in Python Django. The program works well and solves the problem. The program is written following the common naming convention of its respective language.

Before going to the next sections, make sure that you have this project on your local machine.

## Python

### How to run?

- Assuming that you have [Python 3.10](https://www.python.org/downloads) installed

- Open a terminal at the project directory and run the commands below to install Python Django and install Rest Django Framework package

```
pip install django
```

```
pip install djangorestframework
```

- Apply migrations by calling migrate
```
python manage.py migrate
```


- To run the program, we use the command
```
python manage.py runserver
```

The program will pop up a local host link, you can click the link to see the endpoints that are available to use. Once you put the correct API, it will return the corresponding data.

