kata = input("Input : ")
print ("Output :")
for i in range (len(kata)-1):
    print (" "*(len(kata)-i)+kata[0:i+1])
for i in range (len(kata)+1):
    print (" "*(i+1)+kata[0:len(kata)-i])