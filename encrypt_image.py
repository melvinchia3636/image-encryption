import base64
from encrypt_kit import type1
import threading
import math

def encrypt(image, codefile, keyfile):

    def encrypt_phase_2(string, codefile, keyfile):
        final = type1.encrypt(string)
        open(codefile, "a").write(final[0])
        open(keyfile, "a").write(final[1])
    
    with open(image, "rb") as image_file:
        encoded_string = str(base64.b64encode(image_file.read()))
        print(len(encoded_string))
        #print(encoded_string)

    for i in range(math.floor(len(encoded_string)/100000)):
            threading.Thread(target=encrypt_phase_2(encoded_string[i*100000:(i+1)*100000], codefile, keyfile)).start()
            print((i+1)*100000)
    threading.Thread(target=encrypt_phase_2(encoded_string[(i+1)*100000:len(encoded_string)], codefile, keyfile)).start()

def decrypt(codefile, keyfile, outfile):

    global final
    final = ''

    def decrypt_phase_2(string, key):
        global final
        final += type1.decrypt(string, key)


    lol = open(codefile).read()
    lol2 = open(keyfile).read()
    print(len(lol2))

    for i in range(math.floor(len(lol2)/100000)):
            threading.Thread(target=decrypt_phase_2(lol[i*100000*8:(i+1)*100000*8], lol2[i*100000:(i+1)*100000])).start()
            print((i+1)*100000)
    threading.Thread(target=decrypt_phase_2(lol[(i+1)*100000*8:len(lol)], lol2[(i+1)*100000:len(lol2)])).start()
    final = final.replace(' ', '').replace('b\'', '').replace('\'', '')

    open(outfile, 'wb').write(base64.b64decode(final))
