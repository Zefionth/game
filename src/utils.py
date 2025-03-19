import pygame

def load_image(path, size=None):
    """
    Загружает изображение и масштабирует его до указанного размера.
    Поддерживает PNG с прозрачностью.
    """
    try:
        image = pygame.image.load(path).convert_alpha()  # Загружаем с прозрачностью
    except pygame.error as e:
        print(f"Ошибка загрузки изображения: {e}")
        return None

    if size:
        image = pygame.transform.scale(image, size)  # Масштабируем изображение
    return image