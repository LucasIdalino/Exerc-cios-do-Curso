from time import sleep


def maior(*num):
    print("=="*15)
    print("Analisando os valores passados...")
    for c in num:
        print(f"{c}", end=" ", flush=True)
        sleep(0.3)
    print(f"Foram informados {len(num)} valores ao todo.")
    print(f"O maior valor informado foi {max(num)}.")


maior(4, 8, 7)
maior(9, 7, 2, 5, 4)
maior(27, 28, 19, 50)
maior(2)
maior(0)
maior(2, 3)
