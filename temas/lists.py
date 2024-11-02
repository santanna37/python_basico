
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
sold = 1.5

#Add another day to week
sales_w2.append(int(input("Add another day: ")))

# Compbine the two lists
sales.extend(sales_w1)
sales.extend(sales_w2)

# Calcule and print how much :
best_day = max(sales)*sold
worst_day = min(sales)*sold

#prints
print(f"best day {best_day}")
print(f"worst day: {worst_day}")
print(f"bombine: {best_day+worst_day}")