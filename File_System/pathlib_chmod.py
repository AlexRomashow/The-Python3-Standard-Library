import os
import pathlib
import stat

# Создание исходного тестового файла
f = pathlib.Path('pathlib_chmod_example.txt')
if f.exists():
    f.unlink()
f.write_text('contents')

# Определение уже установленных разрешений c помощью модуля stat
existing_permissions = stat.S_IMODE(f.stat().st_mode)
print('Before: {:o}'.format(existing_permissions))

# Определение способа изменения разрешений
if not (existing_permissions & os.X_OK):
    print('Adding execute permission')
    new_permissions = existing_permissions | stat.S_IXUSR
else:
    print('Removing execute permission')
    # Использовать оператор xor для снятия бита, предоставляющего
    # пользователю право на выполнение файла
    new_permissions = existing_permissions ^ stat.S_IXUSR

# Внести изменение и отобразить новое значение режима
f.chmod(new_permissions)
after_permissions = stat.S_IMODE(f.stat().st_mode)
print('After: {:o}'.format(after_permissions))
