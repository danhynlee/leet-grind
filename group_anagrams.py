# Given an array of strings strs, group the anagrams together. 
# An anagram is a word formed by rearranging the letters of another word.

"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation: Words with the same characters (sorted) belong to the same group.
"""

"""
eat -> aet
tea -> aet
ate -> aet

tan -> ant
nat -> ant

bat -> abt

right side will be sorted keys in the hashmap

"""
from collections import defaultdict
def group_anagrams(strs: list[str]) -> list[list[str]]:
  anagrams = defaultdict(list)

  for word in strs:
    sorted_word = ''.join(sorted(word))
    anagrams[sorted_word].append(word)

  return list(anagrams.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
print(group_anagrams(["anti", "tian", "tin", "an", "tina", "nah", "aha", "aint", "it", "int"]))

# O(n * k log k) where n is the number of words and k is the maximum length of a word. Sorting each word takes O(k log k).
# O(n * k) where n is the number of words and k is the maximum length of a word. Inserting each word into the hashmap takes O(k) time.



def group_anagrams_by_char_count(strs: list[str]) -> list[list[str]]:
  anagrams = defaultdict(list)

  for word in strs:
    char_count = [0] * 26
    for char in word:
      char_count[ord(char) - ord('a')] += 1
    anagrams[tuple(char_count)].append(word)

  return list(anagrams.values())

print(group_anagrams_by_char_count(["eat","tea","tan","ate","nat","bat"]))
print(group_anagrams_by_char_count(["anti", "tian", "tin", "an", "tina", "nah", "aha", "aint", "it", "int"]))