import requests,re,random,os

def main():
    os.system('clear')
    cookies = input(' [?] masukan cookie : ')
    limit   = int(input(' [?] Limit comen : '))

    print('\n [*] Gunakan tanda koma untuk pemisahan text komen contoh : hell bang,gw mau recode bang')
    text_komen = input(' [?] Text komen : ')
    userid     = input(' [?] Id postingan : ')
    with requests.Session() as x:
         x.headers.update({
            "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com",
            "origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0",
            "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8",
         })
         try:
               link = x.get("https://business.facebook.com/business_locations", cookies = {'cookie':cookies})
               search = re.search("(EAAG\w+)", link.text).group(1)
               if 'EAAG' in search:
                   komen(cookies,search,limit,text_komen,userid)
         except AttributeError:exit('\n [×] gagal komen, cookie invalid')

def komen(coki,token,limit,text_komen,userid):
    a = 0
    for _ in range(limit):
        a +=1
        for z in text_komen.split(','):
            b = requests.post(f'https://graph.facebook.com/{userid}/comments/?message={z}&access_token={token}', cookies={'cookie':coki})
            if 'Kami membatasi seberapa sering Anda dapat memposting, berkomentar, atau melakukan hal-hal lain dalam jumlah waktu tertentu guna membantu melindungi komunitas dari spam. Anda bisa mencoba lagi nanti. Pelajari Selengkapnya' in b.text:
                exit('\n [×] akun di batasi kontol')
            if 'id' in b.text:
                print(f'\r [*] komen ke : {a}',end=' ')
            else:
                continue

if __name__ == '__main__':
	main()
