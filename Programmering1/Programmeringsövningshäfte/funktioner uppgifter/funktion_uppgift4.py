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
    for i, amount in enumerate(amounts):
        print(names[i], int(cash / amount))
        cash -= int(cash / amount) * amount

konv_till_lämpliga_pengar(13353)
