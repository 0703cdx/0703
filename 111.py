import streamlit as st
st.title("作业-陈达熙")
st.header("开始")
st.text("沟通是一件很棒的事情")
st.header("上")
st.subheader('战士,刺客',anchor='shanxi')
st.text('你的任务是,带线,切C,推塔,带领队伍获得胜利.')
st.header("中",anchor='area')
st.subheader('法师')
st.text('你的任务是,支援,后排输出,控场,推搭,带领队伍获得胜利.')
st.header("下",anchor='linfen')
st.subheader('射手')
st.text('你的任务是,发育后排输出,推塔,带领队伍获得胜利.')
st.subheader('python代码块')
python_code = '''def helloa():
print("你好!")
'''

st.code(python_code, language=None)

st.markdown('# 获胜')
st.markdown('## 获胜')
st.markdown('### 获胜')
st.markdown('#### 获胜')
st.markdown('##### 获胜')
st.markdown('###### 获胜')

st.markdown('*获胜*')

st.markdown('**获胜**')

st.markdown('***获胜***')
  

import pandas as pd   # 导入Pandas并用pd代替
import streamlit as st  # 导入Streamlit并用st代表它

# 定义数据,以便创建数据框
data = {
    '上':[4, 8, 10, 20, 2],
    '中':[4, 8, 10, 20, 2],
    '下':[4, 8, 10, 20, 2],

}
# 定义数据框所用的索引
index = pd.Series(['04', '08', '10', '20', '2'], name='时间')
# 根据上面创建的data和index，创建数据框
df = pd.DataFrame(data, index=index)

st.subheader('静态表')
st.table(df)
