TOKEN = "1115116047:AAHYkwtlGkKMx37BXOk7K19PUooQMBLiEiI"
import sqlite3
import random 
def nm(uid,un,tx,path):
	db = sqlite3.connect(path)
	sql = db.cursor()
	sql.execute("SELECT id FROM un where user_id ="+str(uid))
	a=str(sql.fetchone())
	print (a+" "+str(uid))
	if a == 'None':
		sql.execute("SELECT max(id) FROM un ")
		a=str(sql.fetchone())
		a=a.replace(")", "")
		a=a.replace(",", "")
		a=a.replace("(", "")
		id=a
		if a == id:
			id=int(id)+1
			sql.execute("INSERT INTO un VALUES(?,?,?)",(id,uid,un))
			db.commit()
		else:
			print("test")

def add(path,uid,text):
	db = sqlite3.connect(path)
	sql = db.cursor()
	sql.execute("SELECT max(id) FROM us ")
	a=str(sql.fetchone())
	a=a.replace(")", "")
	a=a.replace(",", "")
	a=a.replace("(", "")
	id=a
	if a == id:
		id=int(id)+1
		sql.execute("INSERT INTO us VALUES(?,?,?)",(id,uid,text))
		db.commit()
		print('Done!')
def max_id(path):
	db = sqlite3.connect(path)
	sql = db.cursor()
	sql.execute("""SELECT max(id) FROM un """)
	a=str(sql.fetchone())
	a=a.replace(")", "")
	a=a.replace(",", "")
	a=a.replace("(", "")
	return a
def und(path,ud):
	db = sqlite3.connect(path)
	sql = db.cursor()
	sql.execute("SELECT user_id FROM un WHERE id = "+str(ud))
	a=str(sql.fetchone())
	a=a.replace(")", "")
	a=a.replace(",", "")
	a=a.replace("(", "")
	a=a.replace("'", "")
	return a

def connect(path):
	db = sqlite3.connect(path)
	sql = db.cursor()

	sql.execute("""CREATE TABLE IF NOT EXISTS "us" (
		"id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
		"user_id"	TEXT,
		"text"	TEXT
		);	""")
	db.commit()
	sql.execute("""CREATE TABLE IF NOT EXISTS "un" (
		"id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
		"user_id"	TEXT,
		"name"	TEXT
		);	""")
	db.commit()
	print('Connected!')
def conv(text):
	sa =      ' qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
	sb=[' 𝚚𝚠𝚎𝚛𝚝𝚢𝚞𝚒𝚘𝚙𝚊𝚜𝚍𝚏𝚐𝚑𝚓𝚔𝚕𝚣𝚡𝚌𝚟𝚋𝚗𝚖𝚀𝚆𝙴𝚁𝚃𝚈𝚄𝙸𝙾𝙿𝙰𝚂𝙳𝙵𝙶𝙷𝙹𝙺𝙻𝚉𝚇𝙲𝚅𝙱𝙽𝙼',
	' 𝕢𝕨𝕖𝕣𝕥𝕪𝕦𝕚𝕠𝕡𝕒𝕤𝕕𝕗𝕘𝕙𝕛𝕜𝕝𝕫𝕩𝕔𝕧𝕓𝕟𝕞ℚ𝕎𝔼ℝ𝕋𝕐𝕌𝕀𝕆ℙ𝔸𝕊𝔻𝔽𝔾ℍ𝕁𝕂𝕃ℤ𝕏ℂ𝕍𝔹ℕ𝕄',
	' ǫᴡᴇʀᴛʏᴜɪᴏᴘᴀsᴅғɢʜᴊᴋʟᴢxᴄᴠʙɴᴍQWERTYUIOPASDFGHJKLZXCVBNM',
	' 𝓆𝓌ℯ𝓇𝓉𝓎𝓊𝒾ℴ𝓅𝒶𝓈𝒹𝒻ℊ𝒽𝒿𝓀𝓁𝓏𝓍𝒸𝓋𝒷𝓃𝓂𝒬𝒲ℰℛ𝒯𝒴𝒰ℐ𝒪𝒫𝒜𝒮𝒟ℱ𝒢ℋ𝒥𝒦ℒ𝒵𝒳𝒞𝒱ℬ𝒩ℳ',
	' 𝔮𝔴𝔢𝔯𝔱𝔶𝔲𝔦𝔬𝔭𝔞𝔰𝔡𝔣𝔤𝔥𝔧𝔨𝔩𝔷𝔵𝔠𝔳𝔟𝔫𝔪𝔔𝔚𝔈ℜ𝔗𝔜𝔘ℑ𝔒𝔓𝔄𝔖𝔇𝔉𝔊ℌ𝔍𝔎𝔏ℨ𝔛ℭ𝔙𝔅𝔑𝔐',
	' bʍǝɹʇʎnᴉodɐspɟƃɥɾʞlzxɔʌquɯbʍǝɹʇʎnᴉodɐspɟƃɥɾʞlzxɔʌquɯ',
	' Ҩ山乇尺ㄒㄚㄩ|ㄖ卩卂丂ᗪ千ᘜ卄ﾌҜㄥ乙乂匚ᐯ乃几爪Ҩ山乇尺ㄒㄚㄩ|ㄖ卩卂丂ᗪ千ᘜ卄ﾌҜㄥ乙乂匚ᐯ乃几爪',
	' 𝘲᭙ꫀ𝘳𝓽ꪗꪊ𝓲ꪮρꪖ𝘴ᦔᠻᧁꫝ𝓳𝘬ꪶɀ᥊ᥴꪜ᥇ꪀꪑ𝘲᭙ꫀ𝘳𝓽ꪗꪊ𝓲ꪮρꪖ𝘴ᦔᠻᧁꫝ𝓳𝘬ꪶɀ᥊ᥴꪜ᥇ꪀꪑ']
	fm = list(sb[random.choice([1, 2,3,4,5,6,7,0])])
	nt=''
	
	st=list(sa)
	for a in range(len(text)):
		for b in range(53):
			if text[a]==st[b]:
				nt=nt+fm[b]
	if nt =="":
		nt="Siznig so'roving  qabul qilinmadi!\nIltinos faqat lotin hariflarini ishlating)"
	return nt+random.choice(list("︎❣︎☾︎☽︎♫︎𓂸シ︎㋛︎♡︎❥︎ఌ︎ꨄ︎❦︎:☹︎☻︎☠︎︎☏︎𓆉︎𓁹𓂀★✰✯☆✩✵༆༄߷𖦹☢︎︎☼︎᯽✫۞𖣔⍟𖣘❀:❁᯾✪⁂𑁍᪥𖧷𓅓𓆙␈𐂃𐂂𓀬𓆈♔♕☯︎♲︎︎︎𒊹︎︎︎♪➪⌨︎♧︎︎︎☘︎☜︎︎︎☞︎︎︎☟︎︎︎✍︎𓇽☮︎☃︎꧁꧂☂︎𖠌ꕥ𖨆"))