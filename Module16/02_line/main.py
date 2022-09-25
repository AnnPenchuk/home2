height1=[]
for i in range(160,176,2):
    height1.append(i)
print('первая шеренга',height1)

height2=[]
for i in range(162,180,3):
    height2.append(i)
print('вторая шеренга',height2)

height1.extend(height2)
#print(height1)
list.sort(height1)
print(height1)
