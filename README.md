# 💈 BarberFlow — Sistema de Agendamento para Barbearias

> 🚧 **Status: Em desenvolvimento**

O **BarberFlow** é uma plataforma web em desenvolvimento, criada para facilitar a conexão entre clientes e barbearias, tornando a busca por estabelecimentos e a solicitação de atendimentos mais práticas, organizadas e acessíveis.

A proposta é oferecer uma solução digital para pequenos empreendedores do setor de barbearias, permitindo que divulguem seus estabelecimentos e organizem seus atendimentos, enquanto os clientes podem encontrar opções de acordo com suas necessidades.

---

## 🎯 Objetivos do projeto

O principal objetivo do BarberFlow é simplificar a relação entre clientes e barbearias por meio de uma plataforma centralizada, intuitiva e funcional.

### Busca simplificada

Facilitar a descoberta de barbearias por nome, bairro ou cidade, ajudando os clientes a encontrar estabelecimentos que atendam às suas preferências e estejam em regiões convenientes.

### Organização de atendimentos

Permitir que os clientes solicitem reservas e acompanhem suas informações, enquanto os proprietários dispõem de uma estrutura digital que poderá evoluir para auxiliar na organização da rotina de atendimento.

### Apoio a pequenos empreendedores

Oferecer ferramentas digitais que auxiliem na administração e divulgação dos estabelecimentos, contribuindo para que pequenos negócios fortaleçam sua presença na internet sem depender exclusivamente de processos manuais.

### Centralização de informações

Reunir dados sobre barbearias, serviços, preços e localização em um único ambiente, tornando mais fácil consultar informações antes de escolher um estabelecimento.

### Praticidade para os usuários

Reduzir a dependência de mensagens, ligações e anotações para organizar atendimentos, buscando tornar a experiência de clientes e proprietários mais simples e conveniente.

---

## ✨ Funcionalidades atuais

O projeto já possui uma estrutura funcional com recursos básicos de navegação, autenticação, cadastro de estabelecimentos e solicitação de reservas. Como o desenvolvimento continua em andamento, essas funcionalidades representam a base atual da aplicação.

### Área do cliente

#### Cadastro e autenticação

O sistema permite criar uma conta e realizar login para acessar a área pessoal. Essa estrutura possibilita identificar os usuários e associar suas solicitações de atendimento às respectivas contas.

#### Pesquisa de barbearias

A página inicial permite pesquisar estabelecimentos por nome, bairro ou cidade, facilitando a descoberta de opções disponíveis na plataforma.

#### Página individual da barbearia

Cada estabelecimento possui uma página própria para apresentar suas informações e os serviços disponíveis, ajudando o cliente a conhecer melhor a barbearia antes de solicitar um atendimento.

#### Solicitação de reservas

O cliente pode selecionar um serviço e uma data para enviar uma solicitação de atendimento. O sistema registra a reserva e permite consultar seus detalhes posteriormente.

#### Painel pessoal

A área do cliente reúne as reservas realizadas, permitindo consultar informações sobre os atendimentos solicitados sem precisar procurar os dados novamente na página do estabelecimento.

### Área do proprietário

#### Painel de gerenciamento

O proprietário possui uma área separada da área do cliente, preparada para concentrar as ferramentas de administração da barbearia.

#### Cadastro de estabelecimento

Cada conta de proprietário pode cadastrar uma barbearia. A restrição é aplicada tanto na interface quanto nas regras do sistema, evitando que uma mesma conta registre vários estabelecimentos.

#### Limite diário de clientes

O proprietário pode definir uma capacidade diária de atendimento. Essa configuração serve como base para controlar a quantidade de solicitações aceitas por dia, embora o gerenciamento completo de filas e da duração dos serviços ainda esteja planejado.

### Estrutura técnica

#### Aplicação com Django

O projeto utiliza o Django para gerenciar rotas, autenticação, processamento de formulários, regras de negócio e comunicação com o banco de dados.

#### Integração com banco de dados

Os dados de usuários, estabelecimentos, serviços e reservas são organizados por meio dos modelos e do ORM do Django, facilitando a manutenção e a evolução da aplicação.

#### Controle de acesso

O sistema separa as áreas de clientes e proprietários e utiliza autenticação para proteger páginas que exigem uma conta. As permissões continuam sendo aprimoradas conforme novas funcionalidades são adicionadas.

---

## 🗺️ Funcionalidades planejadas

O BarberFlow continuará evoluindo conforme o desenvolvimento da aplicação e as necessidades de seus futuros usuários. As funcionalidades descritas nesta seção representam objetivos futuros e não devem ser consideradas disponíveis na versão atual.

