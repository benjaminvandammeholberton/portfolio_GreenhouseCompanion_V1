Here is the way to run the backend server.
Make sure to have:

- python 3.9 or higher installed and pip
- mysql with root credentials

Works with UNIX

clone the repository
go to the repository : cd portfolio_GreenhouseCompanion

1. Create virtual environnement and activate: 'python3 -m venv venv' then 'source ./venv/bin/activate'
2. install python packages : pip install -r requirements.txt
3. set up database and : install/db_set/setup_mysql_dev.py
4. run the server : go back to main folder, then cd ./api/v1 and type the command flask run + options
5. from another terminal :curl http://127.0.0.1:5000 to verify if it s work, it supposed to answer json : {"error":"Not found"}
6. Add required datas to database (feel free to customize them in the data.json)user create_garden and create_vegetables_from_json

here are the differents routes to get the datas from api:
