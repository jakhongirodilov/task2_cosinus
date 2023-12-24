import random

words = ["tiger", "tree", "underground", "giraffe", "chair"]
word = random.choice(words)
selected_word = list(word)
length = len(selected_word)

wrong_attempts = 5

result = ['_' for i in range(length)]

print(selected_word)
while wrong_attempts > 0 and '_' in result:
    guess = input("Biror harf kiriting: ")

    if guess.isalpha() and len(guess)==1:

        if guess in selected_word:
            order = selected_word.index(guess)
            selected_word[order] = '_'
            result[order] = guess

            print(''.join(result))
        else:
            wrong_attempts -= 1
            print(f"Topolmadingiz, urinishlaringiz soni: {wrong_attempts}")
        
    else:
        print("Noto'g'ri input kiritdingiz! ")

result = ''.join(result)
if wrong_attempts > 0:
    print(f"\nTabriklayman, siz yutdingiz! Natija: {''.join(result)}")
else:
    print(f"\nAfsuski topolmadingiz!")
    print(f"Sizning javob: {result}. To'g'ri javob: {word}")