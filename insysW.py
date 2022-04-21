# NUMBER TO WORDS IN PYTHON (INDIAN SYSTEM) 
def Words(n): 
     units = ["Zero ", " One ", " Two ", " Three ", " Four ", " Five ", " Six ", " Seven ", " Eight ", " Nine "] 
     teens = [" Ten "," Eleven "," Twelve "," Thirteen "," Fourteen "," Fifteen "," Sixteen "," Seventeen "," Eighteen "," Nineteen "] 
     tens = [" Twenty "," Thirty ", " Fourty ", " Fifty ", " Sixty ", " Seventy ", " Eighty ", " Ninety "] 
     if n <=9: 
         return units[n] 
     elif n >= 10 and n <= 19: 
         return teens[n-10] 
     elif n >= 20 and n <= 99: 
         return tens[(n//10)-2] + " " + (units[n % 10] if n % 10 !=0 else "") 
     elif n >= 100 and n <= 999: 
         return Words(n//100) + " Hundred " + (Words(n % 100) if n % 100 !=0 else "") 
     elif n >= 1000 and n <= 99999: 
         return Words(n//1000) + " Thousand " + (Words(n % 1000) if n % 1000 !=0 else "") 
     elif n >= 100000 and n <= 9999999: 
         return Words(n//100000) + " Lac " + (Words(n % 100000) if n % 100000 !=0 else "") 
     elif n >= 10000000 and n <= 999999999:
         return Words(n//10000000) + " Crore " + (Words(n % 10000000) if n % 10000000 !=0 else "") 
     elif n >= 1000000000: 
         return Words(n//1000000000) + " Arab  " + (Words(n % 1000000000) if n % 1000000000 !=0 else "")
