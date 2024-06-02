### Start server

- `source bin/activate`
- `uvicorn books-api.main:app --reload`

### Migrate

- `python3 database.py`


### Sources

- https://github.com/LinkedInLearning/advanced-python-practical-database-examples-4363655/blob/01_05e/books/books-api/database.py
- https://www.linkedin.com/learning/advanced-python-practical-database-examples


### Docker
Complete Docker Commands Summary
Here is a summary of the Docker commands you need:

Pull the MySQL image:

docker pull mysql:latest
Run the MySQL container with a mounted volume for persistence:

docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=your_password -v /my/own/datadir:/var/lib/mysql -d mysql:latest
Access the MySQL container:

docker exec -it mysql-container mysql -u root -p
With these steps, you should have a running MySQL instance in a Docker container, with a database and some records inserted into it.



Run with localhost and 3306 port
(base) vit@idea:~$ docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=kiwiapple -v /home/vit/work/volume:/var/lib/mysql -p 3306:3306 -d mysql:latest
f7fa2befa6462943cca6c63b84cb30aff12646e147b2a832623b25ee4e262129
(base) vit@idea:~$ 




### How to create virtual env
1. Create virtual env with pycharm
2. Run `pip install -r requirements-dev.txt`
