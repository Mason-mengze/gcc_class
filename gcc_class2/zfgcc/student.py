
from zfgcc.zfnew import GetInfo, Login
# from zfnew import GetInfo, Login

from lxml import etree


base_url = "http://jwxw.gzcc.cn"
def login(account,passwd):
    '''登录'''
    lgn = Login(base_url)
    res_text = lgn.login(account, passwd).text
    html = etree.HTML(res_text)        # 序列化html
    try:
        # xpath_str = 'normalize-space(//*[@id="tips"]//text())'
        xpath_str = '//*[@id="tips"]//text()'
        tips = html.xpath(xpath_str)[1].strip()
        if "用户名或密码" in tips:
            # 404代表账号或密码错误
            Status =  404
        else:
            # 500代表内部错误
            Status =  500
        cookies = None
    except:
        cookies = lgn.cookies  # cookiejar类cookies获取方法
        Status = 200
    return (Status, cookies)
def schedule(cookies, year, term):
    '''获取课表'''
    try:
        person = GetInfo(base_url, cookies=cookies)
        schedule = person.get_schedule(str(year), str(term))  # 2019年、第1学期(1 or 2)
        Status = 200
    except:
        Status = 405
        schedule = None
    return (Status, schedule)

def studen_info(cookies):
    try:

        person = GetInfo(base_url=base_url, cookies=cookies)
        info = person.get_pinfo()
        Status = 200
    except:
        Status = 406
        info = None
    return (Status, info)



if __name__ == '__main__':
    # student = Student()
    Status, student_cookies = login("201912340022", "Mz1258012581")
    if Status == 200:
        course = schedule(student_cookies, "2021", "1")
        print(course)
    elif Status == 404:
        print("用户名或密码不正确")
    elif Status == 500:
        print("内部其他错误")

    # student = Student()
    # Status, student_cookies = student.login("201912340022", "Mz1258012581")
    # if Status == 200:
    #     course = student.schedule(student_cookies, "2021", "1")
    #     print(course)
    # elif Status == 404:
    #     print("用户名或密码不正确")
    # elif Status == 500:
    #     print("内部其他错误")


# 获取课程表例子

    # from zfnew import GetInfo, Login

    # base_url = 'http://jwxw.gzcc.cn'

    # lgn = Login(base_url=base_url)
    # lgn.login('201912340022', 'Mz1258012581')
    # cookies = lgn.cookies  # cookies获取方法
    # person = GetInfo(base_url=base_url, cookies=cookies)
    # schedule = person.get_schedule('2022', '1')  # 2019年、第1学期(1 or 2)
    # print(schedule)