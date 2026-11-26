# [튜터의 따뜻한 응원 한마디 🌱]
# 처음이어도 괜찮아요! 차근차근 코드를 채워 멋진 결과물을 확인해 봐요.
# 1) 책 이름과 두 개의 숫자를 차례로 읽어 보세요.
book_name = input()
days = int(input())
pages_per_day = int(input())
# 2) 계획한 전체 쪽수를 구할 자리를 채워 보세요.
# TODO: 읽을 날짜 수와 하루 쪽수로 전체 쪽수를 계산하세요.
result = days * pages_per_day
# 3) 책 이름과 계산 결과를 정해진 형식으로 출력해 보세요.
print("책:", book_name)
print("총 쪽수:", result)
