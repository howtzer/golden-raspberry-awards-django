from django.test import TestCase
from django.test import Client
from django.conf import settings
import django 

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'goldenRaspberryAwardsDjango.settings')
django.setup()



class TestIntegrations(TestCase):

    def test_get_200(self):
        response = Client.get('/', {})
        response_expected = {
            "min": [
                {
                    "producer": "Joel Silver",
                    "interval": 1,
                    "previousWin": 1990,
                    "followingWin": 1991
                },
                {
                    "producer": "Bo Derek",
                    "interval": 6,
                    "previousWin": 1984,
                    "followingWin": 1990
                }
            ],
            "max": [
                {
                    "producer": "Matthew Vaughn",
                    "interval": 13,
                    "previousWin": 2002,
                    "followingWin": 2015
                },
                {
                    "producer": "Buzz Feitshans",
                    "interval": 9,
                    "previousWin": 1985,
                    "followingWin": 1994
                }
            ]
        }
        assert response.status_code == 200
        assert response.json == response_expected
