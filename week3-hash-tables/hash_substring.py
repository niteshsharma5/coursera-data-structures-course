class TextSearch:
    """Rabin–Karp’s algorithm for searching the given pattern in the given text.
    Sample1:
    >>> ts = TextSearch("aba", "abacaba")
    >>> ts.find()
    [0, 4]
    >>> # Explanation:
    >>> # The pattern aba can be found in positions 0 (abacaba) and 4 (abacaba)
    >>> # of the text abacaba.
    >>>
    Sample 2:
    >>> ts = TextSearch("Test", "testTesttesT")
    >>> ts.find()
    [4]
    >>> # Explanation:
    >>> # Pattern and text are case-sensitive in this problem. Pattern “Test“
    >>> # can only be found in position 4 in the text “testTesttesT“.
    >>>
    Sample 3:
    >>> ts = TextSearch("aaaaa", "baaaaaaa")
    >>> ts.find()
    [1, 2, 3]
    >>> # Explanation:
    >>> # Note that the occurrences of the pattern in the text
    >>> # can be overlapping, and that’s fine, you still need to
    >>> # output all of them.
    """
    def __init__(self, pattern, text):
        self._pattern = pattern
        self._text = text
        self._window = len(pattern)
        self._scan_bound = len(text) - len(pattern) + 1
        self._checksums = []

    def checksum(self, string):
        """utility function that returns hash of the string."""
        return sum([ord(string[i]) for i in range(len(string))])

    def precompute_hashes(self):
        """Precomputes hash values for the whole possible pattern entries
        in the text.
        """
        self._checksums = [self.checksum(self._text[:self._window])]

        for i in range(1, self._scan_bound):
            old_hash = self._checksums[i - 1]
            left_l_hash = ord(self._text[i - 1])
            right_l_hash = ord(self._text[i + self._window - 1])

            ith_hash = old_hash - left_l_hash + right_l_hash
            self._checksums.append(ith_hash)

    def find(self):
        """Returns all occurrences of pattern in the text."""
        pattern_checksum = self.checksum(self._pattern)
        self.precompute_hashes()
        results = []
        for i in range(self._scan_bound):
            if pattern_checksum == self._checksums[i]:
                if self._pattern == self._text[i:i + self._window]:#pattern found
                    results.append(i)#append it
        return results

if __name__ == "__main__":
    pattern, text = input().rstrip(), input().rstrip()

    ts = TextSearch(pattern, text)
    answer = ts.find()

    print(" ".join(map(str, answer)))
