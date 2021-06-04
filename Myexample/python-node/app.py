import os
# import time

import requests
import json
import flask
from flask import request

app = flask.Flask(__name__)

# These ports are injected automatically into the container.
dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
# dapr_grpc_port = os.getenv("DAPR_GRPC_PORT", 5000)
dapr_url = "http://localhost:{}/v1.0/bindings/cosmosgraphdb".format(dapr_port)

# Port to communicate with this HTTP server
port = 3000

# n = 0.0
# while True:
#     n += 1.0
    

#     payload = {
#         "metadata": {
#             "Gremlin": "g.addV('student').property('name', 'node 1001').property('GPA', 4.0);"
#         },
#         "operation": "query"
#     }
#     # try:
#     response = requests.post(dapr_url, json=payload)
        
#     # except Exception as e:
#     #     print(e, flush=True)

#     time.sleep(5)

@app.route("/gremlin/<string:gremlin_query>",methods=['POST'])
def kan(gremlin_query):
    payload = {"data":"kankan" , "operation": "query" , "metadata": { "gremlin": gremlin_query }}
        # try:
    response = requests.post(dapr_url, json=payload)
    # print(response.content.decode("utf-8"), flush=True)
    return response.content.decode("utf-8")

app.run(host="0.0.0.0", port=3000)

