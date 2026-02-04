import pytest
import requests
from requests.auth import HTTPBasicAuth

from utils.data_json_read import json_data_read


BASE_URL= "https://restful-booker.herokuapp.com/booking"
header=json_data_read("test_headers.json")
auth=json_data_read("test_user_password.json")
data=json_data_read("test_data.json")
class TestSynchCallApi:
    bookinId = None
    @pytest.mark.dependency(name='create')
    def test_create_booking_synch_call(self):
        resp=requests.post(BASE_URL,headers=header,json=data)
        assert resp.status_code==200
        TestSynchCallApi.bookinId=resp.json()["bookingid"]
        print(TestSynchCallApi.bookinId)
        assert TestSynchCallApi.bookinId,"Booking id not generated "

    @pytest.mark.dependency(depends=['create'])
    def test_getbooking_sync_call(self):
        requests.get(f"{BASE_URL}/{TestSynchCallApi.bookinId}",headers=header)

    @pytest.mark.parametrize("firstname, price",[('John', 100)])
    def test_update_booking_synch_call(self,firstname,price):
        data['firstname']=firstname
        data['price'] = price
        resp=requests.put(f"{BASE_URL}/{TestSynchCallApi.bookinId}",headers=header,json=data,auth=HTTPBasicAuth(json_data_read("test_user_password.json")["username"],json_data_read("test_user_password.json")["password"]))
        assert resp.status_code==200

    def test_delete_booking_sync_call(self):
        resp = requests.delete(f"{BASE_URL}/{TestSynchCallApi.bookinId}", headers=header, json=data,
                            auth=HTTPBasicAuth(json_data_read("test_user_password.json")["username"],
                                               json_data_read("test_user_password.json")["password"]))
        assert resp.status_code == 201






