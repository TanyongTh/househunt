# Househunt

Househunt is a web-scraping tool to help house hunters explore their favorite suburbs for properties on sale from [RealEstate](https://www.realestate.com.au/buy) website and store in database or export it to CSV file.
### Live here:  http://househunt.ap-southeast-2.elasticbeanstalk.com/

## Future features
   - Export data to .csv file
   - Automatic scraping
   - Access user control
   - Modify data
   - Support multiple websites

## Technologies/Tools
   1. [Python 3.6.1](https://www.python.org/)
   2. [Django 1.11.1](https://www.djangoproject.com/)
   3. [PostgreSQL 9.6.3](https://postgresapp.com/)
   4. [Amazon Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/), [EC2](https://aws.amazon.com/ec2/),         [S3](https://aws.amazon.com/s3/), and [RDS](https://aws.amazon.com/rds/)
   5. [EB CLI 3.x](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-cmd-commands.html)
   6. [pgAdmin (optional)](https://www.pgadmin.org/)


## Getting Started

### To run web application locally

1. Grap project code from [this](https://github.com/TanyongTh/househunt.git) repository:
   ```
      $ git clone https://github.com/TanyongTh/househunt.git
   ```

2. Create virtual environment
   Open Terminal and run all these commands:
   ```
      $ cd dirname (dirname is a directory where you want to create virtualenv)
      $ python3 -m venv myenv
      $ cd myenv
      $ source bin/activate
   ```
   A cousor will change from **$**  ---->  **(myenv) $**

3. Install requirements.txt via pip:
   ```
      (myenv) $ cd househunt
      (myenv) $ pip3 install -r requirements.txt
   ```
   Deacticate env:
   ```
      $ deactivate
   ```
    
 4. Install PostgreSQL application and create new database:
    
    4.1 Go to https://postgresapp.com, download app and follow the instruction.
    4.2 After PostgreSQL running locally, go to terminal again and run commands:
    ```
      $ createdb `whoami`
      $ psql
      # CREATE USER adminpdb WITH PASSWORD 'adminpdb';
      # CREATE DATABASE househuntdb OWNER adminpdb;
    ```
   
    4.3 Check DATABASE configuration again in *settings.py*
   
     ```Python
         DATABASES = {
            'default': {
               'ENGINE': 'django.db.backends.postgresql_psycopg2',
               'NAME': 'househuntdb',
               'USER': 'adminpdb',
               'PASSWORD': 'adminpdb',
               'HOST': 'localhost',
               'PORT': '5432',
            }
         }
      ```
    
   5. Now you can set up the database schema, create a superuser, and run the app:
   
      ```
         (myenv) $ python manage.py migrate
         (myenv) $ python manage.py createsuperuser --username admin
         Enter email address: your email address
         Enter password: your password
         (myenv) $ python manage.py runserver

         Performing system checks...
         System check identified no issues (0 silenced).
         June 29, 2017 - 03:00:10
         Django version 1.11.1, using settings 'mysite.settings'
         Starting development server at http://127.0.0.1:8000/
         Quit the server with CONTROL-C.
      ```
   
 
 
## Test

    
## Deployment


## Acknowledgments 


