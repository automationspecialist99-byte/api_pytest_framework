import yaml
import pytest

from utils.api_client import APIClient

@pytest.fixture(scope="session")
def config():
    with open("config/config.yaml") as file:
        return yaml.safe_load(file)

@pytest.fixture(scope="session")
def api_client(config):
    return APIClient(
        base_url=config["base_url"],
        timeout=config["timeout"]
    )




