from PIL import Image, ImageDraw, ImageFont
import textwrap
import re


def create_text_image(text, font_path, font_size=24, max_width=1800, bold=True):
    # 创建一个透明的图像
    img = Image.new("RGBA", (1, 1), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # 加载字体
    font = ImageFont.truetype(font_path, font_size)

    # 将文本分行
    lines = textwrap.wrap(text, width=int(max_width // font_size*wrap_index))

    # 计算文本大小
    max_line_width = 0
    total_height = 0
    for line in lines:
        line_width, line_height = draw.textsize(line, font=font)
        max_line_width = max(max_line_width, line_width)
        total_height += line_height
    total_height += 15

    # 创建适当大小的图像
    # img = Image.new("RGBA", (max_line_width, total_height), color=(255, 255, 255, 0))
    img = Image.new("RGBA", (max_width, total_height), color=(255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # 在图像上绘制文本
    y_text = 10
    x_text = 10
    for line in lines:
        if bold:
            draw.text((x_text- 1, y_text - 1), line, font=font, fill='black')
            draw.text((x_text+ 1, y_text - 1), line, font=font, fill='black')
            draw.text((x_text- 1, y_text + 1), line, font=font, fill='black')
            draw.text((x_text+ 1, y_text + 1), line, font=font, fill='black')

            draw.text((x_text- 2, y_text - 2), line, font=font, fill='black')
            draw.text((x_text+ 2, y_text - 2), line, font=font, fill='black')
            draw.text((x_text- 2, y_text + 2), line, font=font, fill='black')
            draw.text((x_text+ 2, y_text + 2), line, font=font, fill='black')

            draw.text((x_text- 1, y_text - 2), line, font=font, fill='black')
            draw.text((x_text+ 1, y_text - 2), line, font=font, fill='black')
            draw.text((x_text- 1, y_text + 2), line, font=font, fill='black')
            draw.text((x_text+ 1, y_text + 2), line, font=font, fill='black')

            draw.text((x_text- 2, y_text - 1), line, font=font, fill='black')
            draw.text((x_text+ 2, y_text - 1), line, font=font, fill='black')
            draw.text((x_text- 2, y_text + 1), line, font=font, fill='black')
            draw.text((x_text+ 2, y_text + 1), line, font=font, fill='black')

            draw.text((x_text- 1, y_text - 2), line, font=font, fill='black')
            draw.text((x_text+ 2, y_text - 1), line, font=font, fill='black')
            draw.text((x_text- 1, y_text + 2), line, font=font, fill='black')
            draw.text((x_text+ 2, y_text + 1), line, font=font, fill='black')

            draw.text((x_text- 2, y_text - 1), line, font=font, fill='black')
            draw.text((x_text+ 1, y_text - 2), line, font=font, fill='black')
            draw.text((x_text- 2, y_text + 1), line, font=font, fill='black')
            draw.text((x_text+ 1, y_text + 2), line, font=font, fill='black')

            draw.text((x_text- 1, y_text - 2), line, font=font, fill='black')
            draw.text((x_text+ 2, y_text - 1), line, font=font, fill='black')
            draw.text((x_text- 2, y_text + 1), line, font=font, fill='black')
            draw.text((x_text+ 1, y_text + 2), line, font=font, fill='black')

            draw.text((x_text- 2, y_text - 1), line, font=font, fill='black')
            draw.text((x_text+ 1, y_text - 2), line, font=font, fill='black')
            draw.text((x_text- 1, y_text + 2), line, font=font, fill='black')
            draw.text((x_text+ 2, y_text + 1), line, font=font, fill='black')

            draw.text((x_text- 0, y_text - 1), line, font=font, fill='black')
            draw.text((x_text+ 0, y_text - 1), line, font=font, fill='black')
            draw.text((x_text- 0, y_text + 1), line, font=font, fill='black')
            draw.text((x_text+ 0, y_text + 1), line, font=font, fill='black')

            draw.text((x_text- 0, y_text - 2), line, font=font, fill='black')
            draw.text((x_text+ 0, y_text - 2), line, font=font, fill='black')
            draw.text((x_text- 0, y_text + 2), line, font=font, fill='black')
            draw.text((x_text+ 0, y_text + 2), line, font=font, fill='black')

            draw.text((x_text- 1, y_text - 0), line, font=font, fill='black')
            draw.text((x_text+ 1, y_text - 0), line, font=font, fill='black')
            draw.text((x_text- 1, y_text + 0), line, font=font, fill='black')
            draw.text((x_text+ 1, y_text + 0), line, font=font, fill='black')

            draw.text((x_text- 2, y_text - 0), line, font=font, fill='black')
            draw.text((x_text+ 2, y_text - 0), line, font=font, fill='black')
            draw.text((x_text- 2, y_text + 0), line, font=font, fill='black')
            draw.text((x_text+ 2, y_text + 0), line, font=font, fill='black')

        
        line_width, line_height = draw.textsize(line, font=font)
        draw.text((x_text, y_text), line, font=font, fill='white')
        y_text += line_height
    


    return [img, total_height]


def get_text(fn):
    fn1 = fn + "_en.txt"
    fn2 = fn + "_names.txt"
    t = list()
    with open(fn1, "r", encoding="utf-8") as f2, open(fn2, "r", encoding="utf-8") as f1:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        lines1 = list(map(str.strip, lines1))
        lines2 = list(map(lambda x: " "*3 + x.strip(), lines2))

    t = list(zip(lines1, lines2))
    return t


def pdraw(fn, font_path, font_size, max_width):
    f2 = open(f"{fn}_wg.txt", "w", encoding="utf-8")
    for title, text in get_text(fn):    
        pd = create_text_image(text, font_path, font_size, max_width)
        Image = pd[0]
        Image.save(f"./new/{title.replace('.png', '')}_en.png")
        print(f"{title}_cn.png\t{pd[1]}", file=f2)
    f2.close()


# 使用示例
# font_path = "WeiNiZhuYiLangManXingShu-2.ttf"
# image = create_text_image(text2)
# image.show()  # 显示图片
# image.save("output.png")
# print("图片已保存为  output.png")


p1 = [5,5,5,5,5,5,6,6,9,5]
p1_s = [0,5,10,15,20,25,30,36,42,51]

def trans_height(wg, p, s):
    lt = []
    res = []
    # linespace = 10
    def sum_n(t1, n1):
        return sum(t1[i:i+n1]) 
    with open(wg, 'r') as f1, open(f'{wg}_hg.txt', 'w') as f2:
        for line in f1.readlines():
            title, height = line.split('\t')
            height = int(height)
            lt.append(height)
    for i, start in zip(p,s):
        for x in range(i):
            res.append(sum(lt[start:start+x], linespace*x)+ firstline_space)
    return res

def edit_svg(fn, wg, p, s):
    ht = trans_height(wg, p, s)
    count = 0

    def check(t1, t2):
        for i in range(len(t1)):
            if t1[i] in t2:
                return t1[i]
        return False
    # input outpufile.txt

    pattern1 = r"<image (id='[^']*') x='[^']*' (y='[^']*') width='[^']*' (height='[^']*') xlink:href='[^']*'/>"

    def replace_line(match, y, width, title, height):
        # return f"<image {match.group(1)} width='{width}' {match.group(2)} xlink:href='./{title}' {match.group(3)}/>"
        return f"<image {match.group(1)} x ='150' y = '{y}' width='{width}' height='{height}' xlink:href='./{title}'/>"

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
                    height = dic[title].strip()
                    title = ck+'_en.png'
                    # res = re.sub(pattern, replace_values(title, width), text)
                    res = re.sub(pattern1, lambda m: replace_line(m, y=ht[count], width=iw, title=title, height=height), lines2[i])
                    print(res,  end='',  file=f3)
                    count +=1

                else: 
                    print(lines2[i], end='', file=f3)


# fp = "WeiNiZhuYiLangManXingShu-2.ttf"
# fp = "kyotonortherndemofpu-zvk13.ttf"
fp = "Kaushanscript.ttf"
# fp = "arial.ttf"

fs = 45
iw = 1900
ih = 1000
linespace = 3
firstline_space = 70
wrap_index = 2.36
pdraw("tgm1", fp, fs, iw)
edit_svg("tgm1", "tgm1_wg.txt", p1, p1_s)
