num2roman = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
              50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
num = int(input("Enter a number: "))

#Values in descending order
des_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

for x in des_values:
    if num != 0:
        quotient= num//x

        #If quotient is not zero output the roman equivalent
        if quotient != 0:
            for y in range(quotient):
                print(num2roman[x], end="")

        #update integer with remainder
        num = num%x

