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
  - Migrate useful settings from cookiecutter
- Install Dependencies
  - Start server until dependencies are met
  - In the future `pip -r requirements/local.py`
- Static File Structure
  - `mkdir -p cms_minimal/static/css/ cms_minimal/static/js`
  - `mkdir cms_minimal/templates`

# Example Venv scripts
**Never keep these in a repository**
## ~/.virtualenvs/$App/bin/postactivate
```
export POSTGRES_PASSWORD=random
export POSTGRES_USER=app_name
export POSTGRES_DB=app_name
export DATABASE_URL=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@127.0.0.1:5432/${POSTGRES_DB}

# General settings
export DJANGO_ADMIN_URL=^admin/
export DJANGO_SETTINGS_MODULE=config.settings.local
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
unset DJANGO_SETTINGS_MODULE
unset DJANGO_SECRET_KEY
```

# Install Django CMS
http://docs.django-cms.org/en/release-3.3.x/how_to/install.html
- Install requirements
  - `pip install django_cms`
  - `pip install djangocms-text-ckeditor`
  - `pip install 'django-reversion<2.0'`
- Configure config/settings/common.py
- Configure URLs
- Create base templates
  - cms_minimal/templates/base.html
  - cms_minimal/templates/feature.html
  - cms_minimal/templates/menu.html
  - cms_minimal/templates/page.html
- Database Setup
  - `python manage.py migrate`
- Test Configuration
  - `python manage.py cms check`

# alt-shift-f formats HTML
http://stackoverflow.com/questions/21190300/how-to-set-html-auto-indent-format-on-sublime-text-3
