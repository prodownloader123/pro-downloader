from flask import Flask, request, render_template_string
import yt_dlp
app = Flask(__name__)
HTML = """<html><head><meta name="viewport" content="width=device-width"><style>body{background:#111;color:#fff;font-family:sans-serif;text-align:center;padding:20px}.card{background:#222;padding:20px;border-radius:15px;max-width:450px;margin:auto}input{width:92%;padding:14px;border-radius:10px;border:none}button{width:95%;padding:14px;background:#ff004f;color:#fff;border:none;border-radius:10px;margin-top:10px;font-weight:bold}a.down{display:block;margin-top:20px;padding:14px;background:#00d26a;color:#fff;text-decoration:none;border-radius:10px}</style></head><body><h2>🔥 PRO Downloader</h2><div class="card"><form method="POST"><input name="url" placeholder="Link Paste Karo - TikTok/Insta/FB/YT" required><button>Get Video</button></form>{% if link %}<a class="down" href="{{ link }}" target="_blank">📥 DOWNLOAD NOW</a><p>{{ title }}</p>{% endif %}</div></body></html>"""
@app.route('/', methods=['GET','POST'])
def home():
    link=None; title=None
    if request.method=='POST':
        url=request.form.get('url')
        try:
            with yt_dlp.YoutubeDL({'quiet':True}) as ydl:
                info=ydl.extract_info(url, download=False)
                if 'entries' in info: info=info['entries'][0]
                for f in reversed(info.get('formats',[])):
                    if f.get('vcodec')!='none':
                        link=f['url']; break
                title=info.get('title','Ready')
        except: pass
    return render_template_string(HTML, link=link, title=title)
if __name__=='__main__': app.run(host='0.0.0.0', port=5000)
