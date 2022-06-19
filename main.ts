let number = 0
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    basic.clearScreen()
    number = randint(0, 10)
    if (number < 3) {
        basic.showIcon(IconNames.Yes)
    } else if (number > 3) {
        basic.showIcon(IconNames.No)
    } else {
        basic.showIcon(IconNames.Diamond)
    }
    
})
