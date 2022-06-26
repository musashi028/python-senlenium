from xpinyin import Pinyin

# 实例拼音转换对象
p = Pinyin()
arr = (
    '张三','李四')
for tp in arr:
    ret = p.get_pinyin(tp, "")
    print(tp + " " + ret + '\n')
# 进行拼音转换
