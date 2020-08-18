#!/usr/bin/python3
# coding=UTF-8

from http import HTTPStatus
from aiqdoctests.structures import AiqTest
import os


class tests(AiqTest):
    def __init__(self, *args, **kws):
        super().__init__(*args, **kws)
        self.setStructure("file_upload")

    def test_happy_day(self):
        script_dir = os.path.dirname(__file__)
        files = {'uploaded_file': open(script_dir + '/example_file.txt','rb')}

        r = self.assertOK(method='POST', files=files)

        jsonResponse = r.json()

        data = jsonResponse['data']

        self.assertEqual(data['message'], 'Ok!')
        self.assertTrue(data['success'])

    def test_without_files(self):
        r = self.assertResponseStructure(
            HTTPStatus.BAD_REQUEST.value,
            method='POST'
        )

        jsonResponse = r.json()

        data = jsonResponse['data']

        self.assertEqual(data['message'], 'File was not found.')
        self.assertFalse(data['success'])
