from HandleJs import Py4Js

def open_url(url):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    #url.request.Rquest()包装请求，再通过urlopen获取页面
    req = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode('utf-8')
    return data

def max_length(content):
    if len(content) > 4891:
        print("超过翻译长度")
        return

def print_result(url):
    result = url
    end = result.find("\",")
    if end > 4:
        print(result[4:end])

def en_to_zn(content,tk):
    max_length(content)
    content = urllib.parse.quote(content)
    url = "http://translate.google.cn/translate_a/single?client=t"\
          "&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca"\
          "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1"\
          "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s"%(tk,content)
    result = open_url(url)
    print_result(result)

def zn_to_en(content,tk):
    max_length(content)
    content = urllib.parse.quote(content)
    url = "http://translate.google.cn/translate_a/single?client=t"\
          "&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca"\
          "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8"\
          "&source=btn&ssel=3&tsel=3&kc=0&tk=%s&q=%s"%(tk,content)
    result = open_url(url)
    print_result(result)

def main():
    js = Py4Js()
    while True:
        content = input("[1.英译汉 2.汉译英 q!退出翻译]输入翻译内容:")
        choose = input("选择翻译选项:")
        if choose == 'q!':
            print("End")
            break
        elif choose == '1':
            tk = js.getTk(content)
            en_to_zn(content,tk)
        elif choose == '2':
            tk = js.getTk(content)
            zn_to_en(content,tk)

if __name__ == "__main__":
    main()
