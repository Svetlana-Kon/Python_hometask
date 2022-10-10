def log_info(info):
    with open('log.5-8.txt', 'a', encoding = 'utf-8') as l:
        if len(info.split()) == 1:
            l.write(f'экспорт - {info}' + '\n')
        else:
            l.write(f'импорт - {info}' + '\n')