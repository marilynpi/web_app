#!/bin/bash

# Get enviroment variables
source ../.env

# Create Database
sudo -u postgres psql -c "CREATE DATABASE web_app;"
sudo -u postgres psql -c "CREATE USER web_app_user WITH PASSWORD 'web_app_password';"
sudo -u postgres psql -c "ALTER ROLE web_app_user SET client_encoding TO 'utf8';"
sudo -u postgres psql -c "ALTER ROLE web_app_user SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE web_app_user SET timezone TO 'UTC';" 
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE web_app TO web_app_user;"

# Start service
echo "Start PostgreSql service..." 
sudo service postgresql start
