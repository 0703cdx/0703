import streamlit as st

# 设置页面布局
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
    col1, col2 = st.columns(2)
    with col2:
        st.image("https://via.placeholder.com/400x200?text=学生数据可视化图表", use_column_width=True)  # 实际使用时替换为真实图表

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
        st.write("Pandas\nNumPy")
    with col8:
        st.markdown("**可视化**")
        st.write("Plotly\nMatplotlib")
    with col9:
        st.markdown("**机器学习**")
        st.write("Scikit-learn")
