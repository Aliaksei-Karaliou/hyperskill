income = int(input())

if income <= 15527:
    tax_percent = 0
elif income <= 42707:
    tax_percent = 15
elif income <= 132406:
    tax_percent = 25
else:
    tax_percent = 28

calculated_tax = income * tax_percent / 100

print(f"The tax for {income} is {tax_percent:.0f}%. That is {calculated_tax:.0f} dollars! ")
