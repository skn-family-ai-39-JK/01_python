# [튜터의 따뜻한 응원 한마디 🌱]
# 처음이어도 괜찮아요! 차근차근 코드를 채워 멋진 결과물을 확인해 봐요.
# 1) 문장과 찾을 낱말을 차례로 읽어요.
sentence = input()
keyword = input()
# TODO: 단어 수와 낱말의 위치, 포함 여부를 구해 보세요.
# sen_word = sentence.count(keyword)
# last_word = len(sentence) -1
word = sentence.split()
first_word = sentence.find(keyword)
last_word = sentence.rfind(keyword)
check = "예" if keyword in sentence else "아니오"

# print(sen_word)
# print(last_word)
# print(len(word))
# print(first_word)
# print(last_word)
# print(check)
# result = "단어 수: " + str(len(word)) + "\n첫 위치" + str(first_word) + "\n마지막 위치: " + str(last_word) + "\n포함 여부: " + check
result = f"단어 수: {len(word)}\n첫 위치: {first_word}\n마지막 위치: {last_word}\n포함 여부: {check}"

# 2) 완성한 결과를 출력해요.
print(result)
# print(result2)
