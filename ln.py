from pathlib import Path

p = Path('D:\weather')
file_names = [x.name for x in p.iterdir()]
nums = sorted([x.split('.')[0] for x in file_names])

for i in range(len(nums)):
    Path('D:\weather-ffmpeg\\' + '{0:06d}'.format(i) + '.jpg').symlink_to('D:\weather\\' + nums[i] + '.jpg')
