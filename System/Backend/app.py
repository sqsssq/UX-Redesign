'''
Description: 
Author: Qing Shi
Date: 2022-11-20 19:14:42
LastEditTime: 2024-08-09 22:14:14
'''
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import pandas as pd
from openai import OpenAI
import base64
from PIL import Image
import io
from datetime import datetime


FILE_ABS_PATH = os.path.dirname(__file__)

app = Flask(__name__)
CORS(app)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = 'timetuner'


client = OpenAI(
)

global_prompt = """
# Product Information #

This is the introduction of the product: 
	Microsoft Designer is a graphic design and image editing app powered by AI. Create eye-catching images with your words, craft next-level designs that pop, and even edit photos like an expert. Designer is integrated across your favorite Microsoft apps like Copilot, Bing, Edge, and more to help you create when and where you need it.

# Usability Evaluation Information #

Five users completed a task using this product while following the think-aloud protocol. Please read the <Product Information> for details about the product. 

"""

FILE_ABS_PATH = os.path.dirname(__file__)

def encode_image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format=image.format)
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

# 设置文件上传目录
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/api/test/Save', methods=['POST'])
def save():
    # 获取当前时间作为文件名
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f"{timestamp}.json"
    print(timestamp)
    
    # 获取前端传来的 JSON 数据
    data = request.get_json()
    
    # 设置保存路径（可以根据需要修改）
    save_path = os.path.join('json_files', filename)
    
    # 创建目录（如果不存在）
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # 将数据保存为 JSON 文件
    with open(save_path, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    return jsonify({"message": f"Data saved to {filename}"}), 200


# 设置允许的文件扩展名
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({'message': 'File uploaded successfully', 'url': file_path}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400
    
@app.route('/api/test/GeneralChat', methods=['POST'])
def chat():
    user_message = request.json['history']
    print(user_message)
    general_prompt = """You are a helpful assistant and a professional User experience Designer. You will answer any questions users have about the data. please think step by step. please respond in chinese. and please use the markdown format. thank you"""
    user_message.insert(0, {"role": "system", "content": general_prompt})
    print(user_message)
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = user_message
    )
    print(response)
    get_response = response.choices[0].message.content
    # get_response = 'aaa'
    return jsonify({ 'response': get_response })


@app.route('/api/test/Lucky', methods=['POST'])
def reflect_design():
    global global_prompt
    info = request.json['info']
    print(info)
    # path = FILE_ABS_PATH + '/Product UI/' + info[1]['image_url'] + '.png';
    # image = Image.open(path)
    # base64_image = encode_image_to_base64(image)
    # image_message = {
    #     "type": "image_url",
    #     "image_url": {
    #         "url": f"data:image/png;base64,{base64_image}"
    #     }
    # }
    # info[1] = image_message
    # point_prompt = """As a UX designer well-versed in usability evaluation and product redesign, you have completed usability testing for a product. Please review the <Product Information> for product details and the <Usability Evaluation Information> for insights from the testing. Your task is to develop redesign solutions for selected usability issues according to the guidelines in [Input]. Ensure your communication is UX-focused and easy-to-understand.
    # #Generation Optimization#
    # Respond concisely,  preferably no more than 80 words.
    # Remember that your capabilities are limited. If the instructions exceed your knowledge scope, you should inform users by responding, “Sorry, this instruction is beyond my knowledge scope.’’
    # """
    # general_prompt = """You are a helpful assistant and a professional User experience Designer. You will answer any questions users have about the data. please think step by step. please respond in chinese. thank you. 请根据上文的背景和下面提供的图片和问题以及input的指引，给出回答。如果input是空的就按照背景和图片和问题随机给出回答。
    # 格式是 方法：描述
    # 下面是一个例子，
    # 增强个性化和定制功能：允许用户通过一个高级工具栏详细定制设计元素，如颜色方案、字体和图像，同时提供实时预览功能以便用户即时看到并调整更改。
    # 请返回同样格式的内容，不要加上引号，不要加上换行，不要加上前缀，只需要内容，没有前面多余的信息.只返回一个建议。
    # """

    # user_massage = [{
    #     "role": "system",
    #     "content": global_prompt  + point_prompt + general_prompt
    # }, {
    #     "role": "user",
    #     "content": info
    # }]

    # response = client.chat.completions.create(
    #     model="gpt-4o",
    #     messages=user_massage
    # )
    # get_response = response.choices[0].message.content
    # print(response)
    get_response = 'aaa'
    return jsonify({ 'response': get_response })


@app.route('/api/test/SolutionChat', methods=['POST'])
def solution_chat():
    global global_prompt
    user_message = request.json['history']
    # image_name = request.json['image_name']
    # if (user_message.length == 1):
    #     return jsonify({ 'response': '请输入问题' })
    general_prompt = """You are a helpful assistant and a professional User experience Designer. You will answer any questions users have about the data. please think step by step. please respond in chinese. and please use the markdown format. thank you. 请根据上文的背景和下面提供的图片和问题，给出回答。"""
    user_message.insert(0, {"role": "system", "content": global_prompt + general_prompt})
    print(user_message)
    path = FILE_ABS_PATH + '/Product UI/' + user_message[1]['content'][1]['image_url'] + '.png';
    image = Image.open(path)
    base64_image = encode_image_to_base64(image)
    image_message = {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/png;base64,{base64_image}"
        }
    }
    user_message[1]['content'][1] = image_message
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=user_message
    )
    print(response)
    get_response = response.choices[0].message.content
    return jsonify({ 'response': get_response });

