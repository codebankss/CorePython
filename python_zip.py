import time
SIZE = 100000

L1 = list(range(SIZE))
L2 = list(range(SIZE))

start = time.time()
add = [(x+y) for x, y in zip(L1, L2)]
end = time.time()

print((end - start))

