import os

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['D:\\Books']

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'E:\\Backup\\Backup.rar'

# 3. Команда для создания rar-архива и помещения в него данных
rar_command = 'rar a -ag -m5 -r {0} {1}'.format(target_dir, source)

if os.system(rar_command) == 0:
    print('Резервная копия успешно создана в', target_dir)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
