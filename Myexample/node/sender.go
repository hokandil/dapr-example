package mysever

import (
	"go/doc"
	"os"	
    "time"
    "encoding/json"
)

type metadata struct {
	Gremlin   string `json:"Gremlin"`
}
type message struct {
	operation string `json:"operation"`
	metadata metadata `json:"metadata"`
	
}

func main() {
var dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)

var dapr_url = "http://localhost:{}/v1.0/bindings/cosmosgraphdb".format(dapr_port)
var n = 0.0

for{
    n += 1.0
    payload := json.Marshal(
        message { 
            operation: "exec", 
            metadata: json.Marshal(metadata{
                        Gremlin: "g.addV('student').property('name', 'node' " + strconv.Itoa(n) + ").property('GPA', 4.0);"
}),
         })
    print(payload)
    try: func() {
        response = requests.post(dapr_url, payload)
        print(response)
    }
    Catch: func(e Exception) {
        print(e, True)
    }
    time.sleep(5)
   }
}
