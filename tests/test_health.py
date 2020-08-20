#!/usr/bin/python3
# coding=UTF-8

from aiqdoctests.structures import AiqTest


@AiqTest.SetStructure("health")
class tests(AiqTest):
    def test_health(self):
        r = self.assertOK()
        self.assertEqual("Hello World! AiqdocTests-example", r.json())
