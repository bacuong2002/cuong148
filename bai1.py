A = [1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]
B = []
for i in range(0,len(A)):
        if A[i]<30:
            B.append(A[i])
print("B=",B)
n=int(input("Nhập n : "))
for i in range(0,len(A)):
        if A[i]>n:
            print("B=",A[i])