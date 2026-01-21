# .\config\urls.py
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

NAVY_1 = "#0A2540"  # Stripe tonu
NAVY_2 = "#1A2B49"
NAVY_3 = "#0F172A"

PROVIDERS_TEXT = "Iyzico, PayTR, Param (ParamPOS), Paynet, iPara, PayU, Paratika"

def _extract_subdomain(host_no_port: str) -> str | None:
    """
    Girdi: "cemyilmaz.localhost" veya "odemesayfasi.com" gibi
    Çıktı: "cemyilmaz" (varsa) yoksa None
    """
    h = host_no_port.lower().strip(".")

    # local test
    if h == "localhost":
        return None
    if h.endswith(".localhost"):
        sub = h[: -len(".localhost")]
        return sub if sub else None

    # prod domain
    if h == "odemesayfasi.com":
        return None
    if h.endswith(".odemesayfasi.com"):
        sub = h[: -len(".odemesayfasi.com")]
        return sub if sub else None

    return None


def landing_or_organizer(request):
    host = request.get_host()  # "cemyilmaz.localhost:8000"
    host_no_port = host.split(":")[0]
    sub = _extract_subdomain(host_no_port)

    if sub:
        # ORGANIZER (subdomain) sayfası
        html = f"""<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>{sub} | odemesayfasi.com</title>
  <style>
    :root {{
      --navy1:{NAVY_1};
      --navy2:{NAVY_2};
      --navy3:{NAVY_3};
      --text:#111827;
      --muted:#6B7280;
      --border:#E5E7EB;
      --bg:#FFFFFF;
      --card:#F9FAFB;
    }}
    *{{box-sizing:border-box}}
    body{{margin:0;font-family:system-ui,Segoe UI,Arial;color:var(--text);background:var(--bg);line-height:1.5}}
    .wrap{{max-width:1080px;margin:0 auto;padding:20px}}
    .nav{{display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--border)}}
    .brand{{display:flex;align-items:center;gap:10px;font-weight:900;color:var(--navy1)}}
    .dot{{width:10px;height:10px;border-radius:999px;background:var(--navy1)}}
    .btn{{display:inline-flex;align-items:center;justify-content:center;padding:10px 14px;border-radius:12px;border:1px solid var(--border);font-weight:900;text-decoration:none;color:var(--navy1);background:#fff}}
    .btnp{{background:var(--navy1);border-color:var(--navy1);color:#fff}}
    h1{{margin:22px 0 8px;font-size:34px;line-height:1.15;letter-spacing:-0.02em}}
    .lead{{margin:0 0 14px;color:var(--muted);font-size:16px;max-width:820px}}
    .grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:12px}}
    .card{{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:14px}}
    .kpi{{display:flex;gap:16px;flex-wrap:wrap;margin-top:10px}}
    .pill{{border:1px solid var(--border);border-radius:999px;padding:8px 10px;background:#fff;color:var(--muted);font-weight:800;font-size:13px}}
    code{{background:#fff;border:1px solid var(--border);padding:2px 6px;border-radius:10px}}
    @media (max-width:900px){{
      .grid{{grid-template-columns:1fr}}
      h1{{font-size:28px}}
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="nav">
      <div class="brand"><span class="dot"></span><span>{sub}.odemesayfasi.com</span></div>
      <div style="display:flex;gap:10px;flex-wrap:wrap">
        <a class="btn" href="http://odemesayfasi.com">Ana site</a>
        <a class="btn" href="/admin/">Admin</a>
        <a class="btn btnp" href="javascript:void(0)">Yeni ödeme linki</a>
      </div>
    </div>

    <h1>{sub} için tahsilat sayfası</h1>
    <p class="lead">
      Bu sayfa subdomain’e göre otomatik oluşur. Amaç: sanatçı/organizatör kendi sosyalinde
      <strong>tek link</strong> paylaşsın: <code>{sub}.odemesayfasi.com</code>
    </p>

    <div class="kpi">
      <div class="pill">Mod: Backend-first (SSR)</div>
      <div class="pill">Hedef: Developer Payment Platform</div>
      <div class="pill">Ödeme aracı kurumları: {PROVIDERS_TEXT}</div>
    </div>

    <div class="grid">
      <div class="card">
        <strong>Ödeme Linki (Payment Link)</strong>
        <div style="color:var(--muted);margin-top:6px">
          Örn: <code>{sub}.odemesayfasi.com/pay/konser-2026</code> (yakında)
        </div>
        <div style="margin-top:10px;display:flex;gap:10px;flex-wrap:wrap">
          <a class="btn btnp" href="javascript:void(0)">Ödeme linki oluştur</a>
          <a class="btn" href="javascript:void(0)">Ödeme linklerini gör</a>
        </div>
      </div>

      <div class="card">
        <strong>Seatmap Linki</strong>
        <div style="color:var(--muted);margin-top:6px">
          Örn: <code>{sub}.odemesayfasi.com/seatmap/konser-2026</code> (planlı)
        </div>
        <div style="margin-top:10px;display:flex;gap:10px;flex-wrap:wrap">
          <a class="btn" href="javascript:void(0)">Seatmap konsepti</a>
          <a class="btn" href="javascript:void(0)">Giriş kontrol (QR)</a>
        </div>
      </div>
    </div>

    <div style="margin-top:16px;color:var(--muted);font-size:12px">
      Lokal test: <code>cemyilmaz.localhost:8000</code> gibi deneyebilirsin.
      Prod’da wildcard DNS + wildcard SSL gerekecek (ileride).
    </div>
  </div>
</body>
</html>"""
        return HttpResponse(html)

    # ANA DOMAIN (odemesayfasi.com) sayfası
    html = f"""<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>odemesayfasi.com</title>
  <style>
    :root {{
      --navy1:{NAVY_1};
      --navy2:{NAVY_2};
      --navy3:{NAVY_3};
      --text:#111827;
      --muted:#6B7280;
      --border:#E5E7EB;
      --bg:#FFFFFF;
      --card:#F9FAFB;
    }}
    *{{box-sizing:border-box}}
    body{{margin:0;font-family:system-ui,Segoe UI,Arial;color:var(--text);background:var(--bg);line-height:1.5}}
    .wrap{{max-width:1080px;margin:0 auto;padding:20px}}
    .nav{{display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--border)}}
    .brand{{display:flex;align-items:center;gap:10px;font-weight:900;color:var(--navy1)}}
    .dot{{width:10px;height:10px;border-radius:999px;background:var(--navy1)}}
    .btn{{display:inline-flex;align-items:center;justify-content:center;padding:10px 14px;border-radius:12px;border:1px solid var(--border);font-weight:900;text-decoration:none;color:var(--navy1)}}
    .btnp{{background:var(--navy1);border-color:var(--navy1);color:#fff}}
    .hero{{padding:44px 0 18px}}
    h1{{margin:0 0 12px;font-size:44px;line-height:1.1;letter-spacing:-0.02em}}
    .lead{{margin:0 0 18px;color:var(--muted);font-size:18px;max-width:720px}}
    .grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:18px}}
    .card{{background:var(--card);border:1px solid var(--border);border-radius:16px;padding:14px}}
    @media (max-width:900px) {{
      h1{{font-size:34px}}
      .grid{{grid-template-columns:1fr}}
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="nav">
      <div class="brand"><span class="dot"></span><span>odemesayfasi.com</span></div>
      <div style="display:flex;gap:10px;flex-wrap:wrap">
        <a class="btn" href="/admin/">Admin</a>
        <a class="btn btnp" href="javascript:void(0)">Ödeme sayfası oluştur</a>
      </div>
    </div>

    <div class="hero">
      <h1>Linkle ödeme alın.<br/>Developer Payment Platform (TR).</h1>
      <p class="lead">
        Bu domain bir ürün domain’i. Amaç: Payment Links + Form + Webhook + API.
        Organizatörler kendi subdomain’lerinden link paylaşır.
      </p>

      <div class="grid">
        <div class="card"><strong>Etkinlik bileti</strong><br><span style="color:var(--muted)">Ödeme linki + QR + (planlı) seatmap</span></div>
        <div class="card"><strong>Bağış / rezervasyon</strong><br><span style="color:var(--muted)">Form + ödeme, tek sayfada</span></div>
        <div class="card"><strong>Ödeme aracı kurumları</strong><br><span style="color:var(--muted)">{PROVIDERS_TEXT}</span></div>
      </div>
    </div>
  </div>
</body>
</html>"""
    return HttpResponse(html)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", landing_or_organizer),
]