@app.route('/api/test/GeneratePoint', methods=['POST'])
def generate_point():
    global global_prompt
    info = request.json['info']
    tag = request.json['tag']
    print(info)
    path = FILE_ABS_PATH + '/Product UI/' + info[1]['image_url'] + '.png';
    image = Image.open(path)
    base64_image = encode_image_to_base64(image)
    image_message = {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/png;base64,{base64_image}"
        }
    }
    info[1] = image_message
    get_response = ''
    if tag == 1:
        point_prompt = """As a UX designer well-versed in usability evaluation and product redesign, you have completed usability testing for a product. Please review the <Product Information> for product details and the <Usability Evaluation Information> for insights from the testing. Your task is to develop redesign solutions for selected usability issues according to the guidelines in [Input]. Ensure your communication is UX-focused and easy-to-understand.
        #Generation Optimization#
        Respond concisely,  preferably no more than 80 words.
        Remember that your capabilities are limited. If the instructions exceed your knowledge scope, you should inform users by responding, “Sorry, this instruction is beyond my knowledge scope.’’
        """
        general_prompt = """You are a helpful assistant and a professional User experience Designer. You will answer any questions users have about the data. please think step by step. please respond in chinese. thank you. 请根据上文的背景和下面提供的图片和问题以及input的指引，给出回答。如果input是空的就按照背景和图片和问题随机给出回答。
        格式是 方法：描述
        下面是一个例子，
        增强个性化和定制功能：允许用户通过一个高级工具栏详细定制设计元素，如颜色方案、字体和图像，同时提供实时预览功能以便用户即时看到并调整更改。
        请返回同样格式的内容，不要加上引号，不要加上换行，不要加上前缀，只需要内容，没有前面多余的信息.只返回一个建议。
        """

        user_massage = [{
            "role": "system",
            "content": global_prompt  + point_prompt + general_prompt
        }, {
            "role": "user",
            "content": info
        }]

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=user_massage
        )
        get_response = response.choices[0].message.content
        print(response)
    else:
        metric_prompt = """You are a helpful assistant and a professional User experience Designer. You will answer any questions users have about the data. please think step by step. please respond in chinese. thank you.
        下面给出了两张图片和一个问题，第一张图片是原始设计，第二张图片是最终设计，请分点给出两者的区别，并用一段话来评估最终设计是否能解决可用性问题，这两个信息都用markdown格式。返回一个json对象，包含两个key，change和reflection，value是文字描述，格式如下
        {
            "change": 分点的区别(markdown格式),
            "reflection": 评估最终设计是否能解决可用性问题
        }
        不要加上引号，不要加上换行，不要加上前缀，只需要内容，没有前面多余的信息
        """

        user_message = []
        user_message.append({"role": "system", "content": global_prompt + metric_prompt})

        user_message.append({
            "role": "user",
            "content": info
        })
        print(user_message)
        response = client.chat.completions.create(
            model = "gpt-4o",
            messages = user_message
        )
        print(response)
        get_response = response.choices[0].message.content
    return jsonify({ 'response': get_response })

