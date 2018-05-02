#grade checking
#70 - 100 =A
#60 - 69=B
#50 - 59=C
#45 - 49=D
#40 - 44=E
#0 - 39=F

if(x>70 and x <=100):
    print("A")
elif(x<=69 and x>=60):
    print("B")
elif(x<=59 and x>=50):
    print("C")
elif(x<=49 and x>=45):
    print("D")
elif(x<=44 and x>=40):
    print("E")
elif(x<=39 and x>=0):
    print("F")
else:
    print("repeat class")
