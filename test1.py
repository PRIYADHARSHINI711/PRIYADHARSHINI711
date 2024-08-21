def water_jug_solution():
    c1 =4
    c2 = 3
    target = 2
    j1 = 0
    j2 = 0
    steps = []
    steps.append((j1, j2))
    while j1 != target and j2 != target:
        if j1 == 0:
            j1 = c1
        elif j2 == c2:
            j2 = 0
        else:
            pour_amount = min(j1, c2 - j2)
            j1 -= pour_amount
            j2 += pour_amount
        steps.append((j1, j2))
    return steps
def print_steps(steps):
    for step in steps:
        print(f"J1: {step[0]} ltr, J2: {step[1]} ltr")
if __name__ == "__main__":
    steps = water_jug_solution()
    print_steps(steps)

