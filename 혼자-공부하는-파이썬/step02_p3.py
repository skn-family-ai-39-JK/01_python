# [튜터의 따뜻한 응원 한마디 🌱]
# 처음이어도 괜찮아요! 차근차근 코드를 채워 멋진 결과물을 확인해 봐요.
# 1) 첫째 줄에서 상품 이름을 읽어 보세요.
product = input()
# 2) 둘째 줄에서 한 개 가격을 정수로 읽어 보세요.
price = int(input())
# 3) 셋째 줄에서 수량을 정수로 읽어 보세요.
quantity = int(input())
# 4) 넷째 줄에서 낸 금액을 정수로 읽어 보세요.
paid = int(input())
# 5) 상품 금액과 표시 내용을 포함한 결과를 만들어 보세요.
# TODO: 입력한 정보를 이용해 구매 내역을 완성하세요.
result = "상품: " + product + "\n수량 표시: " + ("★"*quantity) + "\n상품 금액: " + str(price*quantity) + "\n차액(낸 금액-상품 금액): " + str(paid-price*quantity)
# 6) 완성한 구매 내역을 출력해 보세요.
print(result)
