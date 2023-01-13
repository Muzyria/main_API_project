from utilities.http_methods import Http_methods


"""Методы для тестирования Google maps api"""

base_url = "https://rahulshettyacademy.com"  # Базовая URL
key = "?key=qaclick123"  # Параметр для всех запросов


class Google_maps_api:

    """Метод для создания новой локации"""

    @staticmethod
    def create_new_place():
        json_for_create_new_location = {
                                        "location": {"lat": -38.383494, "lng": 33.427362},
                                        "accuracy": 50,
                                        "name": "Frontline house",
                                        "phone_number": "(+91) 983 893 3937",
                                        "address": "29, side layout, cohen 09",
                                        "types": ["shoe park", "shop"],
                                        "website": "http://google.com",
                                        "language": "French-IN"
                                        }

        post_resource = "/maps/api/place/add/json"  # Ресурс метода POST
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_location)
        [print(k) for k in result_post.text.split(',')]
        return result_post

    """Метод для проверки новой локации"""

    @staticmethod
    def get_new_place():
        pass
