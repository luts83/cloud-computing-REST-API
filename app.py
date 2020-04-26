from flask import Flask, render_template, request, jsonify
import json
import requests
import pymysql


app = Flask(__name__)
urls = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=YOUR GOOGLE PLACE API KEY&location={location}&radius={radius}&type=restaurant&keyword=korean"


conn = pymysql.connect(host='database-1.crvfbd6sjy8i.us-east-1.rds.amazonaws.com', user='admin', password='123456789', db='API_test', charset='utf8')
curs = conn.cursor()


@app.route('/todolist/<id>', methods=['GET'])
def getTodoList(id):
    sql = "SELECT * FROM Todo_List WHERE id={id}".format(id=id)
    curs.execute(sql)
    todolist = curs.fetchone()
    
    response = {
        
    }
    if todolist:
        res = requests.get(urls.format(location=(str(todolist[3]) + "," + str(todolist[4])),radius=1000))
        response = {
            "id" : todolist[0],
            "title": todolist[1],
            "contents": todolist[2],
            "lat": todolist[3],
            "lng": todolist[4],
            "location" : res.json()
        }
        print(res)
    return jsonify(response)

@app.route('/todolist', methods=['POST'])
def createTodoList():
    title = request.json.get("title")
    contents = request.json.get("contents")
    lat = request.json.get("lat")
    lng = request.json.get("lng")
    print(title, contents, lat, lng)
    sql = "INSERT INTO Todo_List (title, contents, lat, lng) VALUES ('{title}', '{contents}' ,{lat} ,{lng})".format(
        title=title,
        contents=contents,
        lat=lat,
        lng=lng
    )
    
    
    curs.execute(sql)
    conn.commit()
    response = {
        "suceess" : True
    }
    status_code = 201
    return jsonify(response), 201

@app.route('/todolist/<id>', methods=['PUT'])
def updateTodoList(id):
    title = request.json.get("title")
    contents = request.json.get("contents")
    lat = request.json.get("lat")
    lng = request.json.get("lng")
    print(title, contents, lat, lng)

    sql = "UPDATE Todo_List SET title='{title}', contents='{contents}', lat={lat}, lng={lng} WHERE id={id}".format(
        id = id,
        title = title,
        contents = contents,
        lat = lat,
        lng = lng,
    )
    curs.execute(sql)
    conn.commit()

    response = {
        "suceess" : True
    }
    
    status_code = 201
    return jsonify(response), 200

@app.route('/todolist/<id>', methods=['DELETE'])
def deleteTodoList(id):
    sql = "DELETE FROM Todo_List WHERE id={id}".format(
        id=id,
    )
    curs.execute(sql)
    conn.commit()
    response = {
        "suceess" : True
    }
    
    status_code = 201
    return jsonify(response), 200


app.run(host='0.0.0.0', port=80)
