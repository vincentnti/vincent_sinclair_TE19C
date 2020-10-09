"""
1L mjölk innehåller 15000000 bakterier
I rumstemp ökar antalet med 50% varje timme
Mjörk blir sur när den överstiger 100000000 st
hur många timmar tar det tills mjölken blir sur?
"""
import matplotlib.pyplot as plt
import numpy as np

virus = 15000000
timme = 0

#Extra från genomgång {
y_bakterier = [virus]
x_timmar = [timme]
#}
while virus < 10 * 10000000:
    virus *= 1.5
    timme += 1
    y_bakterier.append(virus)

x_timmar = np.arrange(timme+1)

#Extra från genomgång {
plt.plot(x_timmar,y_bakterier, "*-")
plt.xlabel("Timmar (h)")
plt.ylabel("Antal bakterier")
plt.title("Bakterietillväxt i mjölk")
plt.show()
#}
print("Efter ", timme, " Timmar har mjölken blivit sur i rumstemperatur")
