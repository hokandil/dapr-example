import time
import requests
import os

dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)

dapr_url = "http://localhost:{}/v1.0/bindings/cosmosgraphdb".format(dapr_port)
n = 0.0
while True:
    n += 1.0
    payload = { 
      "operation": "exec" ,
       "metadata": {
            "Gremlin": "g.addV('student').property('name', 'node' " + strconv.Itoa(n) + ").property('GPA', 4.0);",
            }      
    }
    print(payload, flush=True)
    try:
        response = requests.post(dapr_url, json=payload)
        print(response, flush=True)

    except Exception as e:
        print(e, flush=True)

    time.sleep(5)
