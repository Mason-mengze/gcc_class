# 自定义异常日志处理类
class Mylogpetion():
    def __init__(self):
        import traceback  # 回溯模块
        import logging  # 用于写日志的模块
        # logging的基本配置
        logging.basicConfig(
            filename='日志.txt',  # 当前文件写入位置
            format='%(asctime)s %(levelname)s \n %(message)s',  # 格式化存储的日志格式
            #             日期时间        级别           错误信息
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        #     写入日志
        logging.error(traceback.format_exc())
 
 
if __name__ == '__main__':
    

    Mylogpetion()  # 在异常处理的代码块中调用自定义异常类