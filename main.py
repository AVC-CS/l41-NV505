def main():

    N = int(input('Enter the number N: '))
    result = [] #list
    start = 0 #counting/exponent variable
    
    while (start <= N): #while loop to create list
        result.append(2 ** start) 
        start += 1
         
    print(result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
