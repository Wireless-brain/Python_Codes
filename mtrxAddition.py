#Matrix Addition
def newMtrx():
    m=[]
    row=int(input("\n\tEnter the number of rows: "))
    col=int(input("\n\tEnter the number of colomns: "))
    print("\n\tEnter the matrix elements: ")
    for i in range(row):
        a=[]
        for j in range(col):
            a.append(int(input()))
        m.append(a)
    return m

def prntMtrx(m):
    print()
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j]," ",end='')
        print()
        
def mtrxAdd(m1,m2):
    s=[]
    for i in range(len(m1)):
        a=[]
        for j in range(len(m1[i])):
            a.append(m1[i][j]+m2[i][j])
        s.append(a)
    print("\n\tThe sum of the matrices: ")
    prntMtrx(s)
        
print("\n\tFor the first matrix,")
m1=newMtrx()
prntMtrx(m1)
print("\n\tFor the second matrix,")
m2=newMtrx()
prntMtrx(m2)
mtrxAdd(m1,m2)