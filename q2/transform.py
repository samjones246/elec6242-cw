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

if __name__ == "__main__":
    with open("q2.hex", "rb") as f:
        bytestring = bytearray(f.read())
        odds = bytestring[::2]
        evens = bytestring[1::2]
        print(f"{min(odds)}, {max(odds)}")
        print(f"{min(evens)}, {max(evens)}")
        print(" ".join([f"{int(bin(b)[2:]):08d}" for b in bytestring]))
        something = []
        for i in range(len(odds)):
            byte1 = f"{int(bin(odds[i])[2:]):08d}"[:4]
            byte2 = f"{int(bin(evens[i])[2:]):08d}"[4:]
            byte = byte1 + byte2
            something.append(chr(int(byte, base=2)))
        something = []
        for i in range(len(odds)):
            byte1 = f"{int(bin(odds[i])[2:]):08d}"
            byte2 = "0" + f"{int(bin(evens[i])[2:]):08d}"[1:]
            something.append(int(byte1, base=2))
            something.append(int(byte2, base=2))
        distinctA = sorted(list(set(odds)))
        distinctB = sorted(list(set(evens)))
        print(len(distinctA))
        print(len(distinctB))
        mapA = {distinctA[i] : string.ascii_lowercase[i] for i in range(len(distinctA))}
        mapB = {distinctB[i] : string.ascii_uppercase[i] for i in range(len(distinctB))}
        useMap = mapA
        translated = []
        for b in bytestring:
            translated.append(useMap[b])
            useMap = mapB if useMap == mapA else mapA
        print("".join(translated))
        print("".join(translated[::2]))
        print("".join(translated[1::2]))
        pairs = [(odds[i], evens[i]) for i in range(len(odds))]
        pairFrequencies = {}
        for pair in pairs:
            if pair not in pairFrequencies:
                pairFrequencies[pair] = 0
            pairFrequencies[pair] += 1