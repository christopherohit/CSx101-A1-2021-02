def checkYear(year): 
  
    # Return true if year is a multiple 
    # of 4 and not multiple of 100. 
    # OR year is multiple of 400. 
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)); 
  
 
i , year = [int(x) for x in input().split()]
if(checkYear(year)): 
    pass
else: 
    print("Not a Leap Year")