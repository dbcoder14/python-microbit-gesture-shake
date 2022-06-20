y = 0
x = 0
i = 0
while i < 25:
    led.plot(x, y)
    basic.pause(100)
    x += 1
    i += 1
    if x > 4:
        x = 0
        y += 1
basic.clear_screen()