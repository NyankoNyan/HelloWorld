import os
import time
import keyboard # Понадобится установить этот пакет
from itertools import zip_longest

def get_cow_art(offset, mirror):
    """https://www.asciiart.eu/animals/cows"""
    cow_ascii = """
         (__)    
 `\------(oo)
   ||    (__)
   ||w--|| 
    """
    max_len = max(len(s) for s in cow_ascii.split('\n'))
    if mirror:
        cow_ascii = '\n'.join(
            ' ' * (max_len - len(s)) + s[::-1]
            for s in cow_ascii.split('\n'))
        cow_ascii = cow_ascii.translate(str.maketrans("()\\", ")(/"))

    if offset >= 0:
        return '\n'.join(' ' * offset * 3 + s for s in cow_ascii.split('\n'))
    else:
        return '\n'.join(s[-offset*3:] for s in cow_ascii.split('\n'))


def get_field(size):
    field="""
   \|/
      \|/
           \|/
\|/
    """
    max_len = max(len(s) for s in field.split('\n'))
    # Добавляем пробелы справа, чтобы можно было выводить паттерном
    field = '\n'.join(s + ' ' * (max_len - len(s)) for s in field.split('\n'))
    return '\n'.join(s * size for s in field.split('\n'))


def overlay_art(art_back, art_front):
    out_strs = []
    for s_back, s_front in zip_longest(art_back.split('\n'), art_front.split('\n'), fillvalue=""):
        line = []
        for c_back, c_front in zip_longest(s_back, s_front, fillvalue=' '):
            if c_front == ' ':
                line.append(c_back)
            else:
                line.append(c_front)
        out_strs.append(''.join(line))
    return '\n'.join(out_strs)


def cls():
    """ https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console"""
    os.system('cls' if os.name=='nt' else 'clear')


def main_loop():
    offset = 0
    mirror = False
    while True:
        cls()
        if keyboard.is_pressed("left"):
            offset = max(offset-1, -10 // 3)
            mirror = True
        elif keyboard.is_pressed("right"):
            offset = min(offset+1, 50 // 3)
            mirror = False
        elif keyboard.is_pressed("esc"):
            break
        cow_art = get_cow_art(offset, mirror)
        field_art = get_field(10)
        print(overlay_art(field_art, cow_art))
        time.sleep(0.1)


if __name__ == "__main__":
    main_loop()
