# Yolo Augumentation Tool

## 使い方
```
-- オーギュメンテーション --
[前提] アノテーションした画像とjsonをimagesディレクトリに格納済
$ mkdir piman_images piman_labels_json
$ mv ./images/*.png piman_images/
$ mv ./images/*.json piman_labels_json/
$ main.py piman   # --> piman_train_dataにyolo学習用データを生成
-- 学習 --
[前提] https://github.com/AlexeyAB/darknet をpath/to/darknetにクローンし、tinyYolov4の学習環境構築済
$ mv piman_train_data  path/to/darknet
$ cd path/to/darknet 
$ sh piman_train_data/start_tiny_v4.sh 
```