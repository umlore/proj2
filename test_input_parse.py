from flask import Flask, request, jsonify
import requests
import json

#Import parsing functions to test
from rank import parseQueryJson, parseIndexTermsFromQuery

#Testing for input parsing from other groups
#Calls will be made directly from rank.py functions ignoring POST and GET calls

f = open('testing_input_parse.txt','w')

'''
THIS TEST BLOCK IS FOR TESTING THE parseQueryJson METHOD

'''
f.write("RESULTS FOR TESTING parseQueryJson: \n")

# ==============================
# TEST 1: Testing basic query 
# ==============================

# Create dummy data (dictionary)
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

json_query = query_dict

#Pass it into the parsing method
parse_query_result = parseQueryJson(json_query)

#Compare output to original input dictionary to make sure they are the same
json_equals_dict = query_dict == parse_query_result

#Write pass/fail results to output file
f.write("----- Test 1 -----\nTest Passed: %r\n" % json_equals_dict) 

# ==============================
# TEST 2: Testing an empty query
# ==============================
#Create dummy data (dictionary)
query_dict = {
   'search_id': None,
   'raw':
   {
       'raw_search': "",
       'raw_tokens': []
   },
   'transformed':
   {
       'transformed_search': "",
       'transformed_tokens': [],
       'transformed_bigrams': [],
       'transformed_trigrams': [],
   }
}

json_query = query_dict

#Pass it into the parsing method
parse_query_result = parseQueryJson(json_query)

#Compare output to original input dictionary to make sure they are the same
json_equals_dict = query_dict == parse_query_result

#Write pass/fail results to output file
f.write("----- Test 2 -----\nTest Passed: %r\n" % json_equals_dict) 

# ==============================
#TEST 3: Testing an empty input
# ==============================

#Pass it into the parsing method
parse_query_result = parseQueryJson(None)

#Compare output to original input dictionary to make sure they are the same
json_equals_dict = None == parse_query_result

#Write pass/fail results to output file
f.write("----- Test 3 -----\nTest Passed: %r\n" % json_equals_dict) 




'''
THIS TEST BLOCK IS FOR TESTING THE parseIndexTermsFromQuery METHOD

'''
f.write("RESULTS FOR TESTING parseIndexTermsFromQuery: \n")

# ==============================
# TEST 1: Testing basic query 
# ==============================

# Create dummy data (dictionary)
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

# Create expected output list to compare to


#Pass it into the parsing method
parse_query_result = parseQueryJson(json_query)

#Compare output to expected output to make sure it's the same
result_equals_list = query_dict == parse_query_result

#Write pass/fail results to output file
f.write("----- Test 1 -----\nTest Passed: %r\n" % result_equals_list) 

f.close()