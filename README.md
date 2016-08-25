Projects using this template
=============================

* [Topic and Sentiment Analysis Engine](https://github.com/pivotalsoftware/tasa)
* [Content Based Image Retrieval](https://github.com/gautamsm/cbirapp/)
* [Lateral Movement Detection](https://github.com/pivotalsoftware/dsmlatmov)
* [Predictive Maintenance for Drilling Operations](https://github.com/pivotalsoftware/dsmiot)
* [Audio Fingerprinting](https://audiofingapp.pcf1-rdu.nasa.pivotal.io/)

![TASA demo](https://github.com/pivotalsoftware/tasa/raw/gh-pages/images/tasacf_animated_highres.gif)
![CBIR demo](https://github.com/gautamsm/cbirapp/raw/gh-pages/images/cbirapp_animated.gif)
![Lateral movement demo](https://github.com/pivotalsoftware/dsmlatmov/raw/gh-pages/img/dsmlatmov_1080p.gif)
![Predictive Maintenance for Drilling Operations](https://github.com/pivotalsoftware/dsmiot/raw/gh-pages/img/predim_1080p.gif)
![Audio Fingerprinting Animated gif](https://github.com/regunathanr/audio_fingerprinting_mpp/raw/gh-pages/images/audio_fing_demo.gif)


Boilerplate for Flask Apps for Data Science on PCF
===================================================

This repo contains boilerplate code to build your apps on PCF using Flask and psycopg2.
You can checkout this repo into a remote empty repo of your own on GitHub or elsewhere, and customize it appropriate to spin up your own app.
For instance, to use this boiletplate as the building block for your own PCF app, you can do the following:

1. Create an empty repo on GitHub, let's call it MyApp and let's say it's URL is `https://github.com/vatsan/myapp.git`
2. Run `git clone https://github.com/vatsan/dspcfboilerplate.git`. This will clone the boilerplate repo into a local folder on your machine.
3. Rename the cloned repo to whatever you choose it to be (ex: myapp) `mv dspcfboilerplate myapp`
4. From your renamed directory containing the boilerplate (`myapp`), run the following to push the boilerplate code to your newly created GitHub repo `myapp`

        git remote rm origin
        git remote add origin https://github.com/vatsan/myapp.git
        git push origin master


Now your repo `myapp`, will contain the boilerplate code. You may start customizing this repo for your app going forward (ex: changing application name, author, contact info, images etc.)

Pre-requisites
==============

The `conda_requirements.txt` file lists all the python packages that are available via `conda` and are pre-requisites for this app.
The `requirements.txt` file lists all python packages that are only available through `pip` and are pre-requisities for this app.

Code Organization
==================

    dspcfboilerplate/ # root level folder containing all package files & app files
        README.md # This file
        conda_requirements.txt # file containing all `conda` packages needed by this app.
        requirements.txt # file containing all `pip` packages needed by this app (not available via `conda`)
        deploy # bash script to deploy this app (either locally or on PCF)
        setup.py # python packaging tools
        MANIFEST.in #Manifest file for python packaging (what files to include into the python package)
        LICENSE.txt #License for this app    
        dspcfapp/
            server.py #Main module containing all controller code
            static/
               css/ #All user specified css. These will be bundled & minified into "gen/user_css.css" by Flask-Assets.    
               data/   
               img/    
               js/ #All user specified javascript. These will all be bundled & minified into "gen/user_js.js" by Flask-Assets.    
               vendor/ #All bootstrap.js related files (css & javascript)
            templates/ #HTML templates
               layout.html  #Base layout from which every page will inherit. This also contains javascript & css inserts
               home.html #home page template
               about.html #about page template
               contact.html #contact page template 

Pushing the app to Heroku with Heroku Postgres as a service
============================================================

In preparation to push your app to Heroku, first install [Heroku CLI](https://toolbelt.heroku.com/osx).

Clone the dspcfboilerplate app
```
git clone https://github.com/vatsan/dspcfboilerplate.git
```

Switch to the heroku branch in the repo
```
cd dspcfboilerplate
git checkout heroku
```

Create an app on Heroku
```
heroku create --app dspcfboilerplate
```

If you have multiple orgs on Heroku, specify the org name in which you'd like to create this app.
```
heroku create --app dspcfboilerplate --org <ORG_NAME>
```

Take a look at the Procfile to get an understanding of how to spin-up the app. 

Create a Heroku Postgres instance and attach it to your app.
You can spin-up a [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql) service instance from the [add-ons section](https://elements.heroku.com/addons) on Heroku. Once you spin it up, bind it to your dspcfapp from the UI or via commandline.


You can push the app to Heroku using the following command.
```
git add .
git commit -m '<commit message>'
git push heroku heroku:master
```

You should see something like the following:

```
Counting objects: 238, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (151/151), done.
Writing objects: 100% (238/238), 6.84 MiB | 260.00 KiB/s, done.
Total 238 (delta 105), reused 167 (delta 67)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Python app detected
remote: -----> Installing python-2.7.12
remote:      $ pip install -r requirements.txt
remote:        Collecting psycopg2 (from -r requirements.txt (line 1))
remote:          Downloading psycopg2-2.6.2.tar.gz (376kB)
remote:        Collecting flask-assets (from -r requirements.txt (line 2))
remote:          Downloading Flask-Assets-0.11.tar.gz
remote:        Collecting jsmin (from -r requirements.txt (line 3))
remote:          Downloading jsmin-2.2.1.tar.gz
remote:        Collecting pandas (from -r requirements.txt (line 4))
remote:          Downloading pandas-0.18.1-cp27-cp27m-manylinux1_x86_64.whl (14.2MB)
remote:        Collecting gunicorn (from -r requirements.txt (line 5))
remote:          Downloading gunicorn-19.6.0-py2.py3-none-any.whl (114kB)
remote:        Collecting Flask>=0.8 (from flask-assets->-r requirements.txt (line 2))
remote:          Downloading Flask-0.11.1-py2.py3-none-any.whl (80kB)
remote:        Collecting webassets>=0.11 (from flask-assets->-r requirements.txt (line 2))
remote:          Downloading webassets-0.11.1.tar.gz (171kB)
remote:        Collecting pytz>=2011k (from pandas->-r requirements.txt (line 4))
remote:          Downloading pytz-2016.6.1-py2.py3-none-any.whl (481kB)
remote:        Collecting python-dateutil (from pandas->-r requirements.txt (line 4))
remote:          Downloading python_dateutil-2.5.3-py2.py3-none-any.whl (201kB)
remote:        Collecting numpy>=1.7.0 (from pandas->-r requirements.txt (line 4))
remote:          Downloading numpy-1.11.1-cp27-cp27m-manylinux1_x86_64.whl (15.3MB)
remote:        Collecting itsdangerous>=0.21 (from Flask>=0.8->flask-assets->-r requirements.txt (line 2))
remote:          Downloading itsdangerous-0.24.tar.gz (46kB)
remote:        Collecting Werkzeug>=0.7 (from Flask>=0.8->flask-assets->-r requirements.txt (line 2))
remote:          Downloading Werkzeug-0.11.10-py2.py3-none-any.whl (306kB)
remote:        Collecting Jinja2>=2.4 (from Flask>=0.8->flask-assets->-r requirements.txt (line 2))
remote:          Downloading Jinja2-2.8-py2.py3-none-any.whl (263kB)
remote:        Collecting click>=2.0 (from Flask>=0.8->flask-assets->-r requirements.txt (line 2))
remote:          Downloading click-6.6.tar.gz (283kB)
remote:        Collecting six>=1.5 (from python-dateutil->pandas->-r requirements.txt (line 4))
remote:          Downloading six-1.10.0-py2.py3-none-any.whl
remote:        Collecting MarkupSafe (from Jinja2>=2.4->Flask>=0.8->flask-assets->-r requirements.txt (line 2))
remote:          Downloading MarkupSafe-0.23.tar.gz
remote:        Installing collected packages: psycopg2, itsdangerous, Werkzeug, MarkupSafe, Jinja2, click, Flask, webassets, flask-assets, jsmin, pytz, six, python-dateutil, numpy, pandas, gunicorn
remote:          Running setup.py install for psycopg2: started
remote:            Running setup.py install for psycopg2: finished with status 'done'
remote:          Running setup.py install for itsdangerous: started
remote:            Running setup.py install for itsdangerous: finished with status 'done'
remote:          Running setup.py install for MarkupSafe: started
remote:            Running setup.py install for MarkupSafe: finished with status 'done'
remote:          Running setup.py install for click: started
remote:            Running setup.py install for click: finished with status 'done'
remote:          Running setup.py install for webassets: started
remote:            Running setup.py install for webassets: finished with status 'done'
remote:          Running setup.py install for flask-assets: started
remote:            Running setup.py install for flask-assets: finished with status 'done'
remote:          Running setup.py install for jsmin: started
remote:            Running setup.py install for jsmin: finished with status 'done'
remote:        Successfully installed Flask-0.11.1 Jinja2-2.8 MarkupSafe-0.23 Werkzeug-0.11.10 click-6.6 flask-assets-0.11 gunicorn-19.6.0 itsdangerous-0.24 jsmin-2.2.1 numpy-1.11.1 pandas-0.18.1 psycopg2-2.6.2 python-dateutil-2.5.3 pytz-2016.6.1 six-1.10.0 webassets-0.11.1
remote:
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 77.4M
remote: -----> Launching...
remote:        Released v3
remote:        https://dspcfboilerplate.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/dspcfboilerplate.git
 * [new branch]      heroku -> master
 ```

 The app will now be accessible at: [https://dspcfboilerplate.herokuapp.com/](https://dspcfboilerplate.herokuapp.com/)


Screenshots
============

Here are some sample screenshots of the boilerplate app in action:

![screen_1](docs/images/dspcfboilerplate_screen_1.png)

![screen_2](docs/images/dspcfboilerplate_screen_2.png)

![screen_3](docs/images/dspcfboilerplate_screen_3.png)



