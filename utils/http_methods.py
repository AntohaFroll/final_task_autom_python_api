import requests
import allure
from utils.logger import Logger


class HttpMethods:

    headers = {'Content-Type': 'application/json'}
    cookies = ''

    @staticmethod
    def get(url):
        with allure.step('GET'):
            Logger.add_request(url, method='GET')
            response = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
            Logger.add_response(response)
            return response

    @staticmethod
    def post(url, body):
        with allure.step('POST'):
            Logger.add_request(url, method='POST')
            response = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
            Logger.add_response(response)
            return response

    @staticmethod
    def put(url, body):
        with allure.step('PUT'):
            Logger.add_request(url, method='PUT')
            response = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
            Logger.add_response(response)
            return response

    @staticmethod
    def delete(url, body):
        with allure.step('DELETE'):
            Logger.add_request(url, method='DELETE')
            response = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
            Logger.add_response(response)
            return response
