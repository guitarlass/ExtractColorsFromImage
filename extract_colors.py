# import cv2
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
from PIL import Image
import numpy as np
from collections import Counter


def get_colors(image_path, num_colors=5):
    image = Image.open(image_path)
    image = image.convert('RGB')  # Ensure the image is in RGB format
    image = image.resize((150, 150))  # Resize for faster processing
    img_array = np.array(image)

    # Reshape array to be a list of RGB values
    img_array = img_array.reshape((img_array.shape[0] * img_array.shape[1], 3))

    # Count the frequency of each color
    counter = Counter([tuple(color) for color in img_array])

    # Get the most common colors
    most_common_colors = counter.most_common(num_colors)
    print(most_common_colors)

    # Convert colors to hex for HTML display
    hex_colors = ['#{:02x}{:02x}{:02x}'.format(color[0], color[1], color[2]) for color, _ in most_common_colors]

    return hex_colors

# # Function to convert image into RGB
# def load_image(image_path):
#     image = cv2.imread(image_path)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     return image
#
#
# # Function to extract dominant colors
# def extract_colors(image, num_colors):
#     image = image.reshape((image.shape[0] * image.shape[1], 3))
#
#     kmeans = KMeans(n_clusters=num_colors)
#     kmeans.fit(image)
#
#     colors = kmeans.cluster_centers_.astype(int)
#     return colors
#
#
# # Function to display the dominant colors
# def plot_colors(colors):
#     plt.figure(figsize=(8, 2))
#     plt.imshow([colors])
#     plt.axis('off')
#     plt.show()
