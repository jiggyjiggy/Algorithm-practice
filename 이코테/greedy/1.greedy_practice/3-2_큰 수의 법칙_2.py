
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]
# input & setting 동일

# 가장 큰 수가 더해지는 횟수 계산
count = int( m / ( k + 1 )) * k 
count += m % ( k + 1 )  

result = 0 
result += ( count ) * first # 가장 큰 수 더하기
result += ( m - count ) * second    # 두 번째로 큰 수 더하기

print(result)


# 문제 풀이의 로직에서 반복되는 수열에 대해서 파악하면 더 효율적 계산
