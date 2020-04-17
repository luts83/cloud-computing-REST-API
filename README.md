# Cloud computing REST API
mini_project
```shell
AWS EC2 ubuntu
AWS RDS for mysql
Docker
Nginx
Python flask
Google Place API
```
### Installation
```shell
cd /home
git clone https://github.com/luts83/mini_project
cd mini_project
```
### Run
```shell
# Login for Docker repository
docker login
docker pull luts83/mini_project:latest
or
# Just bulid the Docker image
sudo docker build --tag=mini_project:v1 .
sudo docker run -p 8000:80 mini_project:v1
sudo docker run -p 8001:80 mini_project:v1
sudo apt-get install nginx
sudo service nginx start
```
### nginx.conf
Install Nginx and apply the following contents to use the load balancing.
```shell
upstream myserver {
        server 54.172.123.183:8000;
        server 54.172.123.183:8001;
}

server {
        listen       80;
        server_name  54.172.123.183;
        rewrite ^ https://$server_name$request_uri? permanent;
}

server {
        listen  443 ssl;
        listen [::]:443 ssl;
        server_name 54.172.123.183;

        ssl_certificate /home/ubuntu/mini_project/labyu.crt;
        ssl_certificate_key /home/ubuntu/mini_project/labyu.key;
        ssl on;

        location / {
                proxy_pass http://myserver;
        }
}
```
### API
```shell
1. By sending lines of longitude and latitude using the Google Place API, it's used the API that sends the Korean restaurant within 100m radius of the loc$
2. By default, 1-10 of data has been stored in the AWS RDS and results can be checked up to 1-10 through GET method, and new data can be posted from 11 th$
3. Existing information can be updated by PUT method.
4. It is possible to delete existing information by DELETE method.
* id is the number for todolist(it's applicable for autoincrement)
```
Base url = https://54.172.123.183

GET /todolist/:id
```shell
curl -XGET --insecure https://54.172.123.183/todolist/:id
```
POST /todolist
```shell
curl -XPOST -H "Content-Type: application/json" -d '{ "title":"test_title", "contents":"test_contents", "lat":51.498538,  "lng":-0.026507 }' --insecure ht$
```
PUT /todolist/:id
```shell
curl -XPUT -H "Content-Type: application/json" -d '{ "title":"updated_test_title", "contents":"updated_test_contents", "lat":51.498538,  "lng":-0.026507 }$
```
DELETE /todolist/:id
```shell
curl -XDELETE --insecure https://54.172.123.183/todolist/:id
```
