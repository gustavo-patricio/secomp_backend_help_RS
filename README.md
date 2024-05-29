# secomp_backend_help_RS
Projeto desenvolvido tem como objetivo ser um serviço destinado a doadores e a empresas ou órgãos que estão coletando essas doações para o Rio Grande do Sul.

### Visão geral
Construir a parte de Backend da aplicação Help_RS em Python. Essa aplicação deve fornecer aos Doadores informações de como e onde estar entregando suas doações.

### Diagrama de Caso de Uso
```mermaid
flowchart LR
    usuario --> id1
    usuario --> id2
    instituição --> id3
    subgraph Casos de Uso Help RS
    id1([visualiza pontos de entrega])
    id2([visualiza orientações de doações])
    id3([Mantem ponto de entrega])
    end
```
