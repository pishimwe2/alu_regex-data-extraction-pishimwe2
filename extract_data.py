import re

def find_emails(text):
    # Looks for email patterns like john.doe@mail.com or info@company.org
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

def find_urls(text):
    # Detects URLs starting with http or https
    pattern = r'https?://[^\s]+'
    return re.findall(pattern, text)

def find_phone_numbers(text):
    # Recognizes common phone formats (123) 456-7890, 123-456-7890, or 123.456.7890
    pattern = r'(\(\d{3}\)\s*|\d{3}[-.])\d{3}[-.]\d{4}'
    return re.findall(pattern, text)

def find_credit_cards(text):
    # Matches formats like 1234 5678 9012 3456 or 1234-5678-9012-3456
    pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
    return re.findall(pattern, text)

def run_extraction():
    with open("sample_text.txt", "r") as file:
        content = file.read()

        print("== Emails Found ==")
        print(find_emails(content))

        print("\n== URLs Found ==")
        print(find_urls(content))

        print("\n== Phone Numbers Found ==")
        print(find_phone_numbers(content))

        print("\n== Credit Card Numbers Found ==")
        print(find_credit_cards(content))

if __name__ == "__main__":
    run_extraction()
