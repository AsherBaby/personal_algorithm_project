
class TinyURL:

    def __init__(self):
        self.long_to_short = dict()
        self.short_to_long = dict()

    def generate(self, long_url):
        """ Generate tiny url """
        if long_url in self.long_to_short:
            return self.long_to_short[long_url]
        n = self._generate()
        self.long_to_short[long_url] = n
        self.short_to_long[n] = long_url
        return n

    def lookup(self, tiny_url):
        """ Return original long url """
        return (self.short_to_long[tiny_url]
                if tiny_url in self.short_to_long else None)

    def _generate(self):
        return self._encode(len(self.long_to_short))

    def _encode(self, decimal):
        """ [0-9] -> [0-9a-zA-Z] """
        return decimal  # TODO
