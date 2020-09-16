degree = float(input("Grader: "))

def eval_degree(degree):
    if degree == 180:
        eval = "Rak"
    elif degree == 90:
        eval = "Rät"
    elif degree > 180 and degree < 360:
        eval = "Konvex"
    elif degree == 360:
        eval = "Hel"
    elif degree == 0:
        eval = "Null"
    elif degree < 90:
        eval = "Spetsig"
    elif degree > 90:
        eval = "Trubbig"
    return eval

answer = eval_degree(degree)
print("Vinkeln är en:", answer, "Vinkel")