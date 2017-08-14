import requests

def down_image():
    ico_url="http://www.liuchaoblog.com/wp-content/uploads/2017/08/2017081407385781.ico"
    gif_url="http://www.liuchaoblog.com/wp-content/uploads/2017/08/2017081407390359.gif"

    img = requests.get(ico_url).content
    path = r'D:\素描图生成器\程序配置文件（请不要更改）\log' + '.ico'
    with open(path, 'wb') as f:
        f.write(img)

    img = requests.get(gif_url).content
    path = r'D:\素描图生成器\程序配置文件（请不要更改）\background' + '.gif'
    with open(path, 'wb') as f:
        f.write(img)