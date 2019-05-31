import random
import uinput

from html_element import html_raw
from time import sleep

_KEYS = {'esc':uinput.KEY_ESC,
         '1':uinput.KEY_1,
         '2':uinput.KEY_2,
         '3':uinput.KEY_3,
         '4':uinput.KEY_4,
         '5':uinput.KEY_5,
         '6':uinput.KEY_6,
         '7':uinput.KEY_7,
         '8':uinput.KEY_8,
         '9':uinput.KEY_9,
         '0':uinput.KEY_0,
         '-':uinput.KEY_MINUS,
         '=':uinput.KEY_EQUAL,
         'backspace':uinput.KEY_BACKSPACE,
         'tab':uinput.KEY_TAB,
         'q':uinput.KEY_Q,
         'w':uinput.KEY_W,
         'e':uinput.KEY_E,
         'r':uinput.KEY_R,
         't':uinput.KEY_T,
         'y':uinput.KEY_Y,
         'u':uinput.KEY_U,
         'i':uinput.KEY_I,
         'o':uinput.KEY_O,
         'p':uinput.KEY_P,
         '[':uinput.KEY_LEFTBRACE,
         ']':uinput.KEY_RIGHTBRACE,
         'enter':uinput.KEY_ENTER,
         'control':uinput.KEY_LEFTCTRL,
         'a':uinput.KEY_A,
         's':uinput.KEY_S,
         'd':uinput.KEY_D,
         'f':uinput.KEY_F,
         'g':uinput.KEY_G,
         'h':uinput.KEY_H,
         'j':uinput.KEY_J,
         'k':uinput.KEY_K,
         'l':uinput.KEY_L,
         ';':uinput.KEY_SEMICOLON,
         '\'':uinput.KEY_APOSTROPHE,
         'shift':uinput.KEY_LEFTSHIFT,
         '\\':uinput.KEY_BACKSLASH,
         'z':uinput.KEY_Z,
         'x':uinput.KEY_X,
         'c':uinput.KEY_C,
         'v':uinput.KEY_V,
         'b':uinput.KEY_B,
         'n':uinput.KEY_N,
         'm':uinput.KEY_M,
         ',':uinput.KEY_COMMA,
         '.':uinput.KEY_DOT,
         '/':uinput.KEY_SLASH,
         # '':uinput.KEY_RIGHTSHIFT,
         # '':uinput.KEY_KPASTERISK,
         # '':uinput.KEY_LEFTALT,
         ' ':uinput.KEY_SPACE,
         # '':uinput.KEY_CAPSLOCK,
         # '':uinput.KEY_F1,
         # '':uinput.KEY_F2,
         # '':uinput.KEY_F3,
         # '':uinput.KEY_F4,
         # '':uinput.KEY_F5,
         # '':uinput.KEY_F6,
         # '':uinput.KEY_F7,
         # '':uinput.KEY_F8,
         # '':uinput.KEY_F9,
         # '':uinput.KEY_F10,
         # '':uinput.KEY_NUMLOCK,
         # '':uinput.KEY_SCROLLLOCK,
         # '':uinput.KEY_KP7,
         # '':uinput.KEY_KP8,
         # '':uinput.KEY_KP9,
         # '':uinput.KEY_KPMINUS,
         # '':uinput.KEY_KP4,
         # '':uinput.KEY_KP5,
         # '':uinput.KEY_KP6,
         # '':uinput.KEY_KPPLUS,
         # '':uinput.KEY_KP1,
         # '':uinput.KEY_KP2,
         # '':uinput.KEY_KP3,
         # '':uinput.KEY_KP0,
         # '':uinput.KEY_KPDOT,
         # '':uinput.KEY_F11,
         # '':uinput.KEY_F12,
         # '':uinput.KEY_KPENTER,
         # '':uinput.KEY_RIGHTCTRL,
         # '':uinput.KEY_KPSLASH,
         # '':uinput.KEY_RIGHTALT,
         # '':uinput.KEY_HOME,
         # '':uinput.KEY_UP,
         # '':uinput.KEY_PAGEUP,
         # '':uinput.KEY_LEFT,
         # '':uinput.KEY_RIGHT,
         # '':uinput.KEY_END,
         # '':uinput.KEY_DOWN,
         # '':uinput.KEY_PAGEDOWN,
         # '':uinput.KEY_INSERT,
         # '':uinput.KEY_DELETE,
         # '':uinput.KEY_MUTE,
         # '':uinput.KEY_VOLUMEDOWN,
         # '':uinput.KEY_VOLUMEUP,
         # '':uinput.KEY_POWER,
         # '':uinput.KEY_KPEQUAL,
         # '':uinput.KEY_PAUSE,
         # '':uinput.KEY_LEFTMETA,
         # '':uinput.KEY_RIGHTMETA,
         }

_HTML_REPLACEMENTS = {'<div class="letters" tabindex="1">':'',
                      '<span class="incomplete current">':'',
                      '<span class="incomplete">':'',
                      '</span>':'',
                      '</div>':'',
                      '\'':'\\\''}


def get_string_from_html(html_str):
    for i, j in _HTML_REPLACEMENTS.iteritems():
        html_str = html_str.replace(i, j)
    return html_str


def get_dur(string, wpm):
    '''wpm = (5 * number of characters) / (time taken)'''
    wps = wpm/60.0
    num_char = len(string)
    return 60.0 / (5.0 * wpm)


class Keyboard(object):

    def __init__(self):
        self._keyboard = uinput.Device(list(_KEYS.values()))

    def emit_click(self, char, is_upper = False):
        # print('\ndebug: %s,%s' %(char,is_upper))
        if is_upper:
            self._keyboard.emit_combo([_KEYS['shift'], _KEYS[char],])
        elif char == ':':
            self._keyboard.emit_combo([_KEYS['shift'], _KEYS[';'],])
        else:
            self._keyboard.emit_click(_KEYS[char])

    def type(self, string, wpm = 172, err_pct_goal = 99):
        dur = 60.0 / (5.0 * wpm) * err_pct_goal / 100.0
        for cc in string:
            if random.random() > err_pct_goal/100.0:
                self.emit_click('e')
            else:
                uppercase = False
                if cc.isupper():
                    uppercase = True
                    cc = cc.lower()
                self.emit_click(cc, is_upper = uppercase)
            sleep(dur)


if __name__ == '__main__':

    kb = Keyboard()

    sleep(2)
    str_to_type = get_string_from_html(html_raw)
    kb.type(str_to_type)
    sleep(1)
