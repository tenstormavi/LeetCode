"""
Given the standard mapping from English letters to digits on a phone keypad
(1 → "" 2 -> a,b,c 3 -> d,e,f 4 -> g,h,i 5 -> j,k,l 6 -> m,n,o 7 -> p,q,r,s 8 -> t,u,v 9 -> w,x,y,z)

write a program that outputs all words that can be formed from any n-digit phone number from the list of
given KNOWN_WORDS considering the mapping mentioned above.

KNOWN_WORDS= ['careers', 'linkedin', 'hiring', 'interview', 'linkedgo']

phoneNumber: 2273377
Output: ['careers']

phoneNumber: 54653346
Output: ['linkedin', 'linkedgo']
"""


def letterCombinations(phoneNumber, KNOWN_WORDS):
    digitToChar = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        "0": ""
    }

    # Helper function to check if a word can be formed using the digits in the phone number
    def canFormWord(word, phoneNumber):
        for i, digit in enumerate(phoneNumber):
            if i >= len(word):
                return False
            if word[i] not in digitToChar[digit]:
                return False
        return True

    # Check each known word if it can be formed using the digits in the phone number
    output = [word for word in KNOWN_WORDS if canFormWord(word, phoneNumber)]

    return output


KNOWN_WORDS = ['careers', 'linkedin', 'hiring', 'interview', 'linkedgo']
phoneNumber1 = "2273377"
phoneNumber2 = "54653346"

print("Output for phoneNumber1:", letterCombinations(phoneNumber1, KNOWN_WORDS))
print("Output for phoneNumber2:", letterCombinations(phoneNumber2, KNOWN_WORDS))