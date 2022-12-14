import os
from cgai_path import CGAIPATH



# p = r'C:\PyOut\Test\test_hiero\v001\musk_%04d.exr'
p = r'C:\PyOut\Test\test_hiero\v001\musk_0001.exr'

cpath = CGAIPATH()

# 判断提供的路径是否为序列
result = cpath.isSequence(p)
print('isSequence:',result)  # ('C:\\PyOut\\Test\\test_hiero\\v001\\musk_', '%04d')

if result:
    filename = cpath.get_filename(p)
    print(filename)  # musk

# 获取文件序列
paths,missings = cpath.get_files(p,missing=True)
print('paths:',paths) # ['C:\\PyOut\\Test\\test_hiero\\v001\\musk_0001.exr',...,'C:\\PyOut\\Test\\test_hiero\\v001\\musk_0049.exr']
print()
print(missings)


a = r'C:\PyOut\Test\test_hiero\v001\musk_0001.exr'
# a = 'LYX10_SH0040_cmp_cp_v001.mov'
a = r'C:\PyOut\Test\test_hiero\v001\LYX10_SH0040_cmp_cp_v001.mov'
# 获取文件名称
filename = cpath.get_no_version_name(a)
print('filename:',filename)  # musk_0001



