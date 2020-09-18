import os
import sys
from PIL import Image

if __name__ == '__main__':

    dataset_path = ['val', 'test']
    input_dir_name = 'face_dataset_RGB'
    target_dir_name = 'face_dataset_depth_8bit'
    result_dir_name = 'result'

    for dataset in dataset_path:
        count = 1

        input_dir_path = os.path.join(os.getcwd(), dataset, input_dir_name)
        target_dir_path = os.path.join(os.getcwd(), dataset, target_dir_name)

        if not os.path.exists(os.path.join(dataset, result_dir_name)):
                os.makedirs(os.path.join(dataset, result_dir_name))

        for root, _, input_file_names in os.walk(input_dir_path):
            for input_file_name in input_file_names:

                if not input_file_name.endswith('.png'): continue

                input_file_path = os.path.join(root, input_file_name)
                output_file_path = input_file_path.replace('rgb', 'depth').replace(input_dir_name, target_dir_name)

                print(input_file_path, output_file_path) 

                images = [Image.open(x) for x in [input_file_path, output_file_path]]
                widths, heights = zip(*(i.size for i in images))

                total_width = sum(widths)
                max_height = max(heights)

                new_im = Image.new('RGB', (total_width, max_height))

                x_offset = 0

                for im in images:
                    new_im.paste(im, (x_offset,0))
                    x_offset += im.size[0]

                new_im.save(os.path.join(dataset, result_dir_name, '%d.png' % count))
                count += 1
