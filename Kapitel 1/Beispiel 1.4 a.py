import numpy as np

gl= np.array([[2,4,2,60],
              [7,6,2,122],
              [12,22,11,342]], dtype=np.float64)  
print(gl)

# dimension
print(gl.shape)
print(gl.shape[0])  # number of rows
print(gl.shape[1])  # number of columns


# elements
print(gl[1,3])

# Gaussian elimination
# Spalte 0
# for row in range(1, 3):
#     factor = gl[row,0]/gl[0,0]
#     for col in range(0, 4):
#         gl[row,col]= gl[row,col] - factor * gl[0,col]

for row in range(1, 3):
    factor = gl[row,0]/gl[0,0]
    gl[row,:] = gl[row,:] - factor * gl[0,:]
print(gl)

for row in range(2, 3):
    factor = gl[row,1]/gl[1,1]
    gl[row,:] = gl[row,:] - factor * gl[1,:]


gl[2,:]= gl[2,:]/gl[2,2]
gl[1,:]= gl[1,:] - (gl[1,2]/gl[2,2]) * gl[2,:]
gl[0,:]= gl[0,:] - (gl[0,2]/gl[2,2]) * gl[2,:]

gl[1,:]=gl[1,:]/ gl[1,1]
gl[0,:]=gl[0,:] - (gl[0,1]/gl[1,1]) * gl[1,:]
gl[0,:]=gl[0,:]/ gl[0,0]

print(gl)


# gl[1,:] = gl[1,:] - factor * gl[0,:]
# print(gl)  

# gl[1,:] = gl[1,:] - (gl[1,0]/gl[0,0]) * gl[0,:]
# print(gl)   

# a = np.arange(15).reshape(3, 5)
# print(a)

# print(a.shape)

# list2 = [1,2,3]
# vector2 = np.array(list2)
# print(vector2)

# list3 = [2,3,4]
# vector3 = np.array(list3)

# # Scalar multiplication
# print(vector2*3)

# # Dot product
# print(vector2.dot(vector3))

# list4 =[[2],[4],[6]]
# vector4=np.array(list4)
# # 1 2
# # 2 3
# # 3 4
# print(np.cross(vector2, vector3))
