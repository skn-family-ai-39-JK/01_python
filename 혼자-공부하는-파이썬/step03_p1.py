# [튜터의 따뜻한 응원 한마디 🌱]
# 처음이어도 괜찮아요! 차근차근 코드를 채워 멋진 결과물을 확인해 봐요.
# 1) 입력된 이름을 읽어 보관해요.
name = input()
# 2) 수량과 가격도 각각 읽어 보관해요.
quantity_text = int(input())
price_text = int(input())
# TODO: 입력값을 숫자로 바꾸고 주문 정보를 정리해 보세요.
result = "이름: " + name + "\n수량: " + str(quantity_text) + "개\n금액: " + str(f'{quantity_text*price_text:,}') + "원"
# 3) 완성한 결과를 출력해요.
print(result)
