import json

# 读取原始 JSON 数据
with open('info_t.json', 'r') as file:
    json_data = json.load(file)

# 递归函数，用于遍历 JSON 数据并添加 default 属性
def add_default_property(data):
    for dd in data:
        print(dd)
        for d in data[dd]['info']:
            
                # "status": 0,
                # "vision": 0,
                # "repeat_status": 0,
            d['vision'] = 0
            d['repeat_status'] = 0
            d['default'] = {
                "description": d['description'],
                "tag": d['tag'],
                "second_tag": d['second_tag'],
                "reason": d['reason'],
                "unique_tag": d['unique_tag'],
                "user_said": d['user_said'],
            }
    # if isinstance(data, dict):
    #     if 'unique_tag' in data:
    #         # 添加 default 属性并复制相关字段
    #         data['default'] = {
    #             'description': data.get('description'),
    #             'tag': data.get('tag'),
    #             'second_tag': data.get('second_tag'),
    #             'reason': data.get('reason'),
    #             'unique_tag': data.get('unique_tag'),
    #             'user_said': data.get('user_said')
    #         }
    #     # 递归处理字典中的每个值
    #     for key, value in data.items():
    #         add_default_property(value)
    # elif isinstance(data, list):
    #     # 递归处理列表中的每个元素
    #     for item in data:
    #         add_default_property(item)
    # print(data)
    return data

res_data = add_default_property(json_data)

with open('output.json', 'w') as file:
    json.dump(res_data, file, indent=4, ensure_ascii=False)


# print()