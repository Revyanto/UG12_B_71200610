x = int(input("Input : "))
print ("Output :")
for i in range (1,x):
    if i > 1:
        print ("  "*(x+1-i) +" *"+"  "*(i-2)+" *")
    else:
        print ("  "*(x+1-i)+" *"*i)
print ("  "+" *"*x) 