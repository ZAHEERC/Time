a = int(input())
x1 = int(a/86400)
a1 = a%86400
x2 = int(a1/3600)
a2 = a1%3600
x3 = int(a2/60)
x4 = a2%60
z = ""
    
#if(a > 86400):
    #print(str(x1) + " Days " + str(x2) + " Hours " + str(x3) + " Minutes " + str(x4) + " Seconds" )
if(a1 == 0):
    print(str(x1) + " Days")
elif(a > 86400 and a2 == 0):
    print(str(x1) + " Days " + str(x2) + " Hours")
elif(3600 <= a1 < 86400):
    print(str(x1) + " Days " + str(x2) + " Hours")
elif(a > 86400 and x2 != 0 and x4 == 0):
    print(str(x1) + " Days " + str(x2) + " Hours " + str(x3) + " Minutes")
elif(a > 86400 and x2 != 0 and x3 != 0):
    print(str(x1) + " Days " + str(x2) + " Hours " + str(x3) + " Minutes " + str(x4) + " Seconds")
elif(a < 86400 and x4 == 0):
    print(str(x2) + " Hours " + str(x3) + " Minutes")
elif(a < 86400 and x4 != 0):
    print(str(x2) + " Hours " + str(x3) + " Minutes " + str(x4) + " Seconds")