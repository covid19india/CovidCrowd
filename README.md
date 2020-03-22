# CovidCrowd

A crowd-sourcing platform for the Covid-19 Pandemic

## Workflow

![FlowChart](https://github.com/tecoholic/CovidCrowd/raw/master/docs/CovidCrowd-Workflow.png)


## Development

1. Install Spatial Data Requirements

#### For Ubuntu

```shell script
sudo apt install libsqlite3-mod-spatialite python-gdal
```
#### For Mac

```shell script
brew update
brew install spatialite-tools
brew install gdal
```

1. Setup virtual environment

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

## Populating the Database

The Raw Data sheet from the Google Sheets is dumped as a CSV file into the `data`
folder periodically and can be used for initializing or updating the database.

```shell script
python manage.py importcsv ./data/raw_data.csv
```

This will create a new report for every row that has a data entry. Mainly it looks
to see if the `Date Announced` column has a value. If the `Patient number` is
already present it will be skipped. So running multiple imports is not an issue.

**Note:** It will only generate "Report" objects and not "Patient" objects. You
 will have to manually create a patient based on the imported reports. Apologies
 for inconvenience during setup. We emphasize on clarity of data over simplicity
  of creating a patient record.
