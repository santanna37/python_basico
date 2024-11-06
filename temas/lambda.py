def func(n):
    return lambda a: a*n
# a*2
doubler = func(2)
print(doubler(3))
quintipler = func(5)
print(quintipler(3))

def price_calc(start,hourly_rate):
    return lambda hours: start + hourly_rate * hours
    
walkin_cost = price_calc(10,30)


