t = input("enter the number of test cases :")
l = input("enter the initial range")
r = input("enter the final range ")
count= 0
prime = 0

for i in range(0,t):
    for j in range (l,r,1):
        for k in range(1,r):
            if j%k == 0:
                count=count +1
                continue 
        if count == 2:
            print j

    
        
            
