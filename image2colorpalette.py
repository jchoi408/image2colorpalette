import numpy as np
import cv2
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

%matplotlib inline

class image2colorpalette:
    def __init__(self, image_rgb, palette_size=10):
        
        self.image_rgb = image_rgb
        self.palette_size = palette_size
        
        # Extract all of the lists of pixel colors into a list of lists.
        all_pixels = [list(pixel.flatten()) for sublist in image_rgb for pixel in sublist]

        all_pixels = []
        for sublist in image_rgb:
            for pixel in sublist:
                # Convert pixel from array to list and then add it to the list of lists.
                all_pixels.append(list(pixel.flatten()))

        all_pixels_df = pd.DataFrame(all_pixels, columns=['Red', 'Green', 'Blue'])

        clustering_kmeans = KMeans(n_clusters=palette_size)
        clustering_kmeans.fit_predict(all_pixels_df)
        all_pixels_df['clusters'] = clustering_kmeans.labels_

        cluster_medians = all_pixels_df.groupby('clusters').median().round(0)

        # Create list of lists for np.array
        cluster_rgb = []
        cluster_hex = []

        i = 0

        while i < len(cluster_medians):
            # Create RGB of pixel to insert.
            insert_rgb = [cluster_medians.iloc[i][0], cluster_medians.iloc[i][1], cluster_medians.iloc[i][2]]

            cluster_rgb.append(insert_rgb)

            # Convert RGB to HEX
            insert_hex = '#{:02x}{:02x}{:02x}'.format(cluster_medians.iloc[i][0], cluster_medians.iloc[i][1], cluster_medians.iloc[i][2])

            cluster_hex.append(insert_hex)

            i+=1

        self.cluster_rgb = np.array(cluster_rgb)
        self.cluster_hex = np.array(cluster_hex)

    def get_rgb(self):
        return self.cluster_rgb

    def get_hex(self):
        return self.cluster_hex
    
    def show_palette(self):
        
        indices = np.array([range(0,len(self.cluster_rgb))])

        plt.figure()

        #subplot(r,c) provide the no. of rows and columns
        f, axarr = plt.subplots(2,1,figsize=(15,10), constrained_layout=True) 

        # use the created array to output your multiple images. In this case I have stacked 4 images vertically
        axarr[0].imshow(self.cluster_rgb[indices])
        axarr[0].axis('off')

        axarr[1].imshow(self.image_rgb)
        axarr[1].axis('off')

        # Print out the colors in a concatenated string format.
        print('RGB')

        print_cluster_rgb = []
        for i in self.cluster_rgb:
            insert_formatted_rgb = '(' + ','.join([str(num) for num in i]) + ')'
            print_cluster_rgb.append(insert_formatted_rgb)

        # Concatenate list to string
        print_cluster_rgb = ', '.join(print_cluster_rgb)

        print(print_cluster_rgb)

        print('\n')

        print('HEX')

        # Concatenate list to string
        print_cluster_hex = ', '.join(self.cluster_hex)

        print(print_cluster_hex)
        
