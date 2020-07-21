from selenium import webdriver;
import time;
import requests;
from bs4 import BeautifulSoup;

cookies = [
    {'domain': '.tieba.baidu.com', 'httpOnly': False, 'name': 'Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948', 'path': '/',
     'secure': False, 'value': '1584609086'},
    {'domain': '.tieba.baidu.com', 'expiry': 1609430399.72359, 'httpOnly': False, 'name': 'TIEBAUID', 'path': '/',
     'secure': False, 'value': '4744b33b6c637a5b3e205323'},
    {'domain': '.tieba.baidu.com', 'expiry': 1609430399.905504, 'httpOnly': False, 'name': 'TIEBA_USERTYPE',
     'path': '/', 'secure': False, 'value': 'f986682cd5dcf50afc7f2e6b'},
    {'domain': '.baidu.com', 'expiry': 1616145084.659632, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/',
     'secure': False, 'value': 'F0E854C5146E3AFA2956E528D83DF3AC:FG=1'},
    {'domain': '.baidu.com', 'expiry': 1843809083.768725, 'httpOnly': True, 'name': 'BDUSS', 'path': '/',
     'secure': False,
     'value': 'czdTdjT1U0RGFUYTZDUU1FUnMzbTdwZHpmaTRZcGtQMFV5OHFyQ0hjZzd4SnBlSUFBQUFBJCQAAAAAAAAAAAEAAAAVn-cuY0hpTGxpbmfs4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADs3c147N3NeSG'},
    {'domain': '.tieba.baidu.com', 'expiry': 1616145086, 'httpOnly': False,
     'name': 'Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948', 'path': '/', 'secure': False, 'value': '1584609061'},
    {'domain': '.tieba.baidu.com', 'expiry': 1587201083.991077, 'httpOnly': True, 'name': 'STOKEN', 'path': '/',
     'secure': False, 'value': 'ace2820c0d4da1305057bda7b88ba1eb891574f2fa1d6e67ec8d3b70068789f4'}
];
url = "http://tieba.baidu.com/home/main?id=tb.1.c4478512.gC_66woPPBxHTCQqRCDTng?t=1577555214&fr=userbar&red_tag=e2980213665";
# opw = webdriver.Chrome();
# opw.get(url);
# time.sleep(20);
def get_sing_in_web():
    headers = {
        "Host":"tieba.baidu.com",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    cookie = "BIDUPSID=1D58066D67F301E4010ED11DD3D02D4E; PSTM=1575966931; BAIDUID=1D58066D67F301E44A045F42A0C2CCA0:FG=1; TIEBA_USERTYPE=8b7f763fc16554d19f1ffd56; bdshare_firstime=1576487506618;rpln_guide=1;H_WISE_SIDS=139560_100808_141277_140829_139403_138497_139811_135846_141000_128144_139148_138471_139096_141345_140142_133994_138878_137985_140173_131246_132551_137743_138165_107317_138883_140260_141211_141031_141368_141410_140632_140202_139297_136862_138585_139625_140113_136196_140591_140578_133847_140792_140065_131423_140972_136413_137756_110085_140327_127969_140269_141356_140593_140864_139887_139407_128195_138312_138426_141193_138943_139676_141191_140596_138755_140962;MCITY=-119%3A;TIEBAUID=4744b33b6c637a5b3e205323;BDUSS=dodlFxdGhsVGZVRGZwT1FXLWY2dWpiM1A4bWVBSy04RX5oVENza2hoSlV4cHBlSVFBQUFBJCQAAAAAAAAAAAEAAAAVn-cuY0hpTGxpbmfs4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFQ5c15UOXNeNW;STOKEN=cf94f57d6cd8db881ddfa675494eaf2744c27f6d9ee70218b6366da46b8aa6af;BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; wise_device=0; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1584616529,1584617069,1584617127,1584755385; st_key_id=17; 786931477_FRSVideoUploadTip=1; showCardBeforeSign=1; st_data=a1b6e0f05185bb535cf67fad7eb6d5b313b8c3e90809a327dfd975d77bf2548085680b0cbf0d542c8eb8c0af17f8d02e1ecb69fab6844c39de8ace789b76995837549678bd6de935c5b135548fc5a497792f7a0b0846c00a0bb3ee74bb6a1a1bf56fc71d2550fffd1fe23661f8484d39027e2118736ea42509647e63436994b3; st_sign=15060e82; H_PS_PSSID=30962_1463_31119_21089_30903_30824_31086; delPer=0; PSINO=7; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1584761141";
    cookie_dict = {i.split("=")[0]:i.split("=")[-1] for i in cookie.split(";")};
    # print(cookie_dict)
    resp = requests.get(url=url,headers=headers,cookies=cookie_dict);
    soup = BeautifulSoup(resp.text,"html.parser");
    div = soup.find("div",class_="tbui_panel_content");
    a = soup.select(".tbui_panel_content a");
    print(a)
    print(soup);

def login_web():
    '''
    获取cookie
    :return:cookies 
    '''
    # opt = webdriver.ChromeOptions();
    # driver = webdriver.Chrome(options=opt);
    # driver.get(url=url);
    # driver.find_element_by_class_name("u_login").click();
    # time.sleep(3);
    # driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click();
    # driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("18925800360");
    # driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("zxcv96548854");
    # driver.find_element_by_id("TANGRAM__PSP_10__memberPass").click();
    # driver.find_element_by_id("TANGRAM__PSP_10__submit").click();
    # time.sleep(60);
    # cookies = driver.get_cookies()


    driver = webdriver.Chrome();
    driver.get(url=url);
    for cookie in cookies:
        if "expiry" in cookie:
            del cookie["expiry"];
        driver.add_cookie(cookie_dict=cookie);
    driver.get(url=url);
    #一键签到
    # driver.find_element_by_class_name("onekey_btn").click();
    # driver.find_element_by_class_name("sign_btn_nonmember").click();

    # driver.find_element_by_css_selector("#forum_group_wrap>a").click();
    # driver.close();
if __name__ == "__main__":
    get_sing_in_web();

