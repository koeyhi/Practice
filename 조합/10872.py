N = int(input())
result = 1
for i in range(1, N+1): result *= i
print(result)
    
# import math
# math.factorial(int(input())) # math 라이브러리 factorial 함수 사용

# def f(n): return 1 if n < 2 else f(n-1)*n # 재귀함수 사용
# print(f(int(input())))