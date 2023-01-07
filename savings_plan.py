import numpy as np

monthly_amount = float(input("How much to want to to save each month? "))
yearly_rate = float(input("What is the yearly interest rate? "))
save_time = int(input("How many months will you save? "))
plot_points = np.array([0,0])

def monthly_interest_rate(yearly_rate):
    monthly_rate = yearly_rate / 12 / 100
    return monthly_rate

def graph_plot(i, savings):
    new_plot = np.array([i, savings])
    new_plot_points = np.append((plot_points, new_plot), axis=0)
    print(new_plot_points)
    return new_plot_points

def current_balance(monthly_amount, save_time, monthly_rate):
    i = 1
    savings = 0
    while i <= save_time:
        savings += monthly_amount
        interest = monthly_rate * savings
        savings += interest
        #graph_plot(i, savings)
        print(f" month {i} savings: {savings:.2f}, interest: {interest:.2f}")
        i += 1
    return savings

monthly_rate = monthly_interest_rate(yearly_rate)
total_savings = current_balance(monthly_amount, save_time, monthly_rate)
print(f"Your total saving will be: ${total_savings:.2f}")

