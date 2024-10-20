import os, re, textwrap, json

str_dic = json.load(open('./get_font_size/character_widths.json', 'r', encoding='utf-8'))

def get_width(character):
    return [character, str_dic.get(character, 0)]

def walk(adr):
    mylist = []
    for root, dirs, files in os.walk(adr):
        for name in files:
            adrlist = os.path.join(root, name)
            mylist.append(adrlist)
    return mylist


def create_file(dstname):
    if not os.path.exists(os.path.dirname(dstname)):
        os.makedirs(os.path.dirname(dstname))

fl = walk('script')
sumlen = 0


def ww(line):
    line_len = len(line)
    message_len = 0
    is_message = 0
    new_word = ""
    new_line = ""

    for j in range(len(line)):
      character = line[j]
      char_l = line[j-1] if j > 0 else " "
      char_r = line[j+1] if j < line_len - 1 else " "

      if ord(char_l) == 9670: #find the second ◆, where message starts
        is_message += 1

      # if is_message >= 2:
        # if character == " " and message_len > 25: #add a [n] after a space, when character count is over 30
      
      if message_len > 190:
          new_line = new_line + "[n]"
          message_len = sum(get_width(character)[1] for character in new_word)
          new_word = new_word + character  
          continue

      if (character in ['s', 'n', 'c'] and char_l == '[' and char_r == ']') or character == '}': 
        message_len = 0 

      if is_message >= 2 and character not in '※[]{}、()': 
          message_len += get_width(character)[1]
          # message_len += 1


      new_word = new_word + character  

      if character == ' ' or j == line_len - 2:
        new_line = new_line + new_word
        new_word = ""
      
      
      # test
      # print(f'{character} {message_len}')

    return new_line

def main():
  for fn in fl:
      src = open(fn, 'r', encoding='utf8')
      script_lines = src.readlines()

      dstname = 'script_done' + fn[6:-3] + 'txt'
      create_file(dstname)
      dst = open(dstname, 'w', encoding='utf8')
      
      #get the number of lines
      line_count = 0
      for line in script_lines: line_count += 1
      
      for i in range(line_count):
        line = script_lines[i]

        #split up lines that are too long to fit on-screen
        new_line = ""
        if not ord(line[0]) == 9670: continue #first character must be ◆
        new_line = ww(line)
        script_lines[i] = new_line
  
      dst.writelines(script_lines)
      dst.close()

test = '''◆00000004◆  Therefore, that counterstrike was equally ferocious. It reverberated with a thunderous roar, utterly inconceivable for mere steel clashing against steel, to the point where the very atmosphere wailed in its final throes.[z]
'''
test = '''◆00000028◆  A lawless world where universal faith held no place. Such is the principle of the demonic world that would in time be defined as Maraloka.[z]
'''
print(ww(test), file=open('testww.txt', 'w', encoding='utf8'))
main()