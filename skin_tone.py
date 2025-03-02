from sklearn.cluster import KMeans
import cv2
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color

def get_skin_tone(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    h, w, _ = image.shape
    skin_region = image[h//3:2*h//3, w//3:2*w//3]
    pixels = skin_region.reshape(-1, 3)

    kmeans = KMeans(n_clusters=1)
    kmeans.fit(pixels)
    dominant_color = kmeans.cluster_centers_[0]

    rgb_color = sRGBColor(dominant_color[0]/255, dominant_color[1]/255, dominant_color[2]/255)
    lab_color = convert_color(rgb_color, LabColor)
    
    if lab_color.lab_b < 20:
        return "Cool (Pink/Blue undertones)"
    elif lab_color.lab_b > 25:
        return "Warm (Yellow/Golden undertones)"
    else:
        return "Neutral (Balanced undertones)"
