def recoverSecret(triplets):
    secret = []
    for a in triplets:
        x = a[0]
        y = a[1]
        z = a[2]
        if x not in secret:
            secret.insert(0, x)
        if y not in secret:
            secret.insert(secret.index(x) + 1, y)
        if y in secret and secret.index(y) < secret.index(x):
            secret.pop(secret.index(y))
            secret.insert(secret.index(x) + 1, y)
        if z not in secret:
            secret.insert(secret.index(y) + 1, z)
        if z in secret and secret.index(z) < secret.index(y):
            secret.pop(secret.index(z))
            secret.insert(secret.index(y) + 1, z)
    return "".join(secret)


if __name__ == "__main__":
    pass
