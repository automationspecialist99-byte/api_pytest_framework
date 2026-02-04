
from utils.assertions import assert_status_code
from utils.logger import get_logger


def test_get_booking_id(api_client,config):
    responses = api_client.get(config["booking"] + "/" + str(config["retrieve_booking_id"]))
    assert_status_code(responses, config["success_status_code"])
    get_logger().info("Get booking details successfully")

def test_get_booking_with_non_existing_id(api_client,config):
    responses = api_client.get(config["booking"] + "/" + str(config["retrieve_booking_non_existing_id"]))
    assert_status_code(responses, config["error_status_code"])
    get_logger().info("Unable to get the booking due to Non existing ID")