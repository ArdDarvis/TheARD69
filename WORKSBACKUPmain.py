print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

# Correctly configure your row and column pins
keyboard.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15)
keyboard.row_pins = (board.GP22, board.GP21, board.GP20, board.GP19, board.GP18)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# This is the complete keymap for your keyboard layout
keyboard.keymap = [
    # Row 0 (13 keys) -> Padded to 14
    [   KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPACE, KC.NO,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.DEL,
        KC.LSHIFT, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCOLON, KC.QUOTE, KC.ENTER, KC.BSLASH, KC.NO,
        KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMMA, KC.DOT, KC.SLASH, KC.NO, KC.UP, KC.NO,
        KC.LGUI, KC.NO, KC.LCTRL, KC.LALT, KC.SPACE, KC.SPACE, KC.SPACE, KC.SPACE, KC.NO, KC.NO, KC.NO, KC.LEFT, KC.DOWN, KC.RIGHT,
    ]
       
]


if __name__ == '__main__':
    keyboard.go()


 
 
