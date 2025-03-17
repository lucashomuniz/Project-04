# TRATAMENTO DE DADOS EM SQL

## STEP A: TRATAMENTO DA COLUNA "DATA" DA TABELA FATO_VENDAS
WITH base_data AS (SELECT
f.* EXCEPT(dta_venda),
DATE_ADD(dta_venda, INTERVAL 3 YEAR) AS dta_venda
FROM `project-test-3003.dataset_test.fato_vendas` f),

## STEP B1: PREENCHIMENTO DADOS VAZIOS "VLR_PRECO_UNITÁRIO" NA TABELA FATO_VENDAS
corrected_prices AS (

WITH average_prices AS (
SELECT
b.nom_sexo_cliente,
b.id_linha_produto,
b.nom_filial,
b.dta_venda,
AVG(SAFE_CAST(a.vlr_preco_unitario AS FLOAT64)) AS avg_last_20_days
FROM base_data b
LEFT JOIN base_data a
ON  b.nom_sexo_cliente = a.nom_sexo_cliente
AND b.id_linha_produto = a.id_linha_produto
AND b.nom_filial = a.nom_filial
AND a.dta_venda <= b.dta_venda
AND a.dta_venda > DATE_SUB(b.dta_venda, INTERVAL 20 DAY)
GROUP BY
b.nom_sexo_cliente,
b.id_linha_produto,
b.nom_filial,
b.dta_venda)

SELECT
b.* EXCEPT(vlr_preco_unitario),
COALESCE(
SAFE_CAST(b.vlr_preco_unitario AS FLOAT64),
avg_last_20_days) AS vlr_preco_unitario
FROM base_data b
LEFT JOIN average_prices ap
ON  b.nom_sexo_cliente = ap.nom_sexo_cliente
AND b.id_linha_produto = ap.id_linha_produto
AND b.nom_filial = ap.nom_filial
AND b.dta_venda = ap.dta_venda),

## STEP B2: CRIAÇÃO COLUNA "VLR_MARGEM_BRUTA" NA TABELA FATO_VENDAS
final_calculations AS (SELECT
cp.*,
dp.perc_imposto,
cp.vlr_preco_unitario * (1 + dp.perc_imposto) AS vlr_preco_total,

CASE WHEN cp.id_linha_produto = 1 THEN dmb.perc_marg_bruta_id_linha_produto_1
WHEN cp.id_linha_produto = 2 THEN dmb.perc_marg_bruta_id_linha_produto_2
WHEN cp.id_linha_produto = 3 THEN dmb.perc_marg_bruta_id_linha_produto_3
WHEN cp.id_linha_produto = 4 THEN dmb.perc_marg_bruta_id_linha_produto_4
WHEN cp.id_linha_produto = 5 THEN dmb.perc_marg_bruta_id_linha_produto_5
WHEN cp.id_linha_produto = 6 THEN dmb.perc_marg_bruta_id_linha_produto_6
ELSE 0 END AS perc_marg_bruta,

(cp.vlr_preco_unitario * (1 + dp.perc_imposto)) *
CASE WHEN cp.id_linha_produto = 1 THEN dmb.perc_marg_bruta_id_linha_produto_1
WHEN cp.id_linha_produto = 2 THEN dmb.perc_marg_bruta_id_linha_produto_2
WHEN cp.id_linha_produto = 3 THEN dmb.perc_marg_bruta_id_linha_produto_3
WHEN cp.id_linha_produto = 4 THEN dmb.perc_marg_bruta_id_linha_produto_4
WHEN cp.id_linha_produto = 5 THEN dmb.perc_marg_bruta_id_linha_produto_5
WHEN cp.id_linha_produto = 6 THEN dmb.perc_marg_bruta_id_linha_produto_6
ELSE 0 END AS vlr_margem_bruta
FROM corrected_prices cp
LEFT JOIN `project-test-3003.dataset_test.dim_produtos` dp ON cp.id_linha_produto = dp.id_linha_produto
LEFT JOIN `project-test-3003.dataset_test.dim_margem` dmb ON TRUE),

## STEP B3: INCLUSÃO DA COLUNA "NOM_LINHA_PRODUTO"
final_result AS (SELECT
fc.*,
dp2.nom_linha_produto
FROM final_calculations fc
LEFT JOIN `project-test-3003.dataset_test.dim_produtos` dp2
ON fc.id_linha_produto = dp2.id_linha_produto)

SELECT *
FROM final_result