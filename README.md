# Flask Service
### For microservice purpose
## Step installation and run your server 
1. Setup virtual environment
    ```shell
    python3 -m venv venv
    ```
2. Use virtual environment
    ```shell
    source venv/bin/activate
    ```
3. Install requirements
   ```shell
   pip install -r requirements.txt
   ```
4. Run http app
    ```shell
    python run.py http
    ```
   
## Migrations
#### Used alembic for migration
See the documentation https://alembic.sqlalchemy.org/en/latest
### Common tools usage 
1. ##### Generate migration, example :
    ```shel
    alembic revision -m "Create table users"
    ```
   You will got new file like this `834aca5b7697_create_table_users.py`
2. ##### Run migration
    ```shel
    alembic upgrade head
    ```