# Textile Assembly

> Lifecycle assessment datasets for generic garment and accessory assembly (cutting, sewing, finishing) across apparel and home-textile product types.

**15 datasets** | Functional unit: 1 kg assembled product | All 16 EF 3.1 impact indicators

## Overview

This process category covers textile assembly: the conversion of finished fabric into a final product through cutting, sewing, and ancillary make-up operations. The system boundary includes direct electricity (cutting tables, sewing machines, pressing equipment), indirect energy (HVAC, compressed air, lighting), sewing thread, packaging, fabric losses (cutting waste), and capital goods (machine amortisation). Datasets are provided per product archetype (apparel, accessories, home textiles), each representing an average-case generic assembly inventory.

## Datasets

The table below gives an overview of the GHG emission factor for each dataset. For the complete LCIA results, see [impact-scores.csv](impact-scores.csv): all 16 EF 3.1 indicators plus DQR scores and the Input required (kg) loss factor.

**Input required (kg)** is the kg of input fabric required per 1 kg of finished assembled product, accounting for cutting losses and other product-specific fabric waste. Callers scale the upstream fabric input by this factor and add a textile-waste flow for the lost fraction. See the repo-level [Handling material losses](../../README.md#handling-material-losses) note.

| Activity | GHG (kgCO2eq/kg) | Input required (kg) |
|----------|------------------:|------------------:|
| Generic assembly, Accesory | 3.18 | 1.1111 |
| Generic assembly, Bag | 2.24 | 1.1111 |
| Generic assembly, Belt-shawl-hat-bag-scarf | 2.68 | 1.1111 |
| Generic assembly, Dress | 0.26 | 1.2195 |
| Generic assembly, Houseware | 6.30 | 1.2000 |
| Generic assembly, Jacket | 2.60 | 1.1905 |
| Generic assembly, Pants | 0.42 | 1.1628 |
| Generic assembly, Shirts | 0.26 | 1.1494 |
| Generic assembly, Shorts | 0.42 | 1.1765 |
| Generic assembly, Skirts | 0.42 | 1.1628 |
| Generic assembly, Suit | 2.60 | 1.1905 |
| Generic assembly, Sweater | 0.33 | 1.1111 |
| Generic assembly, Swimwear | 0.09 | 1.2195 |
| Generic assembly, Tshirt | 0.15 | 1.1494 |
| Generic assembly, Underwear | 4.35 | 1.1494 |

## Methodology

Detailed methodology documentation: [methodology/](methodology/)
