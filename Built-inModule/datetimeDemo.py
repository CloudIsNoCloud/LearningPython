'datetime是Python处理日期和时间的标准库。'

from datetime import datetime

# 打印现在的时间
print('现在时间：%s' % datetime.now())

# 打印一个指定的时间
print('指定时间：%s' % datetime(1999, 9, 9, 9, 9, 9, 9))

# timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。
t = 1234567890.0
# 本地时间
print('本地时间：%s' % datetime.fromtimestamp(t))
# UTC时间
print('UTC时间：%s' % datetime.utcfromtimestamp(t))

# 字符串转时间
print('字符串转时间：%s' % datetime.strptime('1999-9-9 9:9:9', '%Y-%m-%d %H:%M:%S'))

# 时间转字符串
print('时间转字符串：%s' % datetime.now().strftime('%a, %b %d %H:%M'))

# datetime加减，加减可以直接用+和-运算符，不过需要导入timedelta这个类
from datetime import timedelta
print(datetime.now() + timedelta(days=1, hours=1))

# 本地时间转UTC
from datetime import timezone
print("本地时间转UTC：%s" % datetime.now().replace(
    tzinfo=timezone(timedelta(hours=8))))

# 通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
# 通过astimezone()方法，可以转换到任意时区
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('用UTC时间算出来的 +10:00 ：%s' %
      utc_dt.astimezone(timezone(timedelta(hours=10))))

# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str
# 请编写一个函数将其转换为timestamp
import re


def to_timestamp(dt_str, tz_str):
    tz_int = int(re.match(r'^UTC([+-]\d+)\:\d{2}$', tz_str).group(1))
    dt_time = datetime.strptime(
        dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone(timedelta(hours=tz_int)))
    return dt_time.timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2
print('ok')
