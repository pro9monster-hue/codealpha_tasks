import re

INPUT_FILE = "input_emails.txt"
OUTPUT_FILE = "extracted_emails.txt"

def extract_and_save_emails():
    print(f"Starting email extraction from '{INPUT_FILE}'...")
    
    try:
        with open(INPUT_FILE, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: Input file '{INPUT_FILE}' not found.")
        return
    except Exception as e:
        print(f"Error reading input file: {e}")
        return

    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    emails = re.findall(email_regex, content)
    
    if not emails:
        print("No email addresses found.")
        return
        
    unique_emails = sorted(list(set(emails)))
    
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
            for email in unique_emails:
                outfile.write(email + '\n')
        
        print(f"\nExtraction complete. Found {len(emails)} email(s) and saved {len(unique_emails)} unique email(s) to '{OUTPUT_FILE}'.")
    except Exception as e:
        print(f"Error writing to output file: {e}")

if __name__ == "__main__":
    extract_and_save_emails()
