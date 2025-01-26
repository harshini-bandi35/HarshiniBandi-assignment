t=int(input())
for i in range(t):
    year=int(input("enter the year: "))
    if year%100==0:
        if year%4==0 and year%400==0:
            print(f"The {year} is a leap year")
        else:
            print(f"The {year} is not a leap year")
    if year%100!=0:
        if year%4==0:
            print(f"The {year} is a leap year")
        else:
            print(f"The {year} is not a leap year")