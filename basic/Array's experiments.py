a = [x for x in range(1,6)]
b = [x for x in range(6,11)]
c = a,b
с = list(c)
print((c[0]),'\n',(c[1]))

c[0][1] = 15
c[0][3] = 15
c[1][0] = 15
c[1][2] = 15
c[1][4] = 15

print('     New Array \n',(c[0]),'\n',(c[1]))

f1 = filter(lambda x: x==15,c[0])
f2 = filter(lambda x: x==15,c[1])
d = zip(f1,f2)
print(list(d))

def delete(Array):
    Array_temp = []
    for i in range(len(Array)):
        if Array[i]!=15:
            Array_temp.append(Array[i])
    return(Array_temp)

def delete_map(val):
    if val != 15:
        return val
    else:
        return None

c0 = delete(c[0])
c1 = delete(c[1])
c_new = [c0,c1]
print(f"c_new variable -> {c_new}")

c00 = list(filter(lambda x: x!=None,map(delete_map,c[0])))
c01 = list(filter(lambda x: x!=None,map(delete_map,c[1])))
c_new1 = [c00,c01]
print(f"c_new1 variable ->{c_new1}")