##Tweet Tempest

UI for building a proper tweetstorm.  It will break apart your large text into properly sized tweets, complete with 1/, 2/, etc as well as the ability to have the tweetstorm be directed at specific person(s).  It will mark each tweet to be a reply of the previous so Twitter's threading works properly.

Motivation for building this was a proof-of-concept with Django/Ng8.

### Backend Tech
- Django
- Python Social Auth
- Twitter
- Django Webpack Loader

### Frontend Tech
- Angular 8
- Lodash
-

### Status
Works but needs lots of polish still.  See TODO.md for details

### To Run
1. Create a python virtual env, activate the venv, and `pip install -r requirements.lock`,
2. Copy `secrets.sample` to `secrets.json`
3. `./manage.py generate_secret_key`, copy the value to `SECRET_KEY` in `secrets.json`
4. Create your own twitter app.  Fill in `CONSUMER_KEY` and `CONSUMER_SECRET` in `secrets.json`
5. Run `./manage.py runserver` in one window
6. Run `npm run watch` in another window
7. Browser to `http://127.0.0.1:8000/`
8. Log in with your Twitter account
