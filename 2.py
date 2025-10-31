import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# 设置输出右对齐，防止中文不对齐
pd.set_option('display.unicode.east_asian_width', True)

def get_dataframe_from_csv():
    # 读取指定路径的CSV文件
    df = pd.read_csv('D:\\cdx_env\\student_data_adjusted_rounded.csv')
    return df

# 读取数据
df = get_dataframe_from_csv()

# ========== 处理分类变量（性别、专业）并训练模型 ==========
# 定义特征：数值特征 + 分类特征
numeric_features = ['每周学习时长（小时）', '上课出勤率', '作业完成率', '期中考试分数']
categorical_features = ['性别', '专业']

# 构建预处理管道：对分类变量进行独热编码
preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ]
)

# 构建模型管道：预处理 + 线性回归
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

# 训练模型
target = df['期末考试分数']
model.fit(df, target)

# ========== 期末成绩预测交互面板（含性别、专业选择） ==========
st.header("期末成绩预测")
st.markdown("请输入学生的学习行为、性别及专业信息，系统将预测其期末成绩")

# 数值特征输入
study_hours = st.number_input("每周学习时长（小时）", min_value=0.0, max_value=50.0, value=20.0, step=0.1)
attendance = st.number_input("上课出勤率", min_value=0.0, max_value=1.0, value=0.8, step=0.01)
homework = st.number_input("作业完成率", min_value=0.0, max_value=1.0, value=0.8, step=0.01)
midterm = st.number_input("期中考试分数", min_value=0.0, max_value=100.0, value=70.0, step=0.1)

# 分类特征选择（性别、专业）
gender = st.selectbox("性别", df['性别'].unique())
major = st.selectbox("专业", df['专业'].unique())

# 预测按钮
if st.button("预测期末成绩"):
    # 构造输入数据
    input_data = pd.DataFrame({
        '每周学习时长（小时）': [study_hours],
        '上课出勤率': [attendance],
        '作业完成率': [homework],
        '期中考试分数': [midterm],
        '性别': [gender],
        '专业': [major]
    })
    # 预测期末成绩
    predicted_score = model.predict(input_data)[0].round(1)
    # 展示预测结果
    st.success(f"预测期末成绩：{predicted_score} 分")
