test = [{'domain': '.tieba.baidu.com', 'httpOnly': False, 'name': 'Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948', 'path': '/', 'secure': False, 'value': '1584609086'}, {'domain': '.tieba.baidu.com', 'expiry': 1609430399.72359, 'httpOnly': False, 'name': 'TIEBAUID', 'path': '/', 'secure': False, 'value': '4744b33b6c637a5b3e205323'}, {'domain': '.tieba.baidu.com', 'expiry': 1609430399.905504, 'httpOnly': False, 'name': 'TIEBA_USERTYPE', 'path': '/', 'secure': False, 'value': 'f986682cd5dcf50afc7f2e6b'}, {'domain': '.baidu.com', 'expiry': 1616145084.659632, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': 'F0E854C5146E3AFA2956E528D83DF3AC:FG=1'}, {'domain': '.baidu.com', 'expiry': 1843809083.768725, 'httpOnly': True, 'name': 'BDUSS', 'path': '/', 'secure': False, 'value': 'czdTdjT1U0RGFUYTZDUU1FUnMzbTdwZHpmaTRZcGtQMFV5OHFyQ0hjZzd4SnBlSUFBQUFBJCQAAAAAAAAAAAEAAAAVn-cuY0hpTGxpbmfs4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADs3c147N3NeSG'}, {'domain': '.tieba.baidu.com', 'expiry': 1616145086, 'httpOnly': False, 'name': 'Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948', 'path': '/', 'secure': False, 'value': '1584609061'}, {'domain': '.tieba.baidu.com', 'expiry': 1587201083.991077, 'httpOnly': True, 'name': 'STOKEN', 'path': '/', 'secure': False, 'value': 'ace2820c0d4da1305057bda7b88ba1eb891574f2fa1d6e67ec8d3b70068789f4'}];
test2 = "a=b;c=d;e=f;";
test_dict = {};
for i in test2.split(";"):
    print(i)
    a = i.split("=")[0];
    b = i.split("=")[-1];
    test_dict[a] = b;
# test_dict = {i.split("=")[0]:i.split("=")[-1] for i in test2.split(";")};
print(test_dict)
