def main():

    N = int(input('Enter the number N: '))
    result = []
    start = 0
    
    while (start <= N):
        result.append(2 ** start)
        start += 1
        
    
    print(result)
        
        
    
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
