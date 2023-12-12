# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

class MyError(Exception): # 예외를 만들기 위해서 클래스를 만들어줍니다.
    pass

def solution(my_string, target):
    
    # 제한사항 만들기
    if not (1 <= len(my_string) <= 100): # my_string의 길이가 1이상 100이하가 아니라면 MyError 발생
        raise MyError("my_string의 글자 수 범위가 초과됐습니다.")
    if not (1 <= len(target) <= 100): # target의 길이가 1이상 100이하가 아니라면 MyError 발생
        raise MyError("target의 글자 수 범위가 초과됐습니다.")
    if not my_string.islower(): # my_string이 소문자가 아니라면 MyError 발생
        raise MyError("my_string를 소문자로 바꿔주세요.")
    if not target.islower(): # target이 소문자가 아니라면 MyError 발생
        raise MyError("target를 소문자로 바꿔주세요.")

    answer = 0

    if target in my_string: #if문을 활용하여 my_string 문자열 안에 target 문자열이 존재하면 answer의 값이 1로 바뀌게 함
        answer = 1

    return answer #문자열이 포함되어있다면 answer = 1를 반환할 것이고 그렇지 않으면 answer = 0이 반환된다.

while True:    
    try:   
        my_string = input("my_string을 입력하세요 : ")
        target = input("target을 입력하세요    : ")
        result = solution(my_string, target)
        if result == 1:
            print("문자가 포함되어있습니다.")
        else:
            print("문자가 포함되어 있지 않습니다.")
        break
    except MyError as e: # try문에서 에러나면 except문에서 정해놓은 에러메세지 출력
        print(e)
    
