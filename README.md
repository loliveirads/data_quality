# 🚀 **Projeto Data Quality**

## 📚 **Sobre o Projeto**

Este repositório faz parte do projeto **"Data Quality Pipeline"**, cujo objetivo é garantir a **qualidade dos dados** em processos de ETL (Extração, Transformação e Carga). O foco principal está na aplicação de **boas práticas**, **automação**, **testes robustos** e **documentação clara**.

---

## Visite minha documentação

### 📊 **Fluxo do Projeto**

[![Fluxo do Projeto](https://github.com/loliveirads/data_quality/raw/main/pic/fluxo.png)](https://loliveirads.github.io/data_quality/)

## 🎯 **Objetivos do Projeto**

- **📂 Estrutura Padrão para Projetos de Dados:** Organização clara dos diretórios, separando código-fonte, testes, dados e documentação.  
- **⚙️ ETL com SQLAlchemy:** Estrutura robusta para conectar e manipular bancos de dados.  
- **🧪 Testes Automatizados com Pytest:** Garantir que as funções ETL e validações funcionem corretamente.  
- **📊 Validação de Dados com Pandera:** Garantir a integridade e consistência dos dados extraídos.  
- **📑 Documentação com MkDocs:** Facilitar a compreensão e o uso do projeto.  
- **🔄 Automação com Taskipy:** Simplificar tarefas recorrentes, como rodar ETL, testes e documentação.  
- **☁️ Banco de Dados PostgreSQL:** Armazenamento estruturado dos dados.  
- **💡 Integração com ferramentas de desenvolvimento modernas:** Python, Poetry, VSCode.

---

## 🛠️ **Ferramentas Utilizadas**

- **Python 3.11.5:** Linguagem principal do projeto.  
- **Poetry:** Gerenciador de pacotes e dependências Python.  
- **SQLAlchemy:** Conexão e manipulação de bancos SQL.  
- **Pandera:** Validação de DataFrames com regras definidas.  
- **Pytest:** Framework de testes automatizados.  
- **MkDocs:** Ferramenta para documentação de projetos.  
- **Taskipy:** Automatização de tarefas recorrentes.  
- **PostgreSQL:** Banco de dados relacional.  
- **VSCode:** Editor de código.  
- **Pyenv:** Gerenciador de versões Python.  

---

## 📋 **Pré-requisitos**

- [Python 3.11.5](https://www.python.org/downloads/)  
- [Poetry](https://python-poetry.org/docs/#installation)  
- [Pyenv](https://github.com/pyenv/pyenv#installation)  
- [Git](https://git-scm.com/downloads)  
- Banco de Dados PostgreSQL configurado  
- Editor de código **VSCode**

---

## 🚀 **Instalação e Configuração**

### **1. Clone o Repositório**

```bash
git clone https://github.com/loliveirads/data_quality.git
cd data_quality
```

### **2. Configure o Ambiente Python**

```bash
pyenv install 3.11.5
pyenv local 3.11.5
```

### **3. Configure o Poetry**

```bash
poetry env use 3.11.5
poetry shell
```

### **4. Instale as Dependências**

```bash
poetry install
```

### **5. Configure as Variáveis de Ambiente**

Crie um arquivo .env na raiz do projeto com as informações do banco de dados:

### **6. Execute os Testes**

```bash
task test
```
### **7. Documentação do Projeto**

```bash
task doc
```
### **8. Rodar o ETL**

```bash
task run
```

## Contato

Para dúvidas, sugestões ou feedbacks:

* **Luiz Fernando** - [luizfsoliveira.lm@gmail.com](mailto:luizfsoliveira.lm@gmail.com)