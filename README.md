# Yolo Augumentation Tool

## Getting Started
1. アノテーションした画像とjsonをimagesディレクトリに入れる
2. $ mv ./images/*.png xxxx_images/
3. $ mv ./images/*.json xxxx_labels_json/
4. $ main.py piman

## cfg.txt
```
- batch=64
一度に64枚づつ処理。変えない方が良い
- subdivision=32
一度に処理する枚数を分割する。小さいと一度にメモリに乗るが、メモリオーバーになるので、32とする
- max_batches=6000
最低6,000、class x 2,000
- steps=4800, 5400
max_batches*0.8, 0.9
- width,height=416,416
ネットワークサイズ、画像は自動でリサイズされて、余白はパディングされるので、大きさ、アスペクトレシオが異なる画像を使える
- classes=1
(自動化されている)分類するクラスの数
- filters=255
filters=(classes + 5) * 3
(自動化されている)yoloレイヤーの前のフィルターの大きさは分類するクラスの数による
```

## Yolo
`./darknet detector train xxx.data xxx.cfg yolov4.conv.137 -dont_show`