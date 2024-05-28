# Coffee Machine Project

This repository contains a simple command-line coffee machine simulator written in Python. The project was developed as a learning exercise to practice Python programming, including functions, conditionals, loops, and user input handling.

## Features

- Three types of coffee available: Espresso, Latte, and Cappuccino.
- Reports current resource levels.
- Processes user inputs to buy coffee, check resources, or turn off the machine.
- Handles user payments and provides change.
- Shuts down if resources are insufficient.

## How It Works

1. **Menu Options**:
   - `espresso`: Costs $1.5 and requires 50ml water and 18g coffee.
   - `latte`: Costs $2.5 and requires 200ml water, 150ml milk, and 24g coffee.
   - `cappuccino`: Costs $3.0 and requires 250ml water, 100ml milk, and 24g coffee.

2. **Commands**:
   - Enter the type of coffee (`espresso`, `latte`, or `cappuccino`) to buy a coffee.
   - Enter `report` to see the current resource levels.
   - Enter `off` to turn off the machine.

3. **Payment**:
   - Users can insert quarters, dimes, nickels, and pennies.
   - If the inserted money is insufficient, the money is refunded and the machine turns off.

4. **Resource Management**:
   - The machine checks if there are enough resources to make the chosen coffee.
   - If not enough resources, the machine will shut down and indicate which resource is lacking.

## Setup and Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/coffeemachine.git
   cd coffeemachine
