# Bertram Labs Challenge

## Problem

### The Story
Bob, Jeremy, and the other 5 coworkers in the Bertram Labs office love coffee. In fact, everyday, right after lunch, they walk down the street to their favorite coffee shop to grab a cup to go. Bob always gets a cappuccino, Jeremy likes his coffee black, and the others have their favorite coffee beverage too. To ease the checkout process, only one coworker pays for all the coffees each day. As you can imagine, they have a problem everyday: whose turn is it to pay for coffee?

### The Challenge
Write a software program to help the coworkers decide who should pay for coffee. Consider that not all drinks cost the same, so to be fair please take this into account when crafting your solution.

### The Requirements
- Choose any programming language you like!
- Create any interface you like (i.e. GUI, CLI)
- Solution must be published to Github

### Deliverables
- Instructions on how to build and run your solution, preferably in a README.
- Document any assumptions you made in creating your program.
- If needed, document how to enter the data required for your program to run. For
example, the coffee consumers, the price for their coffee, etc.
- The finished software solution must be provided to us to run locally or hosted online.

## Solution

### Explanation
This program randomly selects one of the coworkers to pay for coffee each day. To ensure fairness, a weight is assigned to each coworker based on the price of their preferred coffee beverage. As this solution is based on probability, the law of large numbers will ensure it so that in the long run, the actual ratio of outcomes will converge to the expected ratio, thus ensuring fairness.

In the context of this problem, it means that while it's possible for someone to pay multiple times in a row due to the randomness of the selection process, over a large number of days, each coworker's probability of paying will approach the fair distribution determined by the prices of their favorite drinks.

### Instructions
- To build and run the solution, clone the repo using your local terminal
```git
git clone https://github.com/ariyin/bertram-labs
```
- Open the locally cloned repository in a code editor of your choice (Ex: VSCode)
- The coffee consumers, their preferred choice of coffee, and the price for their coffee can be inserted in the coworkers list in `main.py`
- Run `main.py` by clicking the run code button

### Assumptions
- Each person **always** gets their favorite drink (as implied by "Bob always gets a cappuccino")
- The group of coworkers **always** go together to the coffee shop
    - Bonus: The group of coworkers will not have a falling out or add additional members in the near future
- The prices of the drinks remain **constant**