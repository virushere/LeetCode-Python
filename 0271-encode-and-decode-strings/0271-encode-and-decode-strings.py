class Codec:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for item in strs:
            res = res+str(len(item))+"#"+item
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ""
            while  i < len(s) and s[i].isdigit():
                length += s[i]
                i += 1
            
            length = int(length)
            if s[i] == "#":
                i += 1
            
            res.append(s[i:i+length])
            i += length 
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))