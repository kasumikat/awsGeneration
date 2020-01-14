year = 1
investment = 100 #investment starts off with £100
intrest = 0.1 #intrest rate of 10% 

while investment <= 1000: #when value is at £1000
    print(year)
    year += 1 #each year 
    investment  = (investment * (1 + intrest)) # the total investment
