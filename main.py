#English to Pig Latin

print('Enter the English message to translate into Pig Latin:')
message=input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] #A list of words in pig Latin
for word in message.split():

  prefixNonLetters=""
  while len(word) >0 and not word [0].isalpha():
    prefixNonLetters +=word[0]
    word = word[1:]
