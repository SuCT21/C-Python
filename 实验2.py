#并非转载和翻译，方法非原创，添加了注释而已
#并非转载和翻译，方法非原创，添加了注释而已
#并非转载和翻译，方法非原创，添加了注释而已
str = "今天 sunck,is,a,good man! sunck is a nice man! sunck is a handsome man! sunck is a good man! sunck is a nice man! sunck is a great man! sunck is a noble man! sunck is a cool man!"
word = input("输入要统计的单词，回车结束\n") #输入字符串以外的单词会报错，因为下面字典中只把字符串中存在的单词作为key
list = str.split(" ") #以空格为分隔符，把字符串分割成单词列表
dict = {} #创建一个空字典
for key in list: #把list中的单词，作为字典中的key（在字典中key是唯一的），把遍历到key的次数，作为value；
    if dict.get(key) == None: #在字典中查找key，因为创建的是空字典，每个key第一次get结果都是None
        dict[key] = 1 #（key来自list，绝对是字符串中的单词）第一次遍历到key的时候，get结果是None，在空字典中创建该key的键值对，key：1；在后续的遍历过程中，如果再次遍历到这个key，get结果不是None了
    else:
        dict[key] += 1 #遍历到某个key，已经在字典里存在了，就把次数+1
print(dict[word]) #返回要统计的单词出现次数


