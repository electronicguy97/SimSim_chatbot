import streamlit as st
from streamlit_chat import message
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

@st.cache(allow_output_mutation=True) # 최초 한번만 로드(계속 로드시 시간이 길어짐)
def cached_model():
    model = SentenceTransformer('jhgan/ko-sroberta-multitask')
    return model

@st.cache(allow_output_mutation=True) # 1번만 로드
def get_dataset():
    df = pd.read_csv('chatbot_embedding.csv')
    df['embedding'] = df['embedding'].apply(json.loads)
    return df

model = cached_model()
df = get_dataset()

st.header('심심 챗봇')

#session을 이용해서 초기화
if 'AI' not in st.session_state:
    st.session_state['AI'] = [] # 챗봇 대화 내용 저장을 위해  생성

if 'User' not in st.session_state:
    st.session_state['User'] = [] # 유저 대화 내용 저장

with st.form('form', clear_on_submit=True): #텍스트 입력 창
    user_input = st.text_input('User: ', '')
    submitted = st.form_submit_button('전송')

if submitted and user_input:
    embedding = model.encode(user_input)

    df['distance'] = df['embedding'].map(lambda x: cosine_similarity([embedding], [x]).squeeze()) # cos유사도로 구별
    answer = df.loc[df['distance'].idxmax()]

    st.session_state.User.append(user_input)
    st.session_state.AI.append(answer['챗봇'])

for i in range(len(st.session_state['User'])):
    message(st.session_state['User'][i], is_user=True, key=str(i) + '_user')
    if len(st.session_state['AI']) > i:
        message(st.session_state['AI'][i], key=str(i) + '_bot')
