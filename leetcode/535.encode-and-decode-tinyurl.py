# @leet start
from string import ascii_letters, digits

# 62 chars
CHARS = ascii_letters + digits


class Codec:
    def __init__(self):
        self.next_int: int = 0
        self.long_to_short: dict[str, str] = {}
        self.short_to_long: dict[str, str] = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl in self.long_to_short:
            return self.long_to_short[longUrl]

        n = self.next_int
        self.next_int += 1

        # Get encoding
        encoding_chars: list[str] = [] if n > 0 else [CHARS[0]]

        while n > 0:
            n, r = divmod(n, 62)
            encoding_chars.append(CHARS[r])

        encoding = "".join(encoding_chars)

        # Store and return result
        self.long_to_short[longUrl] = encoding
        self.short_to_long[encoding] = longUrl

        return encoding

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.short_to_long[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @leet end
