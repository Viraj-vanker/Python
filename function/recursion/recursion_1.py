def vv(a):
    if len(a)==0:
        return 0
    return a[0]+vv(a[1:])
print(vv([10,20,30,40]))