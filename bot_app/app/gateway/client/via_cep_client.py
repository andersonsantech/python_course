import requests

class CepRequest:

    BASE_URL = 'https://viacep.com.br/ws/'

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_data(self, cep: str) -> dict:
        try:
            response = requests.get(f'{self.BASE_URL}{cep}/json/')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f'Erro na chamada HTTP: {e}')
            return {}