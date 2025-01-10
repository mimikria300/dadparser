path = input('enter path to ini')

stuff_container = []
f = open(path)

profilers = {}
profiler_index = []

#reader
line = f.readline()
while line!='':
    elem = {}
    elem['stuff'] = ''
    while line != '\n' and line!='':
        if line[0]=='[':
            if line[1:8]=='Profile':
                num = int(line.strip()[1:-1].replace('Profile',''))
                isProfile = True
                profilers[num] = {}
                profiler_index.append(num)
            else: 
                isProfiler = False
                stuff = line
        elif isProfiler:
            param,param_c = line.split('=')
            profilers[num][param] = param_c
        else:
            stuff += line
        line = f.readline()
    if not isProfiler:
        stuff_container.append(stuff)
    line = f.readline()

profiler_index.sort()
#тут функции перестановок/удаления (или не мучиться, хз)
#тут какой-то вайл, который жрет из консоли команды перестановок/удаления


#writer
new_f = open('new'+path,'w')
#надо stuff и профайлеры загнать прост, порядок относительно изначального файла не сохраняем

new_f.close()
f.close()
            


