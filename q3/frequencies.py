import operator
import string

def calc_letter_ranking(txt):
    freqs = {c: 0 for c in string.ascii_lowercase}
    for c in txt:
        if c in freqs:
            freqs[c] += 1
    freqs_sorted = sorted(freqs.items(), key=operator.itemgetter(1), reverse=True)
    print(freqs_sorted)
    return [k for k, v in freqs_sorted]

def tabulate_column(text, colsize):
    table = [[] for _ in range(colsize)]
    i = 0
    for l in text:
        table[i].append(l)
        i = (i + 1) % colsize
    return table

def shift_column(table, i, j):
    out = []
    for row in table:
        newrow = row[:j] + [row[i]] + row[j:i] + row[i+1:]
        out.append(newrow)
    return out


if __name__ == "__main__":
    with open("q3.txt", "r") as f:
        txt = f.read().lower()
        table = tabulate_column(txt, 11)
        table = shift_column(table, 4, 0)
        table = shift_column(table, 5, 4)
        for row in table:
            print(" ".join(row))