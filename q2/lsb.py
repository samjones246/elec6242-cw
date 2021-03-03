def extract_lsbs(bytestring: bytearray):
    out = ""
    for b in bytestring:
        out += str(bin(int(b)))[-1]
    return out

if __name__ == "__main__":
    with open("q2.hex", "rb") as f:
        bytestring = bytearray(f.read())
        lsbs = extract_lsbs(bytestring)
        result = [lsbs[i:i+8] for i in range(0, len(lsbs), 8)]
        print([chr(int(byte, base=2)) for byte in result])