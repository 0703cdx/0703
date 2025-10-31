import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import plotly.graph_objects as go

page = st.sidebar.selectbox("选择页面", ["项目介绍", "专业数据分析", "成绩预测"])

if page == "项目介绍":
    st.set_page_config(layout="wide")

# ---- 标题部分 ----
    st.title("📊 学生成绩分析与预测系统")

# ---- 项目概述部分 ----
    with st.container():
        st.markdown("---")
        st.subheader("📋 项目概述")
        st.write(
            "本项目是一个基于Streamlit的学生成绩分析平台，通过数据可视化和机器学习技术，帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩。"
        )
        st.subheader("主要特点：")
        features = [
            "📊 数据可视化：多维度展示学生学业表现",
            "🔍 专业分析：找出学生的知识薄弱点分析",
            "🤖 智能预测：基于机器学习模型的成绩预测",
            "🎯 学习建议：根据预测结果提供个性化反馈"
        ]
        for feat in features:
            st.write(feat)

# ---- 右侧图表展示（模拟）----
        
# ---- 项目目标部分 ----
    with st.container():
        st.markdown("---")
        st.subheader("🚀 项目目标")
        col3, col4, col5 = st.columns(3)
        with col3:
            st.markdown("#### 🎯 目标一\n分析影响因素")
            st.write("- 识别关键学习指标")
            st.write("- 探索成绩相关因素")
            st.write("- 提供数据支持决策")
        with col4:
            st.markdown("#### 🎯 目标二\n可视化展示")
            st.write("- 专业对比分析")
            st.write("- 作业预测等研究")
            st.write("- 学习模式识别")
        with col5:
            st.markdown("#### 🎯 目标三\n成绩预测")
            st.write("- 机器学习模型")
            st.write("- 个性化预测")
            st.write("- 及时干预预警")

# ---- 技术架构部分 ----
    with st.container():
        st.markdown("---")
        st.subheader("⚙️ 技术架构")
        col6, col7, col8, col9 = st.columns(4)
        with col6:
            st.markdown("**前端框架**")
            st.write("Streamlit")
        with col7:
            st.markdown("**数据处理**")
            st.write('''Pandas

NumPy''')
        with col8:
            st.markdown("**可视化**")
            st.write('''Plotly

Matplotlib''')
        with col9:
            st.markdown("**机器学习**")
            st.write("Scikit-learn")

elif page == "专业数据分析":
    pd.set_option('display.unicode.east_asian_width', True)

    def get_dataframe_from_csv():
        
    # 读取指定路径的CSV文件
        df = pd.read_csv('D:\\cdx_env\\student_data_adjusted_rounded.csv')
        return df

# 读取数据
    df = get_dataframe_from_csv()

# ========== 1. 性别比例（图表左、数据右） ==========
    st.header("1. 性别比例数据")
    gender_count = df.groupby(['专业', '性别'])['学号'].count().reset_index(name='人数')
    total_count = gender_count.groupby('专业')['人数'].sum().reset_index(name='总人数')
    merged = pd.merge(gender_count, total_count, on='专业')
    merged['占比(%)'] = (merged['人数'] / merged['总人数'] * 100).round(1)
    pivot_gender = merged.pivot(index='专业', columns='性别', values='占比(%)').reset_index()
    pivot_gender.columns.name = None

    col_chart1, col_data1 = st.columns([2, 1])
    with col_chart1:
        fig_gender = go.Figure()
        for gender in gender_count['性别'].unique():
            gender_df = gender_count[gender_count['性别'] == gender]
            fig_gender.add_trace(go.Bar(
                x=gender_df['专业'],
                y=gender_df['人数'],
                name=gender,
                marker_color='blue' if gender == '男' else 'lightblue'
            ))
        fig_gender.update_layout(title='各专业男女性别分布', xaxis_title='专业', yaxis_title='人数', barmode='group')
        st.plotly_chart(fig_gender, use_container_width=True)
    with col_data1:
        st.table(pivot_gender)

