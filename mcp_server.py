import sys
import json
from client import BakeryMutexArbitrator

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    arb = BakeryMutexArbitrator(params.get("num_nodes", 3))
    if method == "test_mutex":
        arb.request_ticket(0)
        return {"can_enter_0": arb.can_enter(0)}
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
