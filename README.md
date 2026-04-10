# RAG 知识库问答系统

基于检索增强生成（RAG）技术的智能知识库问答系统，支持上传多种格式文件，构建专属知识库并提供智能问答服务。

## 功能特性

- **多格式文件上传**：支持 TXT、Word、PDF、Excel 等常见文档格式
- **智能问答**：基于上传的知识库内容进行语义理解和回答
- **对话历史**：支持多轮对话，自动记忆上下文
- **去重检测**：基于 MD5 算法避免重复上传相同内容
- **向量检索**：使用 Chroma 向量数据库实现高效语义检索

## 技术栈

| 模块 | 技术 |
|------|------|
| 前端 | Streamlit |
| LLM | 通义千问 (qwen-max) |
| Embedding | text-embedding-v4 |
| 向量数据库 | Chroma |
| 框架 | LangChain |

## 项目结构

```
├── 知识库上传.py          # 知识库文件上传页面
├── pages/
│   └── 智能客服.py        # 智能问答页面
├── rag.py                # RAG 核心链
├── konwledge_base.py     # 知识库服务（文本分割、存储）
├── vector_store.py       # 向量存储服务
├── file_history_store.py  # 对话历史管理
├── config_data.py        # 配置文件
└── requirements.txt      # 依赖列表
```

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置 API Key

在 `.streamlit/secrets.toml` 中配置通义千问 API Key：

```toml
DASHSCOPE_API_KEY = "your-api-key-here"
```

### 3. 启动应用

```bash
streamlit run 知识库上传.py
```

### 4. 使用流程

1. 打开 **知识库上传** 页面上传文档（支持 TXT、Word、PDF、Excel）
2. 切换到 **智能客服** 页面
3. 输入问题，系统将基于已上传的知识库内容进行回答

## 页面说明

### 知识库上传

上传文档到向量数据库，支持的文件格式：
- `.txt` - 文本文件
- `.docx` - Word 文档
- `.pdf` - PDF 文档
- `.xlsx` - Excel 表格

### 智能客服

基于 RAG 架构的智能问答系统，支持多轮对话。

## 注意事项

- `chat_history/` - 对话历史存储目录（不提交到 Git）
- `chroma_db/` - 向量数据库文件（不提交到 Git）
- `md5.text` - 内容去重记录（不提交到 Git）
