# Fundamentos de Segurança da Informação

Este documento reúne os conceitos-base que o agente deve dominar ao conduzir uma análise de segurança. Serve como referência para falar com precisão sobre vulnerabilidades, ameaças, riscos e boas práticas.

---

## Vulnerabilidade, Ameaça e Risco

Esses três termos são frequentemente confundidos, mas significam coisas diferentes. Entender a distinção é essencial para avaliar segurança corretamente.

- **Vulnerabilidade:** uma fraqueza ou falha em um sistema, código, configuração ou processo que pode ser explorada. Exemplos: uma consulta SQL montada por concatenação, uma senha padrão não alterada, um serviço desatualizado. A vulnerabilidade é a "porta aberta".

- **Ameaça:** qualquer agente ou evento com potencial de explorar uma vulnerabilidade e causar dano. Pode ser um atacante externo, um funcionário mal-intencionado, um malware ou até um evento acidental. A ameaça é "quem ou o que pode passar pela porta".

- **Risco:** a probabilidade de uma ameaça explorar uma vulnerabilidade, combinada com o impacto que isso causaria. O risco é o resultado prático: *o quão provável é dar errado, e o quão grave seria*.

Uma forma simples de relacionar:

> **Risco = Ameaça × Vulnerabilidade × Impacto**

Se não há vulnerabilidade, a ameaça não tem por onde entrar. Se não há dado ou ativo valioso, o impacto é baixo mesmo com a falha presente. Por isso a análise de risco sempre considera o contexto: um mesmo bug tem risco diferente em um laboratório isolado e em um sistema de produção com dados financeiros.

---

## A Tríade CIA

A tríade CIA é o modelo central da segurança da informação. Toda vulnerabilidade afeta pelo menos um desses três pilares:

- **Confidencialidade (Confidentiality):** garantir que a informação só seja acessada por quem tem autorização. É violada quando dados vazam — por exemplo, um SQL Injection que expõe a tabela de usuários, ou credenciais trafegando sem criptografia.

- **Integridade (Integrity):** garantir que a informação não seja alterada de forma indevida ou não autorizada. É violada quando um atacante modifica dados — por exemplo, adulterar um registro bancário, ou um ataque que altera o conteúdo de um arquivo em trânsito.

- **Disponibilidade (Availability):** garantir que o sistema e a informação estejam acessíveis quando necessários. É violada em ataques de negação de serviço (DoS), ou quando um ransomware cifra os arquivos e impede o acesso.

Ao avaliar uma falha, é útil perguntar: *qual pilar da tríade ela ameaça?* Isso ajuda a descrever o impacto com precisão. Muitas falhas afetam mais de um pilar ao mesmo tempo.

---

## Severidade: Impacto e Probabilidade

Avaliar uma vulnerabilidade não é só dizer "é grave" ou "não é". Usa-se uma classificação estruturada:

- **Impacto:** o tamanho do dano se a falha for explorada. Considera qual(is) pilar(es) da tríade são afetados e o valor do ativo. Escala comum: baixo, médio, alto, crítico.

- **Probabilidade:** quão fácil ou provável é a exploração. Considera a exposição (interno vs. internet), os privilégios necessários, a complexidade do ataque e os controles existentes. Escala comum: baixa, média, alta.

- **Severidade:** a combinação de impacto e probabilidade. Uma falha de impacto crítico mas de probabilidade baixa pode ter severidade média; uma de impacto alto e probabilidade alta é crítica.

Frameworks como o **CVSS (Common Vulnerability Scoring System)** padronizam essa pontuação, mas o raciocínio impacto × probabilidade é o fundamento.

---

## Frameworks e Referências

Conhecer os padrões da indústria dá rigor à análise e permite comunicação clara entre profissionais:

- **CWE (Common Weakness Enumeration):** catálogo de tipos de fraquezas de software (ex.: CWE-89 para SQL Injection). Classifica a natureza técnica da falha.

- **OWASP Top 10:** lista das vulnerabilidades web mais críticas e comuns, atualizada periodicamente. Boa referência para contextualizar falhas de aplicação.

- **MITRE ATT&CK:** base de conhecimento de táticas e técnicas reais de atacantes, organizadas por fase do ataque. Usada para mapear *como* uma falha seria explorada (ex.: T1190 – Exploit Public-Facing Application).

- **CVE (Common Vulnerabilities and Exposures):** identificadores de vulnerabilidades específicas já publicadas em produtos conhecidos (ex.: CVE-2021-44228, o Log4Shell).

Regra importante: identificadores (CVE, CWE) só devem ser citados quando aplicáveis e verificáveis. Nunca inventar números ou referências.

---

## Boas Práticas de Segurança

Princípios defensivos que orientam tanto a prevenção quanto a correção de falhas:

- **Validação e tratamento de entrada:** nunca confiar em dados vindos do usuário. Usar consultas parametrizadas (contra SQL Injection), validar formatos e codificar saídas (contra XSS).

- **Princípio do menor privilégio (least privilege):** cada usuário, serviço ou processo deve ter apenas as permissões estritamente necessárias. Limita o alcance de um comprometimento.

- **Defesa em camadas (defense in depth):** não depender de um único controle. Combinar validação, autenticação forte, firewall, monitoramento, etc. Se uma camada falha, outra segura.

- **Autenticação forte e MFA:** senhas fortes e únicas, e um segundo fator que torna uma credencial roubada insuficiente para o acesso.

- **Criptografia:** proteger dados sensíveis em trânsito (TLS) e em repouso. Nunca armazenar senhas em texto puro — usar funções de hash apropriadas para senhas.

- **Gestão de atualizações (patch management):** manter sistemas e dependências atualizados fecha vulnerabilidades conhecidas.

- **Segurança por padrão (secure by default):** configurações iniciais devem ser as mais seguras; desativar serviços, contas e recursos desnecessários.

- **Registro e monitoramento (logging):** registrar eventos de segurança permite detectar e responder a incidentes. Sem logs, um ataque pode passar despercebido.

- **Minimizar a exposição:** reduzir a superfície de ataque — não expor à internet o que pode ser interno, segmentar a rede, fechar portas não utilizadas.

---

## Ética e Contexto

Toda análise de segurança deve ser conduzida de forma ética e dentro da autorização:

- Testes ativos só devem ocorrer em sistemas próprios ou com autorização explícita por escrito.
- O objetivo da análise é **fortalecer a defesa**, não produzir roteiros de ataque contra terceiros.
- O contexto (ambiente, dados, exposição, autorização) muda completamente a avaliação de risco — por isso ele é sempre o primeiro passo.
