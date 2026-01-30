import pytest

from utils.assertions import assert_status_code
from utils.data_json_read import json_data_read
from utils.logger import get_logger



def test_update_booking_by_id(api_client, config):
    endpoint=config["booking"] + "/" + str(config["update_booking_id"])
    res = api_client.put(endpoint=endpoint, payload=json_data_read("test_update_json_data.json"), headers=json_data_read("test_headers.json"))
    assert_status_code(res, config["success_status_code"])
    get_logger().info("Booking Id updated successfully ")