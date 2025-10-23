import streamlit as st

st.set_page_config(page_title='动物园', page_icon='🐒')

# 图片数组
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
