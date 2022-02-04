from email.mime import image
import imp
import pandas as pd
import streamlit as st

# https://partrita.github.io/posts/altair/ 참고 - Altair로 시각화하기
import altair as alt # Altair는 Vega 및 Vega-Lite에 기반한 Python용 선언적 통계 시각화 라이브러리입니다
from PIL import Image # 이미지 처리 라이브러리 / 이미지 불러올때 사용함
import base64


#맨 위 상단에 이미지 삽입
# image = Image.open('https://github.com/SEONGJAE-YOO/streamlit_AI_BigData_project/blob/main/dna-app/dna-logo.png')

# st.image('https://drive.google.com/file/d/1vCdI8oJd_UNEJ50-qLc26w4HzNAg3U8k/view?usp=sharing')

#  image_url = os.path.join(DATA_URL_ROOT, selected_frame)
#  image = load_image(image_url)

# st.markdown("[![dna-logo](https://drive.google.com/file/d/1vCdI8oJd_UNEJ50-qLc26w4HzNAg3U8k/view?usp=sharing)](https://drive.google.com/file/d/1vCdI8oJd_UNEJ50-qLc26w4HzNAg3U8k/view?usp=sharing)")

# #centered
# st.markdown(
#     """<a style='display: block; text-align: center;' href="https://github.com/SEONGJAE-YOO/streamlit_AI_BigData_project/blob/main/dna-app/dna-logo.png">dnalogo</a>
#     """,
#     unsafe_allow_html=True,
# )

# image = """

# ![https://github.com/SEONGJAE-YOO/streamlit_AI_BigData_project/blob/main/dna-app/dna-logo.png](https://github.com/SEONGJAE-YOO/streamlit_AI_BigData_project/blob/main/dna-app/dna-logo.png)

# """

# st.markdown(image)

# 위에 소스는 시행착오 한 내용입니다. 시행착오 후 밑에 소스가 이미지가 잘 나타났습니다.

LOGO_IMAGE = "dna-logo.png"

st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
        font-weight:700 !important;
        font-size:50px !important;
        color: #f9a01b !important;
        padding-top: 75px !important;
    }
    .logo-img {
        float:right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
        <p class="logo-text">dna-logo</p>
    </div>
    """,
    unsafe_allow_html=True
)



# 글 쓰기 
st.write("""
# DNA Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
***
""")


######################
# Input Text Box
######################

#st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines() # 여러라인으로 구분되어 있는 문자열을 한라인씩 분리하여 리스트로 반환
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
***
""")

## Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

## DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Print dictionary
st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)

#X_label = list(X)
#X_values = list(X.values())

X

### 2. Print text
st.subheader('2. Print text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

### 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)


st.write("""
# Copyright 2022. SeongJae Yu all rights reserved. (유성재 포토폴리오)
""")