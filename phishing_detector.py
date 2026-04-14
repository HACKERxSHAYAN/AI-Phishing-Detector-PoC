import re
from colorama import Fore, Style, init

# Initialize Colorama for Professional UI
init(autoreset=True)

class PhishBrain:
    def __init__(self):
        # AI Heuristic Weights
        self.trigger_words = {
            'urgent': 15, 'action required': 20, 'account suspended': 25,
            'verify': 10, 'login': 10, 'bank': 15, 'password': 20,
            'unauthorized': 20, 'gift card': 30, 'crypto': 25
        }

    def analyze(self, text):
        print(f"\n{Fore.CYAN}[*] AI ENGINE INITIALIZED: ANALYZING SEMANTIC PATTERNS...")
        score = 0
        findings = []
        text_lower = text.lower()

        # 1. Semantic Analysis (Keyword Weighting)
        for word, weight in self.trigger_words.items():
            if word in text_lower:
                score += weight
                findings.append(f"High-Risk Keyword: {word.upper()}")

        # 2. Structural Analysis (Link Detection)
        links = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        if links:
            score += 25
            findings.append(f"Suspicious URL Detected: {len(links)} link(s)")

        # 3. Urgency/Pressure Detection (Exclamation Overload)
        if text.count('!') > 3:
            score += 10
            findings.append("Urgency Signal: Excessive Exclamation Marks")

        self.generate_report(score, findings)

    def generate_report(self, score, findings):
        print(f"{Fore.YELLOW}--------------------------------------------------")
        print(f"{Fore.WHITE}AI ANALYSIS REPORT")
        print(f"{Fore.YELLOW}--------------------------------------------------")
        
        for item in findings:
            print(f"{Fore.WHITE}[+] {item}")

        print(f"\nTOTAL THREAT SCORE: {score}/100")
        
        if score >= 60:
            print(f"{Fore.RED}{Style.BRIGHT}VERDICT: CRITICAL - PHISHING DETECTED")
        elif score >= 30:
            print(f"{Fore.YELLOW}{Style.BRIGHT}VERDICT: WARNING - SUSPICIOUS CONTENT")
        else:
            print(f"{Fore.GREEN}{Style.BRIGHT}VERDICT: SECURE - NO KNOWN PATTERNS")

if __name__ == "__main__":
    scanner = PhishBrain()
    print(f"{Fore.MAGENTA}--- HACKERxSHAYAN AI Phishing Guard v1.0 ---")
    user_input = input("Paste the suspected email/message content: ")
    scanner.analyze(user_input)