hrs = input("Enter Hours:")
h = float(hrs)
rate = input ("Enter rate")
r = float(rate)
ot = 1.5 * r
pay = 40 * r

    
if h > 40:
    bonus = (h - 40) * ot 
    
    
    
print (pay + bonus)


