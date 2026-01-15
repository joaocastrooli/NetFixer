# NetFixer 🐍💻

O **NetFixer** é uma ferramenta desenvolvida em Python para automatizar o diagnóstico de rede, transformando comandos complexos do terminal em uma solução simples de um clique para o usuário final.

### 💡 Por que foi criado?
Identifiquei que muitos chamados de suporte eram resolvidos com a mesma sequência de comandos. O NetFixer automatiza esse processo, reduzindo o tempo de inatividade e dando autonomia aos colaboradores.

### ⚙️ O que ele faz:
O app executa automaticamente o protocolo padrão de recuperação:
* `ipconfig /release` (Liberação do IP)
* `ipconfig /flushdns` (Limpeza de cache)
* `ipconfig /renew` (Nova concessão de rede)

### 🛠️ Tecnologias e Desafios:
* **Python + Tkinter:** Interface intuitiva com barra de progresso.
* **Subprocess:** Execução de comandos do Windows.
* **Admin Rights:** Gerenciamento de privilégios via código.

---
*Projeto desenvolvido durante meu estágio de TI para otimizar processos reais da equipe.*
