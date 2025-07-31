import requests
import time

url_base = "https://p2a-gateway.up.railway.app"

def claim(headers):
    url = f"{url_base}/api/v1/compute-units/user/interval-rewards/claim"
    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("success", False):
            print("Claim successful:", data.get("message", "No message provided"))
        else:
            print("Claim failed:", data.get("error", "Unknown error"))
    else:
        print("Failed to claim:", response.status_code, response.text)

question_list = [
    {"questionId": "cmdkib6bp02j8pg6s3ps9iwtx", "thumbsUp": True},
    {"questionId": "cmdki8hm902hxpg6s04fdnype", "thumbsUp": False},
    {"questionId": "cmdki49n002g6pg6sjp66dsxw", "thumbsUp": True},
    {"questionId": "cmdki153t02f4pg6szmqsfvch", "thumbsUp": True},
    {"questionId": "cmdhrdxju020ilt6plcdbdey1", "thumbsUp": True},
    {"questionId": "cmdhrbjwt020glt6pn3w5etrw", "thumbsUp": True},
    {"questionId": "cmdeiiybt005qpk6r4sdsqezz", "thumbsUp": True},
    {"questionId": "cmdeimo1z005tpk6rers436k0", "thumbsUp": True},
    {"questionId": "cmdkhxvy402eupg6srm3huby1", "thumbsUp": True},
    {"questionId": "cmdki66w502h2pg6suryytw42", "thumbsUp": True},
    
]

def task(headers, questionId, thumbsUp):
    url = f"{url_base}/api/v1/quest/user/thumbs-questions/answer"
    payload = {
        "questionId": questionId,
        "thumbsUp": thumbsUp
    }
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    if response.status_code == 200 and response.json().get("success", False):
        print(f"Task for question {questionId} completed successfully.")
    else:
        error_message = data.get("error", "Unknown error")
        print(f"{error_message}")


def jalankan_untuk_satu_token(token):
    headers = {
        "Authorization": token.strip(),
        "Content-Type": "application/json"
    }  
    # Claim rewards
    claim(headers)
    
    # Process each question
    for question in question_list:
        task(headers, question["questionId"], question["thumbsUp"])

def main():
    with open("tokens.txt", "r") as f:
        tokens = f.readlines()

    for token in tokens:
        try:
            jalankan_untuk_satu_token(token)
            time.sleep(3)  # jeda antar akun, opsional
        except Exception as e:
            print(f"⚠️  Gagal untuk token ini: {e}")


if __name__ == "__main__":
    try:
        while True:
            main()
            print("✅ Selesai untuk semua token, menunggu 24 jam sebelum mencoba lagi...")
            time.sleep(60 * 24)  # tunggu 24 jam sebelum mencoba lagi
    except KeyboardInterrupt:
        print("Program dihentikan oleh pengguna.")
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")
