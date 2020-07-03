import numpy as np

def matrixinput():
    row=int(input("Input row num of Mat: "))
    col=int(input("Input col num of Mat: "))
    a=[[0 for i in range(col)] for j in range(row)]
    # print(a)
    for i in range(row):
        for j in range(col):
            # print(i,j)
            a[i][j]=input("input "+str(i+1)+","+str(j+1)+": ")
            # print(a)
            # print("---")
    a=np.asmatrix(a,float)
    print("Mat is: ")
    print(a)
    return a

def matmult(a, b):
    return a*b

print("Calc mat mult and mat power.")
selc=input("1. Mat mult.\n2. Mat power.")
if selc=='1':
    mat=[]
    num=int(input("How many matrices will you multiply?"))
    for i in range(num):
        mat.append(matrixinput())
    for i in range(num-1):
        mat[0]*=matmult(mat[0],mat[i+1])
    print(mat[0])
elif selc=='2':
    a=matrixinput()
    num=int(input("input K val:"))
    result=1
    for i in range(num):
        result=matmult(a,result)
    print(result)