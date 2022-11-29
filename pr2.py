with open('inputs/2') as f:
    dat = f.readlines()

dat2 = [l[:-1].split('\t') for l in dat]

sumL = 0
for l in dat2:
    sumL = sumL + max([int(i) for i in l]) - min([int(i) for i in l])
print(sumL)

# part 2

count = 0
from itertools import permutations

for l in dat2:
    perms = permutations([int(i) for i in l],2)
    for p in perms:
        if(p[0]%p[1] == 0):
            count = count+ int(p[0]/p[1])

print(count)




