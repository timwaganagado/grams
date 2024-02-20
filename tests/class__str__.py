class stupid:
    def __init__(self,text):
        self.text = text
    def __str__(self) -> str:
        return f"{self.text}"

a = stupid("now")

print(f"i want burger {a}")