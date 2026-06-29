# Data Quality Rating (DQR) Framework

This document describes the Data Quality Rating (DQR) methodology applied to all process datasets in the Open Source LCA Database for Footwear & Apparel. The approach follows the **Product Environmental Footprint (PEF)** guidance for data quality assessment.

## Method

Each process dataset is assessed using the PEF DQR method. Exchanges that contribute cumulatively to the **top 80% of the GHG impact** are rated individually across four criteria. All remaining exchanges receive a default score of 3.

The four criteria are:

| Criterion | Abbreviation | Description |
|-----------|:------------:|-------------|
| Precision | P | Degree of measurement/estimation accuracy |
| Time representativeness | TiR | Age and currency of the data |
| Technological representativeness | TeR | Match between modelled and actual technology |
| Geographical representativeness | GR | Match between modelled and actual geography |

Each criterion is scored from 1 (best) to 5 (worst). The overall DQR for an exchange is calculated as:

$$
\text{DQR} = \frac{P + TiR + TeR + GR}{4}
$$

## Quality levels

| Overall DQR | Quality level |
|---|---|
| DQR < 1.5 | Excellent quality |
| 1.5 < DQR < 2.0 | Very good quality |
| 2.0 < DQR < 3.0 | Good quality |
| 3.0 < DQR < 4.0 | Fair quality |
| DQR > 4.0 | Poor quality |

## Calculation steps

The following procedure is applied to each process dataset, following the PEFCR approach:

1. **Identify contributions to climate change**: For each activity, compute the percentage contribution of every exchange to the total GHG impact.

2. **Select relevant exchanges**: Choose exchanges that cumulatively contribute to more than 80% of the climate change impact. These are the exchanges that will be individually scored.

3. **Rescale contributions to 100%**: Normalize the selected exchanges so their contributions sum to 100%.

4. **Assign data quality scores through expert judgment**: Rate each selected exchange on the four dimensions (P, TiR, TeR, GR) using a data source hierarchy: primary data > peer-reviewed journals > industry reports > machinery data.

5. **Compute weighted average DQR**: Calculate the overall process DQR as a weighted average across the selected exchanges, where the weights are the rescaled GHG contribution percentages.

All exchanges below the 80% cumulative threshold receive a default score of 3 on all four dimensions.

DQR scores for each dataset are available in the `impact-scores.csv` files.

---

## References

- European Commission (2013). *Commission Recommendation 2013/179/EU on the use of common methods to measure and communicate the life cycle environmental performance of products and organisations*. Official Journal of the European Union.
- Fazio, S., Castellani, V., Sala, S., Schau, E.M., Secchi, M., Zampori, L. and Diaconu, E. (2018). *Supporting information to the characterisation factors of recommended EF Life Cycle Impact Assessment method*. EUR 28888 EN, European Commission.
- Weidema, B.P. and Wesnaes, M.S. (1996). Data quality management for life cycle inventories -- an example of using data quality indicators. *Journal of Cleaner Production*, 4(3-4), pp.167-174.
