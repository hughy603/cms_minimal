# cms_minimal
Django CMS merged with cookie cutter
This removes possibly unused cookiecutter dependencies, but keeps
the project structure.

# Initial Setup
- Setup application **`export App=cms_minimal`**
- Create Git repo
  - `git clone https://github.com/hughy603/$App`
  - `cd $App`
  - `touch .gitignore`
  - `touch .ebignore`
- Create Database
  - `sudo -u postgres createuser -D -A -P $App`
  - `sudo -u postgres createdb -O $App $App`
- Create virtual enviornment `mkvirtualenv $App`
- Copy secrets `cp ~/.virtualenvs/cms_tutorial/bin/post* ~/.virtualenvs/$App/bin/`
  - *Localized to my machine's past projects*
- Edit secret DB settings `vi ~/.virtualenvs/$App/bin/postactivate`
- Install Basic Dependencies
  1. `pip install django`
  2. `pip install django-environ`
- Start a project `django-admin startproject $App`
  - `cd $App/`
- Create configuration directories
  - `mkdir -p config/settings`
  - `touch config/__init__.py`
  - `touch config/settings/__init__.py`
- Setup Urls and WSGI
  - `mv $App/urls.py $App/wsgi.py config/`
  - Modify urls.py and wsgi.py
    - **See git repo for example**
- Create migration location
  - *Need to understand why this is reccomended for the MIGRATION_MODULES setting*
  - `mkdir -p cms_minimal/contrib/sites/migrations`
  - `touch cms_minimal/contrib/__init__.py`
  - `touch cms_minimal/contrib/sites/__init__.py`
  - `touch cms_minimal/contrib/sites/migrations/__init__.py`
- Setup Settings
  - `mv cms_minimal/settings.py config/settings/common.py`
  - Modify common.py to match git `vi config/settings/common.py`
  - Modify local.py to match git `vi config/settings/local.py`

# Example Venv scripts
**Never keep these in a repository**
## ~/.virtualenvs/$App/bin/postactivate
```
export POSTGRES_PASSWORD=random
export POSTGRES_USER=app_name
export POSTGRES_DB=app_name
export DATABASE_URL=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@127.0.0.1:5432/${POSTGRES_DB}

# General settings
export DJANGO_ADMIN_URL=
export DJANGO_SECRET_KEY='123'
```
## ~/.virtualenvs/$App/bin/postdeactivate
```
unset POSTGRES_PASSWORD
unset POSTGRES_USER
export POSTGRES_DB=cms_tutorial
unset DATABASE_URL

# General settings
unset DJANGO_ADMIN_URL
unset DJANGO_SECRET_KEY
```
