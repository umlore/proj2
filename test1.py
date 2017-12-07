from flask import Flask, request, jsonify
import requests
import json


index_json_request = '{"query":["hello", "hi"],"ngrams":["hello"],"aliases":["hello","hell"]}'
the_headers = {"Content-Type": "application/json"}

inverted_index_json = requests.post('http://teamthorn.cs.rpi.edu:5000/ranking', data=index_json_request, headers=the_headers, timeout=1.000)

print(json.loads(inverted_index_json.content))

f = open('testing.txt','w')
f.write(json.loads(inverted_index_json.content))

f.close()