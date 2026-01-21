# /README.md

# odemesayfasi.com

Türkiye için **developer payment platform** (Stripe Payment Links + API yaklaşımı).

Bu repo, **backend-first** (Django + SSR) yaklaşımıyla, “link oluştur → paylaş → ödeme al” akışını kurmayı hedefler.

---

## Vizyon

- odemesayfasi.com bir **ürün domain’i** (Stripe gibi), marka domain’i değil.
- Amaç: geliştiricilerin ve organizatörlerin kolayca **payment link** üretip dağıtabilmesi.
- Kart verisi platformda tutulmaz; **redirect/hosted checkout** + **webhook doğrulama** ile ilerlenir.

---

## Kullanım Senaryoları

- Etkinlik bileti
- Bağış
- Rezervasyon
- Eğitim / workshop
- Form + ödeme
- Link ile ödeme
- Organizatör tahsilatı

---

## Tasarım Dili (Fintech)

Navy tonlar:
- `#0A2540` (ana)
- `#1A2B49`
- `#0F172A`

---

## Subdomain Stratejisi (Önemli)

Organizatör/sanatçı kendi linkini paylaşabilsin:

- `cemyilmaz.odemesayfasi.com`
- `sedayuz.odemesayfasi.com`
- `ajdapekkan.odemesayfasi.com`

Local test örneği:
- `cemyilmaz.localhost:8000
