# import os
# from os import path
# print(os.path.abspath('..'))
# print(os.path.exists('C:/Users/Administrator/PycharmProjects/test2Project.org/test'))
# print(os.path.isfile('C:/Users/Administrator/PycharmProjects/test2Project.org/test/file_test/file_test.py'))
# print(os.path.isdir('C:/Users/Administrator/PycharmProjects/test2Project.org/test/file_test'))
# print(os.path.join('C:/Users/Administrator/', 'PycharmProjects1', 'test2Project.org', 'test', 'file_test'))


from pathlib import Path
# p = Path('..')
# dir = [x for x in p.iterdir() if x.is_dir()]
# print(dir)
# file = [x for x in p.iterdir() if x.is_file()]
# print(file)

q = Path('C:/Users/Administrator/PycharmProjects/test2Project.org/test/123')
# Path.mkdir(q,parents=True)  # parents设置为True，会自动创建不存在的目录
Path.rmdir(q)
# print(p.resolve())
# print(p.is_dir())
