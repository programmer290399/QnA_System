data = open("data.txt",'r',encoding='utf-8').read().replace('\n',' ').replace('\t',' ')
print(type(data))