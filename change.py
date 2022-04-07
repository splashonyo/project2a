print("Please enter an amount in cents less than a dollar.")
amount = eval(input())
print("Your change will be:")
print("Q:", amount // 25)
amount = amount % 25
print("D:", amount // 10)
amount = amount % 10
print("N:", amount // 5)
amount = amount % 5
print("P:", amount)
