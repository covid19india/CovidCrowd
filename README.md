# CovidCrowd

A crowd-sourcing platform for the Covid-19 Pandemic

> This is NOT the project that powers the Covid 19 India Dashboard. [Click here](https://github.com/covid19india/covid19india-react) to switch to the dashboard project.

## Workflow

**Note:** This workflow was never fully implemented. The primary data collection is still based out of Google Sheets

![FlowChart](https://github.com/tecoholic/CovidCrowd/raw/master/docs/CovidCrowd-Workflow.png)


## Development Setup for Backend

1. Install Spatial Data Requirements

#### For Ubuntu

```shell script
sudo apt install libsqlite3-mod-spatialite python-gdal
sudo apt-get install memcached libmemcached-tools -y
```
#### For Mac

```shell script
brew update
brew install spatialite-tools
brew install gdal
```

2. Setup virtual environment

```shell script
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

3. Create a new `.env` from `example.env` and populate the values

```shell script
cp example.env .env
# Edit the .env file according to your needs. If you are new to decouple library read this https://pypi.org/project/python-decouple/
```

4. Generate the local db

```shell script
python manage.py migrate
```

5. To access the admin pages - create a super user

```shell script
python manage.py createsuperuser
```

6. Start local development server

```shell script
python manage.py runserver
```

## Populating the Database

The Raw Data sheet from the Google Sheets is dumped as a CSV file into the `data`
folder periodically and can be used for initializing or updating the database.

```shell script
python manage.py importcsv ./data/raw_data.csv
```

This will create a new report for every row that has a data entry. Mainly it looks
to see if the `Date Announced` column has a value. If the `Patient number` is
already present it will be skipped. So running multiple imports is not an issue.

You can also load the patient travel history into the project using

```shell script
python manage.py importcsv ./data/travel_history.csv --type travel
``` 

### Development Setup for the frontend

There are two frontends for this application:

1. Server side rendered frontend based on Django Templates. This frontend has the crowdsourcing functionality.
2. Client side rendered frontend based on React. This is just provides a table interface and patient details page for browsing the patient database.

There is nothing to be done for the Django based frontend. This Backend setup would automatically handle this.

### Setting up the React Frontend

Install all the node dependencies and start the development server.

```shell script
cd frontend
yarn
yarn start
```

## A Note about caching

Due to the high traffic load a number of Django views are cached. This might interfere with your development.
See `patients/urls.py` for all the cached views and their durations.
