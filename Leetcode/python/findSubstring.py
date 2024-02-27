# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
# Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        words_len = word_len * len(words)
        words_dict = {}
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1
        res = []
        for i in range(word_len):
            left = i
            right = i
            temp_dict = {}
            while right + word_len <= len(s):
                word = s[right:right+word_len]
                right += word_len
                if word in words_dict:
                    temp_dict[word] = temp_dict.get(word, 0) + 1
                    while temp_dict[word] > words_dict[word]:
                        temp_dict[s[left:left+word_len]] -= 1
                        left += word_len
                    if right - left == words_len:
                        res.append(left)
                else:
                    temp_dict.clear()
                    left = right
        return res

print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"])) # [0, 9]
print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"])) # []
print(Solution().findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])) # [6, 9, 12]