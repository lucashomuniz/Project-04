# ✅ PROJECT-20

Este projeto de análise de dados tem como principal objetivo fornecer respostas estratégicas para perguntas de negócio de um supermercado em modernização. Ao utilizar dados capturados recentemente por uma nova ferramenta de armazenamento, o projeto busca transformar essas informações em insights que orientem decisões de investimento, otimização de recursos e melhoria no atendimento ao cliente.

A escolha das ferramentas SQL e Power BI é central para garantir a eficiência e a clareza do processo analítico. O SQL, amplamente reconhecido por sua robustez e flexibilidade no tratamento de grandes volumes de dados, será utilizado para manipular e organizar as bases de dados. Essa abordagem permite não apenas estruturar as informações de forma lógica e confiável, mas também garantir rastreabilidade e eficiência na execução de operações complexas. A capacidade do SQL de integrar e consolidar informações de diferentes tabelas e corrigir inconsistências nos dados é fundamental para criar uma base sólida para as análises subsequentes.

O foco do projeto está em responder questões-chave de negócio, como identificar as melhores linhas de produtos para investimento, entender padrões de comportamento dos clientes e otimizar recursos humanos nas operações. Essa abordagem orientada a perguntas estratégicas garante que os dados sejam utilizados de maneira prática e direcionada, gerando valor mensurável para a empresa. Além disso, o uso integrado de SQL e Power BI reforça a confiabilidade do processo e a qualidade das respostas, estabelecendo um fluxo de trabalho eficiente e orientado a resultados.

Keywords: PowerBI, PowerQuery, DAX, Google Cloud Plataform, Business Analytics, Python Language, Data Visualization, Data Analysis.

# ✅ PROCESS

Na **Fase 1**, são realizadas transformações e manipulações de dados utilizando SQL no ambiente do Google Cloud Platform (GCP). O primeiro passo envolve o tratamento da coluna de datas na tabela “Fato_Vendas”, corrigindo inconsistências geradas por um problema no sistema de coleta, que registrou todas as datas no ano de 2019. Essas datas serão ajustadas para 2022, mantendo os dias e meses originais. Em seguida, será criada uma nova coluna “vlr_margem_bruta”, calculada com base no “vlr_preco_total”, que combina o preço unitário e o imposto. Antes disso, será necessário corrigir os valores nulos na coluna “vlr_preco_unitario”, utilizando a média dos últimos 20 dias, segmentada por gênero, linha de produto e filial. Após essa correção, o cálculo da margem bruta será possível. Por fim, será gerada uma tabela que distribui um investimento mensal de R$ 10.000,00 por filial, com base na quantidade de produtos vendidos por linha de produto e mês. Essa tabela incluirá informações sobre participação relativa e o valor exato investido.

A **Fase 2** concentra-se na criação de visualizações e análises no Power BI, conectando diretamente as tabelas tratadas no GCP. Inicialmente, será analisada a linha de produto mais promissora para investimento em 2023, considerando variáveis como crescimento de vendas mensais, gênero dos consumidores e desempenho geral. Além disso, serão avaliados os horários críticos para alocação de funcionários terceirizados em momentos de pico nas filiais, utilizando padrões de vendas por hora para identificar os períodos de maior demanda. Por fim, será analisada a satisfação dos clientes por filial, avaliando possíveis diferenças nos padrões de atendimento e identificando características que possam justificar qualquer problema.

# ✅ CONCLUSION

FASE 1: 

Na primeira etapa, as bases “fato_vendas”, “dim_produto” e “dim_margem_bruta_perc” foram carregadas na nuvem do Google Cloud Platform (GCP), possibilitando que todo o processo de tratamento ocorresse no BigQuery. Esse ambiente gerenciado e de alto desempenho tornou a manipulação de grandes volumes de dados mais eficiente e simplificou a manutenção de infraestrutura, além de favorecer integrações futuras, como a conexão direta com o PowerBI. As atividades de limpeza e padronização de dados — incluindo correção de datas, preenchimento de valores nulos e cálculo de indicadores — criaram uma base confiável e rastreável para análises avançadas, enquanto a arquitetura distribuída do BigQuery garantiu agilidade no processamento de consultas. A decisão de manter tudo no GCP dispensou a necessidade de pipelines manuais e acelerou tanto o desenvolvimento quanto a atualização de dashboards no PowerBI, resultando em maior produtividade.

FASE 1A:

Para aprimorar a organização e a legibilidade dos ajustes no banco de dados, optou-se pelo uso de Common Table Expressions (CTEs). Essa estratégia dividiu a lógica em etapas nomeadas e modulares, viabilizando a reutilização de resultados intermediários sem duplicar trechos complexos de SQL. O foco principal foi corrigir datas de venda e valores de preço unitário, além de criar uma nova coluna de margem bruta. No “STEP A”, as datas que apareciam incorretamente em 2019 foram ajustadas para 2022 por meio da CTE “base_data”, que aplicou DATE_ADD para somar três anos às datas equivocadas.

