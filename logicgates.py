def AND(a,b):
    if a==1 and b==1:
        return True
    return False
print("AND LOGIC GATE")
print("A=True | B=True | A and B="+str(AND(1,1)))
print("A=True | B=False | A and B="+str(AND(1,0)))
print("A=False | B=True | A and B="+str(AND(0,1)))
print("A=False | B=False | A and B="+str(AND(0,0)))

print()

def OR(a,b):
    if a==0 and b==0:
        return False
    return True
print("OR LOGIC GATE")
print("A=True | B=True | A or B="+str(OR(1,1)))
print("A=True | B=False | A or B="+str(OR(1,0)))
print("A=False | B=True | A or B="+str(OR(0,1)))
print("A=False | B=False | A or B="+str(OR(0,0)))

print()

def NOT(a):
    if a==0 or a==1:
        return not a

print("OR LOGIC GATE")
print("A=True | not A="+str(NOT(1)))
print("A=False | not A="+str(NOT(0)))
