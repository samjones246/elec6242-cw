'''
Allows scoring of text using n-gram probabilities
17/07/12
'''
from math import log10

class ngram_score(object):
    def __init__(self,ngramfile,sep=' '):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.ngrams = {}
        self.f_normal = 0
        self.N_distinct = 100000
        with open(ngramfile, "r") as f:
            lines = f.readlines()
            self.N_distinct = min(self.N_distinct, len(lines))
            for line in lines[:self.N_distinct]:
                key,count = line.split(sep) 
                self.ngrams[key] = int(count)
        self.N_total = sum(self.ngrams.values())
        self.L = len(key)
        self.floor = log10(0.01/self.N_total)
        for key in self.ngrams:
            self.ngrams[key] = log10(self.ngrams[key] / self.N_total)
            self.f_normal += self.ngrams[key]
        self.f_normal = self.f_normal / self.N_distinct

    def score(self,text):
        ''' compute the score of text '''
        f = 0
        k = 0
        words = text.upper().split(" ")
        for word in words:
            for i in range(len(word) - self.L + 1):
                ngram = word[i:i+self.L]
                if ngram in self.ngrams: 
                    f += self.ngrams[ngram]
                else: 
                    f += self.floor
                k += 1
        f = f / k
        score = abs(f - self.f_normal) / self.f_normal
        return score
       
