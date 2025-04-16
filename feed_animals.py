def feed_animals(animals, food):
    if 0 in (len(animals), len(food)):
        return 0
    animals.sort()
    food.sort()

    count = 0
    for f in food:
        if f >= animals[count]:
            count += 1
        if count == len(animals):
            break

    return count