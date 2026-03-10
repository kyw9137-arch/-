from http.server import BaseHTTPRequestHandler, HTTPServer

RAW_HTML = '''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>FCT Dashboard</title>
<style>
:root{
  --bg:#0b0f19; --panel:#121a2a; --panel2:#0f1726;
  --text:#e8eefc; --muted:#9aa6c3; --border:rgba(255,255,255,0.12);
  --accent:#2dd4bf; --warn:#fbbf24; --bad:#fb7185;
  --orange:rgb(255,159,67);
}
*{box-sizing:border-box}
body{
  margin:0;background:var(--bg);color:var(--text);
  font-family:system-ui,-apple-system,"Segoe UI","Noto Sans KR",sans-serif;
}
header{padding:14px 18px;border-bottom:1px solid var(--border);}
.title{font-size:31px;font-weight:950;letter-spacing:1px}
main{padding:16px}
.card{
  background:linear-gradient(180deg,var(--panel),var(--panel2));
  border:1px solid var(--border);border-radius:16px;padding:14px;
}
.h1{color:var(--muted);font-weight:950;margin-bottom:10px}
.small{color:var(--muted);font-size:14px;line-height:1.7}
.btn{
  display:inline-block;margin-top:12px;padding:10px 14px;border-radius:12px;border:1px solid var(--border);
  background:rgba(255,255,255,.06);color:var(--text);font-weight:900;text-decoration:none
}
</style>
</head>
<body>
<header><div class="title">FCT</div></header>
<main>
  <section class="card">
    <div class="h1">대시보드 미리보기</div>
    <div class="small">요청하신 다운로드 기능을 추가했습니다. 아래 버튼으로 HTML 파일을 저장할 수 있습니다.</div>
    <a class="btn" href="/download">HTML 다운로드</a>
  </section>
</main>
</body>
</html>'''

HTML_CONTENT = RAW_HTML
DOWNLOAD_FILENAME = "FCT_Dashboard.html"


def save_dashboard_file() -> None:
    with open(DOWNLOAD_FILENAME, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_CONTENT.encode("utf-8"))
            return

        if self.path in ("/download", f"/{DOWNLOAD_FILENAME}"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Disposition", f'attachment; filename="{DOWNLOAD_FILENAME}"')
            self.end_headers()
            self.wfile.write(HTML_CONTENT.encode("utf-8"))
            return

        self.send_response(404)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write("Not Found".encode("utf-8"))


if __name__ == "__main__":
    save_dashboard_file()
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    print("Serving dashboard at http://localhost:8000")
    print(f"Download URL: http://localhost:8000/download ({DOWNLOAD_FILENAME})")
    server.serve_forever()
