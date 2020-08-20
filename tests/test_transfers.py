#!/usr/bin/python3
# coding=UTF-8

from aiqdoctests.structures import AiqTest
from tests.helpers.constants import BASIC_AUTH


@AiqTest.SetStructure("transfers")
class tests_transfers(AiqTest):
    def test_happy_day(self):
        payload = {
            "transfers": [
                {
                    "value": 25.5,
                    "destination_bank_account": {
                        "name": "Fulano de souza",
                        "cpf_cnpj": "12863843893",
                        "bank_code": "1",
                        "agency": "3333",
                        "account": "12345",
                        "account_digit": "1",
                        "account_type": "CONTA_CORRENTE",
                    },
                },
                {
                    "value": 55.53,
                    "destination_bank_account": {
                        "name": "Fulano de souza",
                        "cpf_cnpj": "12863843893",
                        "bank_code": "077",
                        "agency": "3333",
                        "account": "12345",
                        "account_digit": "1",
                        "account_type": "CONTA_CORRENTE",
                    },
                },
            ]
        }

        r = self.assertOK(headers={"Authorization": BASIC_AUTH}, payload=payload)

        jsonResponse = r.json()

        data = jsonResponse["data"]

        self.assertEqual(2, len(data))

        self.assertEqual(True, data[0]["success"])

        self.assertEqual(False, data[1]["success"])
