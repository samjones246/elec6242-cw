from word_score import word_score
import random
import time
import operator
import string
import pickle
import matplotlib.pyplot as plt

fitness = word_score()

def gen_key():
    return "".join(random.sample(string.ascii_lowercase, k=len(string.ascii_lowercase)))

def gen_population(size, target):
    pop = [gen_key() for _ in range(size)]
    pop = map(lambda i: (i, calc_fitness(i, target)), pop)
    return list(pop)

def decrypt(cipher, key):
    table = str.maketrans(string.ascii_lowercase + string.ascii_uppercase, key.lower() + key.upper())
    text = cipher.translate(table)
    return text

def calc_fitness(key, target):
    return fitness.score3(decrypt(target, key).upper())

def mutate(parent : str, mutation_rate):
    p = mutation_rate / len(parent)
    child = list(parent)
    for i in range(mutation_rate):
        x = random.randrange(0, 26)
        val_x = parent[x]
        y = random.randrange(0, 26)
        val_y = parent[y]
        child[x] = val_y
        child[y] = val_x
    return "".join(child)

def crossover(parent1, parent2):
    child = []
    for i in range(len(parent1)):
        if random.random() < 0.5:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return "".join(child)

def tournament_crossover(target, pop_size, mutation_rate):
    pop = gen_population(pop_size, target)
    best = max(pop, key=operator.itemgetter(1))
    fitness_over_time = {}
    iter_count = 0
    while(iter_count < 250000):
        if iter_count % 1000 == 0:
            fitness_over_time[iter_count] = best[1]
            print(iter_count)
        a = random.choice(pop)
        b = random.choice(pop)
        parent1 = a if a[1] > b[1] else b

        a = random.choice(pop)
        b = random.choice(pop)
        parent2 = a if a[1] > b[1] else b

        child = crossover(parent1[0], parent2[0])
        child = mutate(parent1[0], mutation_rate)
        child = (child, calc_fitness(child, target))
        a = random.randrange(0, len(pop))
        b = random.randrange(0, len(pop))
        if pop[a][1] > pop[b][1]:
            pop[b] = child
        else:
            pop[a] = child
        best = max(pop, key=operator.itemgetter(1))
        iter_count += 1
    return best[0], fitness_over_time

#with open("model.pkl", "rb") as model:
    #fitness = pickle.load(model)

with open("q1.txt", "r") as f:
    correct = "BEGIN Once a laboratory novelty grown only on silicon, the NASA team now grows these forests of vertical carbon tubes on commonly used spacecraft materials, such as titanium, copper and stainless steel. Tiny gaps between the tubes collect and trap light, while the carbon absorbs the photons, preventing them from reflecting off surfaces. Because only a small fraction of light reflects off the coating, the human eye and sensitive detectors see the material as black."
    target = f.read()
    print("Starting evolution...")
    key, fitness_over_time = tournament_crossover(target, 500, 1)
    print(key)
    print(decrypt(target, key))
    fig, ax = plt.subplots()
    ax.plot(fitness_over_time.keys(), fitness_over_time.values())
    plt.show()