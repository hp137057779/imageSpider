# 将 imageSpider.py 操作封装好
# 定义一个接口函数
def function(url):
    import os
    import requests
    from bs4 import BeautifulSoup
    import re
    from datetime import datetime

    # 构造文件夹路径
    folder_path = 'images'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # TargetWeb_url & User-Agent
    # url = 'http://***/147559.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.190 Safari/537.36'}

    # 使用 requests 库下载网页源代码
    r = requests.get(url, headers=headers)

    # 使用 BeautifulSoup 解析 HTML 代码
    soup = BeautifulSoup(r.text, "html5lib")
    # 打印网页源代码(用于Debug)
    # print(soup)

    # 查找所有 img 标签
    img_tags = soup.find_all('img')

    # 使用 regular expression 匹配 .jpg 结尾的图片 URL
    pattern = re.compile(".*\.jpg")

    for img_tag in img_tags:
      # 获取 <img> 标签的 "src" 属性
      img_url = img_tag.attrs["src"]

      # 使用正则表达式模式匹配 URL
      match = pattern.search(img_url)
      if match:
        # 获取匹配的字符串
        matched_string = match.group()
        print(matched_string)

        # 图片链接
        img_download = matched_string
        r = requests.get(img_download, headers=headers)
        # 获取当前系统时间
        current_time = datetime.now()
        # 设置图片文件名，格式为 日期时间.jpg
        img_file_name = current_time.strftime("%Y%m%d%H%M%S") + ".jpg"
        # 下载并保存图片
        with open("images/" + img_file_name, mode="wb") as f:
            f.write(r.content)
