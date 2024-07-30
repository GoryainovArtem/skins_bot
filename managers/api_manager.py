import requests

from config import service_host, service_port


def get_skins_list():
    url = f"http://{service_host}:{service_port}/skins/"
    response = requests.get(url, headers={"accept": "application/json"})
    return response.json()
