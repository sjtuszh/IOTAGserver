import base64

from flask import Flask, request, make_response
app = Flask(__name__)
@app.route('/images/<int:image_id>', methods=['GET'])
def get_image(image_id):
    # conn = sqlite3.connect(DATABASE)
    # cursor = conn.cursor()
    # cursor.execute('SELECT image_path FROM images WHERE id=?', (image_id,))
    # row = cursor.fetchone()
    # conn.close()
    #
    # if row:
    #     image_path = row[0]
    #     with open(image_path, 'rb') as image_file:
    #         image_data = image_file.read()
    #         # 对图像数据进行base64编码
    #         encoded_image = base64.b64encode(image_data).decode('utf-8')
    #
    #     response = make_response(encoded_image)
    #     response.headers['Content-Type'] = 'image/jpeg'
    #     return response
    # else:
    #     return 'Image not found', 404

    # 简化一下就是，不管image的id是多少都随便返回一个jpg
    image_path = '随便放个.png'
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
        # encoded_image = base64.b64encode(image_data).decode('utf-8')
    response = make_response(image_data, 200)
    response.headers['Content-Type'] = 'image/jpeg'
    return response
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)