from pprint import pprint
import requests
from example import token

token = token


class YaUploader:
    def __init__(self, token):
        self.token = token

    def headers(self):
        return {
            'Content-Type': 'application/json', 'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload_link(self):
        url_upload = "https://cloud-api.yandex.net/v1/disk/resources/"
        headers = self.headers()
        params = {"path": "Документы/Нетология", "overwrite": "true"}
        resp = requests.put(url_upload, headers=headers, params=params)
        # print(resp.status_code)
        pprint(resp.json())
        return resp.status_code
        # return resp.json







if __name__ == '__main__':
    a = YaUploader(token=token)
    a.upload_link()


