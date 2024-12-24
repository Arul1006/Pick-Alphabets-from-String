s = input("enter a string ").lower()
l = list(s)
m = []
#print(l) just for checking if current logic working
for j in l:
    if l.count(j) >= 1 and m.count(j) == 0 and j != " ":
        m.append(j)
        n = sorted(m)
print(n)




"""
a=list(input("Enter string\n").lower())
i=97
for i in range (123):
    for j in range (len(a)):
        if a[j] == chr(i):
            print(chr(i))
            a= "".join(a)
            a = a.replace(chr(i), '*')
            a=list(a)
            break
"""































































