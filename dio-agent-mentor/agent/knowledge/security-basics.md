# Fundamentos de segurança da informação

Este arquivo dá ao agente o vocabulário e os conceitos básicos para usar a skill `vulnerability-analysis` com precisão. Leia quando a conversa envolver segurança, vulnerabilidade ou um código/configuração a avaliar.

## Vulnerabilidade, ameaça e risco

Esses três termos são confundidos com frequência, mas significam coisas diferentes:

- **Vulnerabilidade**: uma falha ou fraqueza real, que existe independente de alguém explorar ou não. Exemplo: uma rota de login que monta a consulta SQL concatenando o texto digitado pelo usuário.
- **Ameaça**: alguém ou algo com potencial de explorar a vulnerabilidade. Exemplo: um atacante automatizado testando SQL Injection em formulários públicos.
- **Risco**: a combinação de vulnerabilidade, ameaça e impacto — a chance real de dano, considerando o cenário. O mesmo código vulnerável tem risco baixo dentro de uma rede isolada sem acesso externo, e risco alto se exposto na internet.

Avaliar risco sempre significa olhar os três juntos, não cada um isolado.

## A tríade CIA (confidencialidade, integridade, disponibilidade)

Toda vulnerabilidade de segurança, no fundo, ameaça uma ou mais destas três propriedades:

- **Confidencialidade**: só quem deveria ver os dados, vê. Quebrada quando alguém não autorizado lê informação (ex. SQL Injection expondo senhas de outros usuários).
- **Integridade**: os dados e o sistema continuam corretos e não foram alterados sem autorização. Quebrada quando alguém modifica dados ou código sem permissão (ex. um atacante alterando preços em um banco de dados via injeção).
- **Disponibilidade**: o sistema continua acessível para quem precisa dele. Quebrada quando um serviço cai ou fica inacessível (ex. um ataque de negação de serviço).

Ao avaliar o impacto de uma vulnerabilidade, nomeie qual (ou quais) das três propriedades está em jogo — isso torna a análise concreta em vez de genérica.

## Vocabulário essencial para a análise

- **Superfície de ataque**: todos os pontos por onde um atacante poderia tentar entrar (campos de formulário, portas abertas, APIs, dependências de terceiros).
- **Exploração (exploit)**: o ato de usar uma vulnerabilidade para causar um efeito não pretendido. A skill explica o mecanismo da exploração, mas nunca entrega um exploit funcional pronto.
- **Mitigação**: a correção ou controle que reduz ou elimina o risco. Nem toda mitigação elimina a vulnerabilidade — às vezes só reduz a probabilidade (ex. um firewall não corrige o código vulnerável, só dificulta o acesso a ele).
- **MITRE ATT&CK**: um catálogo público de táticas e técnicas reais usadas por atacantes, organizado por fase do ataque (reconhecimento, acesso inicial, execução, persistência, exfiltração, etc.). Cada técnica tem um código (ex. T1190 — Exploit Public-Facing Application). Citar a técnica certa ajuda o estudante a conectar um bug concreto a um padrão de ataque conhecido, em vez de tratá-lo como um caso isolado.

## Boas práticas defensivas que valem para quase todo caso

- **Nunca confie em entrada do usuário.** Todo dado vindo de fora (formulário, URL, cabeçalho HTTP, arquivo enviado) deve ser validado e tratado antes de usar, nunca concatenado direto em uma consulta, comando ou página.
- **Use consultas parametrizadas, não concatenação de string**, para qualquer acesso a banco de dados.
- **Princípio do menor privilégio**: todo usuário, processo ou credencial deve ter só o acesso mínimo necessário para a tarefa, nunca mais.
- **Não exponha o que não precisa estar exposto.** Um serviço de laboratório não precisa estar acessível pela internet pública; uma mensagem de erro não precisa revelar detalhes internos do sistema.
- **Resposta a incidente é defensiva, nunca ofensiva.** Diante de um ataque real, as ações corretas são: isolar o próprio sistema, preservar evidência (logs), corrigir a vulnerabilidade, e reportar ao CERT.br (https://cert.br) ou ao provedor de origem do ataque. Nunca atacar de volta — além de ilegal (Lei 12.737/2012 no Brasil), o IP de origem costuma ser falsificado ou pertence a uma vítima intermediária, então o "contra-ataque" quase sempre acerta quem não tem nada a ver com o ataque original.

## Como isso se conecta com a skill

A skill `vulnerability-analysis` usa este vocabulário para estruturar a análise: identifica a vulnerabilidade, nomeia a ameaça plausível, mapeia a técnica no MITRE ATT&CK, e avalia o risco em termos de impacto na tríade CIA e probabilidade real de exploração — sempre terminando em uma correção que o próprio estudante escreve.
