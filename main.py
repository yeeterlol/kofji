import re
def kofji(u):
    v = set("aeiou")
    body = re.sub(r'\d+$', '', u.lower())
    if len(body) < 7:
        return False
    flips = sum((a in v) != (b in v) for a, b in zip(body, body[1:]))
    return flips / (len(body) - 1) >= 0.9 and u[-1].isdigit() 
