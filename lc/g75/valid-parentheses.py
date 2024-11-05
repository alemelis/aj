PARENTHESES = {o:c for o,c in zip("([{", ")]}")}

def isValid(self, s: str) -> bool:
    stack = []
    for p in s:  # O(n)
        if p in PARENTHESES.keys(): # O(1)
            stack.append(p) # O(1)
        else:
            # s = "]"
            if not stack or p != PARENTHESES[stack.pop()]: # O(1)
                return False
    # s = "[[["
    return len(stack) == 0
