# fastopen
一个python写的小脚本，用来在mac下快速打开网页使用的

# 效果
配合iTerm终端软件用，使用`option+空格`可快速呼出终端，然后键入`fop baidu`就可以快速调出浏览器并打开百度。

# 命令列表
fastOpen(快速打开)工具帮助：  
使用 fop key value 形式为链接地址存储别名  
使用 fop key形式快速打开链接  
使用 fop k 即参数k来快速关闭浏览器  
使用 fop k key即参数k+key来快速关闭浏览器,同时打开key对应的链接  
使用 fop h 即参数h来查看本帮助  

# 使用前需修改的东西
将代码clone本地后  
将fastopen.py中的python命令地址换掉，将dbfile、chromePath、closeChromeScript也换掉  
用`chmod`命令给fastopen.py文件可执行权限  
用`ln -s`命令为fastopen.py 做个软连接到 /usr/local/bin/fop ，以后就可以直接用`fop`命令来执行操作了  
