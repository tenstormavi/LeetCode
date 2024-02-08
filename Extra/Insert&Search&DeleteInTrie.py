"""
Complete the Insert and Search functions for a Trie Data Structure.
    Insert: Accepts the Trie's root and a string, modifies the root in-place, and returns nothing.
    Search: Takes the Trie's root and a string, returns true if the string is in the Trie, otherwise false.

"""

"""
class TrieNode: 

    def __init__(self): 
        self.children = [None]*26

        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
"""


# Insertion - TC -> O(no_of_words * max_word_length)
# Search - TC -> O(no_of_words * max_word_length)
# Delete - TC -> O(no_of_words * max_word_length)
class Solution:
    # Function to insert string into TRIE.
    def insert(self, root, key):

        # code here
        if not root:
            return

        cur = root
        for chr in key:
            if not cur.children[ord(chr) - ord('a')]:
                cur.children[ord(chr) - ord('a')] = TrieNode()
            cur = cur.children[ord(chr) - ord('a')]
        cur.isEndOfWord = True

    # Function to use TRIE data structure and search the given string.
    def search(self, root, key):

        # code here
        if not root:
            return False

        cur = root
        for chr in key:
            if not cur.children[ord(chr) - ord('a')]:
                return False
            cur = cur.children[ord(chr) - ord('a')]
        return cur.isEndOfWord

    # Function to use TRIE data structure and delete the given string.
    def deleteKey(self, root, key):
        # your code goes here
        cur = root
        for chr in key:
            if not cur.children[ord(chr) - ord('a')]:
                return False
            cur = cur.children[ord(chr) - ord('a')]
            if cur.isEndOfWord:
                cur.isEndOfWord = False
                return True
        return False