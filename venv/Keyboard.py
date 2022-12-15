from utils import sjson_dumps


MAX_BUTTONS_ON_LINE = 5
MAX_DEFAULT_LINES = 10
MAX_INLINE_LINES = 6

class VkKeyboardColor(Enum):

    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    NEGATIVE = 'negative'
    POSITIVE = 'positive'



class VkKeyboardButton(Enum):

    TEXT = "text"
    LOCATION = "location"
    VKAPPS = "open_app"
    OPENLINK = "open_link"
    CALLBACK = "callback"


class Keyboard(obj):
    __slots__ = ('one-time', 'lines', 'keyboard', 'inline')

    def __init__(self, one_time=False, inline=False):
        self.one_time = one_time
        self.inline = inline
        self.lines = [[]]
        self.keyboard = {
        'one_time': self.one_time,
        'inline': self.inline,
        'buttons': self.lines
        }

    def get_keyboard(self):
        return sjson_dumps(self.keyboard)

    @classmethod
    def get_empty_keyboard(cls):
        keyboard = cls()
        keyboard.keyboard['buttons'] = []
        return keyboard.get_keyboard()

    def add_buttons(self, label, color=VkKeyboardColor.PRIMARY, payload=None):

        current_line = self.lines[-1]
        if len(current_line) >= MAX_BUTTONS_ON_LINE:
            raise ValueError(f'Max {MAX_BUTTONS_ON_LINE} buttons on line')

        color_value = color

        if isinstance(color, VkKeyboardColor):
            color_value = color_value.value

        if payload is not None and not isinstance(payload, str):
            payload = sjson_dumps(payload)

        button_type = VkKeyboardButton.TEXT.value

        current_line.append({
            'color': color_value,
            'action': {
                'type': button_type,
                'payload': payload,
                'label': label,
            }
        })
