# [튜터의 따뜻한 응원 한마디 🌱]
# 처음이어도 괜찮아요! 차근차근 코드를 채워 멋진 결과물을 확인해 봐요.
# 1) 첫째 줄에서 기본 요금을 정수로 읽어 보세요.
base_fee = int(input())
# 2) 둘째 줄에서 이동 거리를 정수로 읽어 보세요.
distance = int(input())
# 3) 셋째 줄에서 거리당 요금을 실수로 읽어 보세요.
rate = float(input())
# 4) 넷째 줄에서 할인액을 정수로 읽어 보세요.
discount = int(input())
# 5) 요금을 계산한 결과를 담아 보세요.
# TODO: 입력한 값으로 최종 요금을 계산하세요.
result = "최종 요금: " + str((base_fee + distance*rate) - discount)
# 6) 정해진 형식으로 결과를 출력해 보세요.
print(result)
