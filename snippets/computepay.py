def computepay(hours, rate):
  extra_pay = 0
  extra_time_rate = rate * 1.5

  if (hours > 40):
    extra_time = hours - 40
    extra_pay = extra_time * extra_time_rate
    
  return "Pay: $" + str((rate * 40) + extra_pay)

# rate is $10 per hour
print(computepay(45, 10))