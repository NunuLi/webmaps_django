# webmaps_django
A project displays user's [ArcGIS JavaScript](https://developers.arcgis.com/javascript/3/) applications using Django Web Framework.

## Django 
Django is a free and open-source web framework, written in Python, which follows the **model-view-template** architectural pattern. 
## Set up on your localhost
#### Requirements
1. Python
2. Django
```bash
pip install django
```
#### Install and run locally
1. Clone or download from github.
2. *cd* to the first webmap folder where holds manage.py.
3. Start the Django development server. By default, this will start the development server on the internal IP and port 8000.  
```bash
python3 manage.py runserver
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
#### How this website works
