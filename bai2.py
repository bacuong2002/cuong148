A = [1,1,2,3,5,8,13,21,34,55,88]
B = [1,3,5,4,7,88,66,59,40,54]
print("list A=",A)
print("list B=",B)
C =  set(A)&set(B)
for i in C:
    print("list C=",C)
D= list(set (A) ^ set (C))
print("cac phan tu list A k trung vơi B:",D)
E= list(set (B) ^ set (C))
print("cac phan tu list B k trung vơi B:",E)

