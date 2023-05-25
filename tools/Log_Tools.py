# ----------------------------------------
#              创建姓名：十元        
#              创建时间：2021/2/17 下午3:44
#              更新时间：
# 功能实现：
#   1： 以new的形式实现日志收集打印
#   2：日志切割(时间切割，大小切割)，使用配置控制
#   3：参数化输入输出等级

# ---------------------------------------
import logging
from tools.File_Path import LOG_PATH
import logging.handlers
from tools.Config_Tools import Config_Tools


class Log_new(object):
    def __new__(cls, *args, **kwargs):
        # -------------------------------------------------
        # 创建日志收集器
        # 收集器等级取配置信息
        level = Config_Tools().get('Log', 'Log_collector')
        # 创建一个my_log日志收集器
        new_log = logging.getLogger('my_log')
        # 等级为cinf.ini中的配置的等级
        new_log.setLevel(level)

        # ---------------------------------------------
        # 设置日志输出格式
        Foarmat = '%(asctime)s--> %(levelname)s: --> %(filename)s: %(lineno)s -->%(message)s'
        Foarmater = logging.Formatter(Foarmat)

        # -------------------------------------------------
        # 创建一个输出到控制台的输出器
        new_stream_out = logging.StreamHandler()
        # 输出等级
        level_stream_outlevel = Config_Tools().get('Log', 'log_stream_out')
        new_stream_out.setLevel(level_stream_outlevel)
        # 添加输出格式
        new_stream_out.setFormatter(Foarmater)
        # 统一再最后关联收集器

        # -------------------------------------------------
        # 创建一个输出到文件的的输出器
        new_file_out = logging.FileHandler(LOG_PATH, encoding='utf8')
        # 输出等级
        level_file_out = Config_Tools().get('Log', 'Log_out_file')
        new_file_out.setLevel(level_file_out)
        # 输出格式
        new_file_out.setFormatter(Foarmater)
        # 统一再最后关联收集器

        # -------------------------------------------------
        # 创建一个输出到文件的的输出器（大小切割）
        # 切割大小从配置中获取
        size = int(Config_Tools().get('Log', 'size'))
        number = int(Config_Tools().get('Log', 'size'))
        new_size_file_out = logging.handlers.RotatingFileHandler(LOG_PATH, maxBytes=size,
                                                                 backupCount=number,
                                                                 encoding='utf8')
        # 输出等级
        new_size_file_out.setLevel(level_file_out)
        # 输出格式
        new_size_file_out.setFormatter(Foarmater)
        # 统一再最后关联收集器

        # -------------------------------------------------
        # 创建一个输出到文件的的输出器（大小切割）
        when = Config_Tools().get('Log', 'when')
        interval = int(Config_Tools().get('Log', 'interval'))
        new_time_file_out = logging.handlers.TimedRotatingFileHandler(LOG_PATH, when=when,
                                                                      interval=interval,
                                                                      backupCount=number,
                                                                      encoding='utf8')
        # 设置等级
        new_time_file_out.setLevel(level_file_out)
        # 输出格式
        new_time_file_out.setFormatter(Foarmater)
        # 统一再最后关联收集器

        # -------------------------------------------------
        # 输出到控制台关联收集器
        new_log.addHandler(new_stream_out)
        if Config_Tools().get('Log', 'mode') == '不切割':
            new_log.addHandler(new_file_out)
        elif Config_Tools().get('Log', 'mode') == '时间切割':
            new_log.addHandler(new_time_file_out)
        elif Config_Tools().get('Log', 'mode') == '大小切割':
            new_log.addHandler(new_size_file_out)
        else:
            print("/api_test/config/conf.ini 中配置的mode有问题，无法打印日志到文件中"
                  "请严格按照提示配置：（不切割，时间切割，大小切割）")

        return new_log


mylog = Log_new()

if __name__ == '__main__':
    i = 0
    while True:
        mylog.debug('我是debug')
        mylog.info('我是info')
        mylog.warning('我是warning')
        mylog.error('我是error')
        mylog.critical('我是critical')
