a=input('请输入第1个数字:')
b=input('请输入第2个数字:')
c=input('请输入第3个数字:')
d=input('请输入第4个数字:')
x=[int(a),int(b),int(c),int(d)]
for i in range(len(x)):
    for j in range(i+1):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]
print(x)
