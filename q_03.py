"""
Q 03. 円周率
"""

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
res = [len(w) for w in sentence.replace(",", "").replace(".","").split()]
print(res)
