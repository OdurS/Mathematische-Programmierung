import math
size=int(input("Wie groß soll das Haus sein?"))#größe des Hauses
i=size
breite=size*2
d=size 
bs = "\\"   
while i>1:
    #print(" "*(i-1) + "/" + " "*(2*(size-i)) + "\\")
    
    print(f"{'/':>{i}}{bs:>{(2*(size - i) + 1)}}")
    i=i-1
print("/" + "_"*(breite-2) + "\\")

#print(f"{'/':{1}}{'_':>{(breite-2)}}{bs:{1}}")
a=1
while a<=size-1:
    print("|" + " "*(breite-2) + "|")
    a=a+1
print("|" +  "_"*(breite-2) + "|")
#print(f"{'|':{1}}{'_':>{(breite-2)}}{'|':{1}}")

