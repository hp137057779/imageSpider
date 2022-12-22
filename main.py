# 导入 functions.py 文件
import function

# 定义起始的网址链接url & 需要保存的网页数量
url = "http://***/147559.html"
number = 10

# 为起始网址单独执行一次操作
function.function(url)

# 使用 replace() 方法删除字符串末尾的 .html
url = url.replace(".html", "")

# 循环生成对应数量的字符串
for i in range(2, number + 1):
    # 在原始网址链接后面拼接 "_" 和当前计数变量的值
    new_url = url + "_" + str(i) + ".html"
    print(new_url)
    # 为每个new_url都执行一次操作
    function.function(new_url)


