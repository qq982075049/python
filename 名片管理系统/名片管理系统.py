print("="*50)
print("名i片管理系统 V0.1")
print("1.添加一个新的名片")
print("2.删除一个名片")
print("3.修改一个名片")
print("4.查询一个名片")
print("5.显示所有名片名片")
print("6.退出系统")
print("="*50)
print()

list = []
# ifo = {} 全局变量，注意和下面17行的局部变量去比较，list结果是完全不同的
while True:
		num = int(input("请输入操作对应的数字:"))
		 
		info = {}
		if num==1:
			new_name = input("请输入姓名:")
			new_age = input("请输入年龄:")
			new_addr = input("请输入地址:")
			info["name"] = new_name
			info["addr"] = new_addr
			info["age"] =  new_age
			list.append(info)
			print(list) 
		elif num==2:
			pass
		elif num==3:
			pass
		elif num==4:
			serch_name = input("请输入需要查询的名字:")
		#	for temp in list:
		#		if temp["name"]==serch_name:
		#			print("查到:%s"%temp["name"])
		#			flag = 1
		#			break
		#	if flag==0:
		#		print("查无此人")
		#此方法定义了一个变量来存储这个数值
			for temp in list:
				if temp["name"]==serch_name:
					print("查到:%s"%temp["name"])
					break
			else:
				print("查无此人")
		elif num==5:
			print("姓名\t 年龄\t 地址")
			for temp in list:
				print("%s\t %s\t %s"%(temp["name"],temp["age"],temp["addr"]))
		elif num==6:
			  break
		else:
			print("请重新输入操作对应的数字:")
# 1.字典添加元素之前一定要先定义
# 2.int类型转换如果不是数字程序会崩溃报错
# 3.定义列表和字典要放在循环上面，不然每次都会重新定义，之前存储的数据会消失
# 4.查询名字功能可以使用for...else结构
