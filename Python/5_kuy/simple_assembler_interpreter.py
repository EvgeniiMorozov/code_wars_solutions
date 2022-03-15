def simple_assembler(program: list) -> dict:
    registry = {}
    counter = 0
    while counter < len(program):

        command, subject, value = (program[counter] + " 0").split()[:3]

        if command == "mov":
            if value in registry:
                registry[subject] = registry[value]
            else:
                registry[subject] = int(value)

        if command == "dec":
            registry[subject] -= 1

        if command == "inc":
            registry[subject] += 1

        if command == "jnz":
            if subject in registry:
                if registry[subject]:
                    counter += int(value) - 1
            elif int(subject):
                counter += int(value) - 1

        counter += 1
    return registry


if __name__ == "__main__":
    print(simple_assembler(["mov a 5", "inc a", "dec a", "dec a", "jnz a -1", "inc a"]))
