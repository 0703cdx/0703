import streamlit as st
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

    

   




