import numpy as np
import cv2

# تابعی برای ایجاد گرادیان رنگ بین دو رنگ
def interpolate_color(color1, color2, t):
    return (1 - t) * np.array(color1) + t * np.array(color2)

# تابعی برای رسم تصویر با گرادیان رنگ
def draw_gradient(point1, point2, color1, color2):
    width, height = 400, 400
    image = np.zeros((height, width, 3), dtype=np.uint8)

    # محاسبه شیب خط
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]

    for y in range(height):
        for x in range(width):
            # محاسبه فاصله از نقطه اول
            d1 = np.sqrt((x - point1[0])**2 + (y - point1[1])**2)
            d2 = np.sqrt((x - point2[0])**2 + (y - point2[1])**2)

            # محاسبه t برای رنگ
            if d1 + d2 != 0:
                t = d1 / (d1 + d2)
                color = interpolate_color(color1, color2, t)
                image[y, x] = color.astype(np.uint8)

    return image

# نقاط و رنگ‌ها
point1 = (100, 150)  # نقطه اول
point2 = (300, 350)  # نقطه دوم
color1 = (255, 0, 0)   # رنگ آبی (BGR)
color2 = (0, 0, 255)   # رنگ قرمز (BGR)

# رسم تصویر
image = draw_gradient(point1, point2, color1, color2)

# نمایش تصویر با OpenCV
cv2.imshow('Gradient', image)
cv2.waitKey(0)
cv2.destroyAllWindows()