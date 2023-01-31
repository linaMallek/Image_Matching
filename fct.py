import cv2
import numpy as np
from math import inf
import time
import random
from PIL import Image, ImageDraw, ImageFilter


img1 = cv2.imread("images/image072.png")
img2 = cv2.imread("images/image092.png")

# creer the new image 
img = np.zeros([img1.shape[0],img1.shape[1],3],dtype=np.uint8)
img.fill(0) # or img[:] = 255
cv2.imwrite("new_image.jpg",img)

img3= cv2.imread('new_image.jpg') 


# add borders
# oui on peut utiliser 32 c'est suffisant  
image_bordered = cv2.copyMakeBorder(src=img1,top=64, bottom=64, left=64, right=64, borderType=cv2.BORDER_CONSTANT)

# les images sont en gris 
grayImg1 = cv2.cvtColor(image_bordered , cv2.COLOR_BGR2GRAY)
grayImg2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
grayImg3= cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)


def MSE(bloc1, bloc2):
    block1, block2 = np.array(bloc1), np.array(bloc2)
    return np.square(np.subtract(block1, block2)).mean()


def recherchre_block():
    
    #refaire cela pour eviter 
    imgB1 = cv2.imread('images/image092.png')
    imgB2 = cv2.imread('images/image072.png')
    imgB3 = cv2.imread('images/new_image.png')

#les images sont en gris 
    grayImgB1 = cv2.cvtColor(imgB1, cv2.COLOR_BGR2GRAY)
    grayImgB2 = cv2.cvtColor(imgB2, cv2.COLOR_BGR2GRAY)
    file_coordonner=[]
    file_coordonner1=[]


    tps1 = time.time()
    for i in range (0,grayImgB1.shape[0]-16,16): #colonne with step 16 
     for j in range (0,grayImgB2.shape[1]-16,16): #ligne 
           block1 = grayImgB1[i:i + 16,j:j + 16]
           min1 = inf 
           for i1 in range (max(0,i-7),min(i+7,grayImgB1.shape[0]-16)):
              for  j1 in range (max(0,j-7),min(j+7,grayImgB1.shape[1]-16)):
                block2 = grayImgB2[i1:i1 + 16,j1:j1 + 16]

                new_MSE = MSE(block1, block2)
                if new_MSE  < min1:
                  min1 = new_MSE
                  x1=i1
                  x2=j1 
              
               
           
           if min1 > 50 : 
            print(min1)
            file_coordonner.append((x2,x1))
            file_coordonner1.append((j,i))
            imgB3[i:i+16, j:j+16]= imgB1[x1:x1+16, x2:x2+16]
           
    tps2 = time.time()

    print("le temps d'execution est"+ str(tps2 - tps1))   
    
    #dessiner les rectangle 
    for i in range (len(file_coordonner)) :
     cv2.rectangle(imgB2, (file_coordonner[i][0], file_coordonner[i][1]),
                      (file_coordonner[i][0]+16,file_coordonner[i][1]+16), (0, 0, 255), 2) 

     cv2.rectangle(imgB1, (file_coordonner1[i][0], file_coordonner1[i][1]),
                      (file_coordonner1[i][0]+16,file_coordonner1[i][1]+16), (0, 255, 0), 2) 

    #resize the window pop images 
    imSB2 = cv2.resize(imgB2, (960, 540))  
    imSB3 = cv2.resize(imgB3, (960, 540)) 
    imSB1 = cv2.resize(imgB1, (960, 540)) 

    cv2.imshow("imageB", imSB1)
    cv2.imshow("imageB2", imSB2)
    cv2.imshow("imageB3", imSB3)
    if cv2.waitKey(3) : print("Done")