FASE 1B:

Na sequência, o “STEP B1” corrigiu valores nulos de “vlr_preco_unitario” calculando a média dos preços dos últimos 20 dias conforme gênero do cliente, linha de produto e filial, por meio da CTE “average_prices”. Os valores resultantes foram então aplicados pela CTE “corrected_prices” para preencher os nulos, embora alguns ainda tenham permanecido sem histórico suficiente. Em “STEP B2”, criou-se a coluna “vlr_margem_bruta” combinando o valor de imposto da tabela “dim_produtos” e o percentual de margem bruto obtido em “dim_margem_bruta_perct”. Essa lógica resultou no valor de margem bruta para cada item, concluindo o ajuste das datas, dos preços e do cálculo de margem.

FASE 1C:

O objetivo desta parte foi distribuir um investimento mensal de 10 mil reais por filial, conforme a quantidade de produtos vendidos em cada linha de produto e mês. Inicialmente, a CTE “vendas_resumidas” soma a quantidade de produtos vendidos por filial, mês e linha de produto. A CTE “produtos_totais” obtém o total de vendas em cada filial e mês, permitindo o cálculo da participação relativa na “participacao_produtos”. Por fim, a CTE “investimentos_calculados” distribui o valor do investimento proporcionalmente a essa participação, e a “final_table” faz o JOIN com “dim_produtos” para exibir o nome do produto ao lado do valor de investimento respectivo.

FASE 2:

Nesta segunda fase, desenvolveu-se um dashboard no PowerBI para apresentar de forma clara os resultados extraídos do BigQuery. Graças à arquitetura escalável do GCP, grande parte das transformações pôde ser executada na própria fonte, evitando sobrecarga no PowerQuery. Esse fluxo facilitou ajustes no modelo de dados e proporcionou atualizações quase em tempo real. O dashboard foi organizado em abas específicas para cada pergunta de negócio, permitindo que o usuário navegue de forma segmentada, explorando métricas e visuais relevantes para cada aspecto analisado.

FASE 2A:

Foi criada uma medida DAX, “m_faturamento”, que multiplica a quantidade vendida pelo preço unitário (função SUMX). Em seguida, um Parâmetro possibilita ao usuário escolher a métrica principal (Faturamento, Preço Unitário ou Quantidade de Produtos) em cada visualização. Observando o Faturamento, destaca-se o crescimento do PRODUTO 6 para o público feminino, partindo de 57 mil em janeiro e alcançando 152 mil em março. Para o público masculino, o PRODUTO 3 mostra trajetória similar, indo de 42 mil para 151 mil no mesmo período. Essa análise confirma que esses produtos conciliam bom volume de vendas e preços ascendentes, sendo estratégicos para maximizar retorno financeiro em cada segmento de gênero.

![Screenshot 2025-01-14 at 17 00 38](https://github.com/user-attachments/assets/430a94a5-43c0-44c2-8e17-7ad73299ef76)

FASE 2B:

Aqui, criou-se uma coluna calculada chamada “periodo_venda” para agrupar o horário de venda em intervalos de uma hora. A mesma lógica de Parâmetro permite filtrar a métrica principal, e, considerando o Faturamento, evidencia-se que o intervalo de 19h00 às 20h00 gera R$ 342,17 mil no conjunto total de filiais, sendo também o pico na Filial B e um dos mais altos na A. Já na Filial A, o período de 12h00 às 13h00 se destaca, enquanto na Filial C o horário mais rentável é entre 10h00 e 11h00. Dessa forma, alocar funcionários terceirizados entre 19h00 e 20h00 atende melhor às demandas da maioria das unidades, enquanto 12h00 às 13h00 e 10h00 às 11h00 também merecem atenção.

![Screenshot 2025-01-14 at 17 00 55](https://github.com/user-attachments/assets/af232891-0007-4f24-b6d6-279e03cc0610)

FASE 2C:

Nesta análise, cruzaram-se variáveis como “num_avaliacao”, “nom_filial” e outras características para detectar possíveis problemas de satisfação. Em geral, todas as filiais mostram distribuições de notas relativamente próximas, com a Filial C destacando-se positivamente pelo maior número de avaliações nota 10 e menor incidência de nota 2. Embora existam diferenças como predominância de clientes “member” ou “normal” e variações nos produtos mais avaliados, não há sinal de grave insatisfação. Observa-se que a Filial C obtém resultados mais sólidos em engajamento e avaliação, indicando a oportunidade de compartilhar suas boas práticas com as demais unidades, em vez de se concentrar em eventuais falhas pontuais.

![Screenshot 2025-01-14 at 17 01 05](https://github.com/user-attachments/assets/48530221-fbde-424c-ab9d-79e0939b022b)

