from Image_Comparison_Function import comparison
from Paths import get_files_in_directory, master_path,test_path,result_path
import os


def compare(screen_type, device_type):
    image_list_master = get_files_in_directory(f'{master_path}{device_type}/{screen_type}')
    image_list_test = get_files_in_directory(f'{test_path}{device_type}/{screen_type}')
    for i in range(0, len(image_list_master)):
        first_image = os.path.join(f'{master_path}{device_type}/{screen_type}/{image_list_master[i]}')

        second_image = os.path.join(f'{test_path}{device_type}/{screen_type}/{image_list_test[i]}')

        comparison_output = f'{result_path}{device_type}/{i}.png'

        comparison(first_image, second_image, comparison_output, device_type)
