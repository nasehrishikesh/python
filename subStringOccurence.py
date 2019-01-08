a=input("enter the string: ")
sub_str=input("input sub string to be found: ")
L=[]
si=0

while sub_str in a[si:len(a)]:
    i=a.index(sub_str,si)
    L.append(i)
    si=i+1

print(L)
