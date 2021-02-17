import json
from django.test import TestCase
from django.urls import reverse
from mock import patch

class TemperatureAPIViewTests(TestCase):

    @patch('requests.get')
    def test_get_temperature(self, mock_external_api):
        url = reverse('get_temperature', args=['London']) + '?days=2'
        data = {
                "location": {
                    "name": "London",
                    "region": "City of London, Greater London",
                },
                "current": {
                    "temp_c": 10.0,
                },
                "forecast": {
                    "forecastday": [{
                        "day": {
                            "maxtemp_c": 10.4,
                            "mintemp_c": 7.5,
                            "avgtemp_c": 8.4
                        },
                        "hour": [
                            {
                                "temp_c": 9.3,
                            },
                            {
                                "temp_c": 8.5,
                            },
                            {
                                "temp_c": 9.2,
                            }
                        ],
                        "day": {
                            "maxtemp_c": 15.4,
                            "mintemp_c": 9.0,
                            "avgtemp_c": 12.0
                        },
                        "hour": [
                            {
                                "temp_c": 7.8,
                            },
                            {
                                "temp_c": 8.4,
                            },
                            {
                                "temp_c": 9.2,
                            }
                        ]
                    }]}

                }
        mock_external_api.return_value = MockResponse(data=json.dumps(data))
        response = self.client.get(url)
        self.assertEqual(response.json(), {'maximum': 15.4, 'minimum': 9.0, 'average': 8.47, 'median': 8.4})

    def test_validate_missing_days(self):
        url = reverse('get_temperature', args=['johannesburg'])
        response = self.client.get(url)
        self.assertEqual(response.json(), {'days': ['This field may not be null.']})

    def test_validate_days_out_of_bound(self):
        url = reverse('get_temperature', args=['cairo']) + '?days=20'
        response = self.client.get(url)
        self.assertEqual(response.json(), {'days': ['Days range should be between 1 and 10']})

    def test_validate_city_string(self):
        url = reverse('get_temperature', args=['1234']) + '?days=5'
        response = self.client.get(url)
        self.assertEqual(response.json(), {'city': ['No location found matching the city']})    

    @patch('requests.get')
    def test_no_location_found(self, mock_external_api):
        url = reverse('get_temperature', args=['testing']) + '?days=2'
        data = {
            "error": {
                "code": 1006,
                "message": "No matching location found."
            }
        }

        mock_external_api.return_value = MockResponse(data=json.dumps(data), status_code=400, msg='FAIL')
        response = self.client.get(url)
        self.assertEqual(response.json(), "No location found matching the city")

    @patch('requests.get')
    def test_external_api_error_is_translated(self, mock_external_api):
        url = reverse('get_temperature', args=['Nairobi']) + '?days=2'
        data = {
            "error": {
                "code": 2008,
                "message": "API key disabled."
            }
        }

        mock_external_api.return_value = MockResponse(data=json.dumps(data), status_code=400, msg='FAIL')
        response = self.client.get(url)
        self.assertEqual(response.json(), "Error processing your request. Please contact an administrator")


class MockResponse(object):
    def __init__(self, data, status_code=200, msg='OK'):
        self.content = data
        self.status_code = status_code
        self.ok = msg if msg == 'OK' else False
        self.headers = {'content-type': 'application/json'}