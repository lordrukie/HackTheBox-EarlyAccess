#!/usr/bin/python3
import random
import sys

class Keygen:
    key = ""
    word = list("ABCDEFGHIJKLMNOPQRSTUVWXYX0123456789")

    def __init__(self, magic_num:int=346):
        if magic_num != 0:
            self.magic_num = magic_num

    def key1(self) -> str:
        res = [221, 81, 145]
        for i, v in enumerate(res):
            for ii, vv in enumerate(self.word):
                r = (ord(vv)<<i+1)%256^ord(vv)
                if r == res[i]:
                    key = ""
                    self.key += vv
        self.key += "21"

    def key2(self):
        while True:
            new = random.sample(self.word,5)
            new = ''.join(new)

            p1 = new[::2]
            p2 = new[1::2]
            if sum(bytearray(p1.encode())) == sum(bytearray(p2.encode())):
                self.key += "-"
                self.key += new
                return
    
    def key3(self):
        magic_num = 346
        alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYX")
        number = list("0123456789")
        for x in alpha:
            for y in alpha:
                for num in number:
                    array = "XP{}{}{}".format(x,y,num)
                    if sum(bytearray(array.encode())) == magic_num:
                        self.key += "-"
                        self.key += array

    def key4(self):
        self.key += "-"
        self.key += 'GAMG1'
        return
        # code below is for bruteforcing the key, it take long time so i'll skip this.        
        for a in self.word:
            for b in self.word:
                for c in self.word:
                    for d in self.word:
                        for e in self.word:
                            new = [a,b,c,d,e]
                            if [ord(i)^ord(g) for g, i in zip(self.key.split('-')[0], new)] == [12, 4, 20, 117, 0]:
                                self.key += "-"
                                self.key += ''.join(new)
                                return

    def key5(self):
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
                            return

    def generate(self):
        self.key1()
        self.key2()
        self.key3()
        self.key4()
        self.key5()
        return self.key


key = Keygen()
print(key.generate())

