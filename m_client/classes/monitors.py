# _*_coding:utf-8_*_
__author__ = 'yanjunhui'
import psutil


class Monitor():
    def cpu(self):  # 获取CPU使用百分比
        return psutil.cpu_percent(interval=1)

    def mem(self):
        _handle = lambda self: int(self) / 1024 / 1024  # 转换单位为MB
        _info = psutil.virtual_memory()
        total, available, percent, used, free = _info.total, _info.available, _info.percent, _info.used, _info.free
        return _handle(total), percent, _handle(used), _handle(free)

    def disk(self):
        _mount_dic = {}
        _handle = lambda self: int(self) / 1024 / 1024 / 1024  # 转换单位为GB
        _info = psutil.disk_partitions()  # 所有磁盘挂载信息
        for mount in _info:
            _par_name = mount.mountpoint
            self.vol_per = psutil.disk_usage(_par_name).percent  # 分区使用容量百分比
            self.vol_total = psutil.disk_usage(_par_name).total  # 分区总容量
            self.vol_used = psutil.disk_usage(_par_name).used  # 分区使用容量
            self.vol_free = psutil.disk_usage(_par_name).free  # 分区剩余容量
            self.vol_write_io = psutil.disk_io_counters(perdisk=True)
            _mount_dic[_par_name] = [mount.fstype, self.vol_per, _handle(self.vol_total), _handle(self.vol_used),
                                     _handle(self.vol_free)]
        return sorted(_mount_dic.items(), key=lambda d: d[0])

    def network(self):
        _eth_dic = {}
        _net_io = psutil.net_if_addrs()

        for eth_name, info in _net_io.items():
            print eth_name, info


if __name__ == '__main__':
    m = Monitor()
    print u'CPU使用率:%s%%' % m.cpu()

    print u'总内存:%s MB,占用百分比:%s%%,使用内存:%s MB,剩余内存:%s MB' % m.mem()

    for x in m.disk():
        print u'[%s]:分区格式:%s,使用百分比:%s%%,总容量:%sGB,使用容量:%sGB,剩余容量:%sGB' % (
            x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4])

    m.network()
