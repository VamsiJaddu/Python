#  Simple Interest 
#  s = (P*T*R)/100

P = float(input("Enter the principal value : "))
T = float(input("Enter the Time : "))
R = float(input("Enter the rate of interest value : "))

si = (P*T*R)/100
print("Simple Interest :" , si)

# compond Interest

#  A = P[1 +R/100]**T

# ci = A-P

# A = P*(1 + R/100)**T
A = P*(pow(1 + R/100,T))

ci = A - P 
print("Compound Interest :" ,round(ci,2))











