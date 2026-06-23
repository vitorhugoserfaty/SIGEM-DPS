# SIGEM-DPS

## Protótipo das Telas v1.0

Sistema Integrado de Gestão de Missões da Diretoria de Promoção Social da PMAM.

---

# 1. Tela de Login

## Objetivo

Permitir acesso ao sistema conforme o perfil do usuário.

## Elementos

- Brasão da DPS
- Nome do sistema: SIGEM-DPS
- Campo usuário
- Campo senha
- Botão Entrar

---

# 2. Tela Inicial - Agenda de Missões

## Objetivo

Mostrar as execuções autorizadas, ordenadas por data e hora.

## Informações exibidas

- Data
- Hora
- Nome principal
- Local de saída
- Local de destino
- Status

## Ordenação

1. Data mais próxima
2. Hora mais próxima

O número da OS não define a ordem da agenda.

---

# 3. Nova Missão

## Objetivo

Cadastrar uma nova missão de forma simples e rápida.

## Campos

- Tipo de missão
- Nome principal
- Local de saída
- Local de destino
- Tipo de deslocamento
- Data
- Hora
- Telefone
- Observações

## Botões

- Salvar
- Salvar e enviar para autorização

---

# 4. Importar Solicitação WhatsApp

## Objetivo

Permitir colar uma mensagem recebida por WhatsApp e preencher automaticamente os campos da missão.

## Fluxo

1. Colar texto recebido
2. Clicar em Interpretar
3. Conferir os campos preenchidos
4. Salvar missão

---

# 5. Tela de Autorizações

## Objetivo

Permitir que Autorizadores e Administradores aprovem execuções pendentes.

## Exibição

- Data
- Hora
- Nome principal
- Local de saída
- Local de destino
- Botões Autorizar e Cancelar

---

# 6. Detalhes da Execução

## Objetivo

Visualizar todos os dados da execução.

## Informações

- Número da OS
- Tipo da missão
- Nome principal
- Local de saída
- Local de destino
- Data
- Hora
- Telefone
- Observações
- Status
- Criado por
- Autorizado por

## Botões

- Autorizar
- Imprimir OS
- Iniciar
- Concluir
- Cancelar

---

# 7. Impressão da Ordem de Serviço

## Objetivo

Gerar documento impresso da execução autorizada.

## Deve conter

- Brasão da DPS
- Nome da DPS/PMAM
- Número da OS
- Dados da missão
- Data e hora
- Local de saída
- Local de destino
- Observações
- Responsável pela autorização
- Espaço para assinatura

---

# 8. Roteiro Diário

## Objetivo

Imprimir todas as execuções autorizadas do dia.

## Deve conter

- Data
- Hora
- Nome principal
- Local de saída
- Local de destino
- Observações resumidas

---

# 9. Usuários

## Objetivo

Permitir ao Administrador gerenciar usuários.

## Campos

- Nome
- Usuário
- Senha
- Perfil
- Ativo/Inativo

## Perfis

- Operador
- Autorizador
- Administrador
