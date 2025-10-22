import streamlit as st
import pandas as pd

# 页面设置蜜雪冰城
st.set_page_config(page_title="南宁地图")
st.title("🍔 南宁蜜雪冰城探索")

# 介绍
st.markdown("""
探索广西南宁最受欢迎的蜜雪冰城地点！选择你感兴趣的餐厅类型，查看价格和位置。
""")

# 餐厅数据
restaurants = pd.DataFrame({
    "店面": ["百盛店", "西大地铁站店", "西乡塘市场店", "安吉万达金街店", "正恒店"],
    "类型": ["饮料", "饮料", "饮料", "饮料", "饮料"],
    "评分": [4.2, 4.5, 4.0, 4.7, 4.3],
    "人均消费(元)": [15, 13, 10, 8, 6],
    "位置X": [22.815376, 22.289747, 22.246386, 22.291924, 22.832483],
    "位置Y": [108.321088, 108.289747, 108.246386, 108.291924, 108.299900]
})

# 1. 带点的地图 - 餐厅位置
st.header(" 南宁蜜雪冰城地图")

st.map(pd.DataFrame({
    "lat": restaurants["位置X"],
    "lon": restaurants["位置Y"],
    "店面": restaurants["店面"]
}))

st.header("⭐ 店面评分")
st.bar_chart(restaurants.set_index("店面")["评分"])



df = pd.DataFrame(restaurants)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3, 4, 5], name='店面')
# 将新索引应用到数据框上
df.index = index
st.write(df)
st.header("人均价格")
st.subheader("位置")
st.line_chart(df, x='店面')


data = {
    "月份":['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
    "百盛店":['11', '15', '12', '24', '22', '23', '21', '24', '14', '12', '11', '15'],             
    "西大地铁站店":['11', '18', '12', '23', '15', '22', '11', '22', '11', '22', '21', '14'],
    "西乡塘市场店":['14', '15', '14', '24', '25', '18', '21', '22', '20', '23', '12', '20'],
    "安吉万达金街店":['14', '11', '15', '23', '26', '22', '11', '10', '15', '22', '20', '19'],
    "正恒店":['15', '13', '16', '15', '20', '12', '21', '12', '11', '25', '22', '11'],
}
    
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], name='序号')
 # 将新索引应用到数据框上

df.index = index
st.subheader("价格走势")
# 通过x指定月份所在这一列为折线图的x轴
st.line_chart(df, x='月份')

# 修改df，用月份列作为df的索引，替换原有的索引
df.set_index('月份', inplace=True)


st.header("门店数据")
# 使用write()方法展示数据框
st.write(df)
st.header("面积图")
df = pd.DataFrame(data)
# 定义数据框所用的新索引
index = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], name='序号')
 # 将新索引应用到数据框上
df.index = index
st.area_chart(df, x='月份')
df.set_index('月份', inplace=True)
st.subheader("设置y参数")
# 通过y参数筛选只显示1号门店的数据
st.area_chart(df, y='百盛店')
# 通过y参数筛选只显示2、3号门店的数据
st.area_chart(df, y=['西大地铁站店','西乡塘市场店'])





