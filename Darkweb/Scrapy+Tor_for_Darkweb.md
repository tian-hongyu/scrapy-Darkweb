### 环境准备

IP：144.34.131.212

Port：26316

账号：root

密码：z6KvfKy6fN0y

环境：ubuntu18.04+Python3.6+tor

1.检查Python版本，ubuntu18.04自带python3；

2.安装操作工具apt-get install vim、apt-get install unzip；

3.安装tor，apt-get install tor，torrc文件在/etc/tor/目录下，不需要修改，默认是localhost:9050;

4.启动tor服务：sudo service tor start；

5.安装privoxy:apt-get install privoxy

6.进入/etc/privoxy/文件夹下修改config文件，最后添加上
```
listen-address localhost:8118
forward-socks5 / 127.0.0.1:9050 .
```

7.进入/usr/share/privoxy/文件夹下修改config文件，最后添加上
```
listen-address localhost:8118
forward-socks5 / 127.0.0.1:9050 .
```

8.在/usr/share/privoxy/文件夹下，启动privoxy

```
privoxy
```
9.查看端口是否已开启

```
netstat -anlp | grep 8118
```

10.创建虚拟环境py3_spider并激活使用；
    
    安装虚拟环境

```
sudo pip3 install virtualenv
sudo pip3 install virtualenvwrapper
```
    
    配置虚拟环境


```
#创建虚拟环境管理目录
mkdir ~/.virtualenvs
```


```
打开.bashrc文件
sudo vim ~/.bashrc
```


```
#将以下内容添加到.bashrc文件最后
export WORKON_HOME=$HOME/.virtualenvs  # 所有虚拟环境存储的目录
source /usr/local/bin/virtualenvwrapper.sh
```


```
启用配置文件
source ~/.bashrc
```


```
创建虚拟环境
mkvirtualenv -p /usr/bin/python3 py3_spider
```


11.在py3_spider中安装scrapy:pip3 install scrapy==1.6.0

12.在文件夹/opt/demo/下创建scrapy文件：scrapy startproject Darkweb；

13.进入Darkweb，创建爬虫工程

```
scrapy genspider onion jamiewebgbelqfno.onion
```


### 代码修改
1.在工程目录下的middlewares.py编写新的代理中间件

```
class ProxyMiddleware(object):
    # 单个代理

    def __init__(self, settings):
        self.proxy = settings.get('PROXY')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        request.meta['proxy'] = self.proxy
```

2.在settings.py模块注册进新的中间件

```
PROXY = 'http://127.0.0.1:8118'
DOWNLOADER_MIDDLEWARES = {
    
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':400,
    'Darkweb.middlewares.ProxyMiddleware': 100,
}
```
3.根据不同需求，编写spiders下模块；


4.进入虚拟环境：workon py3_spider



5.开启爬虫，在spiders目录下：

```
scrapy crawl onion --nolog
```
