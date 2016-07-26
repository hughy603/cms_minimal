# cms_minimal
Django CMS merged with cookie cutter

# Setup
- Create Git repo
- Create Database
  1. `sudo -u postgres createuser -D -A -P cms_minimal`
  2. `sudo -u postgres createdb -O cms_minimal cms_minimal`
- Create virtual enviornment `mkvirtualenv cms_minimal`
- Copy secrets `cp ~/.virtualenvs/cms_tutorial/bin/post* ~/.virtualenvs/cms_minimal/bin/`
- Edit secret DB settings `vi ~/.virtualenvs/cms_tutorial/bin/postactivate`
- Install Django `pip install django`
