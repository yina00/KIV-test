import streamlit as st
import importlib

st.set_page_config(page_title="🖼️ 우리반 전시회", layout="centered")

st.title("🎨 우리반 전시회에 오신 것을 환영합니다!")
st.write("원하는 학생의 전시회를 선택하세요.")

# 학생 목록 딕셔너리 (파일명과 일치시켜야 함)
students = {
    "학생1": "student_pages/student1",
    "학생2": "student_pages/student2",
    "학생3": "student_pages/student3",
    "학생4": "student_pages/student4",
    "학생5": "student_pages/student5"
}

# 드롭다운으로 학생 선택
selected = st.selectbox("👤 학생 선택", list(students.keys()))

# 버튼 클릭 시 해당 학생 모듈 실행
if st.button("👉 전시회 열기"):
    module_name = students[selected]
    try:
        student_app = importlib.import_module(module_name)
        student_app.main()  # 각 studentN.py는 main() 함수로 구성되어 있어야 함
    except Exception as e:
        st.error(f"학생 페이지를 불러오는 데 문제가 발생했어요: {e}")
