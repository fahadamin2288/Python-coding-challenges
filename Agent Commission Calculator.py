"""
This code calculates the total sales from the Sales list, then computes the agent's commission based on the total
sales, with different commission rates for different sales thresholds, and finally prints the total sales and the
corresponding commission.
"""


Sales = [15, 225, 5, 41, 85]
Total_sales = 0

for i in Sales:
    Total_sales += i
Total_sales = sum(Sales)
agent_commision = 0
if Total_sales < 100:
    agent_commision += 0
    agent_commisions = agent_commision * Total_sales
elif 100 <= Total_sales < 500:
    agent_commision += 0.05
    agent_commisions = agent_commision * Total_sales
elif 100 <= Total_sales < 1000:
    agent_commision += 0.10
    agent_commisions = agent_commision * Total_sales
else:
    agent_commision += 0.15
    agent_commisions = agent_commision * Total_sales
    print("You got the bonus")
print(f"The total sales is {Total_sales} and the agent commision is {agent_commisions}.")