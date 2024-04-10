#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def assert_sol(K, items, opt_value, sol):
    v = 0
    w = 0
    for i in range(len(sol)):
        if sol[i] == 1:
            v += items[i].value
            w += items[i].weight
    assert(v == opt_value)
    assert(w <= K)



def dynamic_prog(K, items):
    N = len(items)
    tab = [[0 for i in range(N + 1)] for j in range(K + 1)]
    for i in range(1, K + 1):
        for j in range(1, N + 1):
            #print(i,j)
            #print('Weight ',items[j - 1].weight )
            if items[j - 1].weight > i:
                tab[i][j] = tab[i][j - 1]
                #print(tab[i][j - 1])
            else:                
                #print(tab[i][j - 1])
                #print(tab[i - items[j - 1].weight][j - 1] + items[j - 1].value)
                tab[i][j] = max(tab[i][j - 1], tab[i - items[j - 1].weight][j - 1] + items[j - 1].value)
                
    opt = tab[K][N]
    taken = [0] * N
    i, j2 = (K, N)
    while j2 >= 1:
        #print(i, j2)
        if tab[i][j2] == tab[i][j2 - 1]:
            taken[j2 - 1] = 0
        else:
            taken[j2 - 1] = 1
            i -= items[j2 - 1].weight
        j2 -= 1
    assert_sol(K, items, opt, taken)
    return opt, taken, tab



def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    #print(items)

    opt = 1
    value, taken, tab = dynamic_prog(capacity, items)
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(opt) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

