# --- Step 1: Take input for each subject with validation ---

# Maths marks...
while True:
    math_marks = int(input("Enter your Maths marks (out of 100): "))
    if 0 <= math_marks <= 100:
        break
    print("Error: Marks must be between 0 and 100.")

# Physics marks
while True:
    phy_marks = int(input("Enter your Physics marks (out of 100): "))
    if 0 <= phy_marks <= 100:
        break
    print("Error: Marks must be between 0 and 100.")

# Chemistry marks
while True:
    chem_marks = int(input("Enter your Chemistry marks (out of 100): "))
    if 0 <= chem_marks <= 100:
        break
    print("Error: Marks must be between 0 and 100.")

# Hindi marks
while True:
    hindi_marks = int(input("Enter your Hindi marks (out of 100): "))
    if 0 <= hindi_marks <= 100:
        break
    print("Error: Marks must be between 0 and 100.")

# English marks
while True:
    english_marks = int(input("Enter your English marks (out of 100): "))
    if 0 <= english_marks <= 100:
        break
    print("Error: Marks must be between 0 and 100.")

# --- Step 2: Calculate total and percentage ---

total_score = math_marks + phy_marks + chem_marks + hindi_marks + english_marks
your_score = total_score / 500 * 100  # Percentage out of 500 total marks

# --- Step 3: Display results ---

print("\n--- Result Summary ---")
print(f"Maths: {math_marks}/100")
print(f"Physics: {phy_marks}/100")
print(f"Chemistry: {chem_marks}/100")
print(f"Hindi: {hindi_marks}/100")
print(f"English: {english_marks}/100")
print(f"Total Score: {total_score}/500")
print(f"Percentage: {your_score:.2f}%")

# --- Step 4: Print remark based on percentage ---

if your_score < 40:
    print("Keep working hard - there's room for improvement.")
elif your_score < 60:
    print("You are trying your best - keep it up!")
elif your_score < 90:
    print("Excellent work!")
else:
    print("Outstanding! You are a star!")
