a=[(90,20),(30,40),(50,60),(70,80)]
def aa(a):
    b=sorted(a)
    i=len(b)
    f=b[0]
    l=b[i-1]
    return (f,l)
(f,l)=aa(a)
print(f)
print(l)