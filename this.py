import random

quotes = [
    "Stay hungry, stay foolish.",
    "Simplicity is the ultimate sophistication.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "In the middle of difficulty lies opportunity.",
    "First, solve the problem. Then, write the code."
]

def random_quote():
    quote = random.choice(quotes)
    print(f"💬 Quote of the moment: \"{quote}\"")

if __name__ == "__main__":
    random_quote()

