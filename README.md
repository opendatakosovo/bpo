# BPO
##### The Bangladesh Peace Observatory Platform

###### Advancing understanding of peace and tolerance through data insights
#
# Project description
>The Bangladesh Peace Observatory is a virtual platform equipped with mapping and data analytics technology that informs users on the state of violence – political, ethnic, communal, criminal, gender-based, as well as extremist – and other forms of discord in terms of time, space and themes.

> The Bangladesh Peace Observatory brings together different streams of publically available data, analyses and visualizes them in a useful and interactive way for decision makers, civil society and media to understand, consume, and debate.
The Bangladesh Peace Observatory seeks to support a wide range of actors in making better public policy decisions, tailored interventions and programming, enhanced research, and effective advocacy campaigning for social cohesion and peace development based on evidence and data.

> The BPO understands "violence" as defined by the World Health Organization (WHO) in its World report on violence and health (WRVH): "the intentional use of physical force or power, threatened or actual, against oneself, another person, or against a group or community, that either results in or has a high likelihood of resulting in injury, death, psychological harm, maldevelopment, or deprivation."

Hosted by the Centre for Genocide Studies, University of Dhaka.

# Technical Instructions
### 1. Server Installation
#### Environment
- Ubuntu 16.04 LTS 64 bit
- MongoDB 3.2.x
- Apache Virtual Hosts (httpd)

#### Initial Setup
Apache Virtual Host:
```
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi
```

Open the new file in your editor with root privileges:
```
sudo nano app.wsgi
```

And configure the project's path:
```
app_dir_path = '/var/www/bpo'
```

Create and edit project config file:
```
sudo cp config-template.cfg config.cfg
sudo nano config.cfg
```


#### Create New Virtual Host
Copy default virtual host config file to create new file specific to the project:
```
sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/peaceobservatory-cgs.org.conf
```

Open the new file in your editor with root privileges:
```
sudo nano /etc/apache2/sites-available/peaceobservatory-cgs.org.conf
```

And configure it to point to the project's app.wsgi file:
```
<VirtualHost *:80>
  ServerAdmin admin@localhost
  ServerName peaceobservatory-cgs.org

  WSGIScriptAlias / /var/www/bpo/app.wsgi
  <Directory /var/www/bpo>
    Order allow,deny
    Allow from all
  </Directory>

  ErrorLog ${APACHE_LOG_DIR}/error.log
  CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```

#### Enable New Virtual Host
First disable the defaul one:
```
sudo a2dissite 000-default.conf
```

Then enable the new one we just created:
```
sudo a2ensite peaceobservatory-cgs.org.conf
```

Restart the server for these changes to take effect:
```
sudo service apache2 restart
```


### 2. Local Installation (UBUNTU)


First create a folder in your desktop called dev:
```
cd ~
mkdir dev
cd dev
```

Getting the project in your local machine:
```
git clone https://github.com/opendatakosovo/bpo.git
cd bpo
```

Install and run the app:
```
bash install.sh
bash run-debug.sh
```

### 3. Run the importers
```
bash importer.sh
bash import-idams.sh
bash importer-census.sh
bash import-religion.sh
```


