import json
import os
import requests

class PolygonAPI:
    def __init__(self, api_key):
        # Ініціалізує клас з ключем API та базовою URL-адресою Polygon.io
        self.api_key = api_key
        self.base_url = 'https://api.polygon.io'

    def save_stock_info(self, symbol, filename):
        # Зберігає інформацію про певний символ акцій у JSON файл
        stock_info = self.get_stock_info(symbol)
        try:
            with open(filename, 'w') as f:
                json.dump(stock_info, f)
        except Exception as e:
            print(f"Error saving stock info to {filename}: {e}")

    def save_ticker_types(self, filename):
        # Зберігає всі типи тікерів у JSON файл
        ticker_types = self.get_ticker_types()
        try:
            with open(filename, 'w') as f:
                json.dump(ticker_types, f)
        except Exception as e:
            print(f"Error saving ticker types to {filename}: {e}")

    def save_aggregate_bars(self, symbol, multiplier, timespan, start, end, filename):
        # Зберігає агреговані бари для певного символу акцій у JSON файл
        aggregate_bars = self.get_aggregate_bars(symbol, multiplier, timespan, start, end)
        try:
            with open(filename, 'w') as f:
                json.dump(aggregate_bars, f)
        except Exception as e:
            print(f"Error saving aggregate bars to {filename}: {e}")

    def get_stock_info(self, symbol):
        # Метод для отримання інформації про певний символ акцій
        endpoint = f'/v1/meta/symbols/{symbol}/company'
        params = {'apiKey': self.api_key}
        response = requests.get(self.base_url + endpoint, params=params)
        return self.handle_response(response)

    def get_ticker_types(self):
        # Метод для отримання всіх типів тікерів, що підтримуються Polygon.io
        endpoint = '/v3/reference/tickers/types'
        params = {'apiKey': self.api_key}
        response = requests.get(self.base_url + endpoint, params=params)
        return self.handle_response(response)

    def get_aggregate_bars(self, symbol, multiplier, timespan, start, end):
        # Метод для отримання агрегованих барів для певного символу акцій
        endpoint = f'/v2/aggs/ticker/{symbol}/range/{multiplier}/{timespan}/{start}/{end}'
        params = {'apiKey': self.api_key}
        response = requests.get(self.base_url + endpoint, params=params)
        return self.handle_response(response)

    def read_stock_info(self, filename):
        # Читає дані про символ акцій з JSON файлу та повертає список щоденних OHLC даних
        try:
            with open(filename, 'r') as f:
                stock_info = json.load(f)
            return stock_info
        except Exception as e:
            print(f"Error reading stock info from {filename}: {e}")
            return None

    def read_ticker_types(self, filename):
        # Читає типи тікерів з JSON файлу та повертає список типів
        try:
            with open(filename, 'r') as f:
                ticker_types = json.load(f)
            return ticker_types
        except Exception as e:
            print(f"Error reading ticker types from {filename}: {e}")
            return None

    def search_ticker_by_name(self, ticker_name, filename):
        # Шукає тікер за назвою в JSON файлі та повертає відповідний тікер
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            for ticker in data:
                if ticker['name'] == ticker_name:
                    return ticker
            return None
        except Exception as e:
            print(f"Error searching ticker by name in {filename}: {e}")
            return None

    def read_chart_data(self, filename):
        # Читає графік тікера з JSON файлу та повертає відповідні дані
        try:
            with open(filename, 'r') as f:
                chart_data = json.load(f)
            return chart_data
        except Exception as e:
            print(f"Error reading chart data from {filename}: {e}")
            return None

    def create_file(self, filename):
        # Створює пустий JSON файл, якщо він ще не існує
        try:
            if not os.path.exists(filename):
                with open(filename, 'w') as f:
                    f.write('')
        except Exception as e:
            print(f"Error creating file {filename}: {e}")
        return None

    def handle_response(self, response):
        # Обробляє відповідь від сервера, перевіряє статус коду та повертає JSON або повідомлення про помилку
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': f"Failed to fetch data: {response.status_code}"}



