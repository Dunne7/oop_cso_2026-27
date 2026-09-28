class Enemy:
    type = "electric"
    health = 5
    x_pos = 10
    y_pos = 10


if __name__ == "__main__":
    first_enemy = Enemy()

    print(f"enemy type: {first_enemy.type}")
    first_enemy.type = "fire"
    print(f"enemy type: {first_enemy.type}")