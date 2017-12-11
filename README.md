## Python版本 Show me the code.

- Image-to-Ascii: 

	**图片转字符画**，来自[Python 图片转字符画](https://www.shiyanlou.com/courses/370/labs/1191/document)，使用numpy重写。

- soushen-analysis：

	对小说《搜神记》进行了**文本分析**，来自[共现提取《釜山行》人物关系](https://www.shiyanlou.com/courses/677/labs/2202/document)，jieba分词，统计主要人物出现频次，matplotlib画出柱状图；对每段进行人物共性分析，保存至csv，使用gephi绘图。
	<img src="./soushenji-analysis/roles-freq.png" width = "400" height = "400" alt="人物频次" /><img src="./soushenji-analysis/relationship.jpg" width = "400" height = "400" alt="人物关系" />

- Bing-Image:

	-**bing_download**，下载bing七日内的背景（目前bing官方的jsonAPI限制在了七日内）。
	-**ioliu_download**，下载[必应壁纸网站](https://bing.ioliu.cn/)的所有必应壁纸，共600张。
	
- lagou-python

	爬取拉勾网中python的职位信息，加入了在线获取代理的`proxy.py`，使用代理池、header池、mongoDB数据库，Pool多进程爬取。
	
- Ruisi_Pic_Download

	爬取校内PT网站睿思摄影板块的2000多张图片，代码在[睿思图片爬取实战](https://github.com/cloisonne/Ruisi_Pic_Download)