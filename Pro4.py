# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

import math # 모듈 math를 사용하기 위해 import를 사용한다.

def solution(r1, r2):
    answer = 0
    count1 = 0 # 큰 원 정수 좌표 개수 카운트
    count2 = 0 # 작은 원 정수 좌표 개수 카운트

    # 큰 원의 정수 좌표 개수 구하기
    for x in range(1, r2): # x좌표 x=1 부터 x = r2 이하까지 순회한다.
        r2Y = math.sqrt(r2*r2-x*x) # 각 x좌표일 때 y값을 구한다.
        maxY = math.ceil(r2Y) # ceil(올림)통해서 max의 정수 좌표를 구한다. 
        if int (r2Y) == r2Y: # r2Y가 정수인지를 파악 math.sqrt를 사용하면 실수를 반환하기 때문에 isinstance함수를 쓰면 항상 false가 나온다.
            count1 += maxY + 1 # 정수가 맞다면 원위에 점도 포함해야하기 때문에 +1를 한다
        else:
            count1 += maxY # 그게 아니라면 그냥 더한다.
    count1 += 1 # x = r2일때는 항상 점의 개수는 하나밖에 없음으로 1를 더한다.                     
    
    # 작은 원의 정수 좌표 개수 구하기 앞서 했던거 반복
    for x in range(1, r1):                 
        r1Y = math.sqrt(r1*r1-x*x)
        minY = math.ceil(r1Y)
        
        if int (r1Y) == r1Y:
            count2 += minY + 1
        else:
            count2 += minY
    count2 += 1
    
    answer = (count1 - count2 + 1 ) # (큰 원 정수 좌표 - 작은 원 정수 좌표)해서 두 원사이의 정수 좌표개수를 구한다. x = r1일때 중복으로 제거 되므로 +1를 한다.

    return answer *4 # 1사분면만 좌표개수를 구했으므로 전체 개수는 곱하기 4하면 된다.
    

r1 = 2
r2 = 3
res = solution(r1,r2)
print("r1 = ", r1, " / r2 = ", r2, "일때 두 원 사이의 정수좌표 개수는 ", res)
