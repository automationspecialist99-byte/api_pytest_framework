import pytest

from utils.assertions import assert_status_code
from utils.data_json_read import json_data_read
from utils.logger import get_logger


@pytest.mark.skip
def test_delete_booking(api_client,config):
    endpoint = config["booking"] + "/" + str(config["delete_booking_id"])
    response = api_client.delete(endpoint=endpoint,headers=json_data_read("test_headers.json"))
    assert_status_code(response, config["created_status_code"])
    get_logger().info("Booking id successfully deleted")

def test_delete_booking_with_invalid_id(api_client,config):
    endpoint = config["booking"] + "/" + str(config["invalid_id"])
    response = api_client.delete(endpoint=endpoint,headers=json_data_read("test_headers.json"))
    assert_status_code(response, config["invalid_status_code"])
    get_logger().info("Booking id unable to delete due to invalid ID")