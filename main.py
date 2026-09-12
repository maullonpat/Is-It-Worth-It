#IS IT WORTH IT?
print("""
═══════════════════════════════════════════════════
               ❓IS IT WORTH IT❓
═══════════════════════════════════════════════════""")
# GET INPUTS
while True:
  try:
    price = (float(input("🛒 Purchase Price: ₱")))
    if price > 0:
      break
    print("⚠️ Please enter a valid number greater than 0.")
  except ValueError:
    print("⚠️ Please enter a valid number greater than 0.")
  
while True:
  category = input("🏷️ Category (WANT or NEED): ").strip().upper()
  if category in ["WANT", "NEED"]:
    break
  print("⚠️ Please select between WANT or NEED.")

while True:
  try:
    monthly_salary = (float(input("💵 Monthly salary: ₱")))
    if monthly_salary > 0:
      break
    print("⚠️ Please enter a valid number greater than 0.")
  except ValueError:
    print("⚠️ Please enter a valid number greater than 0.")

while True:
  try:
    monthly_necessities = (float(input("🧾 Monthly necessities: ₱")))
    if monthly_necessities > 0:
      break
    print("⚠️ Your necessities must be lower than your monthly salary and greater than 0.")
  except ValueError:
    print("⚠️ Your necessities must be lower than your monthly salary and greater than 0.")

while True:
    try:
        working_days = int(input("📆 Working days per month: "))
        if 0 < working_days <= 31:
            break
        print("⚠️ Please enter a valid working day greater than 0 and less than 32 days.")
    except ValueError:
        print("⚠️ Please enter a whole number.")

def financial_calculator():
     daily_income = monthly_salary / working_days
     disposable_budget = monthly_salary - monthly_necessities
     salary_percentage = price / monthly_salary * 100
     days_needed = price / daily_income
     months_needed = price / disposable_budget
     monthly_value = price / 12

     # Store data to dict 
     financial_overview = {
        "monthly_salary": monthly_salary,
        "daily_income": daily_income,
        "price": price,
        "category": category,
        "monthly_necessities": monthly_necessities,
        "working_days": working_days,
        "disposable_budget": disposable_budget,
        "salary_percentage": salary_percentage,
        "days_needed": days_needed,
        "months_needed": months_needed,
        "monthly_value": monthly_value       
     }

     return financial_overview

def determine_risk(financial_overview):
     if financial_overview["salary_percentage"] <= 5:
          return "🟢 LOW 🟢"
     elif financial_overview["salary_percentage"] <= 15:
          return "🟡 MEDIUM 🟡"
     else:
          return "🔴 HIGH 🔴"

def generate_insight(risk):
     if risk == "LOW":
          return ("""
                    🟢 COMFORTABLE

       The purchase is relatively small compared
     with your monthly income and disposable budget.
""")
     elif risk == "MEDIUM":
          return ("""
          🟡 THINK CAREFULLY BEFORE BUYING

     This purchase is manageable, but it represents
     a noticeable portion of your available money.

          Consider saving for it before buying.
""")
     else:
          return ("""
          🔴 CONSIDER WAITING OR SAVING
     
     This purchase represents a large portion of
          your income or disposable budget.

     ⚠️ Buying this immediately could significantly
          reduce your financial flexibility.
""")

def display_results(financial_overview, risk, insight):
  total_month = financial_overview["price"]/ financial_overview["monthly_salary"]
  print(f"""
═══════════════════════════════════════════════════
            📊 FINANCIAL OVERVIEW 
═══════════════════════════════════════════════════
💵 Monthly salary: ₱{financial_overview["monthly_salary"]:.2f}
🧾 Monthly necessities: ₱{financial_overview["monthly_necessities"]:.2f}
💰 Disposable budget: ₱{financial_overview["disposable_budget"]:.2f}
📅 Daily income: ₱{financial_overview["daily_income"]:.2f}
═══════════════════════════════════════════════════
              📈 PURCHASE IMPACT 
═══════════════════════════════════════════════════
💸 Salary percentage: {financial_overview["salary_percentage"]:.2f}%
📆 Working days required: {round(financial_overview["price"]/financial_overview["daily_income"])} days
🗓️ Saving time: {int(total_month / 1)} months and {round(total_month % 1)*31} days 
📦 Cost per month (12 months): ₱{financial_overview["monthly_value"]:.2f}
═══════════════════════════════════════════════════
               🚦 FINANCIAL RISK
═══════════════════════════════════════════════════
                    {risk}
     This purchase represents {financial_overview["salary_percentage"]:.2f} of your 
     monthly salary.
     It would take approximately {round(financial_overview["days_needed"])} working
     days of income to earn this amount.
═══════════════════════════════════════════════════
               🎯 FINAL VERDICT 
═══════════════════════════════════════════════════
                    {insight}
═══════════════════════════════════════════════════
""")  
#     return
# def main():

#      if __name__ == "__main__":
#          main()

financial_overview = financial_calculator()
risk = determine_risk(financial_overview)
insight = generate_insight(risk)
display_results(financial_overview, risk, insight)