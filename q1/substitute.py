import frequencies
import string

english_frequencies = 'etaoinsrhdlucmfywgpbvkxqjz'

def perfect_frequency_key(txt):
    ranking = frequencies.calc_letter_ranking(txt)
    key = "".join([english_frequencies[ranking.index(c)] for c in string.ascii_lowercase])
    return key

def decrypt(txt, key):
    return txt.translate(str.maketrans(string.ascii_lowercase, key))

def override_key(key, mask):
    out = ""
    for i in range(len(key)):
        if mask[i] == "#":
            out += key[i]
        else:
            out += mask[i]
    return out

def sub_with_matching_rank(txt):
    ranking = frequencies.calc_letter_ranking(txt)
    out = ""
    for c in txt:
        if c in ranking:
            r = ranking.index(c)
            out += english_frequencies[r]
        else:
            out += c
    return out

def fix_case(orig, target):
    out = ""
    for i in range(len(orig)):
        if orig[i].isupper():
            out += target[i].upper()
        else:
            out += target[i]
    return out

if __name__ == "__main__":
    with open("q1.txt", "r") as f:
        orig = f.read()
        txt = orig.lower()
        key = "".join(reversed(string.ascii_lowercase))
        mask = "###iwvutsr#ponkml#h##ed##a"
        key = override_key(key, mask)
        key = "zyxiwvutsrqponkmljhgfedcba"
        print("Key: " + key)
        subbed = decrypt(txt, key)
        print(fix_case(orig, subbed))

