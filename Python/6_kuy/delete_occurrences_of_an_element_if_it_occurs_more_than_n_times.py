def delete_nth(order: list, max_e: int) -> list:
    stack = []
    for i in order:
        if stack.count(i) < max_e:
            stack.append(i)
    return stack


if __name__ == "__main__":
    print(delete_nth([20, 37, 20, 21], 1))

'''
def delete_nth(order,max_e):
    return [o for i,o in enumerate(order) if order[:i].count(o)<max_e ]
'''
