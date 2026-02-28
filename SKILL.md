---
name: financial-freedom-ai-v1-0
description: BTC/USD Spot mid-term quantitative trading strategy (Financial Freedom AI V1.0). Provides comprehensive trend following, reversal, and breakout trading logic, including ATR-based dynamic stop loss and complex position management formulas. Suitable for 1h timeframe analysis.
---

# Financial Freedom AI V1.0

## Overview

This SKILL encapsulates the "Financial Freedom AI V1.0" quantitative trading strategy. It is a mid-term trading strategy specifically designed for the BTC/USD spot market. The core lies in using multi-timeframe resonance (D1/H4/H1) to confirm trends, combined with various technical indicators (MA, ADX, SAR, RSI, Stoch, ZigZag, Elliott Wave) for precise entry and dynamic risk control.

## Workflow Decision Tree

When a user requests market analysis or trade execution, follow this process:

1. **Market Environment Analysis**
   - Check D1 timeframe MA100/200 direction to determine the macro trend.
   - Check if ADX(14) is greater than 25 (to determine if a trend exists).
   - Check if Stoch is in overbought/oversold zones.

2. **Timeframe Alignment**
   - **D1**: Determine long-term direction (Long/Short/Sideways).
   - **H4**: Determine mid-term trend.
   - **H1**: Search for specific entry points.

3. **Strategy Selection**
   - **Breakout Long**: Trend up + price breakout of previous high/trendline.
   - **Reversal Long**: Trend up + price pullback to key support (e.g., Fibonacci, Elliott Wave Point D) + indicator oversold.

4. **Entry Validation**
   - Validate if indicators like CCI, MACD, RSI, SAR meet entry requirements.
   - Check candlestick patterns (e.g., Engulfing, Hammer).

5. **Position & Risk Calculation**
   - Calculate position size using the formula: `0.5% + (Total Loss / 11 / Starting Capital * 100)`.
   - Set dynamic stop loss (ATR * 2).

6. **Exit Execution**
   - Monitor SAR reversal, 1:3 Risk/Reward ratio, or Stoch overbought signals for profit taking.

## Core Capabilities

### 1. Technical Indicator Configuration
- **MA**: 100, 100, 200 (Multi-timeframe filter).
- **ADX**: 14 (Threshold 25).
- **SAR**: 0.02, 0.02, 0.125 (Entry and profit taking).
- **ATR**: 14 (Used for stop loss and volatility filtering).

### 2. Detailed Entry Strategies
- **Breakout Long**: 
  - Conditions: D1/H4 MA up + H1 breakout of previous high.
  - Filters: ADX > 25, MACD crossover, CCI > 100.
- **Reversal Long**:
  - Conditions: D1 MA up + H1 reaches oversold zone (RSI < 30, Stoch < 20).
  - Signal: SAR upward reversal + candlestick reversal pattern.

### 3. Risk & Position Management
- **Stop Loss Strategy**: 
  - Dynamic Stop Loss: ATR * 2.
  - Black Swan Stop Loss: Price < Entry Price - ATR * 5.
- **Position Management**: 
  - Initial ratio 0.5%.
  - Compensatory position sizing logic (see `scripts/calc_position_size.py`).

## Resources

### scripts/
- `calc_position_size.py`: Calculates recommended position size and amount based on strategy formulas.

### references/
- `strategy_logic.md`: Contains complete strategy details, indicator parameters, and detailed entry/exit rules.

## Usage Example

**User Request**: "BTC just broke the 65000 resistance on H1, D1 trend is up. Should I open a position?"

**Assistant Response**:
1. Read `references/strategy_logic.md` to confirm breakout long filtering conditions.
2. Check ADX, MACD, CCI indicators (if data provided by user).
3. Call `scripts/calc_position_size.py` to calculate position size.
4. Provide recommendation: According to the strategy, if ADX > 25 and breakout is confirmed on pullback, a long position can be opened with stop loss at `Price - ATR*2`.
