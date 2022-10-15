file_name=input('Введите назвние: ')
simbols=list('@№$%^&\*()')
if file_name.endswith('.txt') or file_name.endswith('.docx'):

   # for i in range(len(simbols)):
        if file_name[0] not in simbols:
            print('Файл назван верно: ', file_name)
        else:
            print('название начинается на один из специальных символов.')
            #break
else:
    print('неверное расширение файла. Ожидалось .txt или .docx.')