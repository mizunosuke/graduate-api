#　魚体が銀色系の場合に使う処理

import cv2
import numpy as np

# 画像の読み込み
img = cv2.imread('IMG_4933.jpeg')

# ガウシアンフィルタによる平滑化
img_blur = cv2.GaussianBlur(img, (9, 9), 0)

# 画像のHSV変換
hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)

#銀色やグレーに近い色相、彩度、明度の範囲を指定
lower_color1 = np.array([0, 35, 0])
upper_color1 = np.array([180, 110, 75])
lower_color2 = np.array([30, 20, 0]) # 変更
upper_color2 = np.array([220, 110, 75])

#指定した範囲の色に含まれるピクセルを抽出
mask1 = cv2.inRange(hsv, lower_color1, upper_color1)
mask2 = cv2.inRange(hsv, lower_color2, upper_color2)
mask = cv2.bitwise_or(mask1, mask2)

#クロージングによるノイズ除去
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
mask_close = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

#輪郭の検出
contours, _ = cv2.findContours(mask_close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#面積が小さい輪郭を除外
contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 600]

#最大の輪郭を取得
max_contour = max(contours, key=cv2.contourArea)

#輪郭の描画
img_contours = cv2.drawContours(img.copy(), [max_contour], -1, (0, 0, 255), 2)

#輪郭の近似
epsilon = 0.02 * cv2.arcLength(max_contour, True)
approx = cv2.approxPolyDP(max_contour, epsilon, True)

#最も離れた2点間の座標を取得
max_dist = 0
for i in range(len(approx)):
    for j in range(i+1, len(approx)):
        temp_dist = np.linalg.norm(approx[i] - approx[j])
        if temp_dist > max_dist:
            max_dist = temp_dist
            max_dist_points = [tuple(approx[i][0]), tuple(approx[j][0])]

#ピクセル単位での距離計算
pixel_distance = max_dist

#最も離れた2点間の描画
img_maxdist = cv2.line(img_contours.copy(), max_dist_points[0], max_dist_points[1], (0, 255, 0), 2)
img_maxdist = cv2.putText(img_maxdist, f"Distance: {pixel_distance:.2f}px", (50,150), cv2.FONT_HERSHEY_SIMPLEX, 4, (0,255,0), 8)

#結果の表示
cv2.imshow('original', img)
cv2.imshow('blurred', img_blur)
cv2.imshow('hsv', hsv)
cv2.imshow('mask', mask)
cv2.imshow('mask_close', mask_close)
cv2.imshow('contours', img_contours)
cv2.imshow('maxdist', img_maxdist)
cv2.waitKey(0)
cv2.destroyAllWindows()