# Financial Freedom AI V1.0 Logic Details

This document contains the complete logic of the "Financial Freedom AI V1.0" quantitative trading strategy, for AI assistants' reference when performing trading analysis or code generation.

## I. Basic Strategy Information
- **Strategy Name**: Financial Freedom AI V1.0
- **Strategy Type**: Trend Following, Reversal, Breakout
- **Applicable Market**: Spot
- **Applicable Assets**: BTC/USD
- **Operating Timeframe**: Main timeframe 1h (H1)
- **Multi-timeframe Resonance**: D1 (Direction), H4 (Trend), H1 (Entry)

## II. Technical Indicator Parameters
- **MA**: 100, 100, 200
- **ADX**: 14, > 25
- **SAR**: 0.02, 0.02, 0.125
- **ZigZag**: 12, 5, 3
- **RSI**: 14, 70/30/50
- **Stoch**: 14, 3, 3, 80/20/35
- **MACD**: 12, 26, 9
- **ATR**: 14

## III. Trading Rules
### 3.1 Entry Rules
- **Breakout Long**: Trend Resonance (D1/H4 MA upward) + Breakout of previous high/trendline + Indicator filtering (CCI, ADX, MACD, ATR) + Retest confirmation.
- **Reversal Long**: D1 MA upward + Elliott Wave/Harmonic Pattern Point D + Indicator oversold (RSI, Stoch, CCI) + Entry signal (ATR, Candlestick patterns, SAR reversal).

### 3.2 Exit and Risk Control
- **Stop Loss**: ATR*2 (Dynamic), ATR*5 (Black Swan), SAR reversal.
- **Take Profit**: Risk/Reward 1:3, SAR trailing stop, Technical level TP, Stoch >= 80.
- **Position Management**: 0.5% + (Total Loss Amount / 11 / Starting Capital * 100).
- **Risk Management**: Single trade max 7%, Single day max 5%, Stop after 13 consecutive losses, Pause for 3 days after 5 consecutive losses.

## IV. Market Filtering
- Do not open positions if ADX <= 25 for 3 consecutive candles.
- ATR <= Historical Average * 0.5 is considered a false breakout.
- Suspend opening new positions 12 hours before major events.
