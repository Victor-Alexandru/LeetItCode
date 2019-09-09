import urllib.parse as parseaza

class Codec:

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        path = parseaza.urlparse(longUrl).path
        hostname =parseaza.urlparse(longUrl).hostname
        tiny_url = 'http://tinyurl.com/'
        print(path)
        path = path[1:]
        for character in path:
               if character == '/':
                      tiny_url+='PPP'
               else:
                      if character.islower():
                             tiny_url+=character.upper()
                      else:
                             tiny_url+=character

        pass
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        pass
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))