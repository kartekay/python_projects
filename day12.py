def is_prime(num):
    if num==1:
        return False
    for i in range(1,num+1):
        if i!=1 and i!=num:
            if num%i==0:
                return False
        
    return True
print(is_prime(int(input("input your number"))))
