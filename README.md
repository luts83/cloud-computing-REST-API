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
Install Nginx and apply the following contents to use the load balancing ans ssl.
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
- By sending lines of longitude and latitude using the Google Place API, it's used the API that sends the Korean restaurant within 100m radius of the location.
- By default, 1-10 of data has been stored in the AWS RDS currently and results can be checked up to 1-10 through GET method, and new data can be posted from 11th data by using POST method.
- Existing data can be updated by PUT method.
- It is possible to delete existing data by DELETE method.
* id is the number for todolist(it's applicable for autoincrement)
```
### RDS for SQL
Contents of existing databases stored in AWS RDS for SQL
```shell
ID,title,contents,lat,lng,created_at
'1','Queen Mary University of London updated','updated','51.524048','-0.040353','2020-04-17 10:49:57'
'2','Canary Wharf','Korean restaurant nearby','51.503425','-0.018629','2020-04-17 10:52:10'
'3','The National Gallery','Korean restaurant nearby','51.508975','-0.128449','2020-04-17 10:53:24'
'4','Big Ben','Korean restaurant nearby','51.500691','-0.124613','2020-04-17 10:54:19'
'5','The British Museum','Korean restaurant nearby','51.519509','-0.126645','2020-04-17 10:54:59'
'6','Trafalgar Square','Korean restaurant nearby','51.507979','-0.127987','2020-04-17 10:56:42'
'7','St. Paul Cathedral','Korean restaurant nearby','51.513323','-0.098276','2020-04-17 10:58:02'
'8','Hyde Park','Korean restaurant nearby','51.50814','-0.16659','2020-04-17 10:59:15'
'9','Buckingham Palace','Korean restaurant nearby','51.501683','-0.140952','2020-04-17 10:59:53'
'10','Covent Garden','Korean restaurant nearby','51.511461','-0.123785','2020-04-17 11:01:07'
```
Base url = https://54.172.123.183

GET /todolist/:id
```shell
curl -XGET --insecure https://54.172.123.183/todolist/:id
```
POST /todolist
```shell
curl -XPOST -H "Content-Type: application/json" -d '{ "title":"test_title", "contents":"test_contents", "lat":51.498538,  "lng":-0.026507 }' --insecure https://54.172.123.183/todolist
```
PUT /todolist/:id
```shell
curl -XPUT -H "Content-Type: application/json" -d '{ "title":"updated_test_title", "contents":"updated_test_contents", "lat":51.498538,  "lng":-0.026507 }' --insecure https://54.172.123.183/todolist/:id
```
DELETE /todolist/:id
```shell
curl -XDELETE --insecure https://54.172.123.183/todolist/:id
```
