# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(kbd)

# define buttons. these can be any physical switches/buttons, but the values
# here work out-of-the-box with a CircuitPlayground Express' A and B buttons.
up = digitalio.DigitalInOut(board.GP9)
up.direction = digitalio.Direction.INPUT
up.pull = digitalio.Pull.UP

dn = digitalio.DigitalInOut(board.GP5)
dn.direction = digitalio.Direction.INPUT
dn.pull = digitalio.Pull.UP

lf = digitalio.DigitalInOut(board.GP8)
lf.direction = digitalio.Direction.INPUT
lf.pull = digitalio.Pull.UP

rt = digitalio.DigitalInOut(board.GP6)
rt.direction = digitalio.Direction.INPUT
rt.pull = digitalio.Pull.UP

z = digitalio.DigitalInOut(board.GP3)
z.direction = digitalio.Direction.INPUT
z.pull = digitalio.Pull.UP

x = digitalio.DigitalInOut(board.GP2)
x.direction = digitalio.Direction.INPUT
x.pull = digitalio.Pull.UP

# space = digitalio.DigitalInOut(board.GP2)
# space.direction = digitalio.Direction.INPUT
# space.pull = digitalio.Pull.UP

enter = digitalio.DigitalInOut(board.GP4)
enter.direction = digitalio.Direction.INPUT
enter.pull = digitalio.Pull.UP

kbd.release_all()
old_up = 0
old_dn = 0
old_lf = 0
old_rt = 0
old_space = 0
old_enter = 0
old_z = 0
old_x = 0
while True:
    if  z.value and (old_z != z.value or old_z == 0):
        old_z = z.value
        kbd.release(Keycode.Z)
    if not z.value and old_z != z.value:
        old_z = z.value
        kbd.press(Keycode.Z)
        
    if  x.value and (old_x != x.value or old_x == 0):
        old_x = x.value
        kbd.release(Keycode.X)
        kbd.release(Keycode.SPACE)
    if not x.value and old_x != x.value:
        old_x = x.value
        kbd.press(Keycode.X)
        kbd.press(Keycode.SPACE)
    
    if  enter.value and (old_enter != enter.value or old_enter == 0):
        old_enter = enter.value
        kbd.release(Keycode.ENTER)
    if not enter.value and old_enter != enter.value:
        old_enter = enter.value
        kbd.press(Keycode.ENTER)
    
    if up.value and (old_up != up.value or old_up == 0):
        old_up = up.value
        kbd.release(Keycode.UP_ARROW)
#         print("up release")
    if not up.value and old_up != up.value:
        old_up = up.value
        kbd.press(Keycode.UP_ARROW)
#         print("up press")

    if  dn.value and (old_dn != dn.value or old_dn == 0):
        old_dn = dn.value
        kbd.release(Keycode.DOWN_ARROW)
    if not dn.value and old_dn != dn.value:
        old_dn = dn.value
        kbd.press(Keycode.DOWN_ARROW)
        
    if  rt.value and (old_rt != rt.value or old_rt == 0):
        old_rt = rt.value
        kbd.release(Keycode.RIGHT_ARROW)
    if not rt.value and old_rt != rt.value:
        old_rt = rt.value
        kbd.press(Keycode.RIGHT_ARROW)
        
    if  lf.value and (old_lf != lf.value or old_lf == 0):
        old_lf = lf.value
        kbd.release(Keycode.LEFT_ARROW)
    if not lf.value and old_lf != lf.value:
        old_lf = lf.value
        kbd.press(Keycode.LEFT_ARROW)
        
#     if space.value and old_space != space.value:
#         old_space = space.value
#         kbd.release(Keycode.SPACE)
#     if not space.value and old_space != space.value:
#         old_space = space.value
#         kbd.press(Keycode.SPACE)

#     elif not dn.value:
#         kbd.send(Keycode.DOWN_ARROW)
#     elif not lf.value:
#         kbd.send(Keycode.LEFT_ARROW)
#     elif not rt.value:
#         kbd.send(Keycode.RIGHT_ARROW)
#         
#     elif not space.value:
#         kbd.send(Keycode.SPACE)
        
    time.sleep(0.01)