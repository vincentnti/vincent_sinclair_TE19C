amounts = [
        1000,
        500,
        200,
        100,
        50,
        20,
        10,
        5,
        2,
        1
    ]
names= [
    "Tusenlappar: ",
    "Femhundralappar: ",
    "Tvåhundralappar: ",
    "Hundralappar: ",
    "Femtilappar: ",
    "Tjugolappar: ",
    "Tiokroner: ",
    "Femkroner: ",
    "Tvåkroner: ",
    "Enkroner: "
]

def convert_to_bills(cash):
    for i, amount in enumerate(amounts):
        if int(cash / amount) != 0:
            print(f"{names[i]}: {int(cash / amount)}")
        cash -= amount * int(cash / amount)

print("Skriv ett tal du vill konvertera till mynt/sedlar")
cash = int(input("Tal: "))
convert_to_bills(cash)