import os
import requests

input_folder = 'input_images'
output_folder = 'output_images'

if not os.path.exists(output_folder):
  os.makedirs(output_folder)


def transform_image(image_name, input_folder, output_folder):
    image_path = os.path.join(input_folder, image_name)
    output_path = os.path.join(output_folder, image_name.split('.')[0] + '_output.png')
    print(image_name,output_path)
    # response = requests.post(
    #     'https://www.cutout.pro/api/v1/matting?mattingType=6',
    #     files={'file': open(image_path, 'rb')},
    #     headers={'APIKEY': 'INSERT_YOUR_API_KEY_HERE'},
    # )
    # with open(output_path, 'wb') as out:
    #     out.write(response.content)


def transform_images_multiple(input_folder, output_folder):
    image_names = os.listdir(input_folder)
    for image_name in image_names:
        transform_image(image_name, input_folder, output_folder)


if __name__ == '__main__':
    transform_images_multiple('input_images', 'output_images')
