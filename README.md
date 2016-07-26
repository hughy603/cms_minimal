# cms_minimal
Django CMS merged with cookie cutter

# Setup
- Setup application **`export App=cms_minimal`**
- Create Git repo
  - `git clone https://github.com/hughy603/cms_minimal`
  - `cd cms_minimal`
  - `touch .gitignore`
  - `touch .ebignore`
- Create Database
  - `sudo -u postgres createuser -D -A -P cms_minimal`
  - `sudo -u postgres createdb -O cms_minimal cms_minimal`
- Create virtual enviornment `mkvirtualenv cms_minimal`
- Copy secrets `cp ~/.virtualenvs/cms_tutorial/bin/post* ~/.virtualenvs/cms_minimal/bin/`
- Edit secret DB settings `vi ~/.virtualenvs/cms_tutorial/bin/postactivate`
- Install Django `pip install django`
- Start a project `django-admin startproject cms_minimal`
  - `cd cms_minimal/`
- Create configuration directory
  - `mkdir -p config/settings`
  - touch config/__init__.py
  - touch config/settings/__init__.py
  - mv cms_minimal/urls.py config/
  - cms_minimal/wsgi.py
