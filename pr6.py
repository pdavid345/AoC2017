with open('inputs/6') as f:
    dat = f.read().split('\t')

vals = [int(i) for i in dat]

# vals = [0, 2, 7,0]
perms = []
perms = perms + [vals.copy()]

isMatch = False
nCycle = 0
import math

while (not isMatch):
    maxVal = max(vals)
    for i,n in enumerate(vals):
        if n == maxVal:
            idx = i
            break
    vals[idx] =0
    vals = vals[idx+1:] + vals[0:idx+1]
    for i in range(len(vals)):
        vals[i] = vals[i] + math.floor(maxVal / (len(vals))) + int(maxVal%len(vals) > i)
    vals = vals[len(vals)-idx-1:] + vals[0:len(vals)-idx-1]
    if vals in perms:
        isMatch = True
        for iCycle,C in enumerate(perms):
            if vals == C:
                nCycle = iCycle

        break
    else:
        perms =perms + [vals.copy()]

print(len(perms))
# for k in perms:
#     print(k,'\n')
print(len(perms)-nCycle)











