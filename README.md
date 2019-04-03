# assemblage
We are in the develop branch of the project assemblage.
A library management system.

# Synopsis

This repository contains the code of ASSEMBLAGE, a library management system.

Python version used - 3.5.0

# Installation

To install the code follow the steps outlined here -

### Step 1 - Ensure all the dependencies are present

```
sudo apt-get install -y ipython3 python3-dev build-essential libssl-dev libffi-dev git python-virtualenv tcl sqlite3 libsqlite3-dev supervisor
```

### Step 2 - Create a new directory and clone repo from stash

```
sudo mkdir -p /var/www/apps/github/assemblage/
sudo chown $USER:`id -gn` /var/www/apps/github/assemblage/
cd /var/www/apps/github
unzip assemblage.gzip assemblage
cd /var/www/assemblage/
```
Note: $USER provides user login name, id -gn provides default user group

### Step 3 - Create a python virtual environment and install python packages

```
cd /var/www/apps/github/assemblage/
virtualenv -p python3.5 env
source env/bin/activate
pip install -r requirements.txt
```

### Step 4 - Create log directory

```
sudo mkdir /var/log/apps/assemblage/
sudo chown $USER:`id -gn` /var/log/apps/assemblage/
```

### Step 5a - Run your app using gunicorn

```
/var/www/apps/github/assemblage/env/bin/gunicorn assemblage:app -b 127.0.0.1:5025 --workers=4 --log-file /var/log/apps/assemblage/gunicorn_main.log --access-logfile /var/log/apps/assemblage/gunicorn_access.log --log-level debug --pid /var/log/apps/assemblage/assemblage.pid
```

### OR Step 5b - Run your app using supervisor to run it in the background

```
Copy assemblage.conf in the assemblage directory to /etc/supervisor/conf.d
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl restart assemblage
```

# Contributors

Niranjan Balasubramani <niranjany5070@gmail.com>
