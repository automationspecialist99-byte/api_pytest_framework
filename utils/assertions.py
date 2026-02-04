
def assert_status_code(response,expected):
    assert response.status_code==expected,f"Expected {expected}, got {response.status_code}"

def assert_key_exists(response_json,key):
    assert key in response_json,f" key {key} not found in the reqsponse json"

def assert_validate_response_data(response):
    data=response.json()
    assert "bookingid" in data,f" bookingid  not found in the reqsponse json"
    assert "booking" in data, f" booking  not found in the reqsponse json"