# Knitting

> Lifecycle assessment datasets for knitted fabric production across flat, circular, seamless, hosiery, and 3D knitting technologies.

**13 datasets** | Functional unit: 1 kg fabric | All 16 EF 3.1 impact indicators

## Overview

This process category covers knitting: the interlocking of yarn loops to form fabric. The system boundary includes direct electricity (knitting machines), indirect energy (HVAC, compressors, lighting), lubricants, yarn losses, textile waste, and capital goods (machine amortisation). Circular knitting datasets are parameterised by yarn fineness (dtex), while other technologies use average-case inventories.

## Datasets

The table below gives an overview of the GHG emission factor for each dataset. For the complete LCIA results, see [impact-scores.csv](impact-scores.csv): all 16 EF 3.1 indicators plus DQR scores and the Input required (kg) loss factor.

**Input required (kg)** is the kg of input yarn required per 1 kg of finished knitted fabric, accounting for technology- and fineness-specific yarn losses. Callers scale the upstream yarn input by this factor and add a yarn-waste flow for the lost fraction. See the repo-level [Handling material losses](../../README.md#handling-material-losses) note. See [methodology](methodology/) for per-technology derivation.

| Activity | GHG (kgCO2eq/kg) | Input required (kg) |
|----------|------------------:|------------------:|
| 3D Knitting, Average | 6.59 | 1.020408163 |
| Circular Knitting, 120 dtex | 3.33 | 1.041666667 |
| Circular Knitting, 150 dtex | 3.29 | 1.041666667 |
| Circular Knitting, 170 dtex | 3.26 | 1.041666667 |
| Circular Knitting, 200 dtex | 3.24 | 1.030927835 |
| Circular Knitting, 300 dtex | 3.20 | 1.030927835 |
| Circular Knitting, 330 dtex | 3.19 | 1.030927835 |
| Circular Knitting, 370 dtex | 3.19 | 1.030927835 |
| Circular Knitting, 45 dtex | 3.69 | 1.052631579 |
| Circular Knitting, 70 dtex | 3.48 | 1.052631579 |
| Flat Knitting, Average | 3.97 | 1.030927835 |
| Hosiery Knitting, Average | 3.96 | 1.020408163 |
| Seamless Knitting, Average | 4.15 | 1.025641026 |

## Methodology

Detailed methodology documentation: [methodology/](methodology/)
