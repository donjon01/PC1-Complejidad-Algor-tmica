# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1huRwzgOO1EwIKYu-g0ZFY1zZUmaCx2fu
"""

import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (229, -1))
sys.setrecursionlimit(107)
from collections import deque

def solve():

    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    n, m = [int(x) for x in input().split()] 

    mtr = [[] for x in range(n)] 
    for i in range(n):
        mtr[i] = list(input())

    vis = [[False for y in range(m)] for x in range(n)]

    st = dq()
 
    def valid(r, c):
        ret = (r >= 0) and (r < n)
        ret = ret and (c >= 0) and (c < m)
        if not ret: 
            return False 
        ret = ret and (mat[r][c] == '@') and (not vis[r][c])
        return ret

    def dfs(r, c): 
        vis[r][c] = True
        st.append((r, c))
        while len(st):
            r, c = st.popleft()
            vis[r][c] = True
            for i in range(8):
                nr, nc = r + dx[i], c + dy[i]
                if valid(nr, nc):
                    vis[nr][nc] = True
                    st.append((nr, nc))
    reg = 0
    for i in range(n):
        for j in range(m):
            if (mat[i][j] == '@') and (not vis[i][j]):
                reg += 1
                dfs(i, j)
    return reg

print(solve())

solve()

solve()

solve()

solve()