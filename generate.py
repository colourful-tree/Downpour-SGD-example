import random

random.seed(2018)

w = [random.uniform(-1, 1) for i in range(10)]

for file_cnt in range(10):
    with open("data/" + str(file_cnt) + ".txt", "w") as fout:
        for i in range(10000):
            x = [random.uniform(-1, 1) for i in range(10)]
            y = 0
            for index in range(10):
                y += w[index] * x[index]
            x = map(lambda a:str(a), x)
            fout.write(" ".join(x) + " " + str(y) + "\n")
print w 
