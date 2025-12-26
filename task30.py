texts = ['kiyik', 'kok', 'samo']
palindromlar = []
for text in texts :
    if text == text[::-1]:
        palindromlar.append(text)
print(palindromlar)


    