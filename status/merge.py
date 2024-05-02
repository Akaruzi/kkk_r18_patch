import os

def main():
    w = open('./merged.txt', 'w', encoding='utf-8')
    ft = os.listdir('./text')
    for f in ft:
        with open(f'text/{f}', 'r', encoding='utf-8') as fp:
            content = fp.read()
        print(f'{f}', file=w)
        print(content, file=w)
        print('', file=w)
        print(f'{f} has done.')
        

main() 