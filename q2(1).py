import random


random.seed(2023)


for i in range(10):
    weight = random.randint(1, 20)
    cost = 0
    # if weight <= 3:
    #     cost += 2.75 * 3
    # else:
        #while weight >= 0:
    if weight > 15:
        cost += (weight - 15) * 3.70
        cost += ((8*3.17) + (4*3) + (3*2.75))
    elif weight > 7:
        cost += (weight - 7) * 3.17
        cost += ((4*3) + (3*2.75))
    elif weight > 3:
        cost += (weight - 3) * 3
        cost += (3 * 2.75)
    else:
        cost += 2.75 * 3

    print(f'The shipping price for a {weight}kg package is ${cost:.2f}')
        
                