from utils.api import GoogleMapsApi
from utils.checking import Checking
import allure


@allure.epic("Test create location")
class TestCreateLocation:

    @allure.description("Test create, update, delete location")
    def test_new_location(self):
        print("\nPOST method")
        post_response = GoogleMapsApi.create_new_location()
        check_post = post_response.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(post_response, 200)
        Checking.check_json_token(post_response, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(post_response, 'status', 'OK')

        print("\nGET method after POST")
        get_response = GoogleMapsApi.check_create_new_location(place_id)
        Checking.check_status_code(get_response, 200)
        Checking.check_json_token(get_response, ['location', 'accuracy', 'name', 'phone_number',
                                                 'address', 'types', 'website', 'language'])
        Checking.check_json_value(get_response, 'website', 'http://google.com')

        print("\nPUT method")
        put_response = GoogleMapsApi.update_adress_location(place_id)
        Checking.check_status_code(put_response, 200)
        Checking.check_json_token(put_response, ['msg'])
        Checking.check_json_value(put_response, 'msg', 'Address successfully updated')

        print("\nGET method after PUT")
        get_response = GoogleMapsApi.check_create_new_location(place_id)
        Checking.check_status_code(get_response, 200)
        Checking.check_json_token(get_response, ['location', 'accuracy', 'name', 'phone_number',
                                                 'address', 'types', 'website', 'language'])
        Checking.check_json_value(get_response, 'address', '100 Lenina street, RU')

        print("\nDELETE method")
        delete_response = GoogleMapsApi.delete_location(place_id)
        Checking.check_status_code(delete_response, 200)
        Checking.check_json_token(delete_response, ['status'])
        Checking.check_json_value(delete_response, 'status', 'OK')

        print("\nGET method after DELETE")
        get_response = GoogleMapsApi.check_create_new_location(place_id)
        Checking.check_status_code(get_response, 404)
        Checking.check_json_token(get_response, ['msg'])
        Checking.check_json_value(get_response, 'msg', "Get operation failed, looks like place_id  doesn't exists")

        print("\nTest new location complete")
