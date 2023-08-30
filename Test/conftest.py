import yaml
import sys
import pytest


class set_up():


    def __init__(self, path_to_config : None) -> None:
        try:
            with open("config.yaml", "r") as file:
                self.data = yaml.safe_load(file)

        except FileNotFoundError as exc:
            print(f"File not found. Ecxeption: {exc}") 
            sys.exit(0)
        except yaml.YAMLError as exc:
            print(f"Error while parsing YAML file: Ecxeption {exc}")
            sys.exit(0)


    def get_url(self):
        return self.data["credentials"]["base_url"]

    def get_headers(self):
        data_headers = self.data["headers"]
        data_headers["Authorization"] = f'{data_headers["Authorization"]} {self.data["credentials"]["Oauth"]}'
        return data_headers
    
    def get_pages(self):
        return self.data["pages"]

    def get_user(self):
        return self.data["user"]


settings = set_up("config.yaml")


@pytest.fixture(scope = "function")
def url():
    return settings.get_url()

@pytest.fixture(scope = "function")
def headers():
    return settings.get_headers()

@pytest.fixture(scope = "function")
def pages():
    return settings.get_pages()

@pytest.fixture(scope = "function")
def user():
    return settings.get_user()
