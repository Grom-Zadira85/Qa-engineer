#!/usr/bin/python
# -*- coding: utf-8 -*-


class SoftwareEngineer:

    def __init__(self):
        self.name = "Konstantin"
        self.role = "Software Engineer"
        self.language_spoken = [" ru_RU", "uk_UA", "en_US"]
        
    def say_hi(self):
        print("Thanks for dropping by, hope you find some of my work interesting.")
        
me = SoftwareEngineer()
me.say_hi()


