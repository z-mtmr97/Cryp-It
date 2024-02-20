from Cryptodome.Cipher import AES
from base64 import b64decode
from getpass import getpass
import os, time, sys

fname = input('-')
# fname = "name"
enc_lines = []
try:
    with open("", 'r+') as f1:                          # File location goes here
        for l in f1:
             for i in l.splitlines():
                if i.endswith('/*'):
                    enc_lines.append(i.strip('/*'))

except FileNotFoundError:
    print("*_*")
    sys.exit(1)

holder = getpass("-")
en_pass = holder.encode("UTF-8")

cipher = AES.new(en_pass, AES.MODE_ECB)


f2 = open("", 'w')                                  # Output File location
f2.write("<h1> . </h1> <ul>" + "\n\n")

for l in enc_lines:

    ct = b64decode(l)
    # print(ct)
    pt = cipher.decrypt(ct)
    # print(pt)
    # print(pt.decode("UTF-8"))
    # print('\n')
    x = list(filter(None, pt.decode("utf-8").splitlines()))
    for i in x:
        a = i.replace('\\n', '')
        f2.write("<li> <a href = \"" + a + "\">" + a + "</a></li>" +"\n\n")


f2.write("</ul>")
path = os.path.realpath(f2.name)
f2.close()
print('*__*')

time.sleep(20)
os.remove(path)


