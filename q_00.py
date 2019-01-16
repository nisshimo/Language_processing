"""
Q 00. 文字列の逆順
"""

#word = input()
word = "stressed"
  
def reverse(word):
    result = ""
    for i in range(len(word)):
        result += word[-1-i]
    return result

result = reverse(word)
print("word:", word)
print("result:", result)
