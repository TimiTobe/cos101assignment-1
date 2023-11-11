print("YUSUF AND SONS")
print("please fill in the required information correct")
p = float(input("what is your principle? "))
r = float(input("what is your interest rate? "))
n = int(input("Enter the number of times interest applies per time period? "))
t = float(input("Enter the number of time periods elapsed"))


SI = p* (1 + r*t)

CI = p* (1 + r/n)**(n*t)

print(f'simple interest = {SI}, compound interest = {CI}')




