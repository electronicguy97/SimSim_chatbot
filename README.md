![구현화면](https://github.com/electronicguy97/SimSim_chatbot/assets/103613730/e5c18ae0-6495-453e-9a7b-9d9689462ca2)


## 사용된 학습 모델

SentenceBERT [jhgan/ko-sroberta-multitask](https://huggingface.co/jhgan/ko-sroberta-multitask)

문장변환용으로 사용

## Dataset

[대화 스크립트 데이터셋](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-006)

## Dependency

- streamlit
- streamlit-chat
- pandas
- sentence-transformers
- scikit-learn

## 경고문
성능향상을 위한 allow_output_mutationcache를 사용하기 위해 steamlit의 cache를 사용
@st.cache_data(ttl=300)  # 캐시 유지 시간을 설정할 수 있음 (초 단위) 또는
@st.cache_resource() 사용하여 경고문을 제거 할 수 있습니다.