### Para clientes

#### Consulta de serviços, preços e informações

A plataforma pretende oferecer páginas mais completas para cada barbearia, reunindo informações sobre os serviços disponíveis, seus respectivos preços, descrições e outros detalhes importantes. Dessa forma, os clientes poderão comparar opções e escolher o estabelecimento que melhor atende às suas expectativas antes de solicitar um atendimento.

#### Sistema de avaliações e comentários

Será planejado um sistema para que clientes possam avaliar suas experiências e compartilhar opiniões sobre as barbearias. As avaliações poderão ajudar outras pessoas a tomar decisões mais informadas, além de oferecer aos proprietários um retorno sobre a qualidade dos serviços prestados.

#### Recomendações e classificação de barbearias

O BarberFlow pretende desenvolver recursos para destacar estabelecimentos com base em critérios relevantes, como avaliações, qualidade percebida e informações cadastradas. O objetivo é facilitar a descoberta de barbearias adequadas às preferências dos clientes, mantendo critérios transparentes para a classificação dos resultados.

#### Consulta de disponibilidade e capacidade diária

Os clientes poderão consultar os dias em que uma barbearia aceita atendimentos e verificar se ainda existem vagas disponíveis. A plataforma deverá considerar o limite diário definido pelo proprietário para evitar solicitações acima da capacidade configurada e ajudar o cliente a escolher uma data adequada.

#### Fila de atendimento e posição do cliente

Uma das funcionalidades planejadas é permitir que os clientes ingressem na fila de atendimento de uma barbearia para acompanhar sua posição. Em vez de depender exclusivamente de horários fixos, o sistema poderá organizar os atendimentos conforme a ordem das solicitações e a disponibilidade do estabelecimento, respeitando suas regras de funcionamento.

#### Estimativa de tempo de espera

A plataforma poderá apresentar uma estimativa aproximada do tempo restante até o atendimento de cada cliente. Essa previsão deverá considerar fatores como a quantidade de pessoas à frente na fila, a duração estimada dos serviços e possíveis atrasos. Como o tempo real pode variar, a estimativa será uma referência, e não uma garantia de horário exato.

#### Notificações e atualizações de atendimento

O sistema pretende oferecer notificações sobre eventos importantes, como confirmação de reservas, alterações no atendimento, cancelamentos e aproximação da vez do cliente. Essas comunicações ajudarão os usuários a acompanhar suas solicitações sem precisar consultar o site repetidamente.

#### Cancelamento de reservas

Os clientes poderão contar com um fluxo próprio para cancelar solicitações de atendimento, seguindo regras claras sobre prazos e condições. O sistema deverá atualizar a disponibilidade da barbearia após o cancelamento e informar o proprietário sobre a alteração, evitando inconsistências na organização da fila.

#### Experiência em dispositivos móveis

O BarberFlow pretende aprimorar sua interface para celulares e tablets, adaptando formulários, menus, páginas de estabelecimentos e informações sobre reservas a diferentes tamanhos de tela. A prioridade será tornar as principais tarefas rápidas e intuitivas, especialmente para clientes que acessam a plataforma enquanto estão fora de casa.

### Para proprietários

#### Edição das informações da barbearia

Os proprietários poderão atualizar os dados do estabelecimento cadastrado, incluindo nome, descrição, endereço, telefone e outras informações relevantes. Isso permitirá manter a página pública atualizada sem depender de alterações manuais no banco de dados ou no código da aplicação.

#### Cadastro e gerenciamento de serviços

A plataforma deverá permitir cadastrar serviços, definir preços, incluir descrições e atualizar informações sempre que necessário. Essa funcionalidade ajudará os clientes a conhecer as opções disponíveis antes de solicitar um atendimento e facilitará a manutenção do catálogo pelo proprietário.

#### Gerenciamento de profissionais

Será planejado um recurso para cadastrar e administrar os profissionais que trabalham na barbearia. A intenção é permitir a organização das informações dos barbeiros e, futuramente, associar atendimentos e disponibilidades aos profissionais correspondentes, caso essa necessidade seja confirmada durante a evolução do projeto.

#### Configuração de funcionamento e disponibilidade

Os proprietários poderão definir dias de funcionamento, períodos de atendimento e limites de capacidade. Essas configurações servirão como base para a organização das reservas e filas, ajudando a evitar solicitações em dias indisponíveis ou acima da capacidade operacional do estabelecimento.

#### Gerenciamento de reservas e filas

