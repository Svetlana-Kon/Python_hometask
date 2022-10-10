def log_info(info):
    with open('dz_log.5-7.csv', 'a', encoding = 'utf-8') as l:
        if len(info.split()) == 1:
            l.write(f'экспорт - {info}' + '\n')
        else:
            l.write(f'импорт - {info}' + '\n')