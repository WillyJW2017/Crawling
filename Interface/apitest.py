import requests
import json

class RunMain:
    def __init__(self, url, method, data):
        self.res = self.run_main(url, method, data)

    def send_post(self, url, data):
        res = requests.post(url = url, data = data)
        return json.loads(res.text)

    def send_get(self, url, data=None):
        res = requests.get(url=url, data=data)
        return json.loads(res.text)

    def run_main(self, url, method, data=None):
        result = None
        if method == 'POST':
            result = self.send_post(url, data)
        else:
            result = self.send_get(url, data)
        return result

if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/login/'
    data = {'username': 'Jacky', 'password': '999999'}
    run = RunMain(url, 'POST', data)
    print(run.res)
