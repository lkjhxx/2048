# 2048

纯 Python 实现\
使用 Arcade 绘图\
后续会将注释补上

## 环境需求：

Python >= 3.9.11\
Arcade >= 2.6.15\
以上版本为本人自用版本，未测试低版本是否可行

## 项目结构：

2048 \
|-- animate \
|&ensp;|-- \_\_init__.py \
|&ensp;|-- animate_list.py &ensp;&emsp; 动画类，存放图形移动的代码 \
|  \
|-- components \
|&ensp;|-- \_\_init__.py \
|&ensp;|-- number.py &emsp;&emsp;&emsp; 数字块，存放数字信息以及位置信息 \
|  \
|-- core \
|&ensp;|-- \_\_init__.py \
|&ensp;|-- my_game.py &nbsp;&ensp;&emsp; 主循环，存放核心代码 \
|  \
|-- graphics  \
|&ensp;|-- \_\_init__.py \
|&ensp;|-- rectangle.py &nbsp;&emsp;&emsp; 矩形，存放矩形位置和颜色 \
|&ensp;|-- text.py &nbsp;&ensp;&emsp;&emsp;&emsp;&emsp; 文本，存放文本位置即相关信息 \
|  \
|-- position  \
|&ensp;|-- \_\_init__.py \
|&ensp;|-- position.py &ensp;&emsp;&emsp;&emsp;存放位置信息 \
|  \
|-- LICENSE \
|-- main.py &emsp;&emsp;&emsp;&emsp;&emsp; 程序入口 \
|-- README.md &ensp;&emsp;&emsp; 自述文件