# ========== 2. 详细数据（图表左、数据右） ==========
    st.header("2. 详细数据")
    grouped_detail = df.groupby('专业').agg({
        '每周学习时长（小时）': 'mean',
        '期中考试分数': 'mean',
        '期末考试分数': 'mean'
    }).round(1).reset_index()
    grouped_detail.columns = ['major', 'study_hours', 'midterm_score', 'final_score']

    col_chart2, col_data2 = st.columns([2, 1])
    with col_chart2:
        study_metric = df.groupby('专业').agg({
            '每周学习时长（小时）': 'mean',
            '期中考试分数': 'mean',
            '期末考试分数': 'mean'
        }).reset_index()
        study_metric['平均考试成绩'] = (study_metric['期中考试分数'] + study_metric['期末考试分数']) / 2
        study_metric = study_metric.round(1)

        fig_study = go.Figure()
        fig_study.add_trace(go.Line(
            x=study_metric['专业'],
            y=study_metric['每周学习时长（小时）'],
            name='平均学习时长（小时）',
            marker_color='orange'
        ))
        fig_study.add_trace(go.Line(
            x=study_metric['专业'],
            y=study_metric['平均考试成绩'],
            name='平均考试成绩',
            marker_color='green',
            yaxis='y2'
        ))
        fig_study.update_layout(
            title='各专业平均学习时长与成绩对比',
            xaxis_title='专业',
            yaxis_title='平均学习时长（小时）',
            yaxis2=dict(
                title='平均考试成绩',
                overlaying='y',
                side='right'
            )
        )
        st.plotly_chart(fig_study, use_container_width=True)
    with col_data2:
        st.table(grouped_detail)

# ========== 3. 出勤率排名（图表左、数据右） ==========
    st.header("3. 出勤率排名")
    attendance_rank = df.groupby('专业')['上课出勤率'].mean().reset_index()
    attendance_rank.columns = ['专业', '平均出勤率']
    attendance_rank['平均出勤率'] = (attendance_rank['平均出勤率'] * 100).round(1)
    attendance_rank = attendance_rank.sort_values(by='平均出勤率', ascending=False).reset_index(drop=True)

    col_chart3, col_data3 = st.columns([2, 1])
    with col_chart3:
        attendance_heat = attendance_rank[['专业', '平均出勤率']]
        fig_heat = px.treemap(
            attendance_heat,
            path=['专业'],
            values='平均出勤率',
            color='平均出勤率',
            color_continuous_scale=['#FFD700', '#90EE90', '#48D1CC', '#4682B4', '#4169E1', '#483D8B'],
            title='各专业平均出勤率(%)',
            labels={'平均出勤率': '平均出勤率(%)'}
        )
        fig_heat.update_layout(margin=dict(t=50, l=20, r=20, b=20))
        st.plotly_chart(fig_heat, use_container_width=True)
    with col_data3:
        st.table(attendance_rank)

# ========== 4. 大数据管理专业专项分析（保持原布局） ==========
    st.header("4. 大数据管理专业专项分析")
    bdm_df = df[df['专业'] == '大数据管理']
    attendance_bdm = bdm_df['上课出勤率'].mean() * 100
    score_bdm = (bdm_df['期中考试分数'].mean() + bdm_df['期末考试分数'].mean()) / 2
    gpa_bdm = 98.8  
    study_hours_bdm = bdm_df['每周学习时长（小时）'].mean()

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("平均出勤率", f"{attendance_bdm:.1f}%")
    with col2:
     st.metric("平均总成绩", f"{score_bdm:.1f}分")
    with col3:
        st.metric("总绩点", f"{gpa_bdm}%")
    with col4:
        st.metric("平均学习时长", f"{study_hours_bdm:.1f}小时")

    col_chart4, col_chart5 = st.columns(2)
    with col_chart4:
        fig_score = px.histogram(
            bdm_df,
            x='期末考试分数',
            title='大数据管理专业总成绩分布',
            labels={'期末考试分数': '总成绩'},
            color_discrete_sequence=['green']
        )
        st.plotly_chart(fig_score, use_container_width=True)
    with col_chart5:
        fig_hours = px.box(
            bdm_df,
            y='每周学习时长（小时）',
            title='大数据管理专业平均学习时长分布',
            color_discrete_sequence=['green']
            )
        st.plotly_chart(fig_hours, use_container_width=True)

else:
    st.title("成绩预测")
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
    
