# Financial Freedom AI V1.0

This is a SKILL designed for a mid-term quantitative trading strategy specifically for the BTC/USD spot market.

## Project Overview
This project encapsulates the "Financial Freedom AI V1.0" quantitative trading strategy, aiming to provide stable decision support for traders by utilizing multi-timeframe resonance, trend following, and dynamic risk control mechanisms.

## Directory Structure
- `SKILL.md`: Core instruction file containing the AI assistant's operational logic and decision tree.
- `references/`: 
  - `strategy_logic.md`: Detailed strategy logic, technical indicator parameters, and entry/exit rules.
- `scripts/`:
  - `calc_position_size.py`: Python script for calculating recommended position size and amount.
- `LICENSE.txt`: Project license agreement (Proprietary).

## Core Strategy Features
- **Multi-timeframe Resonance**: Simultaneously analyzes D1, H4, and H1 timeframes to confirm trend consistency.
- **Dynamic Risk Control**: ATR (Average True Range) based dynamic stop loss and black swan protection.
- **Compensatory Position Management**: Dynamically adjusts position sizing based on total account loss to optimize risk/reward.

## Installation in OpenClaw

To use this SKILL in OpenClaw, you can install it using one of the following methods:

### Method 1: Git Installation (Recommended)
1. Open your OpenClaw terminal or configuration.
2. Run the following command to add this skill:
   ```bash
   openclaw skill add https://github.com/lokuokchon/geminiFinancial-Freedom-AI.git
   ```

### Method 2: Manual Installation
1. Clone this repository into your OpenClaw `skills` directory:
   ```bash
   git clone https://github.com/lokuokchon/geminiFinancial-Freedom-AI.git
   ```
2. Restart OpenClaw or refresh the skill list.

## How to Use
1. Ensure Python 3.x is installed.
2. Before making trading decisions, refer to the technical indicator requirements in `references/strategy_logic.md`.
3. Use `scripts/calc_position_size.py` to calculate the recommended position size for the current environment:
   ```bash
   py scripts/calc_position_size.py <Starting Capital> <Total Loss>
   ```

## Disclaimer
This strategy is for reference and learning purposes only and does not constitute any investment advice. The cryptocurrency market involves high risk; please trade cautiously with a full understanding of the risks.
