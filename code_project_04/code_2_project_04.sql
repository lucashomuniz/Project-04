# TRATAMENTO DE DADOS EM SQL

-- STEP C1: SELEÇÃO DOS DADOS RELEVANTES
WITH vendas_resumidas AS ( SELECT nom_filial, EXTRACT(MONTH FROM dta_venda) AS month, id_linha_produto, SUM(qtd_produtos) AS qtd_produtos
FROM `project-test-3003.dataset_test.fato_vendas`
GROUP BY nom_filial, month, id_linha_produto),

-- STEP C2: CÁLCULO DO TOTAL DE PRODUTOS POR FILIAL E MÊS
produtos_totais AS (SELECT nom_filial, month, SUM(qtd_produtos) AS total_produtos
FROM vendas_resumidas
GROUP BY nom_filial, month),

-- STEP C3: CÁLCULO DA PARTICIPAÇÃO POR LINHA DE PRODUTO
participacao_produtos AS (SELECT v.nom_filial, v.month, v.id_linha_produto, v.qtd_produtos, p.total_produtos, ROUND(v.qtd_produtos / p.total_produtos, 6) AS perc_qtd_produtos
FROM vendas_resumidas v JOIN produtos_totais p
ON v.nom_filial = p.nom_filial AND v.month = p.month),

-- STEP C4: CÁLCULO DO VALOR DE INVESTIMENTO
investimentos_calculados AS (SELECT pp.nom_filial, pp.month, pp.id_linha_produto, pp.qtd_produtos, pp.perc_qtd_produtos,
ROUND(pp.perc_qtd_produtos * 10000, 2) AS valor_investido FROM participacao_produtos pp),

-- STEP C5: TABELA FINAL COM DADOS COMPLETOS
final_table AS (SELECT ic.nom_filial, ic.month, dp.nom_linha_produto, ic.qtd_produtos, ic.perc_qtd_produtos, ic.valor_investido 
FROM investimentos_calculados ic JOIN `project-test-3003.dataset_test.dim_produtos` dp
ON ic.id_linha_produto = dp.id_linha_produto)

SELECT *
FROM final_table