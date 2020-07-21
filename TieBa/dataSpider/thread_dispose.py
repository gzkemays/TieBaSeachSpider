import threading;
import dataSpider.req_url as req_url;
import dataSpider.data_dispose as data_dispose;
import time;

dataList = [];
# 创建多线程类，并重写方法
class myThread(threading.Thread):
    def __init__(self, name):
        # super(myThread, self).__init__();
        threading.Thread.__init__(self);
        self.name = name;

    def run(self):
        time.sleep(1);
        print("线程开启" + self.name);
        preprocessorDict = req_url.program_started("java", "DataInputStream", 20);
        dataList.append(data_dispose.web_dispose(preprocessorDict))
        print("self,result = ", self.result)
        print("线程结束" + self.name);

threadName = ["线程1", "线程2", "线程3"];
threads = [];
start = time.time();
disposeList = [];
# 创建新线程
for tName in threadName:
    thread = myThread(name=tName);
    thread.setDaemon(True);
    thread.start();
    threads.append(thread);
for t in threads:
    t.join();
end = time.time();
print("多线程:", end - start);
print(dataList)