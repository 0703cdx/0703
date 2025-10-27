import streamlit as st


def my_format_func(option):
    return f'选{option}'

st.header('个人信息生成器')
a1, a2= st.columns([1,2])

with a1:
    st.subheader('个人信息表单')
    name = st.text_input('姓名', autocomplete='这是一个占位字符串')

    aa = st.text_input('职位', placeholder='这是一个占位字符串',key="1")

    bb = st.text_input('电话', placeholder='这是一个占位字符串',key='2')

    dd = st.text_input('邮箱', placeholder='这是一个占位字符串')

    date = st.date_input("生日", value=None)
    st.write("你选择的日期是:", date)
 
    st.text('性别')
    lunch = st.radio(
    '你的性别是什么',
    ['男', '女', '其他'],
    horizontal=True,
    label_visibility='hidden'
    )

    
    city = st.selectbox('学历：', ['初中', '高中', '职高', '本科', '大专', '硕士', '博士'],  index=6)

    
    options_1 = st.multiselect(
    '语言能力(可多选）',
    ['中文', '英语', '法语', '俄语', '西班牙语', '阿拉伯语'],
    ['中文'],
    max_selections=6)


    zz= st.multiselect(
    '技能(可多选)',
    ['SQL', 'Python', 'Java', 'JavaScript', 'HTML\CSS', '数据分析', '机械学习', '深度学习'],
    ['Python', 'Java'],
    format_func=my_format_func,
    )

    my_range = range(1, 21)

    numbers = st.select_slider('工作经验', options=my_range, value=5)
    
    values = st.slider(
    '期望薪资',
    5000.0, 50000.0, (10000.0, 20000.0))

    
    init_text = ""
    st.text_area(label='个人简历:', value=init_text,
            height=200, max_chars=20000)
    from datetime import datetime, time
    w = st.time_input("最佳联系时间", time(8, 45))
    uploaded_file = st.file_uploader('图片', type=['jpg', 'jpeg', 'png', ])
    

with a2:
    st.subheader('实时预览')
    st.write("图片:", uploaded_file)
    if uploaded_file is not None:
        st.image(uploaded_file, width=150, caption="图片")
    c1, c2, c3= st.columns([1,1,1])
    with c1:
        st.write("职位:", aa)
        st.write("电话:", bb)
        st.write("邮箱:", bb)
        st.write("生日:", date)
        st.write("最佳联系时间:", w)
    with c2:
        st.write("姓名:", name)
        st.write("性别:", lunch)
        st.write("学历:", city)
        st.write("工作经验:", numbers)
        
    with c3:
        st.write("语言能力:", options_1)
        s=''
        for i in options_1:
            s =s + i
        st.write("技能:", zz)
        st.write("期望薪资:", values)
    st.write("个人简历:", init_text)  
  
    
    
    
    
