# minicurso-devops

- [Introdução](#introdução-à-devops-falando-sobre-jogos)
- [Ferramentas](#ferramentas)
- [Atividades](#atividades)

## Introdução à DevOps falando sobre Jogos

### O que é DevOps

![ciclo-devops](./images/image.png)

<br>

> ### Teoria

DevOps é uma cultura e um conjunto de práticas que une o desenvolvimento de software (Dev) e as operações de TI (Ops). O objetivo é encurtar o ciclo de desenvolvimento, aumentar a frequência de implantações e garantir lançamentos de alta qualidade.

> ### Os 5 Pilares do DevOps (Modelo C.A.L.M.S.)

C - Culture (Cultura):

Ferramentas não consertam problemas humanos. O foco é colaboração, confiança e responsabilidade compartilhada.

Desenvolvedores e Operações participam das mesmas reuniões (Dailies/Plannings) e têm objetivos comuns, não conflitantes.

<br>

A - Automation (Automação):

Automatizar qualquer processo manual repetitivo para ganhar velocidade e consistência.

Na prática: Scripts que criam servidores, instalam dependências e rodam testes sem intervenção humana (Infra as Code, CI/CD).

<br>

L - Lean (Enxuto):

Mentalidade de "menos desperdício". Fazer entregas em lotes pequenos para errar pouco e corrigir rápido.

Na prática: Em vez de lançar uma atualização gigante a cada 6 meses (alto risco), lançar pequenas melhorias toda semana (baixo risco).

<br>

M - Measurement (Medição/Métricas):

Você não melhora o que não mede. É preciso dados para tomar decisões, não "achismo".

Na prática: Medir o tempo de recuperação de falhas, tempo de deploy e frequência de erros, usando dashboards visíveis para todos.

<br>

S - Sharing (Compartilhamento):

O conhecimento deve fluir livremente. O oposto de reter informação para ter poder.

Na prática: Se alguém resolve um problema difícil, documenta e ensina os outros. Sucessos e falhas são compartilhados abertamente para o aprendizado coletivo.

<br>

> ### Prátia

O profissional de DevOps é o arquiteto da automação e da infraestrutura. Ele atua como uma ponte técnica, criando ferramentas e ambientes para que os desenvolvedores tenham autonomia para entregar código rápido, seguro e sem depender de processos manuais.

<br>

---

## Ferramentas

### Git: o melhor check point de todos os tempos

Git é um Sistema de Controle de Versão Distribuído. Ele registra o histórico completo de todas as alterações feitas no código, permitindo que você viaje no tempo para qualquer versão anterior do projeto e saiba exatamente quem fez o quê e quando.

Confiração rápida
~~~sh
git config --global user.name "juninhogameplays"
git config --global user.email "juninhogameplays"@email.com"
~~~

Comandos mais usados:
~~~sh
# inicia um novo repositório na pasta atual
git init .

# cria uma nova branch
git branch nova-branch

# muda para a nova branch
git checkout nova-branch

# atalho: cria uma nova branch e já muda para ela
git checkout -b nova-branch

# adiciona todas as mudanças à área de preparação (stage)
git add .

# salva as mudanças (cria o check point)
git commit -m "estou fazendo um commit"

# envia as mudanças para um repositório remoto
git push

# funde (une) as mudanças da branch escolhida na branch atual
git merge nova-branch
~~~

### Github: qual tal compartilhar o saves com amigos?


O GitHub é uma plataforma de hospedagem de código na nuvem (SaaS). Ele funciona como um servidor central onde os desenvolvedores guardam seus históricos do Git, permitindo backup seguro, gestão de versões e, principalmente, o trabalho colaborativo simultâneo.

<br>

### Docker: um emulador universal

Docker é uma plataforma de containerização que empacota uma aplicação e todas as suas dependências (bibliotecas, arquivos de configuração, etc) em uma unidade padronizada chamada Container. Isso garante o isolamento e a portabilidade, fazendo com que o software rode exatamente da mesma maneira no pc do desenvolvedor e no servidor de produção, eliminando o problema de compatibilidade.

Mais sobre Docker aqui: https://github.com/adelsonsljunior/workshop-docker

<br>

### Dockerhub: o que seria dos emuladores sem um site pra baixar ROMs?

O Docker Hub é o Registry (Registro) oficial de imagens na nuvem. Ele atua como uma biblioteca global onde desenvolvedores e empresas armazenam e compartilham imagens de containers. Em vez de configurar um banco de dados ou um sistema operacional do zero, você baixa a 'imagem' pronta e oficial diretamente do Docker Hub para iniciar seu serviço em segundos.

<br>

### Github Actions

O GitHub Actions é a ferramenta de automação nativa do GitHub. Ela permite criar fluxos de trabalho (pipelines) que executam tarefas automaticamente — como testar o código, gerar versões e fazer o deploy

---

## Atividades

> ### 01 

Suba a seguinte aplicação: https://github.com/adelsonsljunior/urubu-do-pix-backend

<br>

> ### 02

+ Faça o fork deste repositório
+ Crie uma conta no Dockerhub
+ Configure os secrets do Github Actions
+ Subi a imagem pra sua conta no Dockerhub
+ Adapte o `docker-compose.prod.yaml`para rodar sua imagem
+ Suba as mudanças para o Github