def gcd(a,b) :
    if b==0 :
        return a
    else :
        return gcd(b,a%b)
a = int(input())
b = int(input())
if a>b :
    temp = a
    a = b
    b = temp
print('gcd is',gcd(a,b))