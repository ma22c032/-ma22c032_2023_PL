# -*- coding: utf-8 -*-
"""Gambler's ruin

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16JNZ9jWu5XtTt0FeQx3vt3u4-ocC_CPJ
"""

gd = {'a': ['b', 'd'], # a -> b, a -> d
      'b': ['c', 'd', 'a'] } # b -> c, b -> d, b -> a

gd = {'a': {'b': {'weight': 0.1},
'd': {'weight': 0.8}},
'b': {'d': {'weight': 0.5},
'c': {'weight': 0.5}}
}

import networkx as nx
g = nx.DiGraph(gd) # dictionary to graph

g['a']

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline
def plot_gph(g):
    pos = nx.spectral_layout(g)
    nx.draw(g, pos, with_labels=True, node_color='orange')
    labels = nx.get_edge_attributes(g, 'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels);
plot_gph(g)

import numpy as np
np.set_printoptions(suppress=True)
# S0 S1 S2 S3
P = np.array([[0, 0.0, 0.5, 0.5], # S0
              [1.0, 0.0, 0.0, 0.0], # S1
              [0.0, 0.0, 0.0, 1.0], # S2
              [0, 1.0, 0.0, 0.0]]) # S3
# Here S0, S1, S2, S3 are conceptual labels either
# for the Markov chain states or the digraph vertices

gP = nx.from_numpy_array(P, create_using=nx.DiGraph)
plot_gph(gP)

plot_gph(g)

g.nodes # note the ordering of vertices

Pg = nx.convert_matrix.to_scipy_sparse_array(g)
Pg.todense()

def PforG(p=0.4, N=10):
    q = 1 - p
    P = np.diag(q*np.ones(N), k=-1) + np.diag(p*np.ones(N), k=1)
    P[0, :] = 0
    P[0, 0] = 1
    P[N, :] = 0
    P[N, N] = 1
    return P
PforG(p=0.4)

from numpy.linalg import eig, inv, det
P = PforG(p=0.4)
ew, ev = eig(P)
ew

H = ev[:, abs(ew - 1) < 1e-15] # Eigenvectors of eigenvalue 1
M = np.array([H[0, :], H[-1, :]]) # Matrix of the two conditions
det(M)

def Gchances(p=0.4, N=10):
    P = PforG(p, N)
    ew, ev = eig(P)
    H = ev[:, abs(ew - 1) < 1e-15]
    M = np.array([H[0, :], H[-1, :]])
    c = inv(M) @ np.array([0, 1])
    return H @ c

h = Gchances(p=0.4)
h

import numpy as np
from random import uniform

def gamble(init=2, p=0.4, win=10, n=10000):
    """Let G gamble "n" times, starting with "init" chips."""
    wl = np.zeros(n)  # mark win or lose here for each gamble i
    for i in range(n):
        chips = init
        while chips:
            if uniform(0, 1) > p:  # losing game
                chips -= 1
            else:  # winning game
                chips += 1
            if chips == win:  # reached wanted winnings
                wl[i] = 1
                break
    return wl

n = 500000
wl = gamble(n=n)
print('Proportion of winning gambles:', np.count_nonzero(wl) / n)

plt.bar(range(len(h)), h)
plt.title('$G$\'s chances of making 10 chips');
plt.xlabel('Starting number of chips'); plt.ylabel('Probability');

plt.bar(range(len(h)), 1-h, color='red')
plt.title('Chances of $G$\'sruin');
plt.xlabel('Starting number of chips'); plt.ylabel('Probability');

plt.bar(range(len(h)), Gchances(p=0.5, N=10))
plt.title('$G$\'s chances of making 10 chips in unbiased games');
plt.xlabel('Starting number of chips'); plt.ylabel('Probability');

A = [0, 10]
B = range(1, 10)
P = PforG()
PAA = P[np.ix_(A, A)]
PBA = P[np.ix_(B, A)]
PBB = P[np.ix_(B, B)]

PBA

PBB

PAA

np.linalg.inv(np.eye(len(B)) - PBB) @ PBA

from scipy.sparse import diags, eye
from scipy.sparse.linalg import spsolve

def sparseGmats(p=0.4, N=10000):
    """ Return I - PBB and PBA as sparse matrices """
    q = 1 - p
    # Create dia_matrix
    P = diags([q * np.ones(N), p * np.ones(N)], offsets=[-1, 1], shape=(N + 1, N + 1))

    A = [0, N]
    B = list(range(1, N))

    # Convert dia_matrix to csc_matrix
    P = csc_matrix(P)

    I_PBB = (eye(N - 1) - P[B][:, B]).tocsc()
    PBA = P[B][:, A].tocsc()

    return I_PBB, PBA

def ruinG(p=0.4, N=10000):
    """ Given that the winning probability of each game is "p",
    compute the probability of G's ruin for each starting state """
    I_PBB, PBA = sparseGmats(p, N)
    return spsolve(I_PBB, PBA[:, 0])

ruinG(N=10)

fig = plt.figure()
ax = plt.gca()
hs = ruinG(N=20)
ax.plot(hs[:21], 'r-', label='N=20')
hs = ruinG(N=30)
ax.plot(hs, 'r:', label='N=30')
hs = ruinG(N=40)
ax.plot(hs, 'r-.', label='N=40')
ax.set_ylabel('Probability of G\'s ruin')
ax.set_xlabel('Starting state index')
ax.legend();

# Commented out IPython magic to ensure Python compatibility.
def least_ruin_prob(p=0.4, N0=20, dbl=11):
  """ Compute least ruin probability starting with N="N0" and
  recompute "dbl" times, doubling N each time. """
  for i in range(dbl):
    print('N = %5d, least ruin probability = %5.4f'
#       %(N0*2**i, min(ruinG(p=p, N=N0*2**i)[:21])))

least_ruin_prob(p=0.4, dbl=7)

least_ruin_prob(p=0.5, dbl=11)
