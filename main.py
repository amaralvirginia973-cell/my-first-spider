import requests
from bs4 import BeautifulSoup

# 第一阶段：老规矩，暴力抓取底层代码
response = requests.get("https://www.baidu.com")
response.encoding = 'utf-8' 
soup = BeautifulSoup(response.text, "html.parser")
all_links = soup.find_all('a')

print("=====================================")
print("总工，爬虫机器已启动，正在拼命抓取并打包归档...")

# 第二阶段：核心升级！召唤大管家准备建档
# "w" 意思是 write (写入模式)，如果没有这个文件，它会自动帮你新建一个！
# encoding="utf-8" 是极其重要的规矩，防止存进硬盘后变成乱码
with open("baidu_links.txt", "w", encoding="utf-8") as file:
    
    # 派流水线工人把抓到的链接一个一个写进文件里
    for link in all_links:
        # 实用小技巧：用 .strip() 像拧毛巾一样，把文字前后多余的空格死角全拧干
        clean_text = link.text.strip() 
        
        # 严控质量：如果抓到的是空的，就不往文件里存，节省空间
        if clean_text: 
            # 把干净的文字写进文件，并加上 "\n" (这代表敲一下回车换行，保证数据一行一个)
            file.write(clean_text + "\n") 

print("=====================================")
print("报告总工：大功告成！所有战利品已成功封存入【baidu_links.txt】！")