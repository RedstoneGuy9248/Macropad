import board
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.macros import Press, Release, Tap, Macros, Delay
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
encoder_handler = EncoderHandler()
macros = Macros()
keyboard.modules = [encoder_handler, macros]

keyboard.col_pins = (board.GP6, board.GP7, board.GP8)
keyboard.row_pins = (board.GP27, board.GP26, board.GP25)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = ((board.GP21, board.GP22, board.GP24, False),)

encoder_handler.map = [((KC.VOLU, KC.VOLD, KC.MPLY),)]


# to be implemented later


REBOOT_INTO_WINDOWS = KC.MACRO(
    Tap(KC.LGUI(KC.N1)),
    Delay(2000),
    "./windows.sh",
    Tap(KC.ENTER)
)


keyboard.keymap = [[KC.N1, KC.N2, KC.N3], [KC.N4, KC.N5, KC.N6], [KC.N7, KC.N8, KC.N9]]

if __name__ == "__main__":
    keyboard.go()
