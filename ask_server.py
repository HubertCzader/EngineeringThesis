import os
import requests
import json

os.environ['NO_PROXY'] = '127.0.0.1'
url = 'http://127.0.0.1:8000/keys/check/'
ID = 'e2c3d3c4-12ec-4847-a1f3-e49c0c3d5b47'


def check_if_active(key_id):
    response = json.dumps({"active":  bool(requests.get(url + key_id).text)})
    return json.loads(response)


if __name__ == "__main__":
    print(check_if_active(ID))




