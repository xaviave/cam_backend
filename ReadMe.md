# 42 Electronics Camera Backend Tool


## Install command
    sudo apt-get update && sudo apt upgrade
    sudo apt install openssl
    sudo apt -y install python-pip python-dev libpq-dev postgresql postgresql-contrib postgresql-server-dev-NN
    sudo service postgresql start
    
Then in postgresql create your user and the database

Launch this command: `sudo -u postgres psql`

the env var is like this `DATABASE_URL=psql://gmx:1234@127.0.0.1:5432/camera_backend_db`
so adapt your psql command with the right variable
    
    CREATE ROLE gmx;
    CREATE DATABASE camera_backend_db;
    CREATE USER gmx WITH PASSWORD '1234';
    ALTER ROLE gmx SET default_transaction_isolation TO 'read committed';
    GRANT ALL PRIVILEGES ON DATABASE camera_backend_db TO gmx;
    \q

Let's install all the python requirements

    python3.8 -m pip install --upgrade pip
    pip3.8 install -r requirements/requirements.txt

Export the env variables for the project

    set -a && . env/.env && set +a

Then simply launch these commands once and the site is initialised

    python3.8 manage.py makemigrations polls io_ssh
    python3.8 manage.py migrate
    python3.8 manage.py createsuperuser

Then launch the server

    python3.8 manage.py runserver
    
