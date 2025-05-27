import cv2
import os
# Путь к видеофайлу
video_path = "dataset.mp4"

# Папка для сохранения кадров
output_folder = "out"
os.makedirs(output_folder, exist_ok=True)  # Создаем папку, если её нет

# Открываем видео
cap = cv2.VideoCapture(video_path)

# Проверяем, открылось ли видео
if not cap.isOpened():
    print("Ошибка: Не удалось открыть видео!")
    exit()

frame_count = 0

while True:
    # Читаем кадр
    ret, frame = cap.read()

    # Если кадр не прочитан (конец видео или ошибка)
    if not ret:
        break

    # Сохраняем кадр в папку
    frame_name = f"frame_{frame_count:04d}.jpg"  # Формат: frame_0000.jpg, frame_0001.jpg, ...
    cv2.imwrite(os.path.join(output_folder, frame_name), frame)

    frame_count += 1

# Закрываем видео
cap.release()
print(f"Готово! Сохранено {frame_count} кадров в папку '{output_folder}'.")