import time

import streamlit as st
from konwledge_base import KnowledgeBaseService

st.set_page_config(page_title="知识库更新服务", layout="wide")

# 科技感浅色主题 CSS
st.markdown("""
<style>
/* 侧边栏导航标题 */
[data-testid="stSidebarHeader"]::before {
    content: "导航";
    font-size: 1.2rem;
    font-weight: bold;
    position: absolute;
    left: 0.5rem;
    top: 1rem;
}

/* 全局背景和字体 */
.stApp {
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
}

.stAppViewBlock {
    padding-top: 2rem;
}

/* 主标题样式 */
.main-title {
    font-size: 2.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, #2563EB 0%, #7C3AED 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-align: center;
    margin-bottom: 2rem;
}

/* 上传卡片样式 */
.upload-card {
    background: white;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 4px 20px rgba(37, 99, 235, 0.1);
    border: 1px solid rgba(37, 99, 235, 0.1);
    margin: 1rem 0;
}

/* 文件信息卡片 */
.file-info {
    background: linear-gradient(135deg, #2563EB 0%, #7C3AED 100%);
    border-radius: 12px;
    padding: 1.5rem;
    color: white;
    margin: 1rem 0;
}

/* 标签样式 */
.label {
    font-size: 1.1rem;
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 1rem;
}

/* 按钮样式 */
.stDownloadButton > button {
    background: linear-gradient(135deg, #2563EB 0%, #7C3AED 100%);
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.75rem 1.5rem;
    font-weight: 600;
    transition: all 0.3s ease;
}
/* 欢迎消息卡片 */
.welcome-card {
    background: white;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 4px 20px rgba(37, 99, 235, 0.1);
    border: 1px solid rgba(37, 99, 235, 0.1);
    margin-bottom: 2rem;
}

.welcome-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.welcome-text {
    color: #64748b;
    font-size: 1.1rem;
}

.stDownloadButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}

/* 成功消息 */
.success-message {
    background: linear-gradient(135deg, #10B981 0%, #059669 100%);
    border-radius: 8px;
    padding: 1rem;
    color: white;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">📚 知识库更新服务</h1>', unsafe_allow_html=True)

# 上传卡片
st.markdown('''
<div class="welcome-card">
    <div class="welcome-icon">📖</div>
    <p class="welcome-text" style="font-size: 1.3rem; font-weight: 600; color: #1e293b; margin-bottom: 1rem;">使用指南</p>
    <p class="welcome-text" style="text-align: left; line-height: 2;">1️⃣ 首先需要上传你的个人文件<br>2️⃣ 切换到智能客服询问相关问题</p>
</div>
''', unsafe_allow_html=True)
st.markdown('<p class="label">📎 请上传 TXT 文件</p>', unsafe_allow_html=True)

uploader_file = st.file_uploader(
    "选择文件",
    type=['txt'],
    accept_multiple_files=False,
    help="点击按钮选择文件上传",
    label_visibility="collapsed"
)

if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()

if uploader_file is not None:
    file_name = uploader_file.name
    file_type = uploader_file.type
    file_size = uploader_file.size / 1024

    st.markdown(f'''
    <div class="file-info">
        <h3>📄 {file_name}</h3>
        <p>格式：{file_type} | 大小：{file_size:.2f} KB</p>
    </div>
    ''', unsafe_allow_html=True)

    text = uploader_file.getvalue().decode("utf-8")

    with st.spinner("🔄 载入知识库中..."):
        time.sleep(1)
        result = st.session_state["service"].upload_by_str(text, file_name)
        st.markdown(f'<div class="success-message">✅ {result}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
