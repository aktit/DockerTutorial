# DockerTutorial

This is tested on podman centos-8

#1. Install require packages

dnf install podman podman-plugins

#2. Create Network

podman network create flask

podman network ls

#3. Create mysql container

podman run -d --name mysql --network flask --network-alias mysql -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=testing mysql:5.7

#4. Run the DB model on the mysql container

podman cp testing.sql mysql:/tmp

podman exec -it mysql /bin/bash

mysql -u root -p'123456' -t < /tmp/testing.sql

#5. Create api image via Dockerfile

go to flask/api

podman build -t api .

#6 Run the api image

podman run -d --name api -p 5000:5000 --network flask --network-alias flaskapi localhost/api

populate the data via api with favourite internet browser

Eg:

GET method(view data)

http://youripaddress:5000

POST method(add data)
  
http://youripaddress:5000/John/Smith

PUT method(update data)
  
http://youripaddress:5000/1/John/Smith

DELETE method(delete data)
  
http://youripaddress:5000/1

#7 Create the app image via Dockerfile
  
go to flask/client
  
podman build -t app .

#8 Run the app image
  
podman run -d --name app -p 10000:10000 --network flask localhost/app

You can see your data after populating via api method(step 6).