@app.route('/api/test/EvaluatePoint', methods=['POST'])
def evaluate_point():
    global global_prompt
    info = request.json['info']
    criterion = request.json['criterion']
    path = FILE_ABS_PATH + '/Product UI/' + info[1]['image_url'] + '.png';
    image = Image.open(path)
    base64_image = encode_image_to_base64(image)
    image_message = {
        "type": "image_url",
        "image_url": {
            "url": f"data:image/png;base64,{base64_image}"
        }
    }
    info[1] = image_message
    print(criterion)
    evaluation_prompt = """
    Please review the <Product Information> for product details and the <Usability Evaluation Information> for insights from the testing. Your task is to evaluate all the redesign solutions in the <solution list> proposed by UX designers. Refer to the {}, which specifies the names, definitions, and scales for each criterion on a 1-5 Likert scale. Provide a rating for each selected criterion and justify your rating for each solution. If multiple criteria are selected, ensure to provide separate ratings and justifications for each.
    # """.format(criterion)
    general_prompt = """You are a helpful assistant and a professional User experience Designer. You will answer any questions users have about the data. please think step by step. please respond in chinese. thank you. 请根据上文的背景和下面提供的图片和问题,对input给出评分。返回一个javascript的object，criterion中的value作为Key，内容部分Score：评分，Reason:评分理由。不论criterion中的status是什么，都给出评分。下面是一个例子
    对于美观度的评分
    问题
    用户对brand kit的用途表示困惑，表明界面缺乏清晰度。
    input
    实现交互式教程功能：设计一个交互式教程，引导用户一步一步创建和使用品牌套件，通过实际操作加深理解。
    量表
    {
    "status": false,
    "value": "Criterion_10",
    "label": "美观性",
    "Definition": "美观性评估重设计解决方案的视觉吸引力和设计的和谐性。",
    "Rating_1": "非常低：视觉上不吸引人且不协调。",
    "Rating_2": "低：视觉吸引力有限，设计有些不一致。",
    "Rating_3": "中等：视觉上令人满意且大体上一致。",
    "Rating_4": "高：视觉吸引力强且设计元素协调。",
    "Rating_5": "非常高：极具吸引力且设计完全和谐。"
    }
    返回的数据
    {
        "Criterion_10": {
            "Score": 4,
            "Reason": "交互式教程增加了界面的动态性和吸引力。"
        }
    }
    请返回同样格式的内容，不要加上引号，不要加上换行，不要加上前缀，只需要内容，没有前面多余的信息.只返回一个建议。对criterion中的每一个都要给出评分，如果里面有10个指标，就必须给出10个评分。
    """

    user_message = [{
        "role": "system",
        "content": global_prompt + evaluation_prompt + general_prompt
    }, {
        "role": "user",
        "content": info
    }]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=user_message
    )
    print(response)
    get_response = response.choices[0].message.content
    return jsonify({ 'response': get_response })

@app.route('/api/test/AddMetric', methods=['POST'])
def add_metric():
    label = request.json['label']
    metric_prompt = """You are a helpful assistant and a professional User experience Designer. You will answer any questions users have about the data. please think step by step. please respond in chinese. thank you.
    请给出输入的指标的定义，并且对于这个指标分为5级，给出每一级的描述，参照下面的内容
    {
    "label": "美观性",
    "Definition": "美观性评估重设计解决方案的视觉吸引力和设计的和谐性。",
    "Rating_1": "非常低：视觉上不吸引人且不协调。",
    "Rating_2": "低：视觉吸引力有限，设计有些不一致。",
    "Rating_3": "中等：视觉上令人满意且大体上一致。",
    "Rating_4": "高：视觉吸引力强且设计元素协调。",
    "Rating_5": "非常高：极具吸引力且设计完全和谐。"
    }
    返回同样格式的内容，返回形式应该是javascript的object对象形式
    """
    user_message = []
    user_message.append({"role": "system", "content": metric_prompt})
    user_message.append({
        "role": "user",
        "content": label
    })
    print(user_message)
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = user_message
    )
    print(response)
    get_response = response.choices[0].message.content
    # get_response = 'aaa'
    return jsonify({ 'response': get_response })

# @app.route('/api/test/ReflectDesign', methods=['POST'])
# def reflect_result():
#     global global_prompt

#     info = request.json['info']
#     print(info)
#     # path = FILE_ABS_PATH + '/Product UI/' + info[1]['image_url'] + '.png';
#     # image = Image.open(path)
#     # base64_image = encode_image_to_base64(image)
#     # image_message = {
#     #     "type": "image_url",
#     #     "image_url": {
#     #         "url": f"data:image/png;base64,{base64_image}"
#     #     }
#     # }
#     # info[1] = image_message

#     # metric_prompt = """You are a helpful assistant and a professional User experience Designer. You will answer any questions users have about the data. please think step by step. please respond in chinese. thank you.
#     # 下面给出了两张图片和一个问题，第一张图片是原始设计，第二张图片是最终设计，请分点给出两者的区别，并用一段话来评估最终设计是否能解决可用性问题，这两个信息都用markdown格式。返回一个json对象，包含两个key，change和reflection，value是文字描述，格式如下
#     # {
#     #     "change": 分点的区别,
#     #     "reflection": 评估最终设计是否能解决可用性问题
#     # }
#     # 不要加上引号，不要加上换行，不要加上前缀，只需要内容，没有前面多余的信息
#     # """

#     # user_message = []
#     # user_message.append({"role": "system", "content": global_prompt + metric_prompt})

#     # user_message.append({
#     #     "role": "user",
#     #     "content": info
#     # })
#     # print(user_message)
#     # response = client.chat.completions.create(
#     #     model = "gpt-4o",
#     #     messages = user_message
#     # )
#     # print(response)
#     # get_response = response.choices[0].message.content
#     get_response = 'aaa'
#     return jsonify({ 'response': get_response })



def read_json(add):
    with open(add, 'rt', encoding="utf-8") as f:
        cr = json.load(f)
    f.close()
    return cr

if __name__ == '__main__':
    app.run(debug=True)
    

