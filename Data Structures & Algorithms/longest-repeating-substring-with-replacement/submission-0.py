class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        freq = {}
        max_rep_char_cnt = 0
        left = 0

        for right in range(len(s)):
            right_char = s[right]
            freq[right_char] = freq.get(right_char, 0) + 1
            max_rep_char_cnt = max(max_rep_char_cnt, freq[right_char])

            while right-left+1 - max_rep_char_cnt > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len