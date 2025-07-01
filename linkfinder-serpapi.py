#!/usr/bin/env python3
import os, re, time, random
from serpapi import GoogleSearch

# ✅ Your API Key
API_KEY = "970a60226fd2ef2f5beadc3702b5d89c7c9f9465c1f8f751aece8c90148faba4"

# Terminal Colors
RED = "\033[91m"; GREEN = "\033[92m"; YELLOW = "\033[93m"
BLUE = "\033[94m"; CYAN = "\033[96m"; RESET = "\033[0m"

def show_banner():
    os.system("clear")
    print(f"""{RED}
██╗     ██╗███╗   ██╗██╗  ██╗    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗
██║     ██║████╗  ██║██║ ██╔╝    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║     ██║██╔██╗ ██║█████╔╝     ███████╗██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║     ██║██║╚██╗██║██╔═██╗     ╚════██║██║██║╚██╗██║██║  ██║██╔══╝  ╚═══╝
███████╗██║██║ ╚████║██║  ██╗    ███████║██║██║ ╚████║██████╔╝███████╗██║
╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝
{CYAN}     LINK FINDER (SerpApi Powered) by RIMZI{RESET}
""")

descs = [
    "🔥 Active Group", "💬 Chat & Discussion", "🔔 24/7 Members",
    "🌐 Open to All", "✅ Verified Group"
]

def search_groups(site, topic, regex, limit=10):
    query = f"site:{site} {topic}"
    params = {
        "q": query,
        "api_key": API_KEY,
        "engine": "google",
        "hl": "en",
        "num": "20"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    links = []
    for r in results.get("organic_results", []):
        link = r.get("link", "")
        if re.match(regex, link) and link not in links:
            links.append(link)
        if len(links) >= limit:
            break
    return links

def find_whatsapp(topic):
    print(f"\n{CYAN}Searching WhatsApp for:{RESET} {topic}\n")
    links = search_groups("chat.whatsapp.com", topic, r"https://chat\.whatsapp\.com/\S+")
    if links:
        for l in links:
            print(f"{YELLOW}╭──[ ✅ WHATSAPP ]──╮")
            print(f"{GREEN}Link: {l}")
            print(f"{YELLOW}Description: {random.choice(descs)}{RESET}\n")
    else:
        print(f"{RED}❌ No WhatsApp groups found!{RESET}")

def find_telegram(topic):
    print(f"\n{CYAN}Searching Telegram for:{RESET} {topic}\n")
    links = search_groups("t.me", topic, r"https://t\.me/\S+")
    if links:
        for l in links:
            name = l.split("/")[-1]
            print(f"{YELLOW}╭──[ ✅ TELEGRAM ]──╮")
            print(f"{GREEN}Group: {name.title()}")
            print(f"{YELLOW}Link: {l}{RESET}\n")
    else:
        print(f"{RED}❌ No Telegram groups found!{RESET}")

def main():
    while True:
        show_banner()
        print(f"{GREEN}[1]{RESET} WhatsApp Group Finder")
        print(f"{GREEN}[2]{RESET} Telegram Group Finder")
        print(f"{GREEN}[0]{RESET} Exit")
        choice = input(f"\n{BLUE}>> {RESET}").strip()
        if choice == "1":
            find_whatsapp(input("🔍 Topic: ").strip())
        elif choice == "2":
            find_telegram(input("🔍 Topic: ").strip())
        elif choice == "0":
            print(f"{YELLOW}Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid option!{RESET}")
        input(f"\n{CYAN}Press Enter to return to menu...{RESET}")

if __name__ == "__main__":
    main()
