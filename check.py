from PIL import Image

def has_alpha_channel(image_path):
    """Проверяет, есть ли в изображении альфа-канал."""
    try:
        img = Image.open(image_path)
        return img.mode in ('RGBA', 'LA')  # RGBA или LA (Luminance + Alpha)
    except Exception as e:
        print(f"Ошибка при открытии изображения: {e}")
        return False

for i in ("assets/images/enemy1", "assets/images/enemy2.png", "assets/images/enemy3.png", "assets/images/bullet.png", "assets/images/player.png"):
    image_path = i
    if has_alpha_channel(image_path):
        print("Изображение содержит альфа-канал.")
    else:
        print("Изображение НЕ содержит альфа-канал.")