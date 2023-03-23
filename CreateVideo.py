import 'os':
import 'cv2':
Images = []

if ext in ['.gif, .png, .jpeg, .jpg, .jfif']:
    file_name = path+"/"+file

print(file_name)

size = (width, height)

out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

cv2.imread()

out.write()