# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

# letter = ".-.. .. ..-. . / .. ... / . --. --."

class MyError(Exception): # 예외를 만들기 위해서 클래스를 만들어줍니다.
   pass

def solution(letter):

    # 제한사항 만들기
    if not (1 <= len(letter) <= 1000): # letter의 길이가 1이상 1000이하가 아니라면 MyError 발생
        raise MyError("letter의 글자 수 범위가 초과됐습니다.")
    if '  ' in letter: # letter 문자열에 공백이 연속으로 2개 존재하면 MyError 발생
        raise MyError("letter 문자열안에 두 개 이상 공백이 존재합니다.")

    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}

    answer = '' # answer 변수를 빈 문자열로 초기화
    for i in letter.split(' '): # for문을 사용하여 매개변수를 공백을 기준으로 나누어 순서대로 변수 i에 대입한다.
        if i in morse: # 만약 i라는 단어가 morse에 포함되어있으면 answer의 해당 문자를 추가한다.
            answer += morse[i]
        else: # 그렇지 않으면 공백을 추가한다. 
            answer += ' '
    return answer
try:
    letter = ".-.. .. ..-. . / .. ... / . --. --." # 문장을 표현할 때 공백은 '/'로 표현
    result = solution(letter)
    print(result)
except MyError as e: # try문에서 에러나면 except문에서 정해놓은 에러메세지 출력
    print(e)                 
