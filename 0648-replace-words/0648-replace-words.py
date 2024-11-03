class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=len)
        sentence_list = sentence.split()
        for i, word in enumerate(sentence_list):
            for match in dictionary:
                if word.startswith(match):
                    sentence_list[i] = match
                    break
        return " ".join(sentence_list)
                    