class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sentence = sentence.split()
        for i in range(len(sentence)):
            if sentence[i].startswith("$") and sentence[i][1:].replace(",", "", 1).isdigit():
                price = float(sentence[i][1:])
                discounted = price * (1 - discount / 100)
                sentence[i] = f"${discounted:.2f}"
        return " ".join(sentence) 