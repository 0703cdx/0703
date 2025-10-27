import streamlit as st
import pandas as pd

st.title("作业整合")
st.header("很胡乱的作业")
st.text('充斥这无比多的错误,明明清楚也懒得改正了.')

st.title("选项卡简单示例")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["选项卡1", "选项卡2", "选项卡3", "选项卡4","选项卡5"])

with tab1:
    st.set_page_config(page_title='动物园', page_icon='🐒')

    images = [{'url': 'https://hakaimagazine.com/wp-content/uploads/header-proboscis-monkeys.jpg','属性':'成龙'},{
          'url': 'https://www.pennlive.com/resizer/2s9yGlOJZ434P62jhjJw9ngtS8w=/1280x0/smart/advancelocal-adapter-image-uploads.s3.amazonaws.com/image.pennlive.com/home/penn-media/width2048/img/nation-world/photo/monkeyjpg-f0a30582aef21f0b.jpg','属性':'笑'},
          {'url': 'https://wallpapers.com/images/hd/cute-monkey-photo-in-the-shrub-0j8nj9zrmgtu7g4o.jpg','属性':'思索'}]

    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0

    def nextImg():
        st.session_state['ind'] = ( st.session_state['ind'] + 1) % len(images)

    def nextIng():
        st.session_state['ind'] = ( st.session_state['ind'] - 1) % len(images)
    
    st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['属性'])


    a1,a2 = st.columns(2)

    with a1:
        st.button('下一张', on_click=nextImg)
    with a2:
        st.button('上一张', on_click=nextIng)

with tab2:
    st.set_page_config(page_title='音乐播放器', page_icon='♪')

    st.title("音乐播放器")



    audios = [{'url': 'https://music.163.com/song/media/outer/url?id=2619645822.mp3',
          '歌手':'歌手:chilichili',
          '图片':'https://p2.music.126.net/_HtQxqke4nRbWPsA86TCUg==/109951169894151597.jpg?param=500y500',
          '歌名':'搬家前,短暂夜',
          '时长':'时长:3:32'
          },{
          'url': 'https://music.163.com/song/media/outer/url?id=569214247.mp3',
          '歌手':'歌手:毛不易',
         '图片':'https://p2.music.126.net/vmCcDvD1H04e9gm97xsCqg==/109951163350929740.jpg?param=500y500',
          '歌名':'平凡的一天',
          '时长':'时长:4:36'
          },
          {'url': 'https://music.163.com/song/media/outer/url?id=1293886117.mp3',
           '歌手':'歌手:李荣浩',
           '图片':'https://p2.music.126.net/tt8xwK-ASC2iqXNUXYKoDQ==/109951163606377163.jpg?param=500y500',
           '歌名':'年少有为',
           '时长':'时长:4:39'           }]


    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0

    def nextImg():
        st.session_state['ind'] = ( st.session_state['ind'] + 1) % len(audios)

    def nextIng():
        st.session_state['ind'] = ( st.session_state['ind'] - 1) % len(audios)
  
    c1,c2 = st.columns([1,3])
    with c1:
        st.image(audios[st.session_state['ind']]['图片'])


    with c2:
        st.subheader(audios[st.session_state['ind']]['歌名'])
        st.text(audios[st.session_state['ind']]['歌手'])
        st.text(audios[st.session_state['ind']]['时长'])
        st.audio(audios[st.session_state['ind']]['url'])
        a1,a2 = st.columns(2)

        with a1:
            st.button('下一首', on_click=nextImg)
        with a2:
            st.button('上一首', on_click=nextIng)

with tab3:
    sp = [{'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/34/85/33154468534/33154468534-1-192.mp4?e=ig8euxZM2rNcNbNghWdVhwdlhbN1hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&nbs=1&trid=74cbd49c893a4aa0bac472984c808dah&deadline=1761302119&gen=playurlv3&og=hw&uipk=5&mid=0&oi=771356656&platform=html5&os=cosovbv&upsig=43602af0b568a5251dbb945f1dcbd693&uparams=e,nbs,trid,deadline,gen,og,uipk,mid,oi,platform,os&bvc=vod&nettype=0&bw=1769954&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
          'title':'CFO vs AL',
          'episode':'1',
       '介绍':'介绍:CFO vs AL,瑞士轮第一局,中国队最有希望的一年'
          
          },{
          'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/47/91/33155909147/33155909147-1-192.mp4?e=ig8euxZM2rNcNbNg7WdVhwdlhbNBhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&nbs=1&oi=771356656&mid=0&trid=0450aacb81af4e3aa601d0fb9f4044bh&gen=playurlv3&os=cosovbv&og=cos&uipk=5&deadline=1761302158&platform=html5&upsig=6b44c9e3a91747053cc12a9bcd4ef91d&uparams=e,nbs,oi,mid,trid,gen,os,og,uipk,deadline,platform&bvc=vod&nettype=0&bw=1801790&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
          'title':'CFO vs AL',
         'episode':'2',
          '介绍':'介绍:CFO vs AL,瑞士轮第二局,中国队最有希望的一年'
          },
          {'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/19/21/33157222119/33157222119-1-192.mp4?e=ig8euxZM2rNcNbNghwdVhwdlhbNVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1761302200&nbs=1&os=cosovbv&og=hw&uipk=5&oi=771356656&platform=html5&trid=0351b6252092427ca88add2eee92cfbh&mid=0&gen=playurlv3&upsig=1dfd335405234a08206007228ecc8761&uparams=e,deadline,nbs,os,og,uipk,oi,platform,trid,mid,gen&bvc=vod&nettype=0&bw=1764225&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
           'title':'CFO vs AL',
           'episode':'3',
           '介绍':'介绍:CFO vs AL,瑞士轮第三局,中国队最有希望的一年'        }]


    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0

    st.title(sp[st.session_state['ind']]['title'] + '-第' + sp[st.session_state['ind']]['episode'] + '局')
    st.video(sp[st.session_state['ind']]['url'])

    a1, a2, a3 = st.columns(3)


    def play(see):
    
        st.session_state['ind'] = int(see) 
    
    for i in range(len(sp)):
       st.button('第' + str(i + 1) + '局', on_click=play, args=([i]))

    st.text(sp[st.session_state['ind']]['介绍'])

with tab4:
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
        ['中文', '英语', '法语', '俄语', '日语', '阿拉伯语'],
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
       
            s=''
            for i in options_1:
                s =s + i +","

            st.write("语言能力:", s)
        
            v=''
            for r in zz:
                v =v + r +","
            st.write("技能:", v)
            st.write("期望薪资:", values)
        st.write("个人简历:", init_text)
with tab5:
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
