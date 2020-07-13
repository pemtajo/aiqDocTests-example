#!/usr/bin/python3
# coding=UTF-8

from http import HTTPStatus
from aiqdoctests.structures import AiqTest
from tests.helpers.constants import BASIC_AUTH


class tests_url_parameters(AiqTest):
    def __init__(self, *args, **kws):
        super().__init__(*args, **kws)
        self.setStructure("url_parameters")

    def test_happy_day(self):
        r = self.assertResponseStructure(
            HTTPStatus.OK.value,
            parameters_url={"id": 1},
            query_params={"type": "foo"},
            headers={"Authorization": BASIC_AUTH},
        )

        jsonResponse = r.json()

        data = jsonResponse["data"]

        self.assertEqual(1, data["id"])
        self.assertEqual(True, data["success"])
        self.assertEqual("Ok!", data["message"])
        self.assertEqual("foo", data["type"])

    def test_without_url_parameters(self):
        r = self.assertResponseStructure(
            HTTPStatus.BAD_REQUEST.value,
            query_params={"type": "foo"},
            headers={"Authorization": BASIC_AUTH},
        )

        jsonResponse = r.json()

        data = jsonResponse["data"]

        self.assertEqual(False, data["success"])
        self.assertEqual("URL parameter was not found.", data["message"])

    def test_without_query_string(self):
        r = self.assertResponseStructure(
            HTTPStatus.BAD_REQUEST.value,
            parameters_url={"id": 1},
            headers={"Authorization": BASIC_AUTH},
        )

        jsonResponse = r.json()

        data = jsonResponse["data"]

        self.assertEqual(False, data["success"])
        self.assertEqual("Query parameter was not found.", data["message"])

