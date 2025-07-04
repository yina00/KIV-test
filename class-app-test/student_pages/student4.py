import streamlit as st

def main():
    st.set_page_config(page_title="학생4의 전시회입니다", layout="centered")
    
    # 타이틀
    st.title("학생4의 전시회에 오신 것을 환영합니다!")
    st.write("아래에서 원하는 전시회를 선택하세요.")
    
    # 버튼 클릭 여부를 저장하는 상태 변수
    if 'page' not in st.session_state:
        st.session_state.page = "home"
    
    # 버튼 동작 처리
    if st.session_state.page == "home":
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📷 사진 전시회 보기"):
                st.session_state.page = "photo"
        with col2:
            if st.button("🎥 동영상 전시회 보기"):
                st.session_state.page = "video"
    
    # 사진 전시회
    elif st.session_state.page == "photo":
        st.header("📷 사진 전시회")
        #image_path = "/content/drive/MyDrive/[kiv]실습 연습 첨부파일/라푼젤 배경화면.png"
        #st.image(image_path, use_container_width=True)
        if st.button("🔙 뒤로 가기"):
            st.session_state.page = "home"
    
    # 동영상 전시회
    elif st.session_state.page == "video":
        st.header("🎥 동영상 전시회")
        #video_path = "/content/drive/MyDrive/[kiv]실습 연습 첨부파일/wfk테스트영상.mp4"
        #st.video(video_path)
        if st.button("🔙 뒤로 가기"):
            st.session_state.page = "home"
