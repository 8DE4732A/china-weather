import sys
from pathlib import Path

p = Path(sys.path[0] + '/weather')
file_names = [x.name for x in p.iterdir()]
nums = sorted([x.split('.')[0] for x in file_names])

for i in range(len(nums)):
    Path(sys.path[0] + '/weather-ffmpeg/' + '{0:06d}'.format(i) + '.jpg').symlink_to(sys.path[0] + '/weather/' + nums[i] + '.jpg')
