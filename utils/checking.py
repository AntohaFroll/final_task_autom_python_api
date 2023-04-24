import json
from requests import Response


class Checking:
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, f"Fail! Status code {status_code}"
        print(f"Success! Status code {status_code}")

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All fields are present")

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f"Value of '{field_name}' is correct")
