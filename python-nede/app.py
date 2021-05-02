# ------------------------------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------------------------------

import time
import requests
import os

dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
dapr_url = "http://localhost:{}/v1.0/state/bindings/cosmosgraphdb".format(dapr_port)

n = 0
while True:
    n += 1
    message = {"operation": "exec", "metadata" : {"Gremlin": "g.addV('student').property('name', 'node' " + n + ").property('GPA', 4.0);"}}

    try:
        response = requests.post(dapr_url, json=message, timeout=5)
    except Exception as e:
        print(e, flush=True)

    time.sleep(1)
