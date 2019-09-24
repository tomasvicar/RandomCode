import numpy as np
import cv2
import matplotlib.pyplot as plt

class ImShow4(object):
    def __init__(self,data,normalization='minmax-slice'):
        
    
        self.data=data
        self.z = 1
        self.zmax=np.shape(data)[2]
        
        self.t = 1
        self.tmax=np.shape(data)[3]
        
        if normalization=='minmax-slice':
            for k in range(self.zmax):
                for kk in range(self.tmax):
                    tmp=data[:,:,k,kk]
                    tmp=cv2.normalize(tmp, 0, 255, cv2.NORM_MINMAX)
                    data[:,:,k,kk]=tmp
        
        if normalization=='minmax-all':
            cv2.normalize(data, data, 0, 255, cv2.NORM_MINMAX)
            
            
    
    def show(self):
        esc=False
        while esc==False:
            fig, ax = plt.subplots(1, 1)
            
            tmp=self.data[:,:,self.z,self.t]
#            tmp=cv2.copyMakeBorder(tmp,30,0,0,0,cv2.BORDER_CONSTANT,value=[255,255,255] )
#            font = cv2.FONT_HERSHEY_SIMPLEX
#            tmp=cv2.putText(tmp,'z='+ str(self.z) + '   t='+ str(self.t),(0,25), font, 1,(0,0,0), 3, 0)
#            
#            cv2.imshow('imshow4',tmp)
            
            
            img=plt.imshow(tmp)
            
            fig.canvas.mpl_connect('scroll_event', tracker.self.button)
            plt.show()
            
            plt.show()
#            
#            key=input()
            key = cv2.waitKey(9999999)
            if key==ord('w'):
                self.z=(self.z+1)%self.zmax
            if key==ord('s'):
                self.z=(self.z-1)%self.zmax
            if key==ord('d'):
                self.t=(self.t+1)%self.tmax
            if key==ord('a'):
                self.t=(self.t-1)%self.tmax
            
            if key == 27:
                break
            
            
            
#        cv2.destroyAllWindows()
            
            
#cv2.imshow('dfsdfdifj',np.zeros((5,5)))
#key = cv2.waitKey(9999999)       


data=np.random.rand(200,300,20,10)

imshow4=ImShow4(data)
imshow4.show()


#tmp=data[:,:,0,0]
#img=plt.imshow(tmp)
#plt.show()
#plt.waitforbuttonpress()

#img=plt.imshow(tmp)
#plt.show()
#key = cv2.waitKey(9999999)
#key=input()