import requests

# api_uri = "http://localhost:3001/"
# headers_api = {
#     'x-api-token': '4a6b76252f431e0dcc19755e0d752da33e7595bfcc382e14d8fdc7410c7f',
#     'x-app-key': 'dcdf567f-610e-59a6-8297-80c5a99eafdc'
# }

# def api(path):
#     return api_uri+path

# def post(url, data=[]):
#     return requests.post(url=api(url), data=data, headers=headers_api)

# def get(url, params=[]):
#     return requests.get(url=api(url), params=params, headers=headers_api)

# def put(url, data=[]):
#     return requests.put(url=api(url), data=data, headers=headers_api)

# def delete(url, data=[]):
#     return requests.put(url=api(url), data=data, headers=headers_api)

def get(url, headers={}):
    try:
        response = requests.request(
            method='GET',
            url=url,
            headers=headers
            )
        result = response.json()
        requests.session().close()
        return result
    except Exception as e:
        return e

def getPost(url, headers={}, data={}):
    try:
        response = requests.request(
            method='POST',
            url=url,
            headers=headers,
            data=data
            )
        result = response.json()
        requests.session().close()
        return result
    except Exception as e:
        return e