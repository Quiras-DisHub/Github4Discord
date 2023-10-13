import random, sys, time

width = 70        # Setting 1-100
pauseAmount = 0.05 # Setting 0-1.0
print("""Deep Cave
      Press Ctrl-C to stop!""")
time.sleep(3)
leftWidth = 20
gapWidth = 10

while True:
    rightWidth = width - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))
    try:
        time.sleep(pauseAmount)
    except KeyboardInterrupt:
        sys.exit()

    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1
    elif diceRoll == 2 and leftWidth + gapWidth < width - 1:
        leftWidth = leftWidth + 1
    else:
        pass
    