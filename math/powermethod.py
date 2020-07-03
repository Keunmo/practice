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

def powermethod(a,iter_vec):
    count=0
    while True:
        count+=1
        tmp=iter_vec
        #y=iter_vec/max(iter_vec.max(), iter_vec.min(), key=abs)
        x=matmult(a,iter_vec)
        print("---")
        print("x",count,":\n",x)
        m=max(x.max(), x.min(), key=abs) #만약 두 수의 절대값이 같다면 양수가 선택됨.
        iter_vec=x/m
        print("y",count,":\n",iter_vec)
        print("m",count,":\n",m)
        #error=abs(np.min(np.abs(tmp))-np.min(np.abs(iter_vec))) #이전y의 최소절대값과 현재y의 최소절대값 비교. -> 안되는 경우 있음
        error=np.sum(np.abs(tmp-iter_vec), axis=0)  #이전y-현재y의 절대값 행 성분합.
        if error<0.001:
            break
        elif count>20:
            print("Not converge!")
            break
        
    return iter_vec, m 

print("Calc eigenvalue and eigenvector.")
selc=input("Choose method.\n1. Power Method.\n2. Shifted Power method.\n3. Inverse Power Method.\n4. Shifted Inverse Power Method.\n")
if selc == "1":
    print("Select Power Method.")
    print("Input Matrix.")
    a=matrixinput()
    print("Input initial vector: ")
    print("*LARGEST COMPONENT SHOULD BE 1*")
    iter_vec=matrixinput()
    eig_vec, eig_val = powermethod(a,iter_vec)
    print("======================")
    print("eigen vector: \n", eig_vec)
    print("eigen value: \n", eig_val)
elif selc == "2":
    print("Select Shifted Power Method.")
    print("Input Matrix.")
    a=matrixinput()
    p_eigval=int(input("Input privious dominent eigen value: "))
    n=a.shape[0] #a행렬의 행 또는 열. =정방행렬의 크기.
    a=a-(np.eye(n)*p_eigval)    #a에서 pr_eigval단위행렬을 뺌.
    print("Input initial vector: ")
    print("*LARGEST COMPONENT SHOULD BE 1*")
    iter_vec=matrixinput()
    eig_val = powermethod(a,iter_vec)[1]+p_eigval
    print("======================")
    print("eigen value: \n", eig_val)
elif selc == "3":
    print("Select Inverse Power Method.")
    print("Input Matrix.")
    a=matrixinput().I   #inverse matrix of a.
    print("Input initial vector: ")
    print("*LARGEST COMPONENT SHOULD BE 1*")
    iter_vec=matrixinput()
    eig_val = 1/powermethod(a,iter_vec)[1]  #m값의 역수.
    print("======================")
    print("eigen value: \n", eig_val)
elif selc == "4":
    print("Select Shifted Inverse Power Method.")
    print("Input Matrix.")
    a=matrixinput()
    alpha=int(input("Input alpha value: "))
    n=a.shape[0]
    a=a-(np.eye(n)*alpha)
    a=a.I
    print("Input initial vector: ")
    print("*LARGEST COMPONENT SHOULD BE 1*")
    iter_vec=matrixinput()
    eig_val = alpha+(1/powermethod(a,iter_vec)[1])  #alpha+m값의 역수.
    print("======================")
    print("eigen value: \n", eig_val)
else:
    print("Bye")
    


