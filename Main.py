import helper as hp
import cv2

'''
REFERENCE IMAGE
width = 500
height = 500

dX = 155.0
dY = 105.0
dZ = 500.0

dx = 243.0
dy = 170.0
'''

K = hp.create_K()
print(K)


'''
TD2 --------------------------------------------------------------
'''

image = cv2.imread('reference_image.png')  # image au type np.array
tab = cv2.findChessboardCorners(image, (5,8))  # fonction openCV pour trouver les coins du damier
# print(tab[1])
corners = tab[1].reshape(-1,2)   # on prend uniquement les coordonées dans le résultat et on reformate
#print(corners)
cv2.drawChessboardCorners(image, (5,8), corners, tab[0])  # on ajoute les points dans l'image pour les dessiner

cv2.imshow('frame', image)
cv2.waitKey()
cv2.destroyAllWindows()

'''
-----------------------------------------------------------------
'''


