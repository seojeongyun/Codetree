word1 = input()
word2 = input()

# Please write your code here.
answer = 'Yes' if sorted(word1) == sorted(word2) else 'No'
print(answer)