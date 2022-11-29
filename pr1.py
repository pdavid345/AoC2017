with open('inputs/1') as f:
    dat = f.read()

# print(dat)

# append 0th item to end of dat
dat = dat + dat[0]

L = len(dat)-1



count =0
for i in range(L):
    if dat[i] == dat[i+1]:
        count = count+int(dat[i])
print(count)


# Part 2

count =0
for i in range(L-1):
    if dat[i] == dat[int((i+L/2)%L)]:
        count = count+int(dat[i])
print(count)



