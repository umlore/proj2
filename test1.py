from flask import Flask, request, jsonify
import requests
import json


#index_json_request = '{"query":["hello", "hi"],"ngrams":["hello"],"aliases":["hello","hell"]}'
the_headers = {"Content-Type": "application/json"}

updated_query_request = '{"search_id":69,"raw":{"raw_search":"query test example","raw_tokens":["query","test","example"]},"transformed":{"transformed_search":"what even goes here","transformed_tokens":["what","even","goes","here"],"transformed_bigrams":["query test","test example"],"transformed_trigrams":["query test example"]}}'

inverted_index_json = requests.post('http://teamthorn.cs.rpi.edu:5000/ranking', data=updated_query_request, headers=the_headers, timeout=1.000)

print(json.loads(inverted_index_json.content))

f = open('testing.txt','w')
f.write(str(json.loads(inverted_index_json.content)))

f.close()