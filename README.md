# README.md

## 1. Road_Image

处理后的压路机图片，统一英文数字命名，解决中文冲突

## 2. category_and_color.txt

```bash
labels:

Rolling drum
Body
Light
Rolling drum frame
Water tank hold
Grilles
Cleaning scraper
Cab
Roof
Body panel
Wheel
Rolling wheel
Frameframe
Hood

color:

Rolling Drum: Red
Body: Green
Light: Blue
Rolling Drum Frame: Yellow
Water Tank Hold: Cyan
Grilles: Magenta
Cleaning Scraper: Dark Red
Cab: Dark Green
Roof: Dark Blue
Body Panel: Olive
Wheel: Teal
Rolling Wheel: Purple
Frame Frame: Silver
Hood: Gray
```

## 3. labels.xlsx

清洗处理后的标注信息

## 4. semantic_mask

```python
# 将路径进行替换
IMAGE_FOLDER = "Road_Image"
PROCESSED_FOLDER = "processed_images"
LABELS_FILE = "labels.xlsx"
```