# Deploying this application

**Before we begin**, an apology from the author of this README:

This might be the most convoluted deployment setup you might read. I write this
completely with the hope that there is some software that is more complex to deploy
and that the reader has the patience to follow the one below. If this frustrates
you, kindly find a better method for this project and make this document obsolete. 

## Pre-requisites

1. Install Python 3, with all the bells 

```shell script
sudo apt install python3 python3-dev python3-pip python3-venv python-gdal
```

2. Install the DB and related spatial stuff

```shell script
sudo apt install sqlite3 libsqlite3-mod-spatialite
```

3. Install Nginx Web Server. (this thing might already be there in the machine, just run the command anyway)

```shell script
sudo apt install nginx
```

## Setup a special user for running the application

```shell script
sudo adduser --no-create-home --disabled-password apps
```

This will ask a bunch of questions and finally create a user named `apps` that willnot have a home directory or a password.
This user exists for the sole purpose of executing the applications.

**Warning:** We should also add this user to some group, but I had forgotten how or why. So when your application doesn't
write files to disk, or has some other weird bug due to permissions, you have yourself to blame for, don't look at me.

## Get the code into the machine

I use sudo for all the commands including cloning because of the restrictions in my machine, you might run the following
without sudo:

```shell script
sudo mkdir /opt/apps
cd /opt/apps
sudo git clone https://github.com/covid19india/CovidCrowd.git
sudo chown -R apps:apps CovidCrowd  # set the ownership of this directory to apps user
```

**Heads Up:** You might need to do chown and a chmod 755 to this whole dir later if things break due to permissions

### Setup Virtual Environment

```shell script
cd /opt/apps/CovidCrowd
python3 -m venv env
```

### Copy the service file to system location

The application will be run as a system service. This will make sure that the application will run on boot. So rebooting
the VM will automatically bring the app online.

````shell script
sudo cp deployment/covidcrowd.service /etc/systemd/system/
````

Let us also create a couple of folders that this service will require

```shell script
sudo mkdir /var/run/covidcrowd  # this is where the application will have a unix socket
sudo chown -R apps:apps /var/run/covidcrowd
sudo mkdit /var/log/covidcrowd  # this is where the application will write its logs
sudo chown -R apps:apps /var/log/covidcrowd
```

**Warning:** You might have to set `chmod -R 755 ` or something like that on these folders if you have "cannot write"
errors. I don't remember doing it. But I will leave this comment in case you stumble.


### Configure Nginx

Edit the contents of `/etc/nginx/sites-available/default` to match the files `nginx.default` in this folder.
Or create a new file in sites-available and enable that site. Whatever floats your boat. I leave it to you.

```shell script
sudo systemctl restart nginx
```

### Setup the Django app

Login as the apps user for this, because whatever you create now will be used when the app is executed

```shell script
sudo su - apps
cd /opt/apps/CovidCrowd
cp example.env .env
```

Now edit the `.env` file to include the required values. The `DB_` stuff is not needed for this deployment as we are
using only the SQLite Database. You will need to set the SECRET_KEY, DEBUG_FLAG and MY_HOST values for the app to function.
`MY_HOST` will be added to the `ALLOWED_HOSTS` settings for the application. So set it to your app's public address.

**Note:** You will have to register OAuth applications with Github, Twitter and Google to add the Social login values.

Now let us setup the DB and the static files:

```shell script
# inside /opt/apps/CovidCreate as user apps
source venv/bin/activate
pip install -r requirements
python manage.py migrate
python manage.py collectstatic
exit
```
**Note**: pip install might need sudo to work without errors. if `sudo pip install -r requirements` doesn't work, try `sudo venv/bin/pip install -r requirements`

### Start the app

```shell script
sudo systemctl start covidcrowd
systemctl status covidcrowd
# Make sure the application is running
```


If you had followed every step of this document, the app should be alive at your web address.

If the site is actually live, count youself the luckiest person right now.
It took me half an hours to get the static files to serve.

If it is not working, welcome to world of DevOps. All the best for your README :)
