# https://www.codewars.com/kata/58f5c63f1e26ecda7e000029

def wave(people: str) -> list[str]:
    if not people:
        return []
    return [people[:i] + people[i].upper() + people[i+1:] for i in range(len(people)) if people[i].isalpha()]
