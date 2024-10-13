
def pow_recursive(n,exp):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n*pow(n,exp-1)

print(pow_recursive(2,3))
print(pow_recursive(237,61))