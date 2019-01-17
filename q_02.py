"""
Q 03. 「パトカー」＋「タクシー」＝「パタトクカシーー」
"""

w0 = "パトカー"
w1 = "タクシー"
len_w = len(w0)
res = ""
for i in range(len_w):
    res+=w0[i]+w1[i]

print(res)
