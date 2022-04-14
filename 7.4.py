# import os
# from collections import defaultdict
# from os.path import relpath
# import django
# root_dir = django.__path__[0]
# django_files = defaultdict(list)
# for root, dirs, files in os.walk(root_dir):
    # for file in files:
        # ext = file.rsplit('.', maxsplit=1)[-1].lower()
        # rel_path = relpath(os.path.join(root, file), root_dir)
        # django_files[ext].append(rel_path)
# for ext, files in sorted(django_files.items(),
                        # key=lambda x: len(x[1]), reverse=True):
    # print(f'{ext}: {len(files)}')

# print('\nPY FILES')
# print(*sorted(django_files['py'])[:10], sep='\n')


import os

list_file = []

for root, dirs, files in os.walk('./'):
    for file in files:
        ext = os.path.join(root, file)
        list_file.append(os.stat(ext).st_size)
max_file = max(list_file)

""" как дальше я не знаю((( """
i = 1
dict_1 = {}

for _ in range(len(str(max_file))):
    i *= 10
    dict_1[i] = 0

for file in list_file:
    dict_1[10 ** len(str(max_file))] += 1

print(dict_1)