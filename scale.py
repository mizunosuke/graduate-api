import cv2

# 画像の読み込み
img = cv2.imread('IMG_5478.jpeg', 0)

# 自動閾値処理
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 結果を表示
cv2.imshow('image', img)
cv2.imshow('threshold', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# カメラのセンサーサイズ (単位: mm)
SENSOR_SIZE = {
    "iPhone 8": (3.99, 2.95),
    "iPhone 8 Plus": (5.7, 4.28),
    "iPhone X": (6.0, 4.5),
    "iPhone XR": (6.86, 5.14),
    "iPhone XS": (5.68, 4.26),
    "iPhone XS Max": (6.24, 4.68),
    "iPhone 11": (5.68, 4.26),
    "iPhone 11 Pro": (5.67, 4.26),
    "iPhone 11 Pro Max": (6.22, 4.68),
    "iPhone SE (2nd generation)": (4.89, 3.67),
    "iPhone 12": (5.78, 4.34),
    "iPhone 12 Mini": (5.68, 4.26),
    "iPhone 12 Pro": (5.78, 4.36),
    "iPhone 12 Pro Max": (6.33, 4.75),
    "iPhone 13": (5.78, 4.34),
    "iPhone 13 Mini": (5.68, 4.26),
    "iPhone 13 Pro": (5.78, 4.36),
    "iPhone 13 Pro Max": (6.33, 4.75),
}

# 焦点距離
Focal_Lengths = {
    "iPhone 8": 3.99,
    "iPhone 8 Plus": 3.99,
    "iPhone X": 4.0,
    "iPhone XR": 4.25,
    "iPhone XS": 4.25,
    "iPhone XS Max": 4.25,
    "iPhone 11": 4.25,
    "iPhone 11 Pro": 4.25,
    "iPhone 11 Pro Max": 4.25,
    "iPhone SE (2nd generation)": 3.99,
    "iPhone 12": 4.25,
    "iPhone 12 Mini": 4.25,
    "iPhone 12 Pro": 6.0,
    "iPhone 12 Pro Max": 6.1,
    "iPhone 13": 5.4,
    "iPhone 13 Mini": 5.4,
    "iPhone 13 Pro": 7.9,
    "iPhone 13 Pro Max": 7.9,
}