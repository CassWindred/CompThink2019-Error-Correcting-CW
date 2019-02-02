import numpy as n

def findminr(L):
    r=2

    while ((2**r)-(2*r)-1)<L:
        r += 1

    return r

def message(a):
    r = findminr(len(a)) #Find the minimum possible value of r

    out=[]
  #Start with the binary representation of the length
    for i in (n.binary_repr(len(a))):
        out.append(int(i))
    while len(out)<r:
        out.insert(0,0) #Add a zero at location 0
    out.extend(a)
    k=((2**r)-(r)-1)
    print(str(k))
    while len(out)<k:
        out.append(0)
    return out


print(str(message([1,1,1,1,0,1])))

    
    
                         

