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

if __name__ == "__main__":
    with open("q1.txt", "r") as f:
        txt = f.read().lower()
        ranking = calc_letter_ranking("zyxiwvutsrpponkmlihgfedcba")
        print(ranking)