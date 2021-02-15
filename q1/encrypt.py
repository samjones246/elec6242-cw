import sys
import string
plaintext = sys.argv[1]
key = sys.argv[2]
mode = 'd' if len(sys.argv) > 3 else 'e'
if mode =='e':
    table = str.maketrans(key.lower() + key.upper(), string.ascii_lowercase + string.ascii_uppercase)
else:
    table = str.maketrans(string.ascii_lowercase + string.ascii_uppercase, key.lower() + key.upper())
print(plaintext.translate(table))