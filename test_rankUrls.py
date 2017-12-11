from flask import Flask, request, jsonify
import requests
import json

#Import parsing functions to test
from rank import rankUrls

import sys
import os
sys.path.append(os.path.abspath('./rankURL_test'))

from rankURL_test1 import queries, page_rank, inverted_index
sorted_adocs = rankUrls(queries, page_rank, inverted_index)
for doc in sorted_adocs:
    print(doc.document)
print('\n')

from rankURL_test2 import queries, page_rank, inverted_index
sorted_adocs = rankUrls(queries, page_rank, inverted_index)
for doc in sorted_adocs:
    print(doc.document)
print('\n')

#  print(sorted_adocs[0].document)

from rankURL_test3 import queries, page_rank, inverted_index
sorted_adocs = rankUrls(queries, page_rank, inverted_index)
for doc in sorted_adocs:
    print(doc.document)
print('\n')

#  print(sorted_adocs[0].document)

from rankURL_test4 import queries, page_rank, inverted_index
sorted_adocs = rankUrls(queries, page_rank, inverted_index)
for doc in sorted_adocs:
    print(doc.document)

print('\n')
#  print(sorted_adocs[0].document)

from rankURL_test5 import queries, page_rank, inverted_index
sorted_adocs = rankUrls(queries, page_rank, inverted_index)
for doc in sorted_adocs:
    print(doc.document)
print('\n')
#  print(sorted_adocs[0].document)

from rankURL_test6 import queries, page_rank, inverted_index
sorted_adocs = rankUrls(queries, page_rank, inverted_index)
for doc in sorted_adocs:
    print(doc.document)
print('\n')
#  print(sorted_adocs[0].document)