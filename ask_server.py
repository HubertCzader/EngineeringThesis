import requests
import os

os.environ['NO_PROXY'] = '127.0.0.1'
url = 'http://127.0.0.1:8000/'
ID = 'e2055800-058b-42c7-b854-beef168e7ccd'


def check_if_active(key_id):
    return bool(requests.get(url + key_id).text)


if __name__ == "__main__":
    print(check_if_active(ID))




