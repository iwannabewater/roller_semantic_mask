# import os
# import json
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# from PIL import Image

# # 避免超大图像导致的 warning
# Image.MAX_IMAGE_PIXELS = None

# # 定义每个路面压路机部分的固定颜色（归一化的RGB值）
# colors_normalized = {
#     "rolling drum": (1, 0, 0),
#     "body": (0, 1, 0),
#     "light": (0, 0, 1),
#     "rolling drum frame": (1, 1, 0),
#     "water tank hold": (0, 1, 1),
#     "grilles": (1, 0, 1),
#     "cleaning scraper": (0.5, 0, 0),
#     "cab": (0, 0.5, 0),
#     "roof": (0, 0, 0.5),
#     "body panel": (0.5, 0.5, 0),
#     "wheel": (0, 0.5, 0.5),
#     "rolling wheel": (0.5, 0, 0.5),
#     "frameframe": (0.75, 0.75, 0.75),
#     "hood": (0.5, 0.5, 0.5)
# }

# # 加载标签数据
# labels_df = pd.read_excel("labels.xlsx")


# if not os.path.exists("processed_images"):
#     os.makedirs("processed_images")

# # 处理单个图像
# def process_image(image_filename, labels_data, colors):
#     try:
#         # 打开图像
#         image_path = os.path.join("Road_Image", image_filename)
#         img = Image.open(image_path)
#         fig, ax = plt.subplots(figsize=(img.size[0]/100, img.size[1]/100), dpi=100)
#         ax.imshow(img)
        
#         # 提取相应的标签数据
#         label_data = labels_data[labels_data["raw data"] == image_filename]["labels"].iloc[0]
#         label_data_parsed = json.loads(label_data)
        
#         # 遍历每个标签
#         for label in label_data_parsed:
#             original_width = label["original_width"]
#             original_height = label["original_height"]
#             # 根据原始尺寸缩放点坐标
#             scaled_points = [
#                 (point[0] * original_width / 100, point[1] * original_height / 100) 
#                 for point in label["points"]
#             ]
#             # 创建 semantic mask 覆盖到图像上，透明度为0.7
#             polygon = patches.Polygon(scaled_points, closed=label["closed"], facecolor=colors[label["polygonlabels"][0].lower()], edgecolor='black', alpha=0.7)
#             ax.add_patch(polygon)
        
#         # 设置图像属性
#         ax.axis('off')
#         plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
#         plt.margins(0,0)
#         plt.gca().xaxis.set_major_locator(plt.NullLocator())
#         plt.gca().yaxis.set_major_locator(plt.NullLocator())
        
#         # 将处理后的图像保存到指定文件夹
#         save_path = os.path.join("processed_images", image_filename)
#         plt.savefig(save_path, bbox_inches='tight', pad_inches=0, dpi=100)
#         plt.close(fig)
#         img.close()

#     except Exception as e:
#         print(f"Error processing {image_filename}: {str(e)}")

# # 批量处理图像
# image_files = os.listdir("Road_Image")
# for image_filename in image_files:
#     if image_filename in labels_df["raw data"].values:
#         process_image(image_filename, labels_df, colors_normalized)

import os
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image, ImageFile

# 定义路径
IMAGE_FOLDER = "Road_Image"
PROCESSED_FOLDER = "processed_images"
LABELS_FILE = "labels.xlsx"

# 避免超大图像导致的 warning
Image.MAX_IMAGE_PIXELS = None
# 避免图像被截断
ImageFile.LOAD_TRUNCATED_IMAGES = True

# 定义每个路面压路机部分的固定颜色（归一化的RGB值）
colors_normalized = {
    "rolling drum": (1, 0, 0),
    "body": (0, 1, 0),
    "light": (0, 0, 1),
    "rolling drum frame": (1, 1, 0),
    "water tank hold": (0, 1, 1),
    "grilles": (1, 0, 1),
    "cleaning scraper": (0.5, 0, 0),
    "cab": (0, 0.5, 0),
    "roof": (0, 0, 0.5),
    "body panel": (0.5, 0.5, 0),
    "wheel": (0, 0.5, 0.5),
    "rolling wheel": (0.5, 0, 0.5),
    "frameframe": (0.75, 0.75, 0.75),
    "hood": (0.5, 0.5, 0.5)
}


# 加载标签数据
def load_labels(file_path):
    return pd.read_excel(file_path)

# 处理单个图像
def process_image(image_filename, labels_data, colors):
    try:
        # 打开图像
        image_path = os.path.join(IMAGE_FOLDER, image_filename)
        img = Image.open(image_path)
        fig, ax = plt.subplots(figsize=(img.size[0]/100, img.size[1]/100), dpi=100)
        ax.imshow(img)
        
        # 提取相应的标签数据
        label_data = labels_data[labels_data["raw data"] == image_filename]["labels"].iloc[0]
        label_data_parsed = json.loads(label_data)

        # 遍历每个标签
        for label in label_data_parsed:
            original_width = label["original_width"]
            original_height = label["original_height"]
            # 根据原始尺寸缩放点坐标
            scaled_points = [
                (point[0] * original_width / 100, point[1] * original_height / 100) 
                for point in label["points"]
            ]
            polygon = patches.Polygon(scaled_points, closed=label["closed"], facecolor=colors[label["polygonlabels"][0].lower()], edgecolor='black', alpha=0.7)
            ax.add_patch(polygon)
        
        # 设置图像属性
        ax.axis('off')
        plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        plt.margins(0,0)
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())
        
        save_path = os.path.join(PROCESSED_FOLDER, image_filename)
        plt.savefig(save_path, bbox_inches='tight', pad_inches=0, dpi=100)
        plt.close(fig)
        img.close()

    except Exception as e:
        print(f"Error processing {image_filename}: {str(e)}")

# 批量处理图像
def process_all_images():
    """Process all images in the specified folder."""
    if not os.path.exists(PROCESSED_FOLDER):
        os.makedirs(PROCESSED_FOLDER)

    labels_df = load_labels(LABELS_FILE)
    image_files = os.listdir(IMAGE_FOLDER)
    
    for image_filename in image_files:
        if image_filename.endswith(('.jpg', '.jpeg', '.png')) and image_filename in labels_df["raw data"].values:
            process_image(image_filename, labels_df, colors_normalized)


if __name__ == "__main__":
    process_all_images()