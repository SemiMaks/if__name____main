# При непосредственном обращении получим надпись No module
# При импорте модуля получим надпись Runnihg where....

if __name__ == '__main__':
    print('No module')
else:
    print('Running where imported a module')
