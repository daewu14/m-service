# M-Service
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
    python3 run.py http
    ```

## UCase
### Tools usage
1. ##### Generate new ucase
    ```shell
    python3 run.py ucase new
    ```
    - ```
       Folder new ucase : {new-ucase-folder-name}
      ```
    - ```
       New UCase name (on app/ucase/package) : {new-ucase-name}
      ```
    **Result :** Success create new ucase package with 1 ucase
1. ##### Generate existing ucase folder
    ```shell
    python3 run.py ucase update
    ```
    - ```
       Folder existing ucase : {existing-ucase-folder-name}
      ```
    - ```
       New UCase name (on app/ucase/package) : {new-ucase-name}
      ```
    **Result :** Success create new ucase package with 1 ucase

## Migrations
### Common tools usage 
1. ##### Generate migration, example :
    ```shel
    python3 run.py migration --create="create table users"
    ```
   You will got new file like this `migrations/1739724108_321825_create_table_users.py`
2. ##### Run migration up
    ```shel
    python3 run.py migration --migrate=up
    ```
3. ##### Run migration down
    ```shel
    python3 run.py migration --migrate=down
    ```