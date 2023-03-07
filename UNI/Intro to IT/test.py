for x in range(1,6):
    
    answer = int(input(f"Enter Quiz{x} mark (0-5): "))
    while answer > 5 or answer < 0:

        answer = int(input(f"Enter Quiz{x} mark (0-5): "))