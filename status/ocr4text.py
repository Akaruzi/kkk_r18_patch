import base64
import urllib
import requests
import json
import os
import password

API_KEY = password.API_KEY
SECRET_KEY = password.SECRET_KEY

def main():
    fps = os.listdir('./iken')
    for fp in fps:
        ocr(f'./iken/{fp}')

def ocr(fp):
        
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate?access_token=" + get_access_token()
    
    # image 可以通过 get_file_content_as_base64("C:\fakepath\ch01_1_1_text.png",True) 方法获取
    payload= "language_type=JAP&""image=" + get_file_content_as_base64(fp, True)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    res = json.loads(response.text)

    get_text(res, f'{os.path.basename(fp)}')
    

def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded 
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

def get_text(content, fn):
    t = list()
    for i in content['words_result']:
        words = i['words']
        t.append(words)
    return print('\n'.join(t), file=open(f'./text_iken/{fn}.txt', 'w', encoding='utf-8'))

if __name__ == '__main__':
    main()

