d={909:"Nandini",889:"Shahnavaj",654:"Moin",545:"Gaurav",342:"Priyank"}

print(d)
print(d[654])
print(d.get(545))
print(d.items())
print(d.keys())
print(d.values())
d1={123:"Jigar",345:"Ashish"}
d.update(d1)
print(d)
d.pop(123)
print(d)
d.popitem()
print(d)

for i in d:
    print(i," : ",d[i])
