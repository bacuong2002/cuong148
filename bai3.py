print("Nhập giá trị n: ")
n=int(input())
if n > 0:
    giaithua=1
    for i in range(1,n+1):
        giaithua=giaithua*i
    print(n,"giai thua:",giaithua)
else:
    print("nhap n > 0")
