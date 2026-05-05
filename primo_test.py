from ultralytics import YOLO
import cv2
import urllib.request

url="test.jpg"
""" urllib.request.urlretrieve(url, "test.jpg") """

model = YOLO("yolov8n.pt")
results = model(url, conf=0.50)

for box in results[0].boxes:
    classe = results[0].names[int(box.cls)]
    confidenza = float(box.conf)
    print(f"trovato {classe} con confidenza {confidenza:.0%}")
results[0].show()