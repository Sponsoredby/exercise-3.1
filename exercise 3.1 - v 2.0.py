hrs = input("Enter Hours: ")                        # user enter working hours
h = float(hrs)                                      # converts string to float
rate = input ("Enter rate: ")                       # user enters hourly rate
r = float(rate)                                     #converts string to float
br = 1.5 * r                                        # sets the bonus rate
bh = h - 40                                         #calculates the bonus hours
pay = (h - bh) * r

if  h > 40:                                         
    bp = br * bh                                    # calculates the bonus pay
    pay = pay + bp                                  #calculates the total pay including bonus
    

else:
    pay = h * r #normal pay without bonus

print (pay)                                         #prints the pay based on hours world

