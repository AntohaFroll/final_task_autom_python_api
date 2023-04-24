from utils.http_methods import HttpMethods

base_url = 'https://rahulshettyacademy.com'
key = '?key=qaclick123'


class GoogleMapsApi:

    @staticmethod
    def create_new_location():

        json_for_create_new_location = {
            "location": {
            "lat": -38.383494,
            "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
             "shoe park",
            "shop"
             ],
             "website": "http://google.com",
            "language": "French-IN"
        }
        post_resource = '/maps/api/place/add/json'
        post_url = base_url + post_resource + key
        print(post_url)
        post_response = HttpMethods.post(post_url, json_for_create_new_location)
        print(post_response.text)
        return post_response

    @staticmethod
    def check_create_new_location(place_id):
        get_resource = '/maps/api/place/get/json'
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)
        get_response = HttpMethods.get(get_url)
        print(get_response.text)
        return get_response

    @staticmethod
    def update_adress_location(place_id):
        put_resource = '/maps/api/place/update/json'
        put_url = base_url + put_resource + key
        json_for_update_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        print(put_url)
        put_response = HttpMethods.put(put_url, json_for_update_location)
        print(put_response.text)
        return put_response

    @staticmethod
    def delete_location(place_id):
        delete_resource = '/maps/api/place/delete/json'
        delete_url = base_url + delete_resource + key
        json_for_delete_location = {
            "place_id": place_id
        }
        print(delete_url)
        delete_response = HttpMethods.delete(delete_url, json_for_delete_location)
        print(delete_response.text)
        return delete_response
