let [spor, kalp, yüz, boşta] = [false, false, false, true]
function göz_kırp_aç() {
    basic.showLeds(`
. . . . .
. 0 . 1 .
. . . . .
# . . . #
. # # # .
	`)
    basic.pause(50)
    basic.showLeds(`
. . . . .
. 1 . 1 .
. . . . .
# . . . #
. # # # .
`)
    basic.pause(50)
    basic.showLeds(`
. . . . .
. 1 . 0 .
. . . . .
# . . . #
. # # # .
`)
    basic.pause(50)
    basic.showLeds(`
. . . . .
. 1 . 1 .
. . . . .
# . . . #
. # # # .
`)
    for (let _ = 0; _ < 2; _++) {
        basic.pause(100)
        basic.showLeds(`
. . . . .
. 0 . 0 .
. . . . .
# . . . #
. # # # .
`)
        basic.pause(50)
        basic.showLeds(`
. . . . .
. 1 . 1 .
. . . . .
# . . . #
. # # # .
`)
        basic.pause(50)
    }
    basic.pause(500)
}

function kalp_at() {
    basic.showLeds(`
. 0 . 0 .
0 # 0 # 0
0 # # # 0
. 0 # 0 .
. . 0 . .
`)
    basic.showLeds(`
. 1 . 1 .
1 # 1 # 1
1 # # # 1
. 1 # 1 .
. . 1 . .
`)
}

function spor_yap() {
    basic.showLeds(`
1 0 1 0 1
0 1 1 1 0
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
`)
    basic.pause(50)
    basic.showLeds(`
0 0 1 0 0
1 1 1 1 1
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
`)
    basic.pause(50)
    basic.showLeds(`
0 0 1 0 0
0 1 1 1 0
1 0 1 0 1
0 1 0 1 0
0 1 0 1 0
`)
    basic.pause(50)
    basic.showLeds(`
0 0 1 0 0
1 1 1 1 1
0 0 1 0 0
0 1 0 1 0
0 1 0 1 0
`)
    basic.pause(50)
}

function gül_üzül() {
    basic.showLeds(`
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
1 0 0 0 1
0 1 1 1 0
`)
    basic.pause(100)
    basic.showLeds(`
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
`)
    basic.pause(100)
    basic.showLeds(`
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
1 0 0 0 1
`)
    basic.pause(100)
    basic.showLeds(`
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
1 0 0 0 1
`)
    basic.pause(100)
    basic.showLeds(`
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
`)
    basic.pause(100)
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    spor = true
    kalp = false
    yüz = false
    boşta = false
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    yüz = true
    kalp = false
    spor = false
    boşta = false
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    kalp = true
    spor = false
    yüz = false
    boşta = false
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    boşta = true
    kalp = false
    spor = false
    yüz = false
})
basic.forever(function on_forever() {
    if (boşta) {
        göz_kırp_aç()
    } else if (kalp) {
        kalp_at()
    } else if (spor) {
        spor_yap()
    } else if (yüz) {
        gül_üzül()
    } else {
        basic.showLeds(`
. . # # #
. . # . .
. . # # #
. . # . .
. . # . .
`)
    }
    
})
