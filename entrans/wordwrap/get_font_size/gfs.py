import json
from PIL import ImageFont

def get_character_widths(font_path, font_size):
    font = ImageFont.truetype(font_path, font_size)
    widths = {}
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789.!?,;:\':"-':
        widths[char] = font.getsize(char)[0]
    return widths

def save_widths_to_file(widths, file_path):
    with open(file_path, 'w') as f:
        json.dump(widths, f, ensure_ascii=False, indent=4)

# font_path = './msgothic.ttc'  # 请确认这是正确的字体路径
font_path = './ARIAL_UNICODE_MS.ttf' 
font_size = 12  # 你想要的字体大小
character_widths = get_character_widths(font_path, font_size)

# 指定要保存的文件路径
file_path = 'character_widths.json'
save_widths_to_file(character_widths, file_path)

print(f"Character widths have been saved to {file_path}")
