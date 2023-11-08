uvicorn app.main:app --reload

docker run --name mysql -v /home/homero/mysql-db:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=admin -e MYSQL_DATABASE=users -p 3306:3306 -d mysql
