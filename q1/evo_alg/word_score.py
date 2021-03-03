from math import log10
import string
from functools import reduce

class word_score(object):
    def __init__(self):
        ''' load a file containing ngrams and counts, calculate log probabilities '''
        self.Pw = {}
        self.minval = 0
        self.minval2 = 0
        with open("count_1w.txt", "r") as f:
            for line in f.readlines():
                key,count = line.split('\t') 
                self.Pw[key.upper()] = self.Pw.get(key.upper(), 0) + int(count)
        self.N = 1024908267229 ## Number of tokens
        #calculate first order log probabilities
        for key in self.Pw.keys():
            v = log10(float(self.Pw[key])/self.N)
            if v < self.minval:
                self.minval = v
            self.Pw[key] = v
        #get second order word model 
        self.Pw2 = {}
        with open("count_2w.txt", "r") as f:
            for line in f.readlines():
                key,count = line.split('\t') 
                self.Pw2[key.upper()] = self.Pw2.get(key.upper(), 0) + int(count)
        #calculate second order log probabilities
        for key in self.Pw2.keys():
            word1,word2 = key.split()
            if word1 not in self.Pw: 
                v = log10(float(self.Pw2[key])/self.N)
            else: 
                v = log10(float(self.Pw2[key])/self.N) - self.Pw[word1]
            self.Pw2[key] = v
            if v < self.minval2:
                self.minval2 = v
        # precalculate the probabilities we assign to words not in our dict, L is length of word
        self.unseen = [log10(10./(self.N * 10**L)) for L in range(50)]        
        
    # conditional word probability    
    def cPw(self,word,prev='<UNK>'):
        if word not in self.Pw: 
            return self.unseen[len(word)]
        elif prev+' '+word not in self.Pw2: 
            return self.Pw[word]
        else: 
            return self.Pw2[prev+' '+word]
    
    def score(self,text,maxwordlen=20):
        prob = [[-99e99]*maxwordlen for _ in range(len(text))]
        strs = [['']*maxwordlen for _ in range(len(text))]
        for j in range(maxwordlen):
            prob[0][j] = self.cPw(text[:j+1])
            strs[0][j] = [text[:j+1]]
        for i in range(1,len(text)):
            for j in range(maxwordlen):
                if i+j+1 > len(text): break
                candidates = [(prob[i-k-1][k] + self.cPw(text[i:i+j+1],strs[i-k-1][k][-1]),
                               strs[i-k-1][k] + [text[i:i+j+1]] ) for k in range(min(i,maxwordlen))]
                prob[i][j], strs[i][j] = max(candidates)
        ends = [(prob[-i-1][i],strs[-i-1][i]) for i in range(min(len(text),maxwordlen))]
        return max(ends)
    
    def score2(self, text : str):
        words = "".join(filter(lambda l: l in (string.ascii_uppercase + " "), text.upper())).split(" ")
        print(words)
        probs = [-99e99] * len(words)
        prev = '<UNK>'
        for i in range(len(words)):
            probs[i] = self.cPw(words[i], prev)
            prev = words[i]
        print(probs)
        p = reduce(lambda x,y:x*y, probs)
        return p

    def score3(self, text : str):
        words = "".join(filter(lambda l: l in (string.ascii_uppercase + " "), text.upper())).split(" ")
        score = 0
        prev = '<UNK>'
        for word in words:
            if prev + ' ' + word in self.Pw2:
                score += self.Pw2[prev + ' ' + word] - self.minval2
            elif word in self.Pw:
                score += self.Pw[word] - self.minval
            prev = word
        return score
