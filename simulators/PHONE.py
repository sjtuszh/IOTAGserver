import requests
from PIL import Image
from io import BytesIO


# 获取传感器数据
def get_sensor_data():
    url = 'http://localhost:5000/sensor_data'
    response = requests.get(url)
    if response.status_code == 200:
        sensor_data = response.json()
        print("传感器数据:")
        print(sensor_data)
    else:
        print(f"获取传感器数据失败: {response.status_code}")


# 获取图像数据并显示
def get_and_display_image(image_id):
    url = f'http://localhost:5000/images/{image_id}'
    response = requests.get(url)
    if response.status_code == 200:
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image.show()
    else:
        print(f"获取图像失败: {response.status_code}")


if __name__ == "__main__":
    # 获取传感器数据
    get_sensor_data()

    # 获取图像数据并显示
    image_id = 1  # 假设要获取的图像的ID为1
    get_and_display_image(image_id)
