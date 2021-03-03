import pickle
from word_score import word_score

fitness = word_score()

with open("model.pkl", "wb") as f:
    pickle.dump(word_score, f)