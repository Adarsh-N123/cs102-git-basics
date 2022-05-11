def CheckMatrix(A: list)->bool:
    count=0
    L=[]
    valid = True
    x = len(A)
    if len(A)==0:
        return False
    else:
        for i in A:
            for j in i:
                if type(j)==str or type(j)==int:
                    valid = False

        if valid==True:            
            for i in A:
                if len(i)==0:
                    count=count+1
            if count==x:
                return False
            else:
                for i in A:
                    L.append(len(i))
                if max(L)==min(L):
                    return True
                else:
                    return False
        else:
            return False

def Addition(A:list,B:list) -> list:
    if CheckMatrix(A)==True and CheckMatrix(B)==True:
        L1=[]
        L2=[]
        L3=[]
        for i in A:
            L1.append(len(i))
        for j in B:
            L2.append(len(j))
        if L1!=L2:
            return None
        else:
            for i in range(len(A)):
                a = A[i]
                b = B[i]
                l=A[i]
                for k in range(len(A[i])):
                    l[k]=a[k]+b[k]
                L3.append(l)
            return L3

                
    else:
        return None

def Multiplication(A:list,B:list) -> list:
    if CheckMatrix(A)==True and CheckMatrix(B)==True:
        a = len(A)
        for i in A:
            b = len(i)
        c = len(B)
        for j in B:
            d = len(j)
        
        if b!=c:
            return None
        else:
            p = len(A)
            q = len(A[0])
            
            t = len(B)
            r = len(B[0])
            C = []
            for row in range(p):
                curr_row = []
                for col in range(r):
                    curr_row.append(0)
                C.append(curr_row)
            for i in range(p):
                for j in range(r):
                    curr_val = 0
                    for k in range(q):
                        curr_val += A[i][k]*B[k][j]
                    C[i][j] = curr_val
            return C


    else:
        return None
        
def Transpose(A:list) -> list:
    if CheckMatrix(A)==True:
        
        
        transpose= [ [A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
        return transpose
    else:
        return None
def Symmetric(A: list)->bool:
    if CheckMatrix(A)==True:
        if Transpose(A)==A:
            return True
        else:
            return False
    else:
        return False
print(Multiplication([[1.00,2.00],[3.00,4.00]],[[7.00,8.00],[4.00,1.00]]))
    





