# Jane Doe, Max Mustermann, Blatt 1 - Aufgabe 1

# Beispiel aus der Vorlesung zur Berechnung und Ausgabe 
# von Quadratzahlen und Wurzeln
import math

i = 1
length=int(input("Gebe Natürliche Zahl an"))
while i <= length:
    # Berechne die Quadratzahl und die Wurzel aus der Zahl i
    if (i % 2 ==0):
        square = i*i
        sqrt = math.sqrt(i)

        print("{:2d} | {:3d} | {:.4f}".format(i, square, sqrt))
    i = i + 1
    
