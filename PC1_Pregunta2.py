# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hFEzFYTaMfwkpbCHthWHtcJdJWFcoUtF
"""

import random as rnd
import networkx as nx

def readAL2(filename):
    V = []
    Vx = {}
    with open(filename) as f:
        lines = f.readlines()
    u = 0
    for line in lines:
        V.append(line.strip().split(':')[0])
        Vx[V[-1]] = u
        u += 1
    G = [None for _ in range(len(V))]
    u = 0
    for line in lines:
        G[u] = [Vx[a] for a in line.strip().split(':')[1].strip().split()]
        u += 1

    return V, G, Vx

def maximo(G):
    max = 0
    for i in G:
        mn = len(G[i])
        if max < mn:
            max = mn
    print(max)

# Commented out IPython magic to ensure Python compatibility.
# %%writefile graph.al2
# 0: 1 2
# 1: 3 4
# 2: 0 4 5
# 3: 4
# 4: 
# 5: 0 2

V, G, Vx = readAL2('graph.al2')
print(V)
G
getmax(G)