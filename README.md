# SPOJ Ranker
(SPOJ)[https://www.spoj.com/] is a popular online judge containing problems on algorithms and data structures. This application takes handles, scrapes relevant data, stores it in SQLite database and shows a leaderboard which is sorted according to each handle's points. For demo - (youtube/)[https://www.youtube.com/watch?v=hPNCQe4x_T4&feature=youtu.be].

##Requirements
* Python 3.x
* pip
* requests (Run pip install requests)
* bs4 (Beautiful Soup, Run pip install bs4)

##Usage
* Clone this repository.
* Run python manage.py makemigrations
* Run python manage.py migrate
* Run python manage.py runserver

This will serve your django application at localost:8000 by default.
