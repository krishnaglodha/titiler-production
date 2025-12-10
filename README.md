# titiler-production
FastAPI Titiler deployment application

## Step 1 : clone the repo

go to `/opt/` and clone this repo

## Step 2 : Create virtualenv and install everything necessary 

```bash
cd /opt/titiler-production
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Step 3 : Make service file

Copy the `titiler.service` file and put it in `/etc/systemd/system` . Once done run following commands to activate file

```bash
sudo systemctl daemon-reload
sudo systemctl enable titiler
sudo systemctl start titiler
```

Check if service is running properly

```bash
sudo systemctl status titiler
```

## Step 4 : Configure Reverse Proxy

Make sure you have nginx installed. Copy  `/etc/nginx/sites-available/` called `titiler` and add following content


