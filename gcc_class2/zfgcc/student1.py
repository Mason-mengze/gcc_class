
# from zfgcc.zfnew import GetInfo, Login
from zfnew import GetInfo, Login

from lxml import etree

class Student:
    def __init__(self):
        '''初始化'''
        self.base_url = "http://jwxw.gzcc.cn"


    def login(self,account,passwd):
        '''登录'''
        lgn = Login(base_url=self.base_url)
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
            cookies = False
            return (Status, cookies)

        except:
            cookies = lgn.cookies  # cookiejar类cookies获取方法
            Status = 200
            return (Status, cookies)


    def schedule(self,cookies, year, term):
        '''获取课表'''
        person = GetInfo(base_url=self.base_url, cookies=cookies)
        schedule = person.get_schedule(year, term)  # 2019年、第1学期(1 or 2)
        return schedule
    def studen_info(self,cookies):
        person = GetInfo(base_url=self.base_url, cookies=cookies)
        info = person.get_pinfo()
        return info





if __name__ == '__main__':
    student = Student()
    Status, student_cookies = student.login("201912340022", "Mz1258012581")
    if Status == 200:
        # course = student.schedule(student_cookies, "2021", "1")
        course = student.studen_info(student_cookies)

        print(course)
    elif Status == 404:
        print("用户名或密码不正确")
    elif Status == 500:
        print("内部其他错误")


# 获取课程表例子

    # from zfnew import GetInfo, Login

    # base_url = 'http://jwxw.gzcc.cn'

    # lgn = Login(base_url=base_url)
    # lgn.login('201912340022', 'Mz1258012581')
    # cookies = lgn.cookies  # cookies获取方法
    # person = GetInfo(base_url=base_url, cookies=cookies)
    # schedule = person.get_schedule('2022', '1')  # 2019年、第1学期(1 or 2)
    # print(schedule)