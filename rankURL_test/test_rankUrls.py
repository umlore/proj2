from flask import Flask, request, jsonify
import requests
import json

#Import parsing functions to test
from rank import rankUrls

import sys
import os
sys.path.append(os.path.abspath('./rankURL_test'))
from rankURL_test2 import queries, page_rank, inverted_index


sorted_adocs = rankUrls(queries, page_rank, inverted_index)
print(sorted_adocs)
