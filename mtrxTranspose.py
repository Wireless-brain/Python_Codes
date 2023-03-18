#Matrix Transpose

#To create a matrix
def newMtrx(r, c):
    m=[]
    print("\n\tEnter the matrix elements: ")
    for i in range(r):
        a=[]
        for j in range(c):
            a.append(int(input()))
        m.append(a)
    print("\n\tThe entered matrix: ")
    prntMtrx(m)
    return m

#To print a matrix
def prntMtrx(m):
    print()
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j]," ",end='')
        print()
        
#To find the transpose
def transpose(m, r, c):
    s=[]
    for j in range(c):
        a=[]
        for i in range(r):
            a.append(m[i][j])
        s.append(a)
    print("\n\tThe transpose of the matrix is: ")
    prntMtrx(s)
            
#Main
row=int(input("\n\tEnter the number of rows: "))
col=int(input("\n\tEnter the number of colomns: "))
m1=newMtrx(row, col)
transpose(m1, row, col)