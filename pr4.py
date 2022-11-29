with open('inputs/4') as f:
    dat = f.read().split('\n')

lines = [l.split(' ') for l in dat[:-1]]
# print(lines)
c=0
for l in lines:
    if(len(set(l)) == len(l)):
        c = c+1

print(c)

# part 2
def sortLetters(w):
    A = [*w]
    A.sort()
    w = (''.join(A))
    return w

c=0
for l in lines:
    for i in range(len(l)):
        l[i] = sortLetters(l[i])    
    if(len(set(l)) == len(l)):
        c = c+1
print(c)









