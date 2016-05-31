
class TinyURL:

    def __init__(self):
        self.long_to_short = dict()
        self.short_to_long = dict()
        self._encode_table = self._generate_encode_table()

    def generate(self, long_url):
        """ Generate tiny url """
        if long_url in self.long_to_short:
            return self.long_to_short[long_url]
        short_url = self._generate()
        self.long_to_short[long_url] = short_url
        self.short_to_long[short_url] = long_url
        return short_url

    def lookup(self, tiny_url):
        """ Return original long url """
        return (self.short_to_long[tiny_url]
                if tiny_url in self.short_to_long else None)

    def _generate(self):
        return self._encode(len(self.long_to_short))

    def _generate_encode_table(self):
        encode_table = [None] * 62
        for i in range(10):
            encode_table[i] = chr(ord('0') + i)
        for i in range(10, 36):
            encode_table[i] = chr(ord('a') + i - 10)
        for i in range(36, 62):
            encode_table[i] = chr(ord('A') + i - 36)
        return encode_table

    def _encode(self, decimal):
        """ [0-9] -> [0-9a-zA-Z] """
        code = ''
        while decimal > 0:
            code += self._encode_table[decimal%62]
            decimal //= 62
        return code[::-1] if code else '0'  #!
