# Q4 Answer Template
data = input('숫자로 이루어진 문자열을 입력하세요. ')

result=[] # 식
result.append(data[0])
val=int(data[0]) # 연산결과

for i in range(1,len(data)):
    if int(data[i])==0 or int(data[i-1])==0: # 더하기하는 경우
        result.append('+')
        result.append(data[i])
        val=val+int(data[i])
        
    else: # 곱하기하는 경우
        result.append('*')
        result.append(data[i])
        val=val*int(data[i])
        

print(f"{''.join(result)} = {val}")
