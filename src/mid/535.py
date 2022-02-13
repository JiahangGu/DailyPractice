# 主要是搞几个加密的方式，能解密就行

# 1. 使用简单计数，从1开始
# 2. 使用字符哈希，比如一共可能有[0-9a-zA-Z]62个字符，使用62进制做字符串哈希
# 3. 使用随机值，映射结果在map中存储用于解密

class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))