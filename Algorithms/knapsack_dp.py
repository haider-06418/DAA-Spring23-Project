# This algorithm is taken from
# [GeekforGeeks](https://www.geeksforgeeks.org/python-program-for-dynamic-programming-set-10-0-1-knapsack-problem/)


def knapsack_dp(W, V, n, wmax):
    ''' A Dynamic Programming based Python Program for 0-1 Knapsack problem Returns
    the maximum value that can be put in a knapsack of capacity wmax '''
    K = [[0 for x in range(wmax + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for wi in range(wmax + 1):
            if i == 0 or wi == 0:
                K[i][wi] = 0
            elif W[i-1] <= wi:
                K[i][wi] = max(V[i-1] + K[i-1][wi-W[i-1]],  K[i-1][wi])
            else:
                K[i][wi] = K[i-1][wi]

    return K[n][wmax]


import os
from sys import path
path.append("../Dataset/")
import time
import statistics
import matplotlib.pyplot as plt
from contextlib import contextmanager

@contextmanager
def timer(label: str, timelst):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print(f"{label}: {end - start:.3f} seconds")
        timelst.append(end-start)
        
def main():
    categories = ["very_large_n"]
    instances = 10
    iterations = 1
    avg_score = list(); avg_time = list()
    n_lst = list(); c_lst = list()
    for c in categories:
        for i in range(instances):
            score = list()
            timelst = list()
            
            num = "0"*(4-len(str(i)))
            location = f"../Dataset/{c}_group/instance_{num}{i}.txt"
            items = list(); W = list(); V = list()
            with open(location) as f:
                lines = f.readlines()
                num, capacity = lines[0].split()
                num, capacity = int(num), int(capacity)
                for i in lines[1::]:
                    value, weight = i.split()
                    items.append((int(value), int(weight)))
                    W.append(int(weight)); V.append(int(value))
                    
            for i in range(iterations):
                with timer("func", timelst):
                    max = knapsack_dp(W, V, num, capacity)
                score.append(max)
            n_lst.append(num)
            c_lst.append(capacity)
            avg_score.append(statistics.mean(score))
            avg_time.append(statistics.mean(timelst))
            n_t = list(zip(n_lst, avg_time))
            n_t.sort(key=lambda x: x[0])
            # n_t is a list of tuples of (n, time), I want two separate lists of n and time
            n_list, time_list = zip(*n_t)
    with open('analysis3.csv', 'w') as f:
        f.write("score, time\n")
        for i in range(instances*len(categories)):
            if i % instances == 0:
                f.write(f"{categories[i//instances]}\n")
            f.write(f"{avg_score[i]}, {avg_time[i]}\n")
    
    plt.plot(n_list, time_list, label="max")
    plt.show()

main()

