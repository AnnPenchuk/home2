file_name=input('Введите назвние: ')
simbols=list('@№$%^&\*()')
if file_name.endswith('.txt') or file_name.endswith('.docx'):
    #print('Файл назван верно: ',file_name)
    for i in range(len(simbols)):
        if not file_name.startswith(simbols[i]):
            print('Файл назван верно: ', file_name)
        else:
            print('название начинается на один из специальных символов.')
            break
else:
    print('неверное расширение файла. Ожидалось .txt или .docx.')