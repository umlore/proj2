from flask import Flask, request, jsonify
import requests
import json

#Import parsing functions to test
from rank import parseQueryJson, parseIndexTermsFromQuery

#Testing for input parsing from other groups
#Calls will be made directly from rank.py functions ignoring POST and GET calls

'''
THIS TEST BLOCK IS FOR TESTING THE parseQueryJson METHOD

'''
f = open('testing_input_parse.txt','w')
f.write("RESULTS FOR TESTING parseQueryJson: \n")

#TEST 1: Testing basic query
#Create dummy data (dictionary) and jsonify
query_dict = {
   'search_id': 123,
   'raw':
   {
       'raw_search': "dank memes website cat .gif",
       'raw_tokens': ["dank", "memes", "website", "cat", ".gif"]
   },
   'transformed':
   {
       'transformed_search': "dank memes website cat gif",
       'transformed_tokens': ["dank", "memes", "website", "cat", "gif"],
       'transformed_bigrams': ["dank memes", "memes website", "cat gif"],
       'transformed_trigrams': ["dank memes website", "cat gif website", "meme cat website", "meme gif website"],
   }
}

json_query = jsonify(query_dict)

#Pass it into the parsing method
parse_query_result = parseQueryJson(json_query)

#Compare output to original input dictionary to make sure they are the same
json_equals_dict = query_dict == parse_query_result

#Write pass/fail results to output file
f.write("----- Test 1 -----\nTest Passed: %r\n" % json_equals_dict) 


f.close()