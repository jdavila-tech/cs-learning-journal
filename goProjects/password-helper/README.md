# 🔐 Go Project: Password Strength Checker & Generator

## 🧠 What It Does

This is a command-line Go application that helps users evaluate the strength of their passwords and optionally generates a strong one. The user can:

- Enter a password they think is strong
- Get feedback on whether it's Weak, Moderate, or Strong
- Choose to try again or generate a strong password suggestion

---

## 🧱 Core Features

| Feature | Concepts Used |
|--------|---------------|
| Input from user | `fmt.Scanln`, string input |
| Strength checking | string length, character types |
| Conditional logic | `if`, `else if`, `else` |
| Loops | `for`, `switch`, or recursion |
| Arrays, maps | optional for character categories |
| Random password generator | `math/rand`, slices |
| Clean output | `fmt.Printf`, strings |

---

## 🔐 Password Strength Rules

**Basic criteria for evaluation:**

- **Weak**:  
  - Less than 8 characters  
  - Only letters  
  - All lowercase  

- **Moderate**:  
  - At least 8 characters  
  - Contains letters and numbers  

- **Strong**:  
  - At least 12 characters  
  - Contains uppercase, lowercase, numbers, and special characters  

---

## 🗂️ Project Structure

