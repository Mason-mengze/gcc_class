
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from gcc_app.models import UsersAccountInfo, UsersInfo, Schedule
from django.http import JsonResponse
from zfgcc import student
import datetime


# Create your views here.

def index(request):
    # print(request.method)
    return HttpResponse("欢迎使用")

@csrf_exempt
def login(request):
    global cookies

    if request.method == "POST":
        studentid = request.POST.get("studentid")
        passwd = request.POST.get("passwd")
        user_object  = UsersAccountInfo.objects.filter(studentid = studentid, passwd = passwd).first()
        usersinfo_filter= UsersInfo.objects.filter(users=user_object).first()
        '''
        当在用户查询数据库查不到时，可能已在教务系统改密码
        此时我们需尝试登录教务系统，如果可以就更新密码
        '''
        # 当数据库没有记录时
        if not user_object:
            # 登教务系统
            status_login, cookies=student.login(studentid, passwd)
            # print(user_object)
            # 登录教务系统失败时
            if status_login != 200:
                return HttpResponse("用户名或密码错误")

            '''
            登录教务系统成功时，账户与数据库中不匹配有一下两种原因
            1、用户为新用户
            2、用户已在教务系统修改了密码
            '''
            # 先查询学号如果存为空即为新用户， 在数据库中存储账号信息
            user_studentid = UsersAccountInfo.objects.filter(studentid = studentid)     # 查询数据库中的学号
            if not user_studentid:      # 如果数据库中没有这个学号
                UsersAccountInfo.objects.create(studentid = studentid, passwd = passwd) # 将账号与密码写入数据库
                
                today = datetime.datetime.today()
                year = today.year
                month = today.month
                if month > 8 and month < 2: # 当月份在这个区间内就是第二学期
                    term = 2
                else:term = 1

                # 下面两行用于测试
                year = 2021
                term = 2

                status_schedule,schedule =student.schedule(cookies, year, term) # 读取当前学期的课表
                if status_schedule !=200:
                    return JsonResponse ({"message":"数据库课表为空"})
                # print(schedule['normalCourse'])
                # print(type(schedule['normalCourse']))
                user_studentid = UsersAccountInfo.objects.filter(studentid = studentid).first()     # 查询数据库中的学号
                course_list_info = []
                for course in schedule['normalCourse']:
                    detail = Schedule(coursetitle=course["courseTitle"], \
                                    schoolyear=schedule['schoolYear'], \
                                    schoolterm=schedule['schoolTerm'], \
                                    teacher=course["teacher"], \
                                    courseid=course["courseId"],\
                                    coursesection=course["courseSection"], \
                                    courseweek=course["courseWeek"], \
                                    campus=course["campus"], \
                                    courseroom=course["courseRoom"], \
                                    classname=course["className"], \
                                    hourscomposition=course["hoursComposition"], \
                                    weeklyhours=course["weeklyHours"], \
                                    totalhours=course["totalHours"], \
                                    credit=course["credit"],
                                    users=user_studentid)
                    course_list_info.append(detail)
                    
                Schedule.objects.bulk_create(course_list_info)   # 批量存储到数据库

                # 获取学生信息
                status_info, student_info = student.studen_info(cookies)
                if status_info !=200:
                    return JsonResponse ({"message":"获取信息失败"})
                # print(student_info)
                # 将用户信息写入数据库
                UsersInfo.objects.create(name = student_info['name'], \
                                        studentid = student_info['studentId'], \
                                        brithday=student_info['brithday'], \
                                        idnumber=student_info['idNumber'], \
                                        candidatenumber= student_info['candidateNumber'],\
                                        status=student_info['status'],\
                                        collegename=student_info['collegeName'], \
                                        majorname= student_info['majorName'], \
                                        classname=student_info['className'], \
                                        entrydate=student_info['entryDate'], \
                                        domicile=student_info['domicile'], \
                                        politicalstatus=student_info['politicalStatus'], \
                                        national=student_info['national'], \
                                        education=student_info['education'], \
                                        users=user_studentid)
            else:
            # 查询到学号信息，更新密码
                UsersAccountInfo.objects.filter(studentid = studentid).update(passwd=passwd)

            user_object  = UsersAccountInfo.objects.filter(studentid = studentid, passwd = passwd).first()  # 重新获取user_object
            usersinfo_filter= UsersInfo.objects.filter(users=user_object).first()

        request.session["info"] = {"id": user_object.id, "studentid": user_object.studentid, "name":usersinfo_filter.name}
        # print(request.session.get("info"))
        return JsonResponse ({"message":"登录成功"})

def get_schedule(request):
    '''
    检查用户是否已经登录
    已登录可以往下走
    未登录重定向/或提示登录
    '''
    # 登陆检查已在auth.py中使用中间件实现
    login_info = request.session.get("info")
    schoolyear = request.GET.get("schoolyear")
    schoolterm = request.GET.get("schoolterm")
    user_filter = UsersAccountInfo.objects.filter(studentid = login_info['studentid']).first()

    # 下面是检测session中的键值对，已在中间件middleware/auth.py中集成
    # if not user_filter:
    #     return JsonResponse({"message":"数据异常，请重新登录"})
    
    # 筛选课程
    course_list = list(Schedule.objects.filter(schoolyear=schoolyear,\
                        schoolterm=schoolterm,users=user_filter).values_list("coursetitle", "courseroom", "coursesection"))


    # print(schoolyear, schoolterm)
    # print(course_list)
    return JsonResponse(course_list, safe=False)

def logout(request):
    '''
    注销
    '''
    request.session.clear()
    return JsonResponse({"message":"注销成功"})


