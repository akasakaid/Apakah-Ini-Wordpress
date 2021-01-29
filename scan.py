# *-* encoding : utf-8 *-*
# coded : AkasakaID

try:
	import requests
	import os
	import sys
	from concurrent.futures import ThreadPoolExecutor
	from colorama import *
except ImportError:
	open("module.txt","w").write("requests\ncolorama")
	exit("module not installed\npip3 install -r module.txt")

r = requests.Session()
init(autoreset=True)
merah = Fore.LIGHTRED_EX
kuning = Fore.LIGHTYELLOW_EX
hijau = Fore.LIGHTGREEN_EX
biru = Fore.LIGHTBLUE_EX
magenta = Fore.LIGHTMAGENTA_EX
cyan = Fore.LIGHTCYAN_EX
hitam = Fore.LIGHTBLACK_EX
putih = Fore.LIGHTWHITE_EX
reset = Fore.RESET

if not os.path.exists("_wp.txt"):open("_wp.txt","a+").write("")
if not os.path.exists("_no_wp.txt"):open("_no_wp.txt","a+").write("")

class me:
	def __init__(self):
		self.wp = 0
		self.no_wp = 0
		self.loop = 0
		self.ts = 0

	def scan(self,site):
		self.loop += 1
		r1 = r.get(f"{site}/wp-login.php",timeout=10,headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.53"})
		if r1.status_code == 200:
			print(f"{magenta}[{hijau}WP{magenta}] {hijau}{site}                              ")
			if site not in open("_wp.txt").read():
				open("_wp.txt","a+").write(f"{site}\n")
			self. wp += 1
			print(f"{cyan}TOTAL : {hijau}[{putih}{self.loop}{hijau}/{cyan}{self.ts}{hijau}] {putih}[{hijau}wp{putih}] : {self.wp} {magenta}| {putih}[{merah}NO{putih}] : {self.no_wp}  ",flush=True,end='\r')
		else:
			print(f"{magenta}[{merah}NO{magenta}] {hijau}{site}                              ")
			if site not in open("_no_wp.txt").read():
				open("_no_wp.txt","a+").write(f"{site}\n")
			self.no_wp += 1
			print(f"{cyan}TOTAL : {hijau}[{putih}{self.loop}{hijau}/{cyan}{self.ts}{hijau}] {putih}[{hijau}wp{putih}] : {self.wp} {magenta}| {putih}[{merah}NO{putih}] : {self.no_wp}  ",flush=True,end='\r')

	def main(self):
		os.system("cls" if os.name == "nt" else "clear")
		print(f"""
{hijau} █████  ██ ██     ██ {kuning}██████  
{hijau}██   ██ ██ ██     ██ {kuning}     ██ 
{hijau}███████ ██ ██  █  ██ {kuning}  ▄███  
{hijau}██   ██ ██ ██ ███ ██ {kuning}  ▀▀    
{hijau}██   ██ ██  ███ ███  {kuning}  ██    
{merah}[{putih}APAKAH INI WORDPRESS ?{merah}]
{hijau}CODED : {putih}AKASAKAID
{hijau}TEAM  : {putih}BLACK CODER CRUSH                             
""")
		list_ = open(input(f"{putih}SITE LIST : ")).read().splitlines()
		self.ts = len(list_)
		th = int(input(f"{putih}THREAD : "))
		with ThreadPoolExecutor(max_workers=th) as thr:
			for url in list_:
				if "http" not in url and "https" not in url:
					url = f"http://{url}"
				thr.submit(self.scan,url)
		print(f"{cyan}TOTAL : {hijau}[{putih}{self.loop}{hijau}/{cyan}{self.ts}{hijau}] {putih}[{hijau}wp{putih}] : {self.wp} {magenta}| {putih}[{merah}NO{putih}] : {self.no_wp}  ")
try:
	app = me()
	app.main()
except KeyboardInterrupt:exit()