prices = {"banana" : 4,
          "apple" : 2,
          "orange" : 1.5,
          "pear" : 3}

stock = {"banana": 6,
         "apple": 0,
         "orange": 32,
         "pear": 15}

for item in prices.keys():
    print item
    print "price: " + str(prices[item])
    print "stock: " + str(stock[item])

sum = 0
for key in prices:
    sum += prices[key] * stock[key]
print "the total value of the stock is: " + str(sum)

def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
        else:
            print("sorry, " + item + " is sold out!")
    return total

print "the bill for you is: " + str(compute_bill(["apple", "pear", "pear"]))