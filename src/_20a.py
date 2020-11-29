from functools import reduce

# https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def get_presents_for_house(house_n):
    return sum(i * 11 for i in factors(house_n) if house_n / i <= 50)

i = 1
while True:
    presents = get_presents_for_house(i)
    if presents > 34000000:
        print(i)
        break
    i+=1
