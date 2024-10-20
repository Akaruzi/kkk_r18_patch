from PIL import Image, ImageDraw, ImageFont
import textwrap
import re


def draw_vertical_text(
    text, font_path, font_size, image_width, image_height, line_spacing=10, margin=5
):

    # 计算每行可容纳的字符数

    def is_punctuation(char):
        punctuations = "︵︶︽︾︑︒﹁﹂﹃﹄︱︙︓︔︐（）《》、。「」『』―…：；，︙"
        return char in punctuations

    def custom_wrap(text, width):
        lines = []
        for paragraph in text.split("\n"):
            current_line = ""
            for char in paragraph:
                if len(current_line) == width:
                    if not is_punctuation(current_line[-1]):
                        lines.append(current_line[:-1])
                        current_line = current_line[-1]
                    else:
                        lines.append(current_line)
                        current_line = ""
                current_line += char
            if current_line:
                lines.append(current_line)
        return lines

    def process_text(text, image_height, margin, font_size, line_spacing):
        # 计算每行可容纳的字符数
        chars_per_line = (image_height - 2 * margin) // int(font_size*0.85 + line_spacing*0.85)

        # 使用自定义的换行函数处理文本
        lines = custom_wrap(text, chars_per_line)

        return lines

    # chars_per_line = (image_height - 2 * margin) // int(font_size*0.85 + line_spacing*0.85)
    lines = process_text(text, image_height, margin, font_size, line_spacing)

    # # 将文本分割成多行
    # # 分割文本并处理换行符
    # paragraphs = text.split("\n")
    # lines = []

    # for paragraph in paragraphs:
    #     lines.extend(textwrap.wrap(paragraph, width=chars_per_line))
    #     # lines.append("")  # 在每个段落后添加一个空行

    #     # 计算总行数图片宽度
    image_width = len(lines)*(font_size+line_spacing)
    print(image_width)

    # 创建一个白色背景的图片
    image = Image.new("RGBA", (image_width, image_height), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # 加载字体
    font = ImageFont.truetype(font_path, font_size)

    # 计算总行数和起始 x 坐标
    total_lines = len(lines)
    start_x = image_width - margin
    # 描边
    bold =1
    text_color = "black"

    ## 竖排字符转换函数

    def to_vertical_text(text):
        vertical_map = {
            "（": "︵",
            "）": "︶",
            "《": "︽",
            "》": "︾",
            "、": "︑",
            "。": "︒",
            "「": "﹁",
            "」": "﹂",
            "『": "﹃",
            "』": "﹄",
            "―": "︱",
            "——": "︱",
            "…": "︙",
            "：": "︓",
            "；": "︔",
            "，": "︐",
            "？": "︖",
            "?": "︖",
            "[": "﹂",  # 添加左方括号
            "]": "﹁",  # 添加右方括号
        }
        return ''.join(vertical_map.get(char, char) for char in text)

    for i, line in enumerate(lines):
        x =  first_step + start_x - i * (font_size + line_spacing)
        y = margin

        for char in line:
            char = to_vertical_text(char)
            # 如果为符号则换行
            # if char in "，。！？；：":
            #     if bold:
            #         # 通过多次绘制实现加粗效果
            #         draw.text((x + 15, y - 11), char, font=font, fill=text_color)
            #         draw.text((x + 17, y - 11), char, font=font, fill=text_color)
            #         draw.text((x + 15, y - 9), char, font=font, fill=text_color)
            #         draw.text((x + 17, y - 9), char, font=font, fill=text_color)
            #     draw.text((x + 16, y - 10), char, font=font, fill="white")
            #     y += (font_size + line_spacing) * 0.8
            #     continue

            if bold:
                # 通过多次绘制实现加粗效果
                draw.text((x - 1, y - 1), char, font=font, fill=text_color)
                draw.text((x + 1, y - 1), char, font=font, fill=text_color)
                draw.text((x - 1, y + 1), char, font=font, fill=text_color)
                draw.text((x + 1, y + 1), char, font=font, fill=text_color)

                draw.text((x - 2, y - 2), char, font=font, fill=text_color)
                draw.text((x + 2, y - 2), char, font=font, fill=text_color)
                draw.text((x - 2, y + 2), char, font=font, fill=text_color)
                draw.text((x + 2, y + 2), char, font=font, fill=text_color)

                draw.text((x - 1, y - 2), char, font=font, fill=text_color)
                draw.text((x + 1, y - 2), char, font=font, fill=text_color)
                draw.text((x - 1, y + 2), char, font=font, fill=text_color)
                draw.text((x + 1, y + 2), char, font=font, fill=text_color)

                draw.text((x - 2, y - 1), char, font=font, fill=text_color)
                draw.text((x + 2, y - 1), char, font=font, fill=text_color)
                draw.text((x - 2, y + 1), char, font=font, fill=text_color)
                draw.text((x + 2, y + 1), char, font=font, fill=text_color)

                draw.text((x - 1, y - 2), char, font=font, fill=text_color)
                draw.text((x + 2, y - 1), char, font=font, fill=text_color)
                draw.text((x - 1, y + 2), char, font=font, fill=text_color)
                draw.text((x + 2, y + 1), char, font=font, fill=text_color)

                draw.text((x - 2, y - 1), char, font=font, fill=text_color)
                draw.text((x + 1, y - 2), char, font=font, fill=text_color)
                draw.text((x - 2, y + 1), char, font=font, fill=text_color)
                draw.text((x + 1, y + 2), char, font=font, fill=text_color)

                draw.text((x - 1, y - 2), char, font=font, fill=text_color)
                draw.text((x + 2, y - 1), char, font=font, fill=text_color)
                draw.text((x - 2, y + 1), char, font=font, fill=text_color)
                draw.text((x + 1, y + 2), char, font=font, fill=text_color)

                draw.text((x - 2, y - 1), char, font=font, fill=text_color)
                draw.text((x + 1, y - 2), char, font=font, fill=text_color)
                draw.text((x - 1, y + 2), char, font=font, fill=text_color)
                draw.text((x + 2, y + 1), char, font=font, fill=text_color)

            # 绘制每个字符
            draw.text((x, y), char, font=font, fill="white")
            y += (font_size + line_spacing)*0.85

            # 如果超出底部边界，停止绘制
            if y > 3500 :
                break

        # 如果超出左侧边界，停止绘制
        if x < margin:
            break

    return [image, image_width]

def get_text(fn):
    fn1 = fn + "_cn.txt"
    fn2 = fn + "_names.txt"
    t = list()
    with open(fn1, "r", encoding="utf-8") as f2, open(fn2, "r", encoding="utf-8") as f1:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        lines1 = list(map(str.strip, lines1))
        lines2 = list(map(lambda x: '　'+x.strip(), lines2))

    t = list(zip(lines1, lines2))
    return t


def pdraw(fn, font_path, font_size, image_width, image_height):
    f2 = open(f'{fn}_wg.txt', "w", encoding="utf-8")
    for title, text in get_text(fn):
        pd = draw_vertical_text(text, font_path, font_size, image_width, image_height)
        Image = pd[0]
        Image.save(f"./new/{title.replace('.png', '')}_cn.png")
        print(f"{title}_cn.png\t{pd[1]}", file=f2)
    f2.close()

def edit_svg(fn):

    def check(t1, t2):
        for i in range(len(t1)):
            if t1[i] in t2:
                return t1[i]
        return False
    # input outpufile.txt

    pattern1 = r"<image (id='[^']*') (x='[^']*') y='[^']*' width='[^']*' (height='[^']*') xlink:href='[^']*'/>"

    def replace_line(match, width, title, height):
        # return f"<image {match.group(1)} width='{width}' {match.group(2)} xlink:href='./{title}' {match.group(3)}/>"
        return f"<image {match.group(1)} {match.group(2)} y ='140' width='{width}' height='{height}' xlink:href='./{title}'/>"

    for title, text in get_text(fn):
        title = title.replace(".png", "")
        print(title)

        # 使用正则表达式进行替换
        f3 = open(f'./new/{title}.svg', "w", encoding="utf-8")

        with open(f'{fn}_wg.txt', "r", encoding="utf-8") as f1, open(f'{title}.svg', "r", encoding="utf-8") as f2:
            lines1 = f1.readlines()
            dic = {}
            for line in lines1:
                title, width = line.split('\t')
                dic[title.replace('_cn.png', '')] = width.strip()
            print(dic)

            lines2 = f2.readlines()
            for i in range(len(lines2)):
                ck = check(list(map(lambda x: x.replace('.png', '') ,dic.keys())), lines2[i])
                print(ck)
                if ck:
                    # pattern = r"(xlink:href|width)='[^']*'"
                    title = ck + ".png"
                    print("++++++++++++++++++++++++++++")
                    width = dic[title].strip()
                    title = ck+'_cn.png'
                    # res = re.sub(pattern, replace_values(title, width), text)
                    res = re.sub(pattern1, lambda m: replace_line(m, width=width, title=title, height=image_height), lines2[i])
                    print(res,  end='',  file=f3)

                else: 
                    print(lines2[i], end='', file=f3)


# 使用示例
text = "这是一个用Python绘制的多行竖排中文文本示例。它可以自动换行并控制字体大小。"
text2 = """In the start of spring, I wish you to be in good health.
I was deeply grateful when you visited me the other day. I am deeply ashamed of my inadequate welcome to you.
But please pardon my rudeness, I would like to live as time goes by in seclusion here. Though nothing was left, I do not wish to part from Kyogetsu Village.
As for living in the new capital… I do not believe there is a place, nor I am wanted in there.
Nevertheless, I did know you were trying to help me. With that mind, I wrote this letter to appease for your forgiveness.
"""

font_path = "WeiNiZhuYiLangManXingShu-2.ttf" 
# font_path = "DunHuangFeiTian-XingKaiTi-2.ttf"
# font_path = "simsun.ttc"
font_size = 40
image_width = 400
image_height = 980
first_step = -39

# image = draw_vertical_text(text, font_path, font_size, image_width, image_height)[0]
# image.show()  # 显示图片
# image.save("ch01_1_1_text.png")  # 保存图片
# print(get_text('jp1-5.txt'))
