import requests
from requests.auth import HTTPBasicAuth
from utils.logger import get_logger
from utils.data_json_read import json_data_read


class APIClient:
    def __init__(self,base_url,timeout):
        self.base_url=base_url
        self.timeout=timeout
    global LOGGER
    logger=get_logger()


    def get(self,endpoint):
        return requests.get(
            url=f"{self.base_url}{endpoint}",
            timeout=self.timeout

        )

    def post(self,endpoint,payload,headers):
        return requests.post(
            url=f"{self.base_url}{endpoint}",
            json=payload,
            timeout=self.timeout,
            headers=headers
        )


    def put(self,endpoint,payload,headers):
        return requests.put(
            url=f"{self.base_url}{endpoint}",
            json=payload,
            timeout=self.timeout,
            headers=headers,
            auth=HTTPBasicAuth(json_data_read("test_user_password.json")["username"],json_data_read("test_user_password.json")["password"])
        )

    def delete(self,endpoint,headers):
        return requests.delete(
            url=f"{self.base_url}{endpoint}",
            timeout=self.timeout,
            headers=headers,
            auth=HTTPBasicAuth(json_data_read("test_user_password.json")["username"],json_data_read("test_user_password.json")["password"])

        )
