texts = ["kitob", "dastur", "AI", "hello", "python"]
max_word = texts[0]

for word in texts:
    if len(word) > len(max_word):
        max_word = word

print("Natija:", max_word)
