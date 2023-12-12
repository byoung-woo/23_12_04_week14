# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

class MyError(Exception): # 예외를 만들기 위해서 클래스를 만들어줍니다.
    pass

def solution(age):
    
    # 제한사항 만들기
    if (age > 1000): # age의 길이가 1000이하가 아니라면 MyError 발생
        raise MyError("age의 글자 수 범위가 초과됐습니다.")
    if not isinstance(age, int) or age <= 0: # isinstance는 변수가 특정 인스턴스인지 확인하는데 쓰인다. 정수가 아닐 때 에러를 만들고 싶으니까 not instance(age, int)를 하면된다. age <= 0 은 age 마이너스일 때 에러발생
        raise MyError("age가 자연수가 아닙니다.") 
                       
    answer = ''
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] # 각 인덱스에 위치에 알파벳을 부여한다.
    while age > 0: # age가 0 이하면 반복문 종료
        answer = alpha[age % 10] + answer # age를 10으로 나눈 나머지는 alpha 리스트 인덱스 위치를 의미한다.
        age = age // 10 # age를 10으로 나눠서 나온 몫으로 업데이트를 한다.(십의자리이상의 숫자를 추출하기 위해서)

    return answer # answer을 반환한다.
    
while True:    
    try:
        user_input = input("나이(숫자)를 입력하시오 : ") # 숫자를 입력받는다.
        if not user_input.isdigit():
            raise MyError("입력한게 숫자(정수)가 아닙니다.")

        age = (int)(user_input) # 정수를 solution 함수에 집어넣기 위해서 (int)형태로 변환시켜준다.
        result= solution(age)
        print("PROGEAMMER-857식 나이는 " + result)
        break 
    except MyError as e:
        print(e)
