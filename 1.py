num1 = int(input("Enter first number: "))
int(num1)
num2 = int(input("Enter second number: "))
int(num2)
limit = int(input("Enter the limit: "))

def sum(num1, num2, limit):
    total_sum = 0
    for i in range(1, limit):
        if i % num1 == 0 or i % num2 == 0: 
            total_sum += 1
        return total_sum
result = sum(num1, num2, limit)
print(f"The sum of multiplies of {num1} or {num2} up to is {limit} is {result}.")