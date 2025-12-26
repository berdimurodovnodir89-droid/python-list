texts = ["kitob", "dastur", "AI", "hello", "python"]

groups = [
    [],
    [],
    []
]

for i in texts:
    n = len(i)
    if n <= 3:
        groups[0].append(i)
    elif 4 <= n <= 6:
        groups[1].append(i)
    else:
        groups[2].append(i)

print(groups)