def mse_blocks(block1,origin_x,origin_y,step):            
             
             #block de meme position 
             block2=grayImg1[origin_x:origin_x + 16,origin_y:origin_y + 16]
             min=MSE(block1, block2)
             (mse_x,mse_j)=(origin_x,origin_y)
             #blocken cote gauche  
             x1=origin_x
             x2=origin_y-step
            
             block3=grayImg1[x1:x1 + 16,x2:x2 + 16]
             new_mse=MSE(block1, block3)
             if min>new_mse:
                (mse_x,mse_j)=(x1,x2)
                min=new_mse
            #blocken cote gauche  en haut 
             x1_h=x1-step
             x2_h=x2
             
             block4=grayImg1[x1_h:x1_h + 16,x2_h:x2_h + 16]
             new_mse=MSE(block1, block4)
             if min>new_mse:
                (mse_x,mse_j)=(x1_h,x2_h)
                min=new_mse 
            #blocken cote gauche  en bas
             x1_b=x1+step
             x2_b=x2
           
             block5=grayImg1[x1_b:x1_b + 16,x2_b:x2_b + 16]
             new_mse=MSE(block1, block5)
             if min>new_mse:
                (mse_x,mse_j)=(x1_b,x2_b)
                min=new_mse    
            #block en haut de celui du milieu 
             x_milH=origin_x-step  
             j_milH=origin_y
            
             block6=grayImg1[x_milH:x_milH + 16,j_milH:j_milH+ 16]
             new_mse=MSE(block1, block6)
             if min>new_mse:
                (mse_x,mse_j)=(x_milH,j_milH)
                min=new_mse 

            #block milieu en bas 
             x_milB=origin_x+step  
             j_milB=origin_y
            
             block7=grayImg1[x_milB:x_milB + 16,j_milB:j_milB+ 16]
             new_mse=MSE(block1, block7)
             if min>new_mse:
                (mse_x,mse_j)=(x_milB,j_milB)
                min=new_mse             
            #block droit 
             x_droit=origin_x 
             j_droit=origin_y+step 
  
             block8=grayImg1[x_droit:x_droit+ 16,j_droit:j_droit+ 16]
             new_mse=MSE(block1, block8)
             if min>new_mse:
                (mse_x,mse_j)=(x_droit,j_droit)
                min=new_mse 

            #block droit haut
             x_droitH=x_droit-step
             j_droitH=j_droit
            
             block9=grayImg1[x_droitH:x_droitH+ 16,j_droitH:j_droitH+ 16]
             new_mse=MSE(block1, block9)
             if min>new_mse:
                (mse_x,mse_j)=(x_droitH,j_droitH)
                min=new_mse 
            
             return min , (mse_x,mse_j)


def recherche_decho():
    file_coordonner=[]
    file_coordonner1=[]
    


    tps1 = time.time()
    # le -16 a cause du dernier  block si on fait pas -16 le dernier block on pourra pas prendre un bloc de 16 dans img1 
    for i in range (0,grayImg2.shape[0]-16,16): #colonne with step 16 
     for j in range (0,grayImg2.shape[1]-16,16): #ligne 
           block1 = grayImg2[i:i + 16,j:j + 16]
           min = inf 
           # +64 to get the same block from the bordered image 
           origin_x=i+64
           origin_y=j+64
           step=32
           while(step>=1):
             new_mse,(new_x,new_y)=mse_blocks(block1,origin_x,origin_y,step)
            
             if min>new_mse:
                min=new_mse
                (mse_x,mse_j)=(new_x,new_y)
                origin_x=mse_x 
                origin_y=mse_j

               
             step=step // 2
             


           if min > 50 : 
            
            file_coordonner.append((mse_j-64,mse_x-64))
            file_coordonner1.append((j,i))
            #residu 
            grayImg3[i:i+16,j:j+16]= grayImg2[i:i + 16,j:j + 16]-grayImg1[mse_x:mse_x+16,mse_j:mse_j+16]
            
    tps2 = time.time()
    
    print("le temps d'execution est"+ str(tps2 - tps1))
    #dessiner les rectangle 
    for i in range (len(file_coordonner)) :
       couleur = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
       cv2.rectangle(img1, (file_coordonner[i][0], file_coordonner[i][1]),
                      (file_coordonner[i][0]+16,file_coordonner[i][1]+16), couleur, 2) 
       
       cv2.rectangle(img2, (file_coordonner1[i][0], file_coordonner1[i][1]),
                      (file_coordonner1[i][0]+16,file_coordonner1[i][1]+16), couleur, 2)

        
     
      
     #resize the window pop images 
    imS2 = cv2.resize(img2, (960, 540)) 
    imS1 = cv2.resize(img1, (960, 540)) 
    imS3 = cv2.resize( grayImg3 , (960, 540))

    cv2.imshow("image", imS1)
    cv2.imshow("image2", imS2)
    cv2.imshow("image3",imS3)
    
    if cv2.waitKey(2)    : 
      print("Done")
      
                                 

   

    

   

    









                

  























