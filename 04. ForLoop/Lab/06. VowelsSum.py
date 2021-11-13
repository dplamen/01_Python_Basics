score_table = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
text = input()
total = 0
for ch in text:
    if ch in score_table:
        total += score_table[ch]
print(total)