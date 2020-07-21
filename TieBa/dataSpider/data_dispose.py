
def web_dispose(web_dict):
    disposeList = [];
    for i in range(len(web_dict["title"])):
        disposeData = "标题：",web_dict["title"][i],",地址：",web_dict["url"][i];
        disposeList.append(disposeData);
    return disposeList;
