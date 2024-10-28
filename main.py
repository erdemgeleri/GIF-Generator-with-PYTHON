import imageio.v3 as iio

file_names = ["badge_earth.png","badge_fork.png","badge_loop.png","badge_modules.png"]
images = []
for file_name in file_names:
    images.append(iio.imread(file_name))
iio.imwrite("badge-icon.gif",images,duration=500,loop=0)