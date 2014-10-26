#!/bin/env python
# -*- coding: utf-8 -*-

import random

from multiprocessing import Pool
import time

def square_map(x):
    return x * x

def main():
    p = Pool(5)

    i = int(random.random() * 10)
    j = int(random.random() * 10)

    if i > j:
        i, j = j, i
    elif i == j:
        j = int(random.random() + 1) + i

    l = list(range(i, j))

    result = p.map_async(square_map, l)

    map_result = result.get()

    reduce_result = reduce(lambda x, y: x + y, map_result)

    print 'The sum of the squares of numbers in {} is: {}'.format(l, reduce_result)

    p.close()
    p.join()

if __name__ == '__main__':
    main()
