spor, kalp, yüz, boşta = (False, False, False, True)

def on_button_pressed_a():
	global spor, kalp, yüz, boşta
	spor = True
	kalp = False
	yüz = False
	boşta = False

def on_button_pressed_ab():
	global spor, kalp, yüz, boşta
	yüz = True
	kalp = False
	spor = False
	boşta = False

def on_button_pressed_b():
	global spor, kalp, yüz, boşta
	kalp = True
	spor = False
	yüz = False
	boşta = False

def on_gesture_shake():
	global spor, kalp, yüz, boşta
	boşta = True
	kalp = False
	spor = False
	yüz = False

def göz_kırp_aç():
	basic.show_leds("""
. . . . .
. 0 . 1 .
. . . . .
# . . . #
. # # # .
	""")
	basic.pause(50)
	basic.show_leds("""
. . . . .
. 1 . 1 .
. . . . .
# . . . #
. # # # .
""")
	basic.pause(50)
	basic.show_leds("""
. . . . .
. 1 . 0 .
. . . . .
# . . . #
. # # # .
""")
	basic.pause(50)
	basic.show_leds("""
. . . . .
. 1 . 1 .
. . . . .
# . . . #
. # # # .
""")
	for _ in range(2):
		basic.pause(100)
		basic.show_leds("""
. . . . .
. 0 . 0 .
. . . . .
# . . . #
. # # # .
""")
		basic.pause(50)
		basic.show_leds("""
. . . . .
. 1 . 1 .
. . . . .
# . . . #
. # # # .
""")
		basic.pause(50)

	basic.pause(500)

def kalp_at():
	basic.show_leds("""
. 0 . 0 .
0 # 0 # 0
0 # # # 0
. 0 # 0 .
. . 0 . .
""")
	basic.show_leds("""
. 1 . 1 .
1 # 1 # 1
1 # # # 1
. 1 # 1 .
. . 1 . .
""")
def spor_yap(): 
	basic.show_leds("""
1 0 1 0 1
0 1 1 1 0
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
""")
	basic.pause(50)
	basic.show_leds("""
0 0 1 0 0
1 1 1 1 1
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
""")
	basic.pause(50)
	basic.show_leds("""
0 0 1 0 0
0 1 1 1 0
1 0 1 0 1
0 1 0 1 0
0 1 0 1 0
""")
	basic.pause(50)
	basic.show_leds("""
0 0 1 0 0
1 1 1 1 1
0 0 1 0 0
0 1 0 1 0
0 1 0 1 0
""")
	basic.pause(50)

def gül_üzül():
	basic.show_leds("""
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
1 0 0 0 1
0 1 1 1 0
""")
	basic.pause(100)
	basic.show_leds("""
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
""")
	basic.pause(100)
	basic.show_leds("""
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
1 0 0 0 1
""")
	basic.pause(100)
	basic.show_leds("""
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
0 1 1 1 0
1 0 0 0 1
""")
	basic.pause(100)
	basic.show_leds("""
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
""")
	basic.pause(100)


input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
input.on_button_pressed(Button.B, on_button_pressed_b)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
	if boşta:
		göz_kırp_aç()
	elif kalp:
		kalp_at()
	elif spor:
		spor_yap()
	elif yüz:
		gül_üzül()
	else:
		basic.show_leds("""
. . # # #
. . # . .
. . # # #
. . # . .
. . # . .
""")
		
basic.forever(on_forever)