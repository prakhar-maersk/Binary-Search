def sort(n):
    return sorted(n)

def search(x,s):
    n=len(x)//2
    # print(n,x[n],s)
    if x[n]==s:
        return n
    elif n<=1:
        return False
    else:
        if s<x[n]:
            x=x[0:n]
            return search(x,s)
        else:
            x=x[n:len(x)]
            return search(x,s)+n

x=[8,6,4,5,9,7,1,2,49,56,78,59,12,3,54]

q=sort(x)
print(q)
s=int(input("Enter a no."))
print(search(q,s))