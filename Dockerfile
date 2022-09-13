FROM python:3.8

WORKDIR /root/project

COPY . ./

RUN pip install -r /root/project/requirements.txt -i https://mirrors.aliyun.com/pypi/simple
# RUN nohup python -u /root/project/gcc_class2/manage.py runserver 0.0.0.0:8000 > gcc_test.log 2>&1 &

# CMD ["nohup", "python", -"u", "/root/project/gcc_class2/manage.py" "runserver", "0.0.0.0:8000", ">", "gcc_test.log", "2>&1", "&"]
CMD [ "python", "/root/project/gcc_class2/manage.py", "runserver", "0.0.0.0:8000"]
