import pytest
import selenium.webdriver
import json


@pytest.fixture(scope="session")
def config():
    with open("config.json") as config_file:
        config = json.load(config_file)

    assert config["browser"] in ["Chrome", "Headless Chrome", "Firefox"]
    assert isinstance(config["implicit_wait"], int)
    assert config["implicit_wait"] > 0

    return config


@pytest.fixture
def browser(config):
    if config["browser"] == "Chrome":
        options = selenium.webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        b = selenium.webdriver.Chrome(options=options)
    elif config["browser"] == "Headless Chrome":
        options = selenium.webdriver.ChromeOptions()
        options.add_argument("headless")
        b = selenium.webdriver.Chrome(options=options)
    elif config["browser"] == "Firefox":
        b = selenium.webdriver.Firefox()
    else:
        raise Exception(f"Browser: {config['browser']} is not supported")

    b.implicitly_wait(config["implicit_wait"])

    yield b

    b.quit()


@pytest.fixture(scope="session")
def test_data():
    with open(r"data\test_data.json") as test_data_file:
        test_data = json.load(test_data_file)

    return test_data
