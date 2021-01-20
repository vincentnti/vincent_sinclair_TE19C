import random
class Dice:
    def throw (self, amount):
        results = []
        for _ in range(amount):
            results.append(random.randint(1,6))
        return results

dice = Dice()
results = dice.throw(1000000)
proportion = results.count(5)/len(results) #Andel = Delen / Hela
print(proportion)