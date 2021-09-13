bin(19) # will return '0b10011'

#or you can do

def binary(num):
    array = []

    #makes the binary value
    while(num > 0):
        sol1 = num / 2

        check = sol1 - int(sol1)

        if(check > 0):
            array.append("1")
            num = sol1 - 0.5
        else:
            array.append("0")
            num = sol1
            
    #makes sure the binary value is a minimum of 4 bits long
    while(len(array) < 4):
        array.append("0")

    #reverses the array
    array = array[::-1]

    #joins the array into a string, return the string
    string = ''.join(array)

    return string
  
#binary(19) will return 10011