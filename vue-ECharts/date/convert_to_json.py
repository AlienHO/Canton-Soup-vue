import pandas as pd
import json

# 读取 CSV 文件
data = pd.read_csv('path_to_your_data.csv')

# 创建颜色映射，根据四性的值映射到具体的颜色代码
color_map = {
    1: '#81B2D3',
    2: '#B6D399',
    3: '#EFF186',
    4: '#F0C479',
    5: '#E7A380'
}

# 将四性的数值映射到颜色
data['color'] = data['四（五）性'].map(color_map)

# 创建 JSON 数据
chart_data = {
    'x': data['四（五）性'].tolist(),
    'y': data['五味'].tolist(),
    'size': data['引用次数'].tolist(),
    'color': data['color'].tolist(),
    'name': data['材料名称'].tolist(),
    'description': data['描述'].tolist()
}

# 将数据写入 JSON 文件
with open('chart_data.json', 'w') as f:
    json.dump(chart_data, f, ensure_ascii=False)
