def factorial(n):
    if (n==1) or (n==2):
        return 1
    else:
        return factorial(n-1) + factorial(n-2)

number = int(input('请输入一个正整数：'))
result = factorial(number)
print(result)
  
