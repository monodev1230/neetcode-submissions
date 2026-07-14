class Solution:

    # Encodes the array of strings into a single string
    def encode(self, s):
        encoded = ""

        for str_val in s:
            encoded += str(len(str_val))  # store length
            encoded += '#'                # fixed separator
            encoded += str_val            # actual string

        return encoded

    # Decodes the encoded string back into the array of strings
    def decode(self, s):
        result = []
        i = 0
        n = len(s)

        while i < n:
            length = 0

            # Extract the length
            while s[i] != '#':
                length = length * 10 + (ord(s[i]) - ord('0'))
                i += 1

            i += 1  # skip '#'

            # Extract the actual string using the length
            temp = s[i:i + length]
            result.append(temp)

            i += length

        return result

