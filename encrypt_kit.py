import binascii
import base64
import zlib
import threading


class type1():
    
    def __init__(self):

        self.letter = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['z']]
        self.bigletter = [[i2.upper() for i2 in i] for i in self.letter]
        self.result = ''
        self.key = ''

    def decrypt(self, string, key):

        self.__init__()
        self.encrypt = ''.join([chr(int(''.join(i), 16)) for i in list(zip(string[::2], string[1::2]))]).split(' ')
        self.encrypt = [list(zip(i[::2], i[1::2])) for i in ''.join([chr(int(''.join(i), 16)) for i in list(zip(self.encrypt[0][::2], self.encrypt[0][1::2]))]).split(' ')]
        self.key = key.split(' ')
        for i2 in range(len(self.encrypt)):
            for i in range(len(self.encrypt[i2])):
                self.result += self.letter[int(self.encrypt[i2][i][0])-1][int(self.encrypt[i2][i][1])-1] if self.key[i2][i] == 's' else self.bigletter[int(self.encrypt[i2][i][0])-1][int(self.encrypt[i2][i][1])-1] if self.key[i2][i] == 'b' else self.encrypt[i2][i][1] if self.key[i2][i] == 'c' else 0
            self.result += ' '
        return self.result

    def encrypt(self, string):

        self.__init__()
        self.string = string.split(' ')
        count=0

        for i2 in self.string:
            for i in i2:
                if i not in 'abcdefghijklmnopqrstuvwxyz' and i not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    self.result += '|'+i
                    self.key += 'c'
                    #print(count)
                    count+=1
                for a in self.letter:
                    if i in a:
                        self.first = self.letter.index(a)+1
                        self.second = a.index(i)+1
                        self.result = self.result + str(self.first) + str(self.second)
                        self.key += 's'
                for a in self.bigletter:
                    if i in a:
                        self.first = self.bigletter.index(a)+1
                        self.second = a.index(i)+1
                        self.result = self.result + str(self.first) + str(self.second)
                        self.key += 'b'
            self.result += ' '
            self.key += ' '
            #print('done')
        self.result = list(self.result)
        self.result.pop()
        self.result = ''.join(self.result)
        self.key = list(self.key)
        self.key.pop()
        self.key = ''.join(self.key)
        self.result = ''.join([hex(ord(i)).replace('0x', '') for i in self.result])
        self.result = ''.join([hex(ord(i)).replace('0x', '') for i in self.result])
        return self.result, self.key


type1 = type1()

