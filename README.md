# CovidCrowd

A crowd-sourcing platform for the Covid-19 Pandemic

## Workflow

![FlowChart](https://github.com/tecoholic/CovidCrowd/raw/master/docs/CovidCrowd-Workflow.png)


## Development

1. Install SQLite3 and Spatialite

```shell script
sudo apt install libsqlite3-mod-spatialite
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
# Edit the .env file according to your needs

sudo apt-get install libsqlite3-mod-spatialite
```

4. Generate the local db

```shell script
python manage.py migrate
```

5. To access the admin pages - create a super user

```shell script
python manage.py createsuperuser
```
