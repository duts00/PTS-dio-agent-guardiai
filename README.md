# dio-agent-guardiai

Especialização do **DIO Agent** em cibersegurança. Este projeto transforma o agente de estudos da DIO em um analista de segurança — o **GuardiAI** — que, em vez de responder no impulso, entende o contexto, avalia o risco com método e orienta a correção como um profissional de AppSec / Blue Team faria.

Nenhum modelo foi treinado. O agente foi especializado **apenas com arquivos de texto** (uma skill, um arquivo de conhecimento e um ajuste de persona), demonstrando como especializar um agente de IA por contexto — a base de "context engineering".

---

## A especialização que dei ao agente, e por quê

Um agente genérico tende a "resolver rápido": ao receber um código inseguro, ele corrige direto, sem explicar a falha, sem avaliar o risco e sem perguntar se o ambiente é seguro para agir. Isso ficou evidente no teste inicial (ver [Evidências](#evidências)): sem a especialização, o agente apenas editou o arquivo e comentou um aviso do linter, ignorando completamente a análise de segurança.

A especialização em **GuardiAI** muda esse comportamento. O agente passa a conduzir uma análise de segurança estruturada:

- **Entende o contexto antes de agir** (produção ou laboratório? dados sensíveis? exposto à internet? há autorização?);
- **Analisa com base em evidências**, distinguindo o que foi observado do que é suposição;
- **Avalia o risco** em formato padronizado (impacto, probabilidade, severidade e confiança);
- **Relaciona a padrões** reconhecidos (CWE, OWASP, MITRE ATT&CK, CVE), sem inventar identificadores;
- **Orienta a correção** explicando o porquê e como validar a mitigação;
- **Age com ética**, explicando ataques apenas no nível necessário para compreender e defender.

O objetivo é formar um agente que **pergunta antes de agir e ensina, não apenas conserta**.

---

## Arquivos criados e alterados

| Arquivo | Tipo | O que faz |
|---|---|---|
| `skills/vulnerability-analysis/SKILL.md` | criado | O roteiro que o agente segue na análise de vulnerabilidades (processo em 7 etapas, da coleta de contexto à apresentação dos resultados) |
| `skills/vulnerability-analysis/README.md` | criado | Explica a skill para pessoas |
| `agent/knowledge/security-basics.md` | criado | Fundamentos de segurança: vulnerabilidade, ameaça, risco, tríade CIA, severidade, frameworks e boas práticas |
| `agent/persona.md` | alterado | Adicionado o "Modo Especialista: GuardiAI", o caráter de analista de segurança |
| `AGENTS.md` | alterado | Adicionada a skill na tabela de skills e o arquivo de conhecimento na base de conhecimento |
| `app.py` | criado | Código propositalmente vulnerável (SQL Injection) usado para testar o agente |

---

## Como rodar o agente

O agente funciona em qualquer harness compatível com o padrão `AGENTS.md`. Neste projeto foi usado o **Hermes**.

1. **Instale um harness** (ex.: Hermes) seguindo a documentação oficial.
2. **Clone este repositório:**
   ```bash
   git clone https://github.com/duts00/dio-agent-guardiai.git
   cd dio-agent-guardiai
   ```
3. **Faça login no provedor** do harness (ex.: Nous Portal, no Hermes) e selecione um modelo.
4. **Rode o agente a partir da pasta do projeto** (importante: aberto em outro diretório, ele não encontra os arquivos):
   ```bash
   hermes -z "Analise o arquivo app.py deste projeto e verifique se há vulnerabilidades de segurança."
   ```
   Ou, para conversar de forma interativa:
   ```bash
   hermes chat
   ```

---

## A melhoria que escolhi

Além de reproduzir o caminho da aula, escolhi aprofundar a skill com **análise estruturada e baseada em evidências**, atendendo à sugestão de "fazer a análise sair sempre no mesmo formato, para comparar casos". Em relação ao exemplo base, acrescentei:

- **Estado do achado** — cada falha é classificada como *confirmada no material*, *potencial* ou *não determinada*, separando o que o código comprova do que depende de verificação no ambiente.
- **Confiança separada da probabilidade** — a análise distingue "quão provável é a exploração" de "quão sólida é a evidência", um cuidado que evita conclusões falsas.
- **Formato de saída padronizado** — um template fixo de resultado (estado, localização, causa, cenário, impacto, probabilidade, severidade, confiança, referências, correção e validação), permitindo comparar diferentes análises.
- **Regras anti-alucinação** — a skill proíbe inventar linhas, versões, CVEs ou resultados, e exige verificar identificadores em fontes primárias.

---

## Evidências

As capturas de tela estão em [`/images`](./images):

| # | Evidência | Arquivo |
|---|---|---|
| 01 | Agente **sem** a skill: corrige o código direto, sem análise de segurança | `images/01-agente-cru-sem-skill.png` |
| 02 | **GuardiAI** analisa o `app.py`: identifica SQL Injection (CWE-89), explica a exploração e a correção | `images/02-guardiai-analise-appsec.png` |
| 03 | **GuardiAI** em cenário de infraestrutura: questiona a exposição e orienta defesa em camadas | `images/03-guardiai-cenario-infra.png` |

O contraste entre o print 01 (agente genérico) e os prints 02–03 (GuardiAI) demonstra o efeito da especialização por arquivos.

> Observação técnica: a fidelidade com que o agente segue a skill depende da capacidade do modelo usado. Modelos mais capazes tendem a seguir o roteiro defensivo (como perguntar o contexto antes de agir) com mais rigor.

---

## Nota sobre o uso de Inteligência Artificial

Este projeto foi construído com apoio de IA, usada para estruturar e revisar os arquivos, sempre com compreensão e ajuste crítico do conteúdo — o que reflete, na prática, o próprio tema do desafio: **especializar e dirigir um agente de IA é uma habilidade**. Todo o conteúdo foi entendido, testado e adaptado.

---

Desenvolvido por duts00 — Desafio de Projeto DIO (especialização do DIO Agent em segurança)
