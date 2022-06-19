number = 0

def on_gesture_shake():
    global number
    basic.clear_screen()
    number = randint(0, 10)
    if number < 3:
        basic.show_icon(IconNames.YES)
    elif number > 3:
        basic.show_icon(IconNames.NO)
    else:
        basic.show_icon(IconNames.DIAMOND)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
