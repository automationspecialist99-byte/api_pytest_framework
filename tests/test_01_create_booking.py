import json

import pytest

from utils.assertions import assert_status_code,assert_key_exists,assert_validate_response_data
from utils.data_json_read import json_data_read
from utils.logger import get_logger


def test_create_booking(api_client, config):
    response= api_client.post(endpoint=config["booking"],payload=json_data_read("test_data.json"),headers=json_data_read("test_headers.json"))
    assert_status_code(response, config["success_status_code"])
    assert_key_exists(response.json(),"booking")
    assert_validate_response_data(response)
    get_logger().info("Booking Creation successfully completed")

@pytest.mark.parametrize(
    "firstname, price",
    [
        ("John", 100),
        ("Alice", 250),
        ("Bob", 0),
        ("Emma", 9999),
    ]
)
def test_create_booking_parametrize(api_client, config,firstname, price):
    payload={
    "firstname" : firstname,
    "lastname" : "Brown",
    "totalprice" : price,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
    response= api_client.post(endpoint=config["booking"],payload=payload,headers=json_data_read("test_headers.json"))
    assert_status_code(response, config["success_status_code"])
    assert_key_exists(response.json(),"booking")
    assert_validate_response_data(response)
    get_logger().info("Booking Creation with parametrized value successfully completed")

