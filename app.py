import streamlit as st
import pandas as pd
import altair as alt
from streamlit_echarts import st_echarts
import numpy as np
import math

# --- 헤더 옆 링크 아이콘 숨기기 (파일 최상단) ---
st.markdown("""
    <style>
        /* 최신 Streamlit 버전 타겟 */
        a[data-testid="anchor-link"] {
            display: none !important;
            visibility: hidden !important;
        }
        /* 구버전 Streamlit 대비 */
        h1 a.anchor-link, h2 a.anchor-link, h3 a.anchor-link,
        h4 a.anchor-link, h5 a.anchor-link, h6 a.anchor-link {
            display: none !important;
            visibility: hidden !important;
        }
    </style>
    """, unsafe_allow_html=True)
# --- [여기까지] ---


# --- 페이지 설정 ---
st.set_page_config(
    page_title="채유정 | 포트폴리오",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- 컬럼 간 기본 여백(gap) 강제 축소 ---
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        [data-testid="column"] {
            padding-left: 0.2rem !important;
            padding-right: 0.2rem !important;
        }
    </style>
""", unsafe_allow_html=True)


# ===================================================================
# 1. Intro
# ===================================================================
st.header("안녕하세요, 채유정입니다.")
st.markdown(
    """
저는 데이터로 나를 이해하고, 성찰로 길을 찾는 사람입니다.<br>
오늘도 어제를 돌아보며 더 나은 방향으로 나아갑니다.
""",
    unsafe_allow_html=True,
)

st.divider()

# ===================================================================
# 2. What's going on
# [!!!] 이 섹션이 수정되었습니다. (3컬럼) [!!!]
# ===================================================================
st.header("🚀 What’s going on")
st.subheader("[2025: 속해 있는 집단]")

# --- [수정] 3컬럼으로 변경 (컨텐츠1, 공백, 컨텐츠2) ---
col1, col2, col3 = st.columns([1, 1, 1]) # 1:0.2:1 비율 (공백 컬럼 0.2)

with col1:
    st.markdown(
        """
        <div style="line-height: 1.6;">
            <p style="margin-bottom: 0.5rem;">
                <strong>3월 – 현재</strong><br>
                한국외국어대학교 서울캠퍼스<br>
                제1대 AI융합대학 학생회 ‘rAIse’ 교육재정국 국원
            </p>
            <p style="margin-bottom: 0.5rem;">
                <strong>3월 – 현재</strong><br>
                한국외국어대학교 Social Science & AI융합학부<br>
                영화 소모임 ‘cinAIma’ 운영진
            </p>
            <p style="margin-bottom: 0;">
                <strong>9월 – 현재</strong><br>
                한국외국어대학교 Social Science & AI융합학부<br>
                딥러닝 학회 ‘AIEYES’ 1.5기 학회원
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div style="line-height: 1.6;">
            <p style="margin-bottom: 0.5rem;">
                <strong>9월 – 현재</strong><br>
                한국외국어대학교 서울캠퍼스 AI융합대학<br>
                밴드부 ‘Epoch’ 부원
            </p>
            <p style="margin-bottom: 0;">
                <strong>10월 – 현재</strong><br>
                한국외국어대학교 서울캠퍼스<br>
                제59대 하반기 중앙감사위원회 위원
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    with col3:
        st.write('')

st.divider()

# ===================================================================
# 3. About me
# [!!!] 이 섹션이 수정되었습니다. (4컬럼) [!!!]
# ===================================================================
st.header("👤 About me")

# --- [수정] 4컬럼으로 변경 (컨텐츠1, 컨텐츠2, 컨텐츠3, 공백) ---
col1, col2, col3, col4 = st.columns([1, 1, 1, 1]) # 비율 조정

with col1:
    st.markdown(
        """
        <h3 style="margin-top: 0; margin-bottom: 0.5rem;">🎓 Education</h3>
        <ul style="margin-top: 0; margin-bottom: 0; padding-left: 1.2rem; line-height: 1.6;">
            <li>서울정수초등학교 | 졸업</li>
            <li>북악중학교 | 졸업</li>
            <li>계성고등학교(서울) | 졸업</li>
            <li>한국외국어대학교 | 재학</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
        <h3 style="margin-top: 0; margin-bottom: 0.5rem;">✉️ Contact me</h3>
        <p style="margin-bottom: 0; line-height: 1.6;">ujeong601@hufs.ac.kr</p>
        """,
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        """
        <h3 style="margin-top: 0; margin-bottom: 0.5rem;">🛠️ Skills</h3>
        <p style="margin-bottom: 0; line-height: 1.6;">데이터 분석 준전문가 ADsP | 2025 취득</p>
        """,
        unsafe_allow_html=True,
    )
with col4:
    st.write('')

st.divider()

# ===================================================================
# 4. Personality & Mood
# [!!!] 이 섹션이 수정되었습니다. (3컬럼) [!!!]
# ===================================================================
st.header("😊 Personality & Mood")
st.subheader("[2025 : 블로그에서 추출한 나의 성격과 무드]")
st.markdown(
    """
2025년 1월부터 10월까지 제 블로그에 업로드된 일상 사진을 Clip 모델로 감성 분석하여,<br>
긍정보다는 부정, 차분함보다는 활발함에 가깝다는 결과를 얻었습니다.<br>
이를 통해 제가 가지고 있는 에너지와 분위기를 알 수 있습니다.
""",
    unsafe_allow_html=True,
)

try:
    df_mood = pd.read_csv("감성분석.csv")
    df_mood["month_num"] = df_mood["month"].str.replace("월", "").astype(int)
    df_mood = df_mood.sort_values(by="month_num")
    month_list = df_mood["month"].unique().tolist()

    base_palette = [
        "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728",
        "#9467bd", "#8c564b", "#e377c2", "#7f7f7f",
        "#bcbd22", "#17becf", "#aec7e8", "#ffbb78"
    ]
    color_list = [base_palette[i % len(base_palette)] for i in range(len(month_list))]

    for month in month_list:
        key = f"month_{month}"
        if key not in st.session_state:
            st.session_state[key] = True

    # --- [수정] 3컬럼으로 변경 (그래프, 공백, 컨트롤) ---
    chart_col, control_col, blank = st.columns([3, 1, 3])
    # 2.5:0.2:1 비율

    with control_col:
        st.markdown("<h4 style='margin-top: 0; margin-bottom: 0.5rem;'>월 선택</h4>", unsafe_allow_html=True)

        if st.button("전체 선택 / 해제"):
            all_selected = all(st.session_state[f"month_{m}"] for m in month_list)
            new_val = not all_selected
            for m in month_list:
                st.session_state[f"month_{m}"] = new_val

        for month in month_list:
            key = f"month_{month}"
            st.toggle(month, key=key)

        selected_months_list = [
            m for m in month_list if st.session_state[f"month_{m}"]
        ]

    if not selected_months_list:
        data_to_plot = pd.DataFrame(columns=df_mood.columns)
    else:
        data_to_plot = df_mood[df_mood["month"].isin(selected_months_list)]
    

    fixed_min = -0.05
    fixed_max = 0.05

    axis_lines_df = pd.DataFrame(
        {
            "x": [fixed_min, fixed_max, 0, 0],
            "y": [0, 0, fixed_min, fixed_max],
            "line_id": [1, 1, 2, 2],
        }
    )

    with chart_col:
        if data_to_plot.empty:
            st.info("표시할 월을 선택해주세요.")
        else:
            origin_lines = (
                alt.Chart(axis_lines_df)
                .mark_line(color="black", strokeWidth=1.5)
                .encode(
                    x=alt.X("x", scale=alt.Scale(domain=[fixed_min, fixed_max])),
                    y=alt.Y("y", scale=alt.Scale(domain=[fixed_min, fixed_max])),
                    detail="line_id",
                )
            )

            scatter_plot = (
                alt.Chart(data_to_plot)
                .mark_circle(size=100, opacity=0.8)
                .encode(
                    x=alt.X(
                        "x_score",
                        title="부정 → 긍정",
                        axis=alt.Axis(domain=False, gridOpacity=0.3),
                        scale=alt.Scale(domain=[fixed_min, fixed_max]),
                    ),
                    y=alt.Y(
                        "y_score",
                        title="차분 → 활발",
                        axis=alt.Axis(domain=False, gridOpacity=0.3),
                        scale=alt.Scale(domain=[fixed_min, fixed_max]),
                    ),
                    color=alt.Color(
                        "month:N",
                        title="월",
                        legend=alt.Legend(orient="bottom"),
                        scale=alt.Scale(domain=month_list, range=color_list),
                    ),
                    tooltip=["month", "x_score", "y_score"],
                )
                .properties()
                .interactive()
            )

            final_chart = (origin_lines + scatter_plot).properties(
                width=500,
                height=500,
            )

            st.altair_chart(final_chart, use_container_width=False)
            
    with blank:
        st.write('')

except FileNotFoundError:
    st.error("⚠️ '감성분석.csv' 파일을 찾을 수 없습니다. app.py와 같은 폴더에 있는지 확인하세요.")
except Exception as e:
    st.error(f"감성분석.csv 로드 중 오류 발생: {e}")
    st.info("CSV 파일 형식을 확인하세요. 'month', 'x_score', 'y_score' 컬럼이 필요합니다.")

st.divider()

# ===================================================================
# 5. Interests in my formative year
# [!!!] 이 섹션이 수정되었습니다. (3컬럼) [!!!]
# ===================================================================
st.header("🌱 Interests in my formative year")
st.subheader("[2022 – 2024 : 학교생활기록부에서 분석한 나의 관심사]")
st.markdown(
    '''
    2022년부터 2024년까지의 저의 고등학교 학교생활기록부에서 자주 등장하는 단어들을 모은 워드클라우드와,<br>
    LLM이 요약한 저의 학교생활기록부 요약본을 프롬프트화하여 leonardo.ai가 생성한 이미지입니다.<br>
    이를 통해 고등학교 기간의 저의 관심사와 지향성을 알 수 있습니다.
    ''',
    unsafe_allow_html=True,
    )

# --- [수정] 3컬럼으로 변경 (컨텐츠1, 공백, 컨텐츠2) ---
col1, col2, col3 = st.columns([1, 1, 1]) # 1:0.2:1 비율

with col1:
    st.markdown(
        "<h4 style='margin-top: 0; margin-bottom: 0.5rem;'>생기부 분석 워드클라우드</h4>",
        unsafe_allow_html=True,
    )

    # 워드클라우드를 왼쪽 위에 붙이는 구조
    left, blank = st.columns([1, 0.0001])

    with left:
        try:
            df_words = pd.read_csv("워드클라우드.csv")

            palette = [
                "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728",
                "#9467bd", "#8c564b", "#e377c2", "#7f7f7f",
                "#bcbd22", "#17becf"
            ]

            word_data = []
            for i, row in df_words.iterrows():
                color = palette[i % len(palette)]
                word_data.append(
                    {
                        "name": row["word"],
                        "value": row["frequency"],
                        "textStyle": {"color": color},
                    }
                )

            wordcloud_options = {
                "tooltip": {"show": True},
                "series": [
                    {
                        "type": "wordCloud",
                        "shape": "circle",
                        "sizeRange": [12, 60],
                        "rotationRange": [-45, 45],
                        "data": word_data,
                        "textStyle": {"fontFamily": "sans-serif"},
                    }
                ],
            }

            st_echarts(options=wordcloud_options, height="350px", key="wordcloud_square")
            st.caption('단어 위에 마우스를 올리면 빈도 수를 확인할 수 있습니다.')

        except FileNotFoundError:
            st.error("⚠️ '워드클라우드.csv' 파일을 찾을 수 없습니다.")

        except Exception as e:
            st.error(f"⚠️ 워드클라우드 오류 발생: {e}")
       

with col2:
    st.markdown("<h4 style='margin-top: 0; margin-bottom: 0.5rem;'>생기부 지향 이미지</h4>", unsafe_allow_html=True)

    try:
        st.image(
            "생기부 지향 이미지.jpg",

            width=350,
        )
    except FileNotFoundError:
        st.error("⚠️ '생기부 지향 이미지.jpg' 파일을 찾을 수 없습니다. app.py와 같은 폴더에 있는지 확인하세요.")
        st.image(
            "https://via.placeholder.com/400x400/CCCCCC/808080?text=Image+Not+Found",
            caption="대체 이미지",
            width=350,
        )

    if "show_bio_text" not in st.session_state:
        st.session_state.show_bio_text = False

    if st.button("📝 LLM이 분석한 생기부 요약 보기"):
        st.session_state.show_bio_text = not st.session_state.show_bio_text

    if st.session_state.show_bio_text:
        bio_text = """
        고등학교 3년 동안 데이터와 기술을 기반으로 사회 문제를 탐구하고, 현실적인 해결책을 고민해온 학생입니다. 
        통계, 글쓰기, 프로그래밍을 융합한 프로젝트를 통해 사고력과 문제 해결력을 키웠으며, 
        스마트팜, 자연어처리, 도시공학 등 다양한 분야를 탐색하며 진로에 대한 구체적인 방향을 설정했습니다. 
        기술을 사회적 책임과 연결해 바라보며, 사람을 위한 기술을 고민하는 통합적 시각을 갖춘 점이 인상적입니다.
        """
        st.text_area("LLM 분석 결과:", value=bio_text, height=200, disabled=True)
with col3:
    st.write('')