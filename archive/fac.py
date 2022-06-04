def factorial(n):
    result = 1
    for i in range(n):#при n = 5: 0,1,2,3,4
        result *= i + 1
    return result

if __name__ == "__main__":
    print(factorial(5))

#5! = 1 * 2 * 3 * 4 * 5