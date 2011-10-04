#!/usr/bin/env python

class Xbrl():
    def __init__(self, amount=0):
        self.amount = amount

    def times(self, multiplier):
        self.amount *= multiplier

    def parse(self, multiplier):
        self.amount *= multiplier
