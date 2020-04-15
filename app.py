from cassandra.cluster import Cluster
from flask import Flask, render_template, request, jsonify
import json
import requests
import requests_cache
import time

cluster = Cluster(contact_points=['172.17.0.2'],port=9042)
session = cluster.connect()
app = Flask(__name__)

@app.route('/')
def hello():
        name = request.args.get("name","World")
        return('<h1>Hello, {}!</h1>'.format(name))

total_data = []
requests_cache.install_cache('koreanres_api_cache', backend='sqlite', expire_after=36000)

target = {"type" : "korean", "location" : (51.507437, -0.127658), "radius" : 50000}
urls = ["https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyCEo4dxn6iRqv8w-uTuyhqVit7TW_g3kUA&type=restaurant&location={},{}&keyword={}&radius={}".format(target["location"][0],target["location"][1],target["type"],target["radius"])]

@app.route('/korean_res', methods=['GET'])
def koreanres():
    resp = requests.get(urls[0])
    if resp.ok:
        return jsonify(resp.json())
    else:
        print(resp.reason)

@app.route('/korean_res/<name>')
def profile(name):
    rows = session.execute( """Select * From korean_res.korean_res where name = '{}' ALLOW FILTERING""".format(name))
    for korean_res in rows:
        return('<h1>{} has {} of user&#39;s rating!</h1>'.format(name,korean_res.rate_total))
    return('<h1>That korean restaurant does not exist!</h1>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

