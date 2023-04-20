#write a script to  enter any sentence and print those word which is palindrome also print total number of palindrome word.

sentence = input("Enter a sentence:")
words = sentence.split()

palindromes= []
for word in words:
    if word == word[::-1]:
        palindromes.append(word)

print("palindromic word in a sentence:",palindromes)
print("Total number of palindromic words:",len(palindromes))

