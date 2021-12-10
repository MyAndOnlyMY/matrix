s = int(input())
r = int(input())

# zero-main-d matrix
zmd = [1]*s
for i in range(s):
    zmd[i] = [1]*r
    for j in range(r):
        if i==j:
            zmd[i][j] = 0
for i in zmd:
    print(*i)

print()

# string nub matrix
snm = [0]*s
for i in range(s):
    snm[i] = [i+1]*r
for i in snm:
    print(*i)

print()

# num line matrix
nlm = [0]*s
count = 1
for i in range(s):
    nlm[i] = [0]*r
    for j in range(r):
        nlm[i][j] = count
        count +=1
for i in nlm:
    print(*i)

print()

# zero-num matrix
znm = [0]*s
for i in range(s):
    _count = 1
    znm[i] = [0]*r
    for j in range(r):
        if j%2==0:
            znm[i][j] = 0
        else:
            znm[i][j] = _count
            _count += 1
for i in znm:
    print(*i)