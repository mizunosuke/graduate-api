import cv2
import numpy as np

# 画像の読み込み
img = cv2.imread('IMG_5489.jpeg')

# ガウシアンフィルタによる平滑化
img = cv2.GaussianBlur(img, (9, 9), 0)

# 画像のHSV変換
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 色相、彩度、明度の範囲を指定
lower_color1 = np.array([0, 50, 50])
upper_color1 = np.array([20, 255, 255])
lower_color2 = np.array([170, 50, 50])
upper_color2 = np.array([180, 255, 255])

# 指定した範囲内の色だけを抽出
mask1 = cv2.inRange(hsv, lower_color1, upper_color1)
mask2 = cv2.inRange(hsv, lower_color2, upper_color2)
mask = cv2.bitwise_or(mask1, mask2)

# クロージングによるノイズ除去
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# 輪郭の検出
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 面積が小さい輪郭を除外
contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 500]

# 最大の輪郭を取得
max_contour = max(contours, key=cv2.contourArea)

# 輪郭の描画
cv2.drawContours(img, [max_contour], -1, (0, 0, 255), 2)

# 輪郭の近似
epsilon = 0.01 * cv2.arcLength(max_contour, True)
approx = cv2.approxPolyDP(max_contour, epsilon, True)

# 最も離れた2点間の座標を取得
dist = 0
for i in range(len(approx)):
    for j in range(i+1, len(approx)):
        temp_dist = np.linalg.norm(approx[i] - approx[j])
        if temp_dist > dist:
            dist = temp_dist
            max_dist_points = [tuple(approx[i][0]), tuple(approx[j][0])]

# 最も離れた2点間の描画
cv2.line(img, max_dist_points[0], max_dist_points[1], (0, 255, 0), 2)

# 結果の表示
cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
