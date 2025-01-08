a=int(input("Enter an year"))
def leap_year(num):
    if num%4==0:
        if num%100==0 and num%400==0:
           return "year is leap"
        elif num%100==0:
            return "year not leap"
        else:
            return "year is leap"
print(leap_year(a))
