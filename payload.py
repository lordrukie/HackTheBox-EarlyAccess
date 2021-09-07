#!/usr/bin/python3
import random
import sys

class Keygen:
    key = ""
    number = list("0123456789")
    # magic_num = random.sample(number,3)
    # magic_num = ''.join(magic_num)
    # print(magic_num)
    state = ""

    def key3(self):
        alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYX")
        number = list("0123456789")
        magic_num = 300
        while magic_num <= 500:
            magic_num += 1
            for x in alpha:
                for y in alpha:
                    for num in number:
                        self.key = ""
                        array = "XP{}{}{}".format(x,y,num)
                        self.key += "KEY21-7M5W8-"
        
                        if sum(bytearray(array.encode())) == magic_num:
                            self.key += array
                            self.key5()
        
        
    def key5(self):
        self.key += "-GAMG1"
        number = list("0123456789")
        for a in number:
            for b in number:
                for c in number:
                    for d in number:
                        new = ''.join([a,b,c,d])
                        gs = self.key.split('-')
                        if sum([sum(bytearray(g.encode())) for g in gs])  == int(new):
                            self.key += "-"
                            self.key += new
                            if not self.key.split('-')[-1] == self.state:   
                                print(self.key)
                                self.state = new
                            self.key = ""


    def generate(self):
        self.key3()


key = Keygen()
key.generate()

