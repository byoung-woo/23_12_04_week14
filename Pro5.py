# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def compare(x) : # sorted 함수를 사용하기 위해 입력받은 숫자를 문자열로 바꿔주고 길이를 4로 맞추는 함수를 만든다.[:4]
    four_string = (str(x) * 4) [:4]
    return four_string

def solution(numbers):

    # 각 함수의 설명은 보고서에 자세하게 있습니다.
    answer = ''
   
    # numbers안에 있는 숫자를 문자열로 바꿔줍니다.
    string_numbers = []
    for i in numbers:
        string_numbers.append(str(i))
 
    numbers = sorted(string_numbers, key = compare, reverse=True) # sorted함수를 사용하여 numbers의 문자열의 길이를 4로 기준으로 내림차순 정렬합니다.
    if numbers[0] == '0': # 만약 numbers가 모두 0이라면 answer의 값은 0으로 지정해줍니다.
        answer = '0'
    else: # 그렇지 않다면 join을 이용하여 answer의 값을 완성해줍니다.
        answer = ''.join(numbers)
    return answer

numbers = [8, 30, 17, 2, 23]
result = solution(numbers)
print(result)

is_string = isinstance(result, str) # 문제 조건대로 문자열이 맞는지 확인하는 함수. 문자열이면 True를 반환
print("문자열이 맞나요?", is_string)
