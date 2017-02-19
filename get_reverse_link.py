# code utf-8
import urllib
import urllib.request,urllib.parse,urllib.response
import re
import time
class getLinkedDominByBaidu:
    '''通过使用搜索引擎查找反向链接'''
    domin = ""
    pages = 50 # 请求的页面数
    result = [] #结果
    def __init__(self,domin):
        self.domin = domin
    def request_baidu(self,i):
        '''i indent current page no
        '''
        import urllib
        url_search = urllib.parse.urlencode({"wd":self.domin,"pn":i})
        url_search = "http://www.baidu.com/s?"+url_search
        ret = urllib.request.urlopen(url_search).read().decode("utf-8")
        return  ret
        # print(ret)

    def parse_content(self,content):
        '''从返回数据中解析链接 返回list'''
        # print(content)
        url = re.findall("c-showurl\" style=\"text-decoration:none;\">.*?</a",content)
        ret = []
        for i in url:
            tmp = re.sub("c-showurl\" style=\"text-decoration:none;\">","",i)
            tmp = re.sub("<b>","",tmp)
            tmp = re.sub("</b","",tmp)
            tmp = re.sub("\.\.\.&nbsp;</a","",tmp)
            tmp = re.sub(">/","/",tmp)
            ret.append(tmp)
        return  ret
        # print(ret)
    def save_result(self,url):
        self.result.append(url)

    def work(self):
        for i in range(0,self.pages):
            content = self.request_baidu(i)
            url = self.parse_content(content)
            self.save_result(url)
            time.sleep(5)

runAppli = getLinkedDominByBaidu("test.com")
runAppli.work()
print(runAppli.result)