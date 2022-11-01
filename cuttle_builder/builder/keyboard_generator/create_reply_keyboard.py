
from builder import read_file 


def create_reply_keyboard(kb_name, buttons):
    code = read_file('builder/additional/samples/reply_keyboard_sample.txt')
    new_line = '\n'
    code = code.format(kb_name,','.join([
                f'KeyboardButton(text="{button}"){new_line}' 
                for button in buttons
            ]) )
    return code