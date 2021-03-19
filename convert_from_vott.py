import os
import configparser
import glob
import json
import xml.etree.ElementTree as ET

names_dic = {}
object_id = 0


def increment():
    global object_id
    object_id += 1


def xml_to_dic(tree, frame):
    global object_id
    root = tree.getroot()
    size = root.find('size')
    screen_width = float(size.find('width').text)
    screen_height = float(size.find('height').text)
    objects = root.findall('object')
    dic = {}
    for object in objects:
        object_id_str = str(object_id)
        dic[object_id_str] = {}
        name = object.find('name').text
        bndbox = object.find('bndbox')
        xmin = float(bndbox.find('xmin').text) / screen_width
        xmax = float(bndbox.find('xmax').text) / screen_width
        ymin = float(bndbox.find('ymin').text) / screen_height
        ymax = float(bndbox.find('ymax').text) / screen_height
        width = xmax - xmin
        height = ymax - ymin
        dic[object_id_str]['frame'] = frame
        dic[object_id_str]['objectId'] = object_id_str
        dic[object_id_str]['class'] = names_dic[name]
        dic[object_id_str]['bounding'] = {}
        dic[object_id_str]['bounding']['left'] = xmin
        dic[object_id_str]['bounding']['top'] = ymin
        dic[object_id_str]['bounding']['width'] = width
        dic[object_id_str]['bounding']['height'] = height

        increment()
    return dic


def load_names():
    with open('template_names.txt', 'rt') as fin:
        data = fin.read().split('\n')
        for i, line in enumerate(data):
            if line == ' ' or line == '':
                continue
            names_dic[line] = str(i)


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    input_path = config['vott']['InputPath']
    output_path = config['vott']['OutputPath']
    in_dir = glob.glob(os.path.join(input_path, '*.xml'))
    print(input_path)
    out_dir = output_path

    load_names()

    for i, file in enumerate(in_dir):
        tree = ET.parse(file)
        filename = os.path.splitext(os.path.basename(file))[0]
        frame = filename.split('=')[1]

        dic = xml_to_dic(tree, frame)
        out_path = os.path.join(out_dir, filename + '.json')
        with open(out_path, 'wt') as fout:
            json.dump(dic, fout, ensure_ascii=False)


if __name__ == '__main__':
    main()