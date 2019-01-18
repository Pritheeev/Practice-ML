arr = list(raw_input("enter the array to check if it is a rainbow like eg.1234"))
l = len(arr)
for i in range (0,l):
    if int(arr[i+1])==int(arr[i])+1:
        continue
    else:
        print "no"
        break
print "yes"
    
    
