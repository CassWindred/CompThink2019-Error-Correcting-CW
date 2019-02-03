import numpy as np

# function HammingG
# input: a number r
# output: G, the generator matrix of the (2^r-1,2^r-r-1) Hamming code
def hammingGeneratorMatrix(r):
    n = 2 ** r - 1

    # construct permutation pi
    pi = []
    for i in range(r):
        pi.append(2 ** (r - i - 1))
    for j in range(1, r):
        for k in range(2 ** j + 1, 2 ** (j + 1)):
            pi.append(k)

    # construct rho = pi^(-1)
    rho = []
    for i in range(n):
        rho.append(pi.index(i + 1))

    # construct H'
    H = []
    for i in range(r, n):
        H.append(decimalToVector(pi[i], r))

    # construct G'
    GG = [list(i) for i in zip(*H)]
    for i in range(n - r):
        GG.append(decimalToVector(2 ** (n - r - i - 1), n - r))

    # apply rho to get Gtranpose
    G = []
    for i in range(n):
        G.append(GG[rho[i]])

    # transpose
    G = [list(i) for i in zip(*G)]

    return G

def hammingHMatrix(r):
    H=[]
    for i in range(1,2**r):
        H.append(decimalToVector(i,r))

    return H



# function decimalToVector
# input: numbers n and r (0 <= n<2**r)
# output: a string v of r bits representing n
def decimalToVector(n, r):
    v = []
    for s in range(r):
        v.insert(0, n % 2)
        n //= 2
    return v

def vectorToDecimal(v):
    if type(v) is not list:
        v=v.tolist()
    v.reverse()
    out=0
    for i in range(len(v)):
        out+=v[i]*(2**i)
    return out



#Question 1
def message(a):
    r = 2

    while ((2 ** r) - (2 * r) - 1) < len(a): #Find the lowest possible value of r
        r += 1

    out=[]
  #Start with the binary representation of the length
    #for i in (n.binary_repr(len(a))):
    #    out.append(int(i))
    out.extend(decimalToVector(len(a),r))
    while len(out)<r:
        out.insert(0,0) #Add a zero at location 0
    out.extend(a)
    k=((2**r)-(r)-1)
    while len(out)<k:
        out.append(0)
    return out


#Question 2
def hammingEncoder(m):
    r=2
    while not len(m)==(2**r-r-1):
        r+=1
        if r>len(m):
            return []
    genarray=hammingGeneratorMatrix(r)
    m = np.array(m)
    out = np.matmul(m,genarray)%2
    out=out.tolist()

    return out

#Question 3
def hammingDecoder(v):
    r=2
    while not len(v)==(2**r-1):
        r+=1
        if r>len(v):
            return []


    H = hammingHMatrix(r)

    i=np.matmul(v,H)%2

    if i is [0,0,0]:
        return v
    else:
        errorpoint=vectorToDecimal(i)-1
        if v[errorpoint]==1:
            v[errorpoint]=0
        else:
            v[errorpoint]=1
    return v



#print(str(hammingDecoder([0,1,1,0,0,0,0])))

#Question 4
def messageFromCodeword(c):
    r=2
    while not len(c)==(2**r-1):
        r+=1
        if r>len(c):
            return []


    check=0
    out=[]
    for i in range(len(c)):
        if i+1==2**check:
            check+=1
        else:
            out.append(c[i])
    return out

#print(messageFromCodeword([1,1,1,0,0,0,0]))

#Question 5
def dataFromMessage(m):
    r=2
    #Find r
    while not len(m)==(2**r-r-1):
        r+=1
        if r>len(m):
            return []

    #The first r units of the message is L in binary
    binaryL=[]
    for i in range(r):
        binaryL.append(m[i])
    L=vectorToDecimal(binaryL)
    out=[]
   # print(m)
    if r+L>len(m):
        return []
    for i in range(r,r+L):
     #   print(i)
        out.append(m[i])
    print("R is ",r)
    print("L is ", L)
    print(out)
    return out





#Question 6
def repetitionEncoder(m,n):
    out = []
    for i in range(0,n):
        out.append(m[0])
    return out

#Question 7
def repetitionDecoder(v):
    zcount=v.count(0)
    ocount=v.count(1)
    if zcount==ocount:
        return []
    elif zcount>ocount:
        return [0]
    else:
        return [1]