import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="자기소개 페이지", page_icon="😊")

# 2. 제목 부분
st.title("👋 안녕하세요! 저를 소개합니다")

# 3. 레이아웃 나누기 (왼쪽: 이미지, 오른쪽: 설명)
col1, col2 = st.columns([1, 2])

with col1:
    # 본인의 사진이나 캐릭터 이미지를 넣으세요.
    st.image("https://i.namu.wiki/i/_HHTYdKOuG6QdskbyW5ZwepiZw3mplg47y7mA21SEezw96xd2hrzF-JY2euBBKOBRky8Jv4Rb1qv0My_t0U1VQ.webp", 
             caption="나를 나타내는 사진",
             use_container_width=True)

with col2:
    st.subheader("이름: 홍길동")
    st.write("📍 **거주지:** 서울특별시")
    st.write("💻 **관심 분야:** 파이썬, 데이터 분석, 웹 개발")
    st.write("🎨 **취미:** 사진 찍기, 요리하기")

# 4. 추가 상세 소개 (구분선 활용)
st.divider()

st.markdown("""
### 🚀 저의 목표
올해는 **Streamlit**을 마스터해서 나만의 멋진 웹 앱을 3개 이상 만드는 것이 목표입니다! 
궁금한 점이 있다면 언제든 연락해 주세요.
""")
