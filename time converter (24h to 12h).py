def time_converter(time):
   time = time.split(":")
   
   if int(time[0]) == 00:
       return "12:00 a.m."
   elif int(time[0]) < 12:
       if int(time[0]) < 10:
           time = ':'.join(time)
           return time[1:] + " a.m."
       else:
           time = ':'.join(time)
           return time + " a.m." 
   elif int(time[0]) == 12:
       time = ':'.join(time)
       return time + " p.m."
   else:
       time[0] = int(time[0]) - 12
       time[0] = str(time[0])
       time = ':'.join(time)
       return time + " p.m."       
        
 

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
