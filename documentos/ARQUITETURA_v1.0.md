# SIGEM-DPS

## Arquitetura do Sistema v1.0

Sistema Integrado de Gestão de Missões da Diretoria de Promoção Social da PMAM.

---

# OBJETIVO

Desenvolver um sistema web para controle, autorização, acompanhamento e impressão das missões da DPS.

O sistema deverá ser simples, rápido, intuitivo e adaptado à realidade operacional da DPS.

---

# TECNOLOGIAS

## Backend

Python 3

Framework:

Flask

---

## Banco de Dados

PostgreSQL

---

## Frontend

HTML5

CSS3

Bootstrap 5

JavaScript

---

# HOSPEDAGEM

## Ambiente Inicial

GitHub

Render

---

## Ambiente Futuro

Servidor próprio ou hospedagem dedicada.

---

# ESTRUTURA DO PROJETO

SIGEM-DPS

/backend

/database

/static

/static/css

/static/js

/static/img

/templates

/uploads

/documentos

app.py

requirements.txt

README.md

---

# MÓDULOS DO SISTEMA

## Login

Controle de acesso por usuário e senha.

---

## Agenda de Missões

Tela principal do sistema.

Exibe:

* Data
* Hora
* Nome principal
* Local de saída
* Local de destino
* Status

Ordenação:

Data → Hora

---

## Missões

Cadastro da necessidade original.

Exemplos:

* Transporte de paciente
* Transporte de efetivo
* Entrega de cadeira de rodas
* Transporte de cilindro
* Apoio administrativo
* Outros

---

## Recorrências

Controle de missões repetitivas.

Exemplos:

* Todos os dias
* Segunda a Sexta
* Segunda, Quarta e Sexta
* Terça, Quinta e Sábado
* Personalizada

---

## Execuções

Representam os deslocamentos efetivos.

Cada execução poderá gerar sua própria Ordem de Serviço.

---

## Autorizações

Somente usuários com perfil:

* Autorizador
* Administrador

podem autorizar execuções.

---

## Impressão

### Ordem de Serviço Individual

### Roteiro Diário

---

## Usuários

Gerenciamento de usuários.

Perfis:

* Operador
* Autorizador
* Administrador

---

# FLUXO OPERACIONAL

Usuário cadastra missão

↓

Sistema cria recorrência

↓

Sistema gera execuções

↓

Autorizador aprova execução

↓

Sistema gera OS

↓

Impressão

↓

Execução

↓

Conclusão

---

# PRINCÍPIOS DO PROJETO

* Simplicidade
* Rapidez
* Flexibilidade
* Facilidade de uso
* Baixa necessidade de treinamento
* Adaptação à realidade da DPS
* Preservação do histórico
* Foco na missão e não na burocracia

---

# VERSÃO 1.0

Funcionalidades obrigatórias:

* Login
* Agenda
* Cadastro de missão
* Recorrência
* Autorizações
* Impressão de OS
* Roteiro diário
* Histórico
* Gestão de usuários

---

# VERSÕES FUTURAS

* Aplicativo Android
* Notificações
* Integração WhatsApp
* Assinatura digital
* Dashboard estatístico
* Geolocalização
