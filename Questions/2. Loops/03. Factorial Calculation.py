# Statement
# Write a program that calculates the factorial of a given number using a while loop
Num = int(input("Enter a number :"))
Factorial = 1
while Num > 0 :
    Factorial = Factorial * Num
    Num -= 1
print (Factorial)