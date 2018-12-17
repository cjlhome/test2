
def  putinfotodict(filename):
     dict = {}
     with open(filename) as  f:
        lines =  f.readlines().splitlines()#返回一个列表
        for line in lines:
            line = line.replace('(','').replace(')','').replace(',','').replace(':','')
            res = line.split(',')
            checkintime = res[0]
            lessonid = int(res[1])
            userid = int(res[2])
            dict1={'lessonid':lessonid,'checkintime':checkintime}
            if userid not in dict:
                dict[userid]=[]
                dict[userid].append(dict1)
                 return(dict)






