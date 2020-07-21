# coding=utf-8
import requests;
from bs4 import BeautifulSoup;
import time;
import re;
from sys import argv;

#获取网站列表(翻页)
def web_list(tb_title, keyword, page_num):
    page = 1;
    resp_list = [];
    while page <= page_num:
    # 打开 —— 指定的贴吧
        def open_web():
            data = {
                "ie": "utf-8",
                "kw": str(tb_title),
                "qw": str(keyword),
                "pn": page
            }
            response = requests.post(url=url, data=data);
            return response;
        resp = open_web();
        page = page + 1;
        resp_list.append(resp);
    return resp_list;


#获取需要的内容
def bs4_web(resp):
    prefix = "https://tieba.baidu.com/";
    title_list = [];
    url_list = [];
    web_dict = {};
    for context in resp:
        soup = BeautifulSoup(context.text,"html.parser");
        #查找data-fid
        data_fid = soup.find_all("a", class_="bluelink");
        dataFid = "";
        for fid in data_fid:
            #利用has_attr来判断时，其判断对象必须是标签
            if fid.has_attr("data-fid") :
                if True:
                    dataFid = fid["data-fid"];
        screen = soup.find_all("a",class_="bluelink",attrs={"data-fid":dataFid});
        #去掉，搜索出回复的帖
        for need in screen:
            need_url = prefix+need["href"];
            need_tit = need.text;
            # print(need_title)
            if need_tit[0:2] != "回复" :
                title_list.append(need_tit);
                url_list.append(need_url);
    web_dict["title"] = title_list;
    web_dict["url"] = url_list;
    return web_dict;

#判断输入的maxNum是不是在总页数范围之内
def judge_page(get_max,tb_tit,key):
    split = re.compile("\d");
    data = {
        "ie": "utf-8",
        "kw": str(tb_tit),
        "qw": str(key),
        "pn": 1
    }
    response = requests.post(url=url, data=data);
    soup = BeautifulSoup(response.text, "html.parser");
    page_div = soup.find("div", class_="pager pager-search");
    all_page_num = page_div.find_all("a", text=split);
    page_num = len(all_page_num);
    if get_max <= page_num+1:
        return get_max;
    else:
        return page_num+1;

def program_started(tb_tit,key,maxNum):
    start2 = time.time();
    preprocessorDict = bs4_web(web_list(tb_title=tb_tit, keyword=key, page_num=judge_page(int(maxNum), tb_tit, key)));
    end2 = time.time();
    print("获取数据花费时间：", end2 - start2, "获取的数据:", len(preprocessorDict["title"]));
    return preprocessorDict;


if __name__ == '__main__' :
    url = "http://tieba.baidu.com/f/search/res?ie=utf-8&red_tag=j3430565636";
    # sys 获取 java 使用系统命令输入的数据。
    data_disposeList = program_started(argv[1],argv[2],argv[3]);
    start3 = time.time();
    # data_disposeList = program_started("梦幻西游", "sf", 20)
    print(data_disposeList["title"])
    end3 = time.time()
    print("单线程花费时间：", end3-start3);

    # dataList = [];
    # # 创建多线程类，并重写方法
    # class myThread(threading.Thread):
    #     def __init__(self, name):
    #         # super(myThread, self).__init__();
    #         threading.Thread.__init__(self);
    #         self.name = name;
    #
    #     def run(self):
    #         time.sleep(1);
    #         print("线程开启" + self.name);
    #         preprocessorDict = program_started("梦幻西游", "sf", 20);
    #         dataList.append(preprocessorDict);
    #         print("线程结束" + self.name);
    # threadName = ["线程1", "线程2", "线程3"];
    # threads = [];
    # start = time.time();
    # disposeList = [];
    # # 创建新线程
    # for tName in threadName:
    #     thread = myThread(name=tName);
    #     thread.setDaemon(True);
    #     thread.start();
    #     threads.append(thread);
    # for t in threads:
    #     t.join();
    # end = time.time();
    # print("多线程:", end - start);
    #
    # titAllList = []
    # titList = [];
    # final_List = [];
    # for i in range(len(dataList)):
    #     titAllList.append(dataList[i]["title"])
    #     for j in range(len(titAllList[i])):
    #         titList.append(titAllList[i][j])
    # # 定义 pandas.DataFrame 导入对应需要处理的数据列表
    # frame = pandas.DataFrame(titList);
    # # 利用 drop_duplicates keep='first' 时，只保留相同数据中的 1 个数据
    # final_List = frame.drop_duplicates(keep="first")
    # print(final_List , "   length = " ,len(final_List))
    # # dispose_data(pendingList=dataList);
    # # 创建多线程类，并重写方法
    # class myThread(threading.Thread):
    #     def __init__(self, name, func, args=()):
    #         super(myThread, self).__init__();
    #         # threading.Thread.__init__(self);
    #         self.name = name;
    #         self.func = func;
    #         self.args = args;
    #     def run(self):
    #         time.sleep(1);
    #         print("线程开启" + self.name);
    #         program_started("java", "DataInputStream", 20);
    #         self.result = self.func(*self.args)
    #         print("self,result = ",self.result)
    #         print("线程结束" + self.name);
    #     def get_result(self):
    #         # 等线程执行完毕
    #         threading.Thread.join(self)
    #         try:
    #             return self.result
    #         except Exception:
    #             return None
    # threadName = ["线程1" ,"线程2" ,"线程3"];
    # threads = [];
    # start = time.time();
    # disposeList = [];
    # #创建新线程
    # for tName in threadName:
    #     thread = myThread(name=tName,func=program_started,args=("java", "DataInputStream", 20));
    #     thread.setDaemon(True);
    #     thread.start();
    #     thread.join(1);
    #     threads.append(thread);
    #     disposeList.append(thread.get_result())
    #
    # end = time.time();
    # print("多线程:", end - start);
    # print("disposeList = ", disposeList[0]["disposeList"])
