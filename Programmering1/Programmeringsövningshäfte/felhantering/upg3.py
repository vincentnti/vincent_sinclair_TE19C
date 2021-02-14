MONTH_PRICE = 600
ONETIME_PRICE = 100

while True:
    try:
        print("Ange hur många spårvagns resor du vill ta")
        
        trips = input("Antal Resor: ")
        trips = trips.replace(" ", "")
        trips = int(trips)

        assert(trips > 0)
        break
    except ValueError as err:
        print("[X] Det du skriver in måste vara ett nummer och ett heltal t.ex 5")
    except AssertionError as err:
        print("[X] Måste vara fler än 0 resor")
   
month_price = MONTH_PRICE
onetime_price = trips * ONETIME_PRICE

print("Månadskostnad:", month_price, end=" ")
print("Engångskostnad:", onetime_price)

if month_price < onetime_price:
    print(f"Månadskostnaden är billigast för dig! Den är {onetime_price - month_price}kr billigare!")
else:
    print(f"Engångskostnaden är billigast för dig! Den är {month_price - onetime_price}kr billigare!")

   