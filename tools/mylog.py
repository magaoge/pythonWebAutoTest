# -*- coding: utf-8 -*-
# @Time    : 2021/12/20 11:01 上午
# @Author  : Alen
# @Email   : 16621710374@163.com
# @File    : mylog.py
# @Software: PyCharm
import logging #相当于java中的log4j

from tools.path_maneger import test_log_path

logging.shutdown()


class MyLog():

    @staticmethod
    def mylog(msg,leave):

        # 日志级别，从小到大
        # debug<info<warning<error<critical

        # 1.定义一个日志收集器,如果不给参数，默认日志名称为root
        my_logger = logging.getLogger("pyWebAuntoTest")
        # 2.设定日志收集的级别，默认收集级别为warning,日志收集器只能收集到warning及warning级别以上的日志信息
        my_logger.setLevel(leave)

        # 3.创建一个日志的输出渠道，即日志输出到哪里
        # ch = logging.StreamHandler()
        # FileHandler默认是追加模式
        fh = logging.FileHandler(test_log_path,encoding="utf-8")


        # 设置输出的格式
        formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s")

        fh.setFormatter(formatter)

        # 5.两者对接，指定输出渠道
        # my_logger.addHandler(ch)#可去除

        my_logger.addHandler(fh)

        # 4.设定日志的输出级别，默认输出级别为warning
        # ch.setLevel(leave)

        fh.setLevel(leave)

        # 6.收集日志
        if leave == "DEBUG":
            my_logger.debug(msg)
        elif leave == "INFO":
            my_logger.info(msg)
        elif leave == "WARNING":
            my_logger.warning(msg)
        elif leave == "ERROR" :
            my_logger.error(msg)
        elif leave == "CRITICAL":
            my_logger.critical(msg)


        # 关闭日志输出渠道，不然可能会产生日志重复
        # my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    @staticmethod
    def debug(msg):
        MyLog.mylog(msg,"DEBUG")

    @staticmethod
    def info(msg):
        MyLog.mylog(msg,"INFO")

    @staticmethod
    def warning(msg):
        MyLog.mylog(msg,"WARNING")

    @staticmethod
    def error(msg, *args, **kwargs):
        MyLog.mylog(msg,"ERROR")

    @staticmethod
    def critical(msg):
        MyLog.mylog(msg,"CRITICAL")

    # 抄源码的，这里类似是记录一个相当于error级别的日志
    @staticmethod
    def exception(msg, *args, exc_info=True, **kwargs):
        """
        Log a message with severity 'ERROR' on the root logger, with exception
        information. If the logger has no handlers, basicConfig() is called to add
        a console handler with a pre-defined format.
        """
        MyLog.error(msg, exc_info=exc_info)

# if __name__ == '__main__':
#     MyLog.exception("控制台保留输出")
#     MyLog.info("我是info级别日志==========")
#     MyLog.debug("我是debug级别日志")