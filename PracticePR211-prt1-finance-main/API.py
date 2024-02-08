import json
import requests
import os

class PolygonAPI:

    def __init__(self, api_key):
        # Ініціалізуємо клас з ключем API та базовою URL-адресою Polygon.io
        self.api_key = api_key
        self.base_url = 'https://api.polygon.io'

    def save_stock_info(self, symbol, filename):
        # Зберігає інформацію про певний символ акцій у JSON файл
        stock_info = self.get_stock_info(symbol)
        with open(filename, 'w') as f:
            json.dump(stock_info, f)

    def save_ticker_types(self, filename):
        # Зберігає всі типи тікерів у JSON файл
        ticker_types = self.get_ticker_types()
        with open(filename, 'w') as f:
            json.dump(ticker_types, f)

    def save_aggregate_bars(self, symbol, multiplier, timespan, start, end, filename):
        # Зберігає агреговані бари для певного символу акцій у JSON файл
        aggregate_bars = self.get_aggregate_bars(symbol, multiplier, timespan, start, end)
        with open(filename, 'w') as f:
            json.dump(aggregate_bars, f)

    def get_stock_info(self, symbol):
        # Метод для отримання інформації про певний символ акцій
        endpoint = f'/v1/meta/symbols/{symbol}/company'
        params = {'apiKey': self.api_key}
        response = requests.get(self.base_url + endpoint, params=params)

        # Перевірка статусу відповіді
        if response.status_code == 200:
            return response.json()  # Повертаємо результат у форматі JSON
        else:
            return {'error': f"Failed to fetch data: {response.status_code}"}

    def get_ticker_types(self):
        # Метод для отримання всіх типів тікерів, що підтримуються Polygon.io
        endpoint = '/v3/reference/tickers/types'
        params = {'apiKey': self.api_key}
        response = requests.get(self.base_url + endpoint, params=params)

        # Перевірка статусу відповіді
        if response.status_code == 200:
            return response.json()  # Повертаємо результат у форматі JSON
        else:
            return {'error': f"Failed to fetch data: {response.status_code}"}

    def get_aggregate_bars(self, symbol, multiplier, timespan, start, end):
        # Метод для отримання агрегованих барів для певного символу акцій
        endpoint = f'/v2/aggs/ticker/{symbol}/range/{multiplier}/{timespan}/{start}/{end}'
        params = {'apiKey': self.api_key}
        response = requests.get(self.base_url + endpoint, params=params)

        # Перевірка статусу відповіді
        if response.status_code == 200:
            return response.json()  # Повертаємо результат у форматі JSON
        else:
            return {'error': f"Failed to fetch data: {response.status_code}"}

    def read_stock_info(self, filename):
        # Читає дані про символ акцій з JSON файлу та повертає список щоденних OHLC даних
        with open(filename, 'r') as f:
            stock_info = json.load(f)
        return stock_info

    def read_ticker_types(self, filename):
        # Читає типи тікерів з JSON файлу та повертає список типів
        with open(filename, 'r') as f:
            ticker_types = json.load(f)
        return ticker_types

    def search_ticker_by_name(self, ticker_name, filename):
        # Шукає тікер за назвою в JSON файлі та повертає відповідний тікер
        with open(filename, 'r') as f:
            data = json.load(f)
        for ticker in data:
            if ticker['name'] == ticker_name:
                return ticker
        return None

    def read_chart_data(self, ticker_symbol, filename):
        # Читає графік тікера з JSON файлу та повертає відповідні дані
        with open(filename, 'r') as f:
            chart_data = json.load(f)
        return chart_data[ticker_symbol]

    def create_file(self, filename):
        # Створює пустий JSON файл, якщо він ще не існує
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                f.write('')
