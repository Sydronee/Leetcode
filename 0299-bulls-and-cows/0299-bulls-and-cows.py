class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_counts = Counter()
        guess_counts = Counter()

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_counts[secret[i]] += 1
                guess_counts[guess[i]] += 1

        for char in guess_counts:
            cows += min(guess_counts[char], secret_counts[char])

        return f"{bulls}A{cows}B"
