"""Day 1 · 문제 2 (쉬움) — 이름과 나이로 인사말 만들기"""


def make_greeting(name, age):
    """이름(str)과 현재 나이(int)를 받아 인사말 문자열을 반환한다.

    형식: "안녕하세요, <name>님! 내년에는 <age+1>살이 되시네요."

    >>> make_greeting("민수", 25)
    '안녕하세요, 민수님! 내년에는 26살이 되시네요.'
    """
    # TODO: 문자열 이어붙이기(+)와 str()을 사용하세요. (f-string을 써도 됩니다)
    return '안녕하세요, '+ name +'님! 내년에는 '+ str(age + 1) + '살이 되시네요.'


if __name__ == "__main__":
    print(make_greeting("민수", 25))
