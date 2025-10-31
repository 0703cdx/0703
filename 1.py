import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# 设置输出右对齐，防止中文不对齐
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
