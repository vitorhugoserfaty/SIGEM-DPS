# SIGEM-DPS

## Banco de Dados v1.0

Sistema Integrado de Gestão de Missões da Diretoria de Promoção Social da Polícia Militar do Amazonas.

---

# OBJETIVO

O banco de dados do SIGEM-DPS foi projetado para atender às necessidades operacionais da DPS, permitindo o cadastro, autorização, acompanhamento e histórico das missões executadas.

O sistema foi concebido para ser:

* Simples
* Rápido
* Flexível
* Adaptável a novas necessidades
* Fácil de utilizar

---

# ESTRUTURA GERAL

O sistema é composto por quatro entidades principais:

1. Usuários
2. Missões
3. Recorrências
4. Execuções

As Ordens de Serviço serão geradas a partir das Execuções.

---

# TABELA: usuarios

Controle de acesso ao sistema.

| Campo      | Tipo                                   |
| ---------- | -------------------------------------- |
| id         | Inteiro                                |
| nome       | Texto                                  |
| usuario    | Texto                                  |
| senha_hash | Texto                                  |
| perfil     | Operador, Autorizador ou Administrador |
| email      | Texto                                  |
| telefone   | Texto                                  |
| ativo      | Booleano                               |
| criado_em  | Data/Hora                              |

---

# PERFIS DE USUÁRIO

## Operador

Pode:

* Cadastrar missões
* Editar missões
* Consultar agenda
* Imprimir OS

Não pode:

* Autorizar missões
* Gerenciar usuários

---

## Autorizador

Pode:

* Tudo que o Operador faz
* Autorizar execuções
* Cancelar autorizações
* Reabrir execuções quando necessário

---

## Administrador

Pode:

* Tudo que o Autorizador faz
* Criar usuários
* Alterar senhas
* Ativar ou desativar usuários
* Alterar perfis
* Configurar o sistema

---

# TABELA: missoes

Representa a necessidade original da DPS.

Exemplos:

* Maria Leila → FCECON
* João Rossine → HPM
* Jander Guimarães → HPM
* Entrega de cadeira de rodas
* Transporte de efetivo para Manacapuru
* Compra de alimentação para plantão
* Apoio solicitado pelo Comando

---

## Campos

| Campo             | Tipo        |
| ----------------- | ----------- |
| id                | Inteiro     |
| tipo_missao       | Texto       |
| nome_principal    | Texto       |
| local_saida       | Texto       |
| local_destino     | Texto       |
| tipo_deslocamento | Texto       |
| telefone          | Texto       |
| observacoes       | Texto       |
| ativo             | Booleano    |
| criado_por        | FK usuarios |
| criado_em         | Data/Hora   |
| atualizado_em     | Data/Hora   |

---

# TIPOS DE MISSÃO

* Assistencial
* Operacional
* Logística
* Administrativa
* Outros

---

# TIPOS DE DESLOCAMENTO

* Ida
* Retorno
* Ida e Retorno

---

# TABELA: recorrencias

Controla missões repetitivas.

Exemplos:

* Todos os dias
* Segunda a Sexta
* Segunda, Quarta e Sexta
* Terça, Quinta e Sábado
* Datas específicas

---

## Campos

| Campo                | Tipo       |
| -------------------- | ---------- |
| id                   | Inteiro    |
| missao_id            | FK missoes |
| frequencia           | Texto      |
| dias_semana          | Texto      |
| data_inicio          | Data       |
| data_fim             | Data       |
| quantidade_execucoes | Inteiro    |
| ativo                | Booleano   |
| criado_em            | Data/Hora  |

---

# FREQUÊNCIAS PADRÃO

* Única
* Todos os Dias
* Segunda a Sexta
* Segunda, Quarta e Sexta
* Terça, Quinta e Sábado
* Personalizada

---

# TABELA: execucoes

Representa cada deslocamento efetivamente realizado.

É a principal tabela operacional do sistema.

A agenda principal será alimentada por esta tabela.

---

## Campos

| Campo            | Tipo        |
| ---------------- | ----------- |
| id               | Inteiro     |
| missao_id        | FK missoes  |
| numero_os        | Texto       |
| data_execucao    | Data        |
| hora_execucao    | Hora        |
| status           | Texto       |
| veiculo          | Texto       |
| motorista        | Texto       |
| autorizado_por   | FK usuarios |
| data_autorizacao | Data/Hora   |
| criado_em        | Data/Hora   |
| atualizado_em    | Data/Hora   |

---

# STATUS DAS EXECUÇÕES

* Pendente
* Autorizada
* Em Andamento
* Concluída
* Cancelada

---

# REGRAS DAS EXECUÇÕES

* Toda execução nasce como Pendente.
* Somente usuários Autorizadores ou Administradores podem autorizar.
* A agenda principal exibe as execuções.
* A ordenação ocorre por Data e Hora.
* O número da OS não define a ordem de execução.
* Veículo e motorista são opcionais.
* Execuções não podem ser excluídas.
* Execuções canceladas permanecem no histórico.

---

# NUMERAÇÃO DAS ORDENS DE SERVIÇO

Formato:

OS-0001/2026

OS-0002/2026

OS-0003/2026

---

## Regras

* Numeração automática.
* Reinicia a cada ano.
* Não pode ser alterada manualmente.
* Cada execução recebe sua própria OS.

---

# TABELA: historico

Responsável pela auditoria do sistema.

Toda ação relevante será registrada automaticamente.

---

## Campos

| Campo       | Tipo         |
| ----------- | ------------ |
| id          | Inteiro      |
| execucao_id | FK execucoes |
| usuario_id  | FK usuarios  |
| acao        | Texto        |
| data_hora   | Data/Hora    |

---

## Exemplos de ações registradas

* Missão criada
* Missão editada
* Execução criada
* Execução autorizada
* Execução iniciada
* Execução concluída
* Execução cancelada
* Impressão da OS

---

# FLUXO OPERACIONAL

MISSÃO

↓

RECORRÊNCIA

↓

EXECUÇÕES

↓

AUTORIZAÇÃO

↓

ORDEM DE SERVIÇO

↓

EXECUÇÃO

↓

CONCLUSÃO

---

# PRINCÍPIOS DO SIGEM-DPS

* O sistema deve se adaptar à DPS.
* O cadastro deve ser rápido.
* O operador não deve preencher informações desnecessárias.
* Qualquer usuário logado pode cadastrar missões.
* Somente Autorizadores e Administradores podem autorizar.
* O sistema deve ser flexível para comportar situações não previstas.
* Missões não são excluídas.
* O histórico deve ser preservado.
* A agenda operacional é mais importante que o número da OS.
* O foco do sistema é a missão, não o documento.
