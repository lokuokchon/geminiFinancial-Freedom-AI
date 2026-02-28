#!/usr/bin/env python3
import sys

def calculate_position_size(starting_capital, total_loss):
    """
    Calculate single trade position size (Based on JoeQuantStrategy)
    Formula: 0.5% + (Total Loss / 11 / Starting Capital * 100)
    """
    base_percentage = 0.5
    loss_factor = (total_loss / 11 / starting_capital) * 100
    total_percentage = base_percentage + loss_factor
    
    # Calculate specific amount
    position_amount = (total_percentage / 100) * starting_capital
    
    return total_percentage, position_amount

def main():
    if len(sys.argv) < 3:
        print("Usage: py calc_position_size.py <starting_capital> <total_loss>")
        print("Example: py calc_position_size.py 10000 500")
        sys.exit(1)
        
    try:
        starting_capital = float(sys.argv[1])
        total_loss = float(sys.argv[2])
        
        perc, amount = calculate_position_size(starting_capital, total_loss)
        
        print(f"--- JoeQuantStrategy Position Size Calculator ---")
        print(f"Starting Capital: {starting_capital:.2f} USD")
        print(f"Total Loss Amount: {total_loss:.2f} USD")
        print(f"------------------------------------------------")
        print(f"Recommended Position Percentage: {perc:.4f}%")
        print(f"Recommended Position Amount: {amount:.2f} USD")
        
    except ValueError:
        print("Error: Please provide valid numbers for capital and loss.")
        sys.exit(1)

if __name__ == "__main__":
    main()
