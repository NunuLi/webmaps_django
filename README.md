# webmaps_django
A project displays user's [ArcGIS JavaScript](https://developers.arcgis.com/javascript/3/) applications using Django Web Framework.

## Django 
Django is a free and open-source web framework, written in Python, which follows the **model-view-template** architectural pattern. 
## Set up on your localhost
### Requirements
1. Python3
2. Django
```bash
$ pip install django
```
### Install and run locally
1. Clone or download from github.
2. *cd* to the first webmap folder where holds manage.py.
3. Start the Django development server. By default, this will start the development server on the internal IP and port 8000.  
```bash
$ python3 manage.py runserver
```
4. You should be able to see the following message. *Note: This is a server provided by Django and it's only intended for use while developing.*
```bash
Performing system checks...

System check identified no issues (0 silenced).
May 22, 2018 - 10:07:40
Django version 2.0.5, using settings 'webmaps.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
### How this website works
1. Open a browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
2. Log in through the **log in** link. We only have two users in the database right now.
3. After log in, You will go back to the home page. The home page will be update with only the applications that user have.
4. Click on the application link. You can go to each ArcGIS Javascript application page.
5. Log out from the home page when you want to leave.

## Design of website
### URL
A URL pattern is simply the general form of a URL - for example in this website the url looks like this: //homepage/app_id/.

To get from a URL to a view, Django uses what are known as ‘URLconfs’. A URLconf maps URL patterns to views.
There are two URLconf in this website. One is in the project folder (webmaps/webmaps/urls.py), another one is in the *maps* application folder (webmaps/maps/urls.py). 
### Model
Model contains the essential fields and behaviors of the data you're storing. Generally, each model maps to a single database table. In our simple website, we only have two models, **User** and **App**.

**User**

We use the user object from authentication system comes with Django, and import it in the model (webmaps/maps/models.py). User objects are the core of the authentication system. They typically represent the people interacting with your site and are used to enable things like restricting access, registering user profiles, associating content with creators etc.
```python
from django.contrib.auth.models import User
```
The current User table looks like:
```
ID  |name|password
----|----|----
1   |Yiran|Dreamyira 
2   |Emma|Dreamemma
```

**App**

App model is defined with three attributes: 

1. id (**primary key**, added automatically)

2. user_id (**foreign key**, one user can have multiple map apps)

3. app_text (name of the map app)

The current App table looks like:
```
ID  |user_id|app_text
----|----|----
1   |2|Emma's first app 
2   |2|Emma's second app
3|1|Yiran's first app
4|1|Yiran's second app
```
### View
A view is a “type” of Web page in Django application that generally serves a specific function and has a specific template.

**IndexView**

Diaplay the homepage and update it with only the applications related to this user after login.

**detail**

Display the specific ArcGIS JavaScript application according to application id.

### Template
Template is a convenient way to generate HTML dynamically. A template contains the static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted. It holds HTML page and determines the appearance of website.
#### Home
Displays the home page.
#### Log in
Provide a form for user to log in.
#### ArcGIS JS webpages
Each page contains a ArcGIS JavaScript application.
