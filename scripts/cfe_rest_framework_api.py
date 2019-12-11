import requests
import json

ENDPOINT = "http://127.0.0.1:8000/api/status/"


def do(method='get', data={}, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    # print(data)
    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    # print(r.content)
    print("Status code: " + str(r.status_code))
    return r


# Create
response_create = do(method='POST', data={"user": 1, "content": "from tests"})
response = json.loads(response_create.text)
id = response["id"]
print("Response: " + str(response))
print("Created id: " + str(id))

# Update
# response_update = do(method='PUT', data={'id': id, "content": "Updated content! :D"})

# Delete
# do(method='DELETE', data={'id': 5})
