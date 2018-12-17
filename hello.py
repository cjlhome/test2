# print('hello')
# print('world')

# if 5>1:
#     print('zhixing')
# else:
#     print('结束了！')

 # def t2(para):
 #    para = 3
 #    t2()
 #    b = 'a'
 #    t2(b)



# def t2 (para):
#     para [0] = 3
#     b = [1]
#     t2(b)

#
# getName('A old lady come in, the name is Mary, level 94454')



'''
请实现一个程序，实现如下需求点：

1.程序开始的时候提示用户输入学生年龄信息 格式如下：

Jack Green ,   21  ;  Mike Mos, 9;

我们假设 用户输入 上面的信息，必定会遵守下面的规则：
  学生信息之间用分号隔开（分号前后可能有不定数量的空格），
  每个学生信息里的 姓名和 年龄之间用 逗号隔开（逗号前后可能有不定数量的空格）
#-----------------------------------------------------------------
2. 程序随后将输入的学生信息分行显示，格式如下
Jack Green :   21;
Mike Mos   :   09;
学生的姓名要求左对齐，宽度为20， 年龄信息右对齐，宽度为2位，不足前面补零
'''


def stu_inf():
    stu_age = input('请输入学生年龄:')
    stu_inf = stu_age.spilt(';')
    stu_name = ['Jack Green','Mike Mos']
    for one in  stu_name :
     print(' {:20} : {:02}'.format('stu_name','stu_age'))











#----------------------------------
'''
1.下面的log变量记录了云服务器上 当天上传的文件信息
其中第一列是文件名，第二列是文件大小

请编写一个程序，统计出不同类型的 文件的大小总和
比如：
jpeg  9988999
json   324324
png   2423233


1、首先统计文件的所有类型
2、将同一个类型文件的大小相
'''

# def file_inf(file_type, file_length):
#     for one in filelengthinf:
#         if one[0] == file_type:
#             one[1] += file_length
#             return



#------99乘法表

# for i in range(1,10):
#     for j in

# srcStr = 'the name is Mary, '
# # def getName(srcStr):
# #     ret = srcStr.split('the name is')[1].split(',')[0]
# #
# #     print(ret)
# #
# # getName(srcStr)

# def mySort(inList):
# newList = [8,2,3,6,0]
# 
#     while len(inList) > 0:
#        # ---------------重点部分不会写啦！--------
# 
#         inList.pop(curMin)
#         newList.append(theMin)
# 
#    return newList
# 
# print (sort([8,2,3,6,0]))



# inFileName = 'file1.txt'
# outFileName = 'file2.txt'
#
# with open(inFileName) as ifile, open(outFileName, 'w') as ofile:
#     beforeTax = ifile.read().splitlines()
#     # or we could use   beforeTax = ifile.read().split('\n')
#     for one in beforeTax:
#         if one.count(';') != 1:  # ensure valid
#             continue
#
#         namePart, salaryPart = one.split(';')
#         # name Part like  name: Jack  |  salaryPart like    salary:  12000]
#
#         if namePart.count(':') != 1:  # ensure valid
#             continue
#         if salaryPart.count(':') != 1:  # ensure valid
#             continue
#
#         name = namePart.split(':')[1].strip()
#         salary = int(salaryPart.split(':')[1].strip())
#
#         income = int(salary * 0.9)
#         tax = int(salary * 0.1)
#
#         outPutStr = 'name: {:10}   ;    salary:  {:6} ;  tax: {:6} ; income:  {:6}'.format(name, salary, tax, income)
#
#         print
#         outPutStr
#
#         ofile.write(outPutStr + '\n')







# FileName = 'file1.txt'
# FileName2 = 'file2.txt'
#
# beforeTax = ifile.read().splitlines()
#
#     for one in beforeTax:
#
#        # ---------这里的嵌套写不出来啦--------
#        name = nameout.split(':')[1].strip()
#         salary = int(salaryPart.split(':')[1].strip())
#
#         income = int(salary * 0.9)
#         tax = int(salary * 0.1)
#
#         Str1 = 'name: {:10}   ;    salary:  {:6} ;  tax: {:6} ; income:  {:6}'.format(name, salary, tax, income)
#
#         print(str1)
#
#


print