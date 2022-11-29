with open('inputs/5') as f:
    dat = f.read().split('\n')

vals = [int(i) for i in dat]
# print(vals)

# vals = [0,3,0,1,-3]
# print(vals)

idx = 0
cycleCount = 0

while idx < len(vals):
    cycleCount = cycleCount + 1
    jmpVal = vals[idx]
    if(jmpVal > 2):
        vals[idx] = vals[idx] - 1
    else:
        vals[idx] = vals[idx] + 1
    idx = idx + jmpVal
    # print(vals)

print('Cyclecount: ',cycleCount)