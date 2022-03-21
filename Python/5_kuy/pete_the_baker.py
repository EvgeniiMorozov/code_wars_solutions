def cakes(recipe: dict, available: dict) -> int:
    amount = []
    for key, value in recipe.items():
        if key in available:
            amount.append(available[key] // value)
        else:
            return 0

    return min(amount)


if __name__ == "__main__":
    print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))

"""
def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)


def cakes(recipe, available):
    try:
        return min([available[a]/recipe[a] for a in recipe])
    except:
        return 0
"""
