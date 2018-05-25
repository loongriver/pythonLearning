from urllib import request
import chardet

if __name__ == "__main__":
    response = request.urlopen("http://www.fanyi.com/")
    html = response.read()
    #html = html.decode("utf-8")
    charset = chardet.detect(html)
    print(charset)