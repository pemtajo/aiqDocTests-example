#!/usr/bin/python3
# coding=UTF-8

from http import HTTPStatus
from aiqdoctests.structures import AiqTest


class tests(AiqTest):
    def __init__(self, *args, **kws):
        super().__init__(*args, **kws)
        self.setStructure("file_upload")

    def test_happy_day(self):
        files = {'uploaded_file': open('example_file.txt','rb')}

        r = self.assertOK(method='POST', files=files)

        jsonResponse = r.json()

        data = jsonResponse['data']

        self.assertEqual(data['message'], 'Ok!')
        self.assertTrue(len(data['files']) > 0)
        self.assertTrue(data['success'])

    def test_without_files(self):
        r = self.assertResponseStructure(
            HTTPStatus.NOT_FOUND.value,
            method='POST'
        )

        jsonResponse = r.json()

        data = jsonResponse['data']

        self.assertEqual(data['message'], 'File was not found.')
        self.assertTrue(len(data['files']) == 0)
        self.assertFalse(data['success'])
