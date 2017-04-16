import re
try:
	input=open("input.txt",mode="r")
	output=open("output.txt",mode="w")
	src=input.read()
	
	filter=r"^(?![^A-Z]*$|[^a-z]*$|[^0-9]*$|\w*$)((..)*.)$"
	#匹配包含大写字母、小写字母、数字和其它字符的长度为奇数的一行
	for it in re.finditer(filter, src, re.M):
		output.write(it.group()+'\n')
	
	input.close()
	output.close()
except:
	pass