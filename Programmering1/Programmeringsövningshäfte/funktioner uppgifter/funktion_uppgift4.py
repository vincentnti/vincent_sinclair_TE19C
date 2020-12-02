def konv_till_lämpliga_pengar(cash):
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
    names = [
        "Tusenlappar: ",
        "Femhundralappar: ",
        "Tvåhundralappar: ",
        "Hundralappar: ",
        "femtilappar: ",
        "tjugolappar: ",
        "tiokroner: ",
        "femkroner: ",
        "tvåkroner: ",
        "enkroner: "
    ]
    i = 0
    for amount in amounts:
        print(names[i], int(cash / amount))
        i+= 1
        cash -= int(cash / amount) * amount

konv_till_lämpliga_pengar(13353)

#Fungerar men vill ändra lite 