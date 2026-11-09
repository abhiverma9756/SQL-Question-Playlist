class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:

        freq = {}

        # Step 1: Count frequency
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Step 2: Group by frequency
        groups = {}

        for ch, count in freq.items():
            if count not in groups:
                groups[count] = []

            groups[count].append(ch)

        # Step 3: Find majority frequency group
        ans = ""
        max_size = 0
        max_freq = 0

        for f, chars in groups.items():

            if len(chars) > max_size or (len(chars) == max_size and f > max_freq):

                max_size = len(chars)
                max_freq = f
                ans = "".join(chars)

        return ans
