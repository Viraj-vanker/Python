p1={"name": "viraj", "age": 18}
p2={"name": "vanker", "age": 18}
p3={"name": "vir", "age": 18}
a={
    "p1":p1,
    "p2":p2,
    "p3":p3
    }
for i in a.keys():
    for j in a.values():
        print(i,j)
    break