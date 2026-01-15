# langchain-langgraph-studies

Repositório de estudos práticos com **LangChain** e **LangGraph** para construção de sistemas de IA, **agentes** e **pipelines/workflows** inteligentes com Python.

> Objetivo: aprender na prática como compor LLMs, ferramentas e grafos de execução (LangGraph), evoluindo de exemplos simples para fluxos mais “agentic” e controláveis.

---

## ✅ Pré-requisitos

- **Python**: use a versão indicada em `.python-version`
- Recomendado: **uv** (gerenciamento de ambiente e dependências), já que o repositório possui `uv.lock`

---

## ⚙️ Setup rápido (com `uv`)

1) Clone o repositório:

```bash
git clone https://github.com/GamalielGhelli/langchain-langgraph-studies.git
cd langchain-langgraph-studies
```
2) Crie seu ```.env``` baseando neste exemplo:

```
 cp .env-example .env
```

4) Instale as dependências (o uv vai respeitar o lockfile uv.lock):

```
uv sync
```

5) Rode um exemplo:

```
uv run python src/examples/ex001/main.py
```
Troque `ex001` por `ex002` conforme for avançando.

---

# ⚙️ Setup alternativo (sem `uv`)

Se preferir `venv` + `pip`:
```
python -m venv .venv
# Windows (Git Bash)
source .venv/Scripts/activate

# Linux/macOS
# source .venv/bin/activate
```
Depois de ativar o ambiente virtual, instale as dependências utilizando o arquivo `requirements.txt`:

```
pip install -r requirements.txt
```
---

# 📂 Estrutura atual do projeto

```
.
├─ src/
│  └─ examples/
│     ├─ ex001/
│     │  └─ main.py
│     └─ ex002/
│        └─ main.py
├─ .env-example
├─ .python-version
├─ pyproject.toml
└─ uv.lock
```

- `src/examples/` → exemplos organizados por pasta (ex.: `ex001`, `ex002`)
- `.env-example` → modelo de variáveis de ambiente para configuração local
- `pyproject.toml` + `uv.lock` → dependências e lockfile (setup reproduzível)
- `.python-version` → versão de Python sugerida para o projeto

---

# 📈 Evolução

Este repositório é voltado para estudos práticos e será expandido com novos exemplos, explorando conceitos como:
- Chains
- Agentes
- Ferramentas (tool calling)
- Pipelines inteligentes
- Grafos de execução com LangGraph