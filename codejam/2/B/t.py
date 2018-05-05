ss = ['?' for i in range(97)]

ks = [

    (81, 96, 2),
    (71, 86, 1),
    (11, 26, 0),
    (1, 16, 1),
    (61, 76, 3),
    (51, 66, 1),
    (21, 36, 1),
    (41, 56, 4),
    (31, 46, 0),

]
ks.sort(key=lambda x:x[2])
print ks

for k in ks:
    if k[2]==0:
        for i in range(k[0]-1,k[1]):
            ss[i] =0
    else:
        if ss[k[0]-1:k[1]].count('1') > k[2]:
            print "error"
        else:
            while ss[k[0]-1:k[1]].count('1') < k[2]:
                print "suit 1"
                for i in range(k[1]-1,k[0]-2,-1):
                    if ss[i] =="?":
                        ss[i] =1
                        break

print ks