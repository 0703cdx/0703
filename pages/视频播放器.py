import streamlit as st



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

# 显示视频s
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
















                                                            
