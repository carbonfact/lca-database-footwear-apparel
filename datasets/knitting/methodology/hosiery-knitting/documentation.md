# Documentation

> Part of [Hosiery Knitting Methodology](README.md)

## 1. Background

### 1.1 Context

This document presents the modelling assumptions and data sources for **hosiery knitting**, representing the production of socks or similar small-diameter tubular knitted goods.

The model follows the same methodological principles applied in flat and circular knitting, ensuring coherence across all knitting process datasets.

### 1.2 Scope and functional unit

- **Functional unit:** 1 kg of hosiery fabric (average of mixed cotton and synthetic yarns).
- **System boundary:** Gate-to-gate hosiery knitting.
- **Included:**
  - Yarn losses, lubricants and related emissions
  - Electricity consumption (direct and indirect)
  - Machine depreciation (capital goods) and end-of-life (EoL)
  - Textile waste to treatment
- **Excluded:**
  - Fibre and yarn production (modelled upstream)
  - Sewing, dyeing, finishing and packaging
  - Factory building and auxiliary systems beyond indirect energy allocation

## 2. Technical Overview

### 2.1 Process characteristics

Hosiery knitting uses small-diameter single-cylinder circular knitting machines designed for automatic toe closure and optional linking.

Production rates, power consumption and material losses are highly dependent on the gauge, feed configuration and automation level.

Key benchmarks:

- **Output:** ~300--400 pairs/day per standard machine; premium multi-feed models can exceed 800 pairs/day (~33 pairs/h).
- **Machine weight:** typically **230--320 kg**.
- **Energy:** **0.5--1.2 kWh/kg** (machine electricity only).
- **Lubricant consumption:** **0.05--0.10 L/kg**, depending on lubrication system efficiency.
- **Yarn waste:** **2--5%**, depending on toe-closing system and yarn type.
