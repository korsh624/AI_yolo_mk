pip install ultralytics

git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt

Запуск обучения

yolo detect train data=data.yaml model=yolov8n.pt epochs=100 imgsz=640

Вариант 2: YOLOv5
Поместите датасет в папку yolov5/data/.
Запустите обучение:

python train.py --data data.yaml --weights yolov5s.pt --epochs 100 --img 640


--weights yolov5s.pt – можно выбрать yolov5n.pt, yolov5m.pt и т. д.

4. Проверка модели
После обучения:

Веса модели сохраняются в runs/detect/train/weights/best.pt.

Можно протестировать модель на изображении:
yolo detect predict model=best.pt source=test_image.jpg
или на видео:
yolo detect predict model=best.pt source=test_video.mp4

Тонкая настройка (Transfer Learning)
Если у вас мало данных, можно дообучить предобученную модель:
yolo detect train data=data.yaml model=yolov8s.pt epochs=50 lr0=0.001