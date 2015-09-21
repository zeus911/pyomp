# _*_coding:utf-8_*_
__author__ = 'yanjunhui'
import sys

sys.path.append('classes')
from credis import CRedis

if __name__ == '__main__':
    time_out = 30
    while True:
        choose = raw_input('1.查看当前CPU使用率     2.查看当前内存使用率\n选择你要的操作:').strip()
        if choose not in ['1', '2']:
            print '重新输入合法的数值'
            continue
        if choose == '1':
            try:
                r = CRedis()
                r.lpush(redis_key, redis_value)
            except Exception, e:
                print '检查redis连接！'
                break
