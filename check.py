#!/usr/bin/env python3

a = 0.922863
b = [0.0, 0.0, 0.0, 0.114038, 0.186479, 0.238143, 0.277239, 0.308030, 0.332974,
  0.353536, 0.370540, 0.384771, 0.396884, 0.408715, 0.418855, 0.427643, 0.435333,
  0.442118, 0.448149, 0.453544, 0.458401, 0.462794, 0.466788, 0.470435, 0.473778,
  0.476853, 0.479691, 0.482320, 0.484760, 0.487032, 0.489153, 0.489153]
c = 3.460

eps = 1e-7 # for avoiding rounding errors

# enumerate all d
def all_d(d, i, d_min):
    yield d
    if i < 4:
        for di in range(d_min, 32):
            yield from all_d(d + [di], i + 1, di)

# inequality (1)
for d in all_d([], 0, 3):
    f = len(d)
    d_prime = 4 + sum(d) - 2 * f
    delta1 = 1 - f * a / 4 + sum(map(lambda di: b[di] - b[di-1], d))
    delta2 = a - 2 * a / 4 + sum(map(lambda di: b[di], d)) - b[min(30, d_prime)]
    assert(c**(-delta1) + c**(-delta2) <= 1 - eps)

# inequality (2)
for D in range(5, 32):
    for d_prime in range(D, 32):
        assert(-2 * a / D - b[d_prime] + 2 * a / (D - 1) + b[d_prime - 1] >= eps)

# inequality (3)
for d_f in range(3, 32):
    for d_prime in range(d_f+1, 32):
        assert(b[d_f] - b[d_prime] + b[d_prime - d_f + 2] >= eps)

print("all the inequalities are satisfied")