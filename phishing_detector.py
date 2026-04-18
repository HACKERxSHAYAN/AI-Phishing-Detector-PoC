"""
HACKERxSHAYAN AI Phishing Guard v2.0
Hand-Trained ML Model - Student Style Implementation
"""

MANUAL_TEST_CASES = [
    (
        "URGENT: Your account is suspended! Click http://bit.ly/fake to verify now!!!",
        "phishing",
    ),
    ("Meeting scheduled for tomorrow at 3pm in Conference Room B", "legitimate"),
    ("You've won $1000! Claim your prize at https://winner-scam.ru/prize", "phishing"),
    (
        "Project update: The client approved the design, send me the final version",
        "legitimate",
    ),
]

print("[*] Running manual sanity check...")
test_msg, test_label = MANUAL_TEST_CASES[0]
print(f"[*] Test msg: '{test_msg[:40]}...' -> Expected: {test_label}")



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import re
from colorama import Fore, Style, init

init(autoreset=True)

print("[*] Loading dataset...")

import os

if os.path.exists("spam.csv"):
    df = pd.read_csv("spam.csv", encoding="latin-1")
    df = df.rename(columns={"v1": "category", "v2": "message"})
    df["label"] = df["category"].map({"spam": 1, "ham": 0})
else:
    print(
        "[!] 'spam.csv' not found - building training set from hand-labeled examples..."
    )
    phishing_examples = [
        "URGENT: Your account has been compromised! Click http://bit.ly/fake to verify now!!!",
        "You've won $1000! Claim prize at https://winner-scam.ru",
        "Action required: Your account will be suspended. Verify identity: http://phish.com",
        "Password expired. Reset immediately: https://login-security.net/update",
        "Unauthorized login detected. Secure account: http://tracking.link/auth",
        "Bank alert: Suspicious transaction. Click to dispute: https://bit.ly/bank-scam",
        "Your PayPal account limited. Confirm now: www.paypal-secure-login.com",
        "Package delivery failed. Track: https://dhl-tracking.scam",
        "Tax refund pending. Claim before deadline: http://irs-fake.gov/refund",
        "Lottery winner! Congratulations! Provide details: https://international-lottery.net",
        "Your Apple ID locked. Unlock: https://appleid-securitysupport.com",
        "Amazon order cancelled. Refund request: https://amazon-payments.info/claim",
        "Warranty expired. Extend now: https://car-warranty-call.com",
        "Free gift card! Complete survey: https://reward scam.site",
        ".crypto wallet activity. Verify: http://metamask-secure.io",
    ]
    legit_examples = [
        "Meeting scheduled for tomorrow at 3pm in Conference Room B",
        "Project update: The client approved the design, send me the final version",
        "Hey, are we still on for lunch tomorrow? Let me know your availability",
        "The quarterly report is due this Friday. Please submit your section by EOD",
        "Can you review the attached contract and send feedback by Monday?",
        "Reminder: Team meeting at 10am in the main boardroom",
        "I've uploaded the documents to the shared drive. Let me know if access issues",
        "Happy birthday! Hope you have a great day with your family",
        "The server maintenance is scheduled for this weekend. Plan accordingly",
        "Please find the meeting minutes attached. Action items highlighted in yellow",
        "Lunch next week? There's a new restaurant downtown I want to try",
        "The presentation went well. Client approved the proposal. Great work team!",
        "Can you cover my shift on Thursday? I have a doctor's appointment",
        "New policy document released. Read and acknowledge by end of day",
        "The code review feedback is ready. Check the GitLab comments",
    ]
    df = pd.DataFrame(
        {
            "message": phishing_examples + legit_examples,
            "label": [1] * len(phishing_examples) + [0] * len(legit_examples),
        }
    )

print(f"[*] Dataset loaded! {len(df)} total messages")
print(
    f"[*] Spam count: {df['label'].sum()} | Legit count: {len(df) - df['label'].sum()}"
)


print("[*] Vectorizing text data...")

my_vectorizer = TfidfVectorizer(
    max_features=5000,
    stop_words="english",
    ngram_range=(1, 2),  
)

x_data = my_vectorizer.fit_transform(df["message"].fillna(""))
y_data = df["label"].values

print(f"[*] Text converted to {x_data.shape[1]} features per message")



print("[*] Splitting dataset...")
x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.2, random_state=42
)

print("[*] Training model now (this usually takes a few seconds)...")

phish_clf = LogisticRegression(max_iter=1000, solver="liblinear")
phish_clf.fit(x_train, y_train)

print("[*] Model training complete!")

y_pred = phish_clf.predict(x_test)
acc = accuracy_score(y_test, y_pred)
print(f"[*] Model Loaded... Accuracy is looking good at {acc:.2%}")



print("[*] Saving model and vectorizer...")
joblib.dump(phish_clf, "phish_model.pkl")
joblib.dump(my_vectorizer, "vectorizer.pkl")
print("[*] Done! Model saved as 'phish_model.pkl'")




def check_message(user_text):
    """
    Takes a string, returns (is_phishing: bool, confidence: float)
    The model gives us probabilities - e.g. [0.12, 0.88] means 88% spam
    """
    text_vector = my_vectorizer.transform([user_text])

    probas = phish_clf.predict_proba(text_vector)[0]
    phishing_prob = probas[1] if len(probas) > 1 else probas[0]

    is_phishing = phishing_prob > 0.7
    return is_phishing, phishing_prob


def run_scanner():
    print(f"\n{Fore.CYAN}--- HACKERxSHAYAN AI Phishing Guard v2.0 ---")
    print(f"{Fore.YELLOW}[*] ML Model loaded. Ready to scan...")

    while True:
        print(f"\n{Fore.WHITE}[EMAIL] Paste your email/message (or type 'quit'):")
        user_input = input(f"{Fore.GREEN}> ").strip()

        if user_input.lower() in ("quit", "exit", "q"):
            print(f"[*] Shutting down scanner... Stay safe!")
            break

        if not user_input:
            print(f"[!] Empty input - try again")
            continue

        is_phish, confidence = check_message(user_input)

        print(f"\n{Fore.CYAN}[*] Analyzing message patterns...")

        if is_phish:
            risk_color = Fore.RED
            verdict = "PHISHING / SCAM DETECTED"
        else:
            risk_color = Fore.GREEN
            verdict = "LIKELY LEGITIMATE"

        confidence_pct = int(confidence * 100)
        print(f"{Fore.YELLOW}--------------------------------------------------")
        print(f"{Fore.WHITE}AI ANALYSIS RESULTS")
        print(f"{Fore.YELLOW}--------------------------------------------------")
        print(f"{risk_color}{Style.BRIGHT}VERDICT: {verdict}")
        print(f"{Fore.WHITE}Confidence: {confidence_pct}%")

        # Extra detail: show top 3 suspicious words if phishing
        if is_phish and confidence > 0.8:
            print(f"{Fore.RED}[!] Warning: This message looks like a Scam!")



print("\n[*] Testing model on manual test cases...")
for msg, expected in MANUAL_TEST_CASES:
    is_phish, conf = check_message(msg)
    status = (
        "[OK]"
        if (is_phish and expected == "phishing")
        or (not is_phish and expected == "legitimate")
        else "[FAIL]"
    )
    print(f"{Fore.CYAN}{status} '{msg[:50]}...' -> {conf:.1%} | Expected: {expected}")

print(f"\n{Fore.GREEN}[*] Scanner ready! Launching interface...\n")


if __name__ == "__main__":
    run_scanner()
