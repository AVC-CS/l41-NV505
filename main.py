def main():

    N = int(input('Enter the number N: '))
    result = []
    start = 0
    num = 1
    
    while (start <= N):
        start += 1
        num = num*2
        result.append(num)
        
    
    print(result)
        
        
    
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
