import string
import operator
def inc_bytes(bytestring: bytearray, count=1):
    out = bytestring.copy()
    for i in range(len(bytestring)):
        out[i] += count
    return out

def decimal(bytestring : bytearray):
    out = []
    for c in bytestring:
        out.append(f"{int(c):03d}")
    return out

def asBinary(bytestring):
    return " ".join([f"{int(bin(b)[2:]):08d}" for b in bytestring])

def mergePairHalves(odds, evens):
    out = []
    for i in range(len(odds)):
        byte1 = f"{int(bin(odds[i])[2:]):08d}"[:4]
        byte2 = f"{int(bin(evens[i])[2:]):08d}"[4:]
        byte = byte1 + byte2
        out.append(chr(int(byte, base=2)))
    return out

def flipMSB_evens(odds, evens):
    out = []
    for i in range(len(odds)):
        byte1 = f"{int(bin(odds[i])[2:]):08d}"
        byte2 = "0" + f"{int(bin(evens[i])[2:]):08d}"[1:]
        out.append(int(byte1, base=2))
        out.append(int(byte2, base=2))
    return out

def arbitraryMapDistinctBytes(odds, evens):
    distinctA = sorted(list(set(odds)))
    distinctB = sorted(list(set(evens)))
    mapA = {distinctA[i] : string.ascii_lowercase[i] for i in range(len(distinctA))}
    mapB = {distinctB[i] : string.ascii_uppercase[i] for i in range(len(distinctB))}
    useMap = mapA
    translated = []
    for b in bytestring:
        translated.append(useMap[b])
        useMap = mapB if useMap == mapA else mapA
    return translated

def getPairFrequencies(odds, evens):
    pairs = [(odds[i], evens[i]) for i in range(len(odds))]
    pairFrequencies = {}
    for pair in pairs:
        if pair not in pairFrequencies:
            pairFrequencies[pair] = 0
        pairFrequencies[pair] += 1

def mirrorBytes(bytestring, onlyEvens=False):
    out = []
    even = False
    for b in bytestring:
        if even or (not onlyEvens):
            out.append("".join(reversed(hex(b)[2:])))
        else:
            out.append(b)
        even = not even
    return out

def xor(bytestring, key):
    out = []
    for b in bytestring:
        out.append(b ^ key)
    return "".join([chr(b) for b in out])

def xor2(bytestring, key1, key2):
    out = []
    i = key1
    for b in bytestring:
        out.append(b ^ i)
        if i == key1:
            i = key2
        else:
            i = key1
    return "".join([chr(b) for b in out])

if __name__ == "__main__":
    with open("q2.hex", "rb") as f:
        bytestring = bytearray(f.read())
        odds = bytestring[::2]
        evens = bytestring[1::2]
        i = 244
        print(xor2(bytestring, 110, i))