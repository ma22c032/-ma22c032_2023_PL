# -*- coding: utf-8 -*-
"""The Singular Value Decomposition

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19bDPYVsZu-zAqOV39E81g4IclK8aUs9F
"""

!pip install gitpython

from scipy.linalg import svd
import numpy as np
np.set_printoptions(precision=3, suppress=True)

a = np.random.rand(4, 5) + 1j * np.random.rand(4, 5)
u, s, vh = svd(a)

u @ u.T.conjugate() # u is unitary. Its columns are left singular vectors

vh @ vh.T.conjugate() # Rows of vh are right singular vectors

s # Only the diagonal entries of Sigma are returned in s

a = np.random.rand(4, 5)
u, s, vh = svd(a)

u[0, :, np.newaxis] @ vh[np.newaxis, 0, :]

np.outer(u[0, :], vh[0, :])

ar = np.zeros_like(a)
for i in range(4):
  ar += np.outer(u[:, i], s[i] * vh[i, :])

a - ar # a and ar are identical

a = np.array([[0.1, 0.5], [0.4, 0.8]])
u, s, vh = svd(a)

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline
def show(c):
  plt.plot(c[0, :], c[1, :])
  plt.axis('image');
# plot the unit circle and axis segments:
t = np.linspace(0, 3.5 * np.pi , num=300)
l = np.linspace(-1, 1, num=10)
z = np.zeros_like(l)
c = np.array([np.concatenate([l, np.cos(t), z]),
             np.concatenate([z, np.sin(t), l])])
show(c)

show(a @ c)

show(vh @ c)

show(np.diag(s) @ c)

show(u @ c)

show(u @ np.diag(s) @ vh @ c)

cats = plt.imread('/content/cat.png')
cats.shape

np.linalg.norm(cats[..., 0] - cats[..., 2], 'fro')

c = cats[..., 0]
plt.imshow(c, cmap='gray');

u, s, vh = svd(c)#Perform Singular Value Decomposition (SVD) on the red color channel

plt.plot(s);

# Rank 20 approximation of the cats:
l = 20; cl = u[:, :l] @ np.diag(s[:l]) @ vh[:l, :]
plt.imshow(cl, cmap='gray');

# Rank 50 approximation of the cats:
l = 50; cl = u[:, :l] @ np.diag(s[:l]) @ vh[:l, :]
plt.imshow(cl, cmap='gray');

relative_error = 1.e-1

s2 = s**2
total = np.sum(s2)
diff = np.sqrt((total - np.add.accumulate(s2)) / total)
l = np.argmax(diff < relative_error) + 1
l

cl = u[:, :l] @ np.diag(s[:l]) @ vh[:l, :]

np.linalg.norm(c - cl, 'fro') / np.linalg.norm(c, 'fro')

u.shape[0] * l + l + l * vh.shape[0]

c.shape[0] * c.shape[1]

