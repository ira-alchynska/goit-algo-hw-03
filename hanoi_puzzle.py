def move_disk(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"Перемістити диск з {from_rod} на {to_rod}: 1")
        return [(from_rod, to_rod)]
    else:
    
        steps = move_disk(n-1, from_rod, aux_rod, to_rod)
     
        print(f"Перемістити диск з {from_rod} на {to_rod}: {n}")
        steps.append((from_rod, to_rod))
     
        steps.extend(move_disk(n-1, aux_rod, to_rod, from_rod))
        return steps

def print_state(steps, n):
    rods = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print("Початковий стан:", {k: v[:] for k, v in rods.items()})

    for from_rod, to_rod in steps:
        disk = rods[from_rod].pop()
        rods[to_rod].append(disk)
        print(f"Проміжний стан: {from_rod} -> {to_rod}, диск {disk}")
        print({k: v[:] for k, v in rods.items()})

    print("Кінцевий стан:", {k: v[:] for k, v in rods.items()})

def main():
    n = int(input("Введіть кількість дисків: "))
    steps = move_disk(n, 'A', 'C', 'B')
    print_state(steps, n)

if __name__ == "__main__":
    main()
