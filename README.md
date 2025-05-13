<div align="center">

<h1>LangChain + Ollama<br/><sub>Chat with a locally available LLM.</sub></h1>

<pre lang="bash"><code style="white-space: pre-line">A basic implementation of offline chat with large language models.
</code></pre>

<img alt="Repository top language" src="https://img.shields.io/github/languages/top/daniloceesar/langchain-boilerplate.svg" />

<img alt="Repository size" src="https://img.shields.io/github/repo-size/daniloceesar/langchain-boilerplate.svg" />

<a href="https://github.com/DaniloCeesar/langchain-boilerplate/blob/main/LICENSE.md">
<img src="https://img.shields.io/badge/license-GNU%20GPLv2-brightgreen.svg"/>
</a>

</div>
<hr />

## 📚 Project overview

This project has made use of the [LangChain](https://github.com/langchain-ai/langchain) and the [Ollama](https://github.com/ollama/ollama) software.

This repository provides a simple chat implementation, to interact with local Large Language Models (LLMs).

## 🛠️ Development & Testing

### Requirements

- **[Git](https://git-scm.com/)** — free and open source distributed version control system.
- **[Python](https://www.python.org/)** — easy to learn, powerful programming language.
- **[pip](https://pypi.org/project/pip/)** — package installer for Python packages.
- **[Docker](https://www.docker.com/)** or **[Podman](https://podman.io/)** — container engines.

### Build instructions

1. You will need a **Ollama** server up and running, with at least one model locally available (**Please read their [instructions for quickstart](https://github.com/ollama/ollama/)**);
2. `git clone https://github.com/DaniloCeesar/langchain-boilerplate.git` — clone this repository into a new directory;
3. `cd langchain-boilerplate` — change the current directory to this project source code;
4. `cp .env.example .env` — generate a new environment file that will contain your project's environment variables (**Please remember to replace it with your own settings**);
5. `pip install -r requirements.txt` — install the dependencies from `requirements.txt` file into project's folder;
6. `python3 app.py` — run the application. The generated message will be displayed in your terminal.

## 👥 Attributions

This project is built by developing and using open source technology. We may use third party libraries, code sources, and assets both for production and development processes.

## ⚖️ License

This project is licensed under the GNU General Public License v2.0. See the [LICENSE](https://github.com/DaniloCeesar/langchain-boilerplate/blob/main/LICENSE.md) for more information.
