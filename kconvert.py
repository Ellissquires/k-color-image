import os,sys
from PIL import Image
from sklearn.cluster import KMeans
import numpy as np

filename = sys.argv[1:][0]
img = Image.open(filename).convert('RGB')
width, height = img.size

pixel_colors = []
for x in range(width):
    for y in range(height):
        r,g,b = img.getpixel((x,y))
        color = [r,g,b]
        pixel_colors.append(color)


data = np.array(pixel_colors)
kmeans = KMeans(n_clusters=10)
kmeans.fit(data)
centroids = np.rint(kmeans.cluster_centers_)
labels = kmeans.labels_

print(centroids)
for x in range(width):
    for y in range(height):
        r,g,b = img.getpixel((x,y))
        color = [r,g,b]
        color = tuple(centroids[labels[x * height + y]].astype(int))
        img.putpixel((x,y), color)

img.show()

img.save(filename + "_edited", "JPEG")
