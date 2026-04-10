import time
from rag import RagService
import streamlit as st
import config_data as config

st.set_page_config(page_title="智能客服", layout="wide")

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

/* 全局背景 */
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
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🤖 智能客服</h1>', unsafe_allow_html=True)

if "message" not in st.session_state:
    st.session_state["message"] = [{"role": "assistant", "content": "你好，有什么可以帮助你？"}]

if "rag" not in st.session_state:
    st.session_state["rag"] = RagService()

# 欢迎卡片（首次打开时显示）
if len(st.session_state["message"]) == 1:
    st.markdown(f'''
    <div class="welcome-card">
        <div class="welcome-icon">💬</div>
        <p class="welcome-text">上传知识库文件后，我可以帮你解答相关问题</p>
    </div>
    ''', unsafe_allow_html=True)

# 渲染聊天消息 - 使用原生 Streamlit 组件
for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

# 聊天输入框
prompt = st.chat_input("输入您的问题...")

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state["message"].append({"role": "user", "content": prompt})

    ai_res_list = []
    with st.spinner("🤔 AI思考中..."):
        res_stream = st.session_state["rag"].chain.stream({"input": prompt}, config.session_config)

        def capture(generator, cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                yield chunk

        st.chat_message("assistant").write_stream(capture(res_stream, ai_res_list))
        st.session_state["message"].append({"role": "assistant", "content": "".join(ai_res_list)})
