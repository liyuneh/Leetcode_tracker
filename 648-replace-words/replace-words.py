class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split()
        for i in range(len(sentence)):
            for root in dictionary:
                if sentence[i].startswith(root):
                    sentence[i] = root
        return " ".join(sentence)
                 