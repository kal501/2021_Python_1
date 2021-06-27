# 기본 매개변수 중에서 필요한 값만 입력하기

def test(a, b=10, c=100):
    print(a+b+c)
# a는 일반매개변수
# b와 c는 기본매개변수

# 기본형태
test(10, 20, 30)

# 키워드 매개변수로 모든 매개변수를 지정한 형태
test(a=10, b=100, c=200)

# 키워드 매개변수로 모든 매개변수를 마구잡이로 지정한 형태
test(c=10, a=100, b= 200)

# 키워드 매개변수로 일부 매개변수만 지정한 형태
test(10, c=200)