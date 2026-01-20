import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="자기소개 웹앱",
    page_icon="👋",
    layout="centered"
)

# 제목
st.title("👋 안녕하세요!")

# 프로필 사진
st.image(
    "https://images.unsplash.com/photo-1527980965255-d3b416303d12",
    caption="My Profile Photo",
    width=250
)

# 간단한 인사
st.subheader("반갑습니다 😊")
st.write("""
저는 **Streamlit으로 웹앱을 만들고 있는 개발자**입니다.  
간단하지만 보기 좋은 웹 서비스를 만드는 것을 좋아합니다.
""")

# 구분선
st.divider()

# 추가 정보
st.markdown("### 📌 간단한 소개")
st.markdown("""
- 💼 관심 분야: 데이터 분석, 웹앱 개발  
- 🛠 사용 기술: Python, Streamlit  
- 🌱 목표: 쉽고 유용한 웹앱 만들기
""")

# 푸터
st.caption("© 2026 My Introduction App")
