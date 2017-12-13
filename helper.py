import numpy as np
import cv2


def keypoints2numpyarray(kp):
    nb_points_ref=len(kp)
    points_ref=np.zeros((nb_points_ref,2),dtype=np.float)
    for i in range(0,nb_points_ref):
        points_ref[i,:]=kp[i].pt
    return points_ref


def drawMatches(train_img, train_kp, query_img, query_kp, matches,downsampling=2):
    # Create a new output image that concatenates the two images together
    rows1 = int(train_img.shape[0]/downsampling)
    cols1 = int(train_img.shape[1]/downsampling)
    rows2 = int(query_img.shape[0]/downsampling)
    cols2 = int(query_img.shape[1]/downsampling)
    out = np.zeros((max([rows1,rows2]),cols1+cols2,3), dtype='uint8')

    # Place the first image to the left
    tmp_train_img=train_img[::downsampling,::downsampling,:]
    out[:rows1,:cols1] = tmp_train_img

    # Place the next image to the right of it
    tmp_query_img=query_img[::downsampling,::downsampling,:]
    out[:rows2,cols1:] = tmp_query_img

    # For each pair of points we have between both images
    # draw circles, then connect a line between them
    for mat in matches:
        # Get the matching keypoints for each of the images
        train_img_idx = mat.trainIdx
        query_img_idx = mat.queryIdx
        (x1,y1) = train_kp[train_img_idx].pt
        (x2,y2) = query_kp[query_img_idx].pt
        x1=x1/downsampling;x2=x2/downsampling;y1=y1/downsampling;y2=y2/downsampling

        # Draw a small circle at both co-ordinates
        cv2.circle(out, (int(x1),int(y1)), 4, (255, 0, 0), 1)   
        cv2.circle(out, (int(x2)+int(cols1),int(y2)), 4, (255, 0, 0), 1)

        # Draw a line in between the two points
        cv2.line(out, (int(x1),int(y1)), (int(x2)+int(cols1),int(y2)), (255, 0, 0), 1)

    return out


def create_K():

    K = np.zeros((3 ,3))
    K[0] = [790.47, 0, 480]
    K[1] = [0, 793.54, 270]
    K[2] = [0, 0, 1]

    return K


def create_K_prof(width, height, dX, dY, dZ, dx, dy):
    x_0 = width/2.0
    y_0 = height/2.0
    alpha_x = dx*dZ/dX
    alpha_y = dy*dZ/dY

    K = np.zeros((3,3))
    K[0,0] = alpha_x
    K[1,1] = alpha_y
    K[0,2] = x_0
    K[1,2] = y_0
    K[2,2] = 1

    return K


