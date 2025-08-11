#!/usr/bin/env python3
"""
Demonstration script for seed-everything library.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from seed_everything import seed_everything
import random

def main():
    print("=== Seed Everything Demo ===")
    print()
    
    # Show PYTHONHASHSEED before seeding
    print(f"PYTHONHASHSEED before: {os.environ.get('PYTHONHASHSEED', 'Not set')}")
    
    # Set seed
    print("Setting seed to 42...")
    seed_everything(42)
    print(f"PYTHONHASHSEED after: {os.environ['PYTHONHASHSEED']}")
    print()
    
    # Generate some random values
    print("Generating random values with seed 42:")
    values_1 = [round(random.random(), 4) for _ in range(5)]
    print(f"Values 1: {values_1}")
    
    # Reset and generate again
    print("\nResetting seed to 42 and generating again:")
    seed_everything(42)
    values_2 = [round(random.random(), 4) for _ in range(5)]
    print(f"Values 2: {values_2}")
    
    print(f"\nValues match: {values_1 == values_2}")
    
    # Try different seed
    print("\nUsing different seed (123):")
    seed_everything(123)
    values_3 = [round(random.random(), 4) for _ in range(5)]
    print(f"Values 3: {values_3}")
    print(f"Different from seed 42: {values_1 != values_3}")
    
    print("\n✓ Demo completed successfully!")

if __name__ == '__main__':
    main()