O painel do proprietário deverá evoluir para permitir o acompanhamento dos atendimentos solicitados, a confirmação ou o cancelamento de reservas e a organização da fila. Também poderão ser implementadas regras para registrar ausências e avançar a fila de maneira organizada, preservando a consistência das informações.

#### Controle de capacidade diária

O sistema pretende aprimorar o controle de capacidade para considerar não apenas a quantidade máxima de clientes, mas também o tempo necessário para executar os serviços. Essa abordagem poderá ajudar a reduzir sobrecargas e tornar a organização dos atendimentos mais compatível com a rotina real da barbearia.

#### Histórico de atendimentos e indicadores

Os proprietários poderão consultar informações sobre atendimentos anteriores e acompanhar indicadores básicos do estabelecimento. Esses dados poderão auxiliar na identificação de períodos de maior movimento, na avaliação da demanda e no planejamento das atividades do negócio.

#### Publicações, promoções e novidades

Uma funcionalidade futura poderá permitir que os proprietários publiquem informações sobre promoções, novos serviços, mudanças no funcionamento e outras novidades. O objetivo será ampliar a presença digital das barbearias e facilitar a comunicação com clientes interessados.

### Melhorias gerais da plataforma

#### Aprimoramento da interface e da navegação

A interface continuará sendo refinada para tornar as páginas mais consistentes, os formulários mais claros e as ações principais mais fáceis de encontrar. O foco será reduzir etapas desnecessárias e oferecer uma experiência intuitiva tanto para clientes quanto para proprietários.

#### Segurança e validação de dados

O projeto deverá receber melhorias contínuas de segurança, incluindo validações no servidor, controle de permissões e proteção das operações realizadas pelos usuários. Essas medidas serão importantes para impedir ações não autorizadas e preservar a integridade dos dados de clientes, reservas e estabelecimentos.

#### Otimização de desempenho

Serão avaliadas consultas ao banco de dados, carregamento de páginas e operações que possam se tornar lentas com o crescimento da quantidade de usuários e barbearias. O objetivo é manter a aplicação responsiva sem introduzir complexidade técnica antes que ela seja necessária.

#### Testes automatizados

O BarberFlow pretende incorporar testes automatizados para verificar regras importantes, como cadastro de estabelecimentos, limites de capacidade, permissões de acesso e criação e cancelamento de reservas. Os testes ajudarão a detectar regressões e a tornar futuras alterações mais seguras.

#### Preparação para produção

Antes da disponibilização pública, serão realizados ajustes de implantação, configuração de variáveis de ambiente, proteção de informações sensíveis e preparação do banco de dados PostgreSQL. Essa etapa também deverá contemplar configurações adequadas de segurança, tratamento de erros e monitoramento básico da aplicação.

---

## 🛠️ Tecnologias utilizadas

O projeto utiliza tecnologias voltadas ao desenvolvimento web, com foco em organização, manutenção e evolução gradual da aplicação.

| Tecnologia | Aplicação no projeto |
|---|---|
| Python | Linguagem principal utilizada no desenvolvimento |
| Django | Framework responsável pela aplicação web e pelas regras de negócio |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização e identidade visual |
| SQLite | Banco de dados utilizado no ambiente de desenvolvimento |
| Git | Controle de versão do código-fonte |
| GitHub | Hospedagem do repositório |
| Visual Studio Code | Ambiente de desenvolvimento |

### Arquitetura da aplicação

A arquitetura utiliza o Django como núcleo da aplicação, reunindo páginas, autenticação, regras de negócio e acesso ao banco de dados. Essa abordagem permite desenvolver e manter as principais funcionalidades em uma estrutura integrada, sem a complexidade desnecessária de múltiplos serviços independentes.

O banco de dados SQLite é utilizado no ambiente de desenvolvimento, enquanto a adoção do PostgreSQL está prevista para a preparação do sistema para produção. Essa evolução permitirá trabalhar com uma configuração mais apropriada para uma aplicação disponibilizada publicamente.

---

## ⚙️ Como executar localmente

Para executar o BarberFlow em seu computador, é necessário ter Python e Git instalados. Os comandos abaixo consideram um ambiente Windows utilizando o Git Bash.

### Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
cd PASTA_DO_PROJETO
```

Substitua `URL_DO_REPOSITORIO` pelo endereço real do projeto no GitHub e `PASTA_DO_PROJETO` pelo nome da pasta criada.

### Criar e ativar o ambiente virtual

Um ambiente virtual mantém as dependências do projeto isoladas das demais instalações Python do computador.

```bash
python -m venv .venv
source .venv/Scripts/activate
```

### Instalar as dependências

Caso o repositório contenha um arquivo `requirements.txt`, instale as dependências listadas nele:

```bash
pip install -r requirements.txt
```

Se esse arquivo ainda não existir, será necessário instalar as dependências compatíveis com o projeto e gerar um arquivo de requisitos antes de disponibilizar instruções definitivas de instalação.

### Aplicar as migrações

As migrações criam ou atualizam as estruturas necessárias no banco de dados conforme os modelos da aplicação.

```bash
python manage.py migrate
```

### Iniciar o servidor de desenvolvimento

```bash
python manage.py runserver
```

Depois de iniciar o servidor, acesse o endereço abaixo pelo navegador:

`http://127.0.0.1:8000/`

> **Observação:** os comandos consideram uma configuração Django padrão. Dependências adicionais, variáveis de ambiente ou ajustes específicos podem ser necessários conforme a configuração atual do repositório.

---

## 🎨 Identidade visual

A identidade visual do BarberFlow busca transmitir modernidade, confiança e profissionalismo, utilizando uma paleta predominantemente escura com detalhes dourados.

### Azul-escuro — `#0B111D`

A cor azul-escura constitui a base visual da interface, ajudando a criar uma aparência moderna e consistente. Seu uso como cor predominante também favorece o contraste com elementos de destaque.

### Dourado — `#FFBE00`

O dourado é utilizado como cor de destaque para chamar a atenção para elementos importantes da interface, como botões e ações principais. A combinação com o fundo escuro busca reforçar a identidade visual da plataforma.

### Experiência de navegação

A proposta visual é oferecer uma interface organizada, agradável e funcional, priorizando a clareza das informações e a facilidade de navegação. O desenvolvimento deverá manter essa identidade consistente nas áreas de clientes e proprietários, inclusive em dispositivos móveis.

---

## 💡 Propósito e utilidade

Pequenas barbearias frequentemente dependem de mensagens, ligações e anotações para organizar seus atendimentos. Embora esses métodos possam funcionar, eles também podem dificultar o controle da disponibilidade, a organização das filas e a comunicação com os clientes.

O BarberFlow pretende centralizar essas atividades em uma plataforma digital, facilitando a descoberta de estabelecimentos e a solicitação de atendimentos por parte dos clientes, além de oferecer ferramentas de organização para os proprietários.

### Benefícios para os clientes

A plataforma pretende diminuir o esforço necessário para encontrar uma barbearia, consultar informações e solicitar um atendimento. Com os recursos planejados de disponibilidade, fila e notificações, os clientes também poderão ter mais clareza sobre o andamento de suas solicitações.

### Benefícios para os proprietários

O BarberFlow busca oferecer uma estrutura digital para apoiar a divulgação e a organização do estabelecimento. A evolução do painel administrativo poderá reduzir tarefas repetitivas, facilitar o controle dos serviços e melhorar a visibilidade das reservas e da capacidade de atendimento.

### Visão de longo prazo

A intenção é construir uma solução prática e acessível que ajude pequenos negócios a fortalecer sua presença digital, melhorar a organização cotidiana e proporcionar uma experiência mais conveniente aos seus clientes. O projeto será desenvolvido de forma gradual, priorizando funcionalidades úteis e uma arquitetura que possa ser mantida e ampliada sem complexidade desnecessária.

---

## 🚧 Estado do desenvolvimento

O BarberFlow permanece em desenvolvimento. A estrutura inicial, a autenticação, as páginas principais, o cadastro de barbearias e o fluxo básico de reservas já foram implementados.

### Etapa atual

O foco está na consolidação das funcionalidades existentes e na expansão das ferramentas de gerenciamento para proprietários. Também fazem parte dos próximos passos o aprimoramento da experiência dos clientes e o fortalecimento das regras de negócio relacionadas à disponibilidade e à capacidade de atendimento.

### Próximas etapas

A evolução do projeto deverá contemplar o gerenciamento de serviços e profissionais, as melhorias no fluxo de reservas, a organização de filas e a implementação gradual de recursos de avaliação e comunicação.

As funcionalidades descritas como planejadas representam objetivos futuros e ainda não devem ser consideradas disponíveis na versão atual.

---

## 👨‍💻 Autor

**bitcore** — [@bitcore-dev](https://github.com/bitcore-dev)

Desenvolvedor e criador do BarberFlow.

---

**BarberFlow — Conectando clientes e barbearias de forma mais simples, prática e organizada.**
