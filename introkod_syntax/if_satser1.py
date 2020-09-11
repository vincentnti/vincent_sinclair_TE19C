#Jämt eller udda
"""
tal = int(input("Tal: "))
if tal % 2 == 0:
    print("Jämt")
else: 
    print("Udda")

print(tal%2)
"""
#Vinkel

vinkel = float(input("Ange en vinkel v i grader där v är stlrre än >= 0 <= 360: "))

if vinkel == 90:
    print("rät")
elif vinkel < 90 and vinkel >= 0:
    print("spetsig")
elif vinkel > 90 and vinkel < 180:
    print("trubbig") 
else:
    print("annat inte rät, spetsig eller trubbig")