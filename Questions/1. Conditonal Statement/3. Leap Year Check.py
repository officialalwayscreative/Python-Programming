# Statement
# Write a program that checks if a given year is a leap year.
Year = int(input("Enter a year :"))
if Year%400==0 :
    if Year%4==0 :
        print ("Leap Year")
    else :
        print ("Not Leap Year")
elif Year%4==0 :
    print ("Leap Year")
else :
    print ("Not Leap Year")