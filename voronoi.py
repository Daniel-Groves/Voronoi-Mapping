from PIL import Image
import time
nsites = 5
pic = Image.open("thescream.jpg") #insert name of image to map here
pix = pic.load()
print(pic.size)
from PyProbs import Probability as pr


xnsitesgap = pic.size[0]/(nsites-1)
ynsitesgap = pic.size[1]/(nsites-1)
totalpix = pic.size[1]*pic.size[0]
xsites = []
sitesrgb = []
ysites = []

def even_sites(nsites):
    for i in range(nsites-1):
        for j in range(nsites-1):
            xsites.append(round(xnsitesgap*i))
            ysites.append(round(ynsitesgap*j))
            sitesrgb.append(pix[round(xnsitesgap*i),round(ynsitesgap*j)])
     
def random_sites(totalpix):
    for i in range(pic.size[1]):
        for j in range(pic.size[0]):
            if pr.Prob(1/10):
                xsites.append(j)
                ysites.append(i)
                print(i,j)
                sitesrgb.append(pix[j,i])
     
def weighted_sites(totalpix):
    for i in range(10,pic.size[1]-10):
        for j in range(10,pic.size[0]-10):
            r,g,b = pix[j,i]
            upv = abs(pix[j,i-1][0]-r) + abs(pix[j,i-1][1]-g) + abs(pix[j,i-1][2]-b)
            downv = abs(pix[j,i+1][0]-r) + abs(pix[j,i+1][1]-g) + abs(pix[j,i+1][2]-b)
            leftv = abs(pix[j-1,i][0]-r) + abs(pix[j-1,i][1]-g) + abs(pix[j-1,i][2]-b)
            rightv = abs(pix[j+1,i][0]-r) + abs(pix[j+1,i][1]-g) + abs(pix[j+1,i][2]-b)
            variance = int(upv + downv + leftv + rightv)
            if pr.Prob(variance/5000):
                if pr.Prob(1/1):
                    xsites.append(j)
                    ysites.append(i)
                    totr = 0
                    totg = 0
                    totb = 0
                    for q in range(j-10,j+10):
                        for p in range(i-10,i+10):
                            try:
                                totr += pix[q,p][0]
                                totg += pix[q,p][1]
                                totb += pix[q,p][2]
                            except IndexError:
                                print("error")
                                print(q,p)
                    


                    sitesrgb.append((round(totr/400),round(totg/400),round(totb/400)))

weighted_sites(totalpix)    
            
    

print(xsites)
print(ysites)



for i in range(pic.size[1]):
    print(i)
    for j in range(pic.size[0]):
        closestindex = 0
        closestdistance = 1000000000000000
        for q in range(len(xsites)):
            distance = (i-ysites[q])**2 + (j-xsites[q])**2
            if distance < closestdistance:
                closestdistance = distance
                closestindex = q
        pix[j,i] = sitesrgb[closestindex]

          
pic.save("newscream.png")  #Insert name of what you want to save mapping as  
