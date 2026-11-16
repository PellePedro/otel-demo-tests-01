import json  # noqa: F401


def test_h14_66vchsjnup_sek_0001(api):
    resp = api.get("/api/recommendations", params={"productIds": ["66VCHSJNUP"], "currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "66VCHSJNUP" not in [product["id"] for product in products]


def test_h14_1ymwwn1n4o_sgd_0002(api):
    resp = api.get("/api/recommendations", params={"productIds": ["1YMWWN1N4O"], "currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "1YMWWN1N4O" not in [product["id"] for product in products]


def test_h14_l9ecav7kim_thb_0003(api):
    resp = api.get("/api/recommendations", params={"productIds": ["L9ECAV7KIM"], "currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "L9ECAV7KIM" not in [product["id"] for product in products]


def test_h14_2zyfj3gm2n_try_0004(api):
    resp = api.get("/api/recommendations", params={"productIds": ["2ZYFJ3GM2N"], "currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "2ZYFJ3GM2N" not in [product["id"] for product in products]


def test_h14_0puk6v6ev0_usd_0005(api):
    resp = api.get("/api/recommendations", params={"productIds": ["0PUK6V6EV0"], "currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "0PUK6V6EV0" not in [product["id"] for product in products]


def test_h14_ls4psxunum_zar_0006(api):
    resp = api.get("/api/recommendations", params={"productIds": ["LS4PSXUNUM"], "currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "LS4PSXUNUM" not in [product["id"] for product in products]


def test_h14_9siqt8tojo_aud_0007(api):
    resp = api.get("/api/recommendations", params={"productIds": ["9SIQT8TOJO"], "currencyCode": "AUD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "9SIQT8TOJO" not in [product["id"] for product in products]


def test_h14_6e92zmyyfz_bgn_0008(api):
    resp = api.get("/api/recommendations", params={"productIds": ["6E92ZMYYFZ"], "currencyCode": "BGN"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "6E92ZMYYFZ" not in [product["id"] for product in products]


def test_h14_hqtgwgpnh4_brl_0009(api):
    resp = api.get("/api/recommendations", params={"productIds": ["HQTGWGPNH4"], "currencyCode": "BRL"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "HQTGWGPNH4" not in [product["id"] for product in products]


def test_h14_oljcespc7z_cad_0010(api):
    resp = api.get("/api/recommendations", params={"productIds": ["OLJCESPC7Z"], "currencyCode": "CAD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "OLJCESPC7Z" not in [product["id"] for product in products]


def test_h14_66vchsjnup_chf_0011(api):
    resp = api.get("/api/recommendations", params={"productIds": ["66VCHSJNUP"], "currencyCode": "CHF"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "66VCHSJNUP" not in [product["id"] for product in products]


def test_h14_1ymwwn1n4o_cny_0012(api):
    resp = api.get("/api/recommendations", params={"productIds": ["1YMWWN1N4O"], "currencyCode": "CNY"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "1YMWWN1N4O" not in [product["id"] for product in products]


def test_h14_l9ecav7kim_czk_0013(api):
    resp = api.get("/api/recommendations", params={"productIds": ["L9ECAV7KIM"], "currencyCode": "CZK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "L9ECAV7KIM" not in [product["id"] for product in products]


def test_h14_2zyfj3gm2n_dkk_0014(api):
    resp = api.get("/api/recommendations", params={"productIds": ["2ZYFJ3GM2N"], "currencyCode": "DKK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "2ZYFJ3GM2N" not in [product["id"] for product in products]


def test_h14_0puk6v6ev0_eur_0015(api):
    resp = api.get("/api/recommendations", params={"productIds": ["0PUK6V6EV0"], "currencyCode": "EUR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "0PUK6V6EV0" not in [product["id"] for product in products]


def test_h14_ls4psxunum_gbp_0016(api):
    resp = api.get("/api/recommendations", params={"productIds": ["LS4PSXUNUM"], "currencyCode": "GBP"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "LS4PSXUNUM" not in [product["id"] for product in products]


def test_h14_9siqt8tojo_hkd_0017(api):
    resp = api.get("/api/recommendations", params={"productIds": ["9SIQT8TOJO"], "currencyCode": "HKD"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "9SIQT8TOJO" not in [product["id"] for product in products]


def test_h14_6e92zmyyfz_hrk_0018(api):
    resp = api.get("/api/recommendations", params={"productIds": ["6E92ZMYYFZ"], "currencyCode": "HRK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "6E92ZMYYFZ" not in [product["id"] for product in products]


def test_h14_hqtgwgpnh4_huf_0019(api):
    resp = api.get("/api/recommendations", params={"productIds": ["HQTGWGPNH4"], "currencyCode": "HUF"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "HQTGWGPNH4" not in [product["id"] for product in products]


def test_h14_oljcespc7z_idr_0020(api):
    resp = api.get("/api/recommendations", params={"productIds": ["OLJCESPC7Z"], "currencyCode": "IDR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "OLJCESPC7Z" not in [product["id"] for product in products]


def test_h14_66vchsjnup_ils_0021(api):
    resp = api.get("/api/recommendations", params={"productIds": ["66VCHSJNUP"], "currencyCode": "ILS"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "66VCHSJNUP" not in [product["id"] for product in products]


def test_h14_1ymwwn1n4o_inr_0022(api):
    resp = api.get("/api/recommendations", params={"productIds": ["1YMWWN1N4O"], "currencyCode": "INR"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "1YMWWN1N4O" not in [product["id"] for product in products]


def test_h14_l9ecav7kim_isk_0023(api):
    resp = api.get("/api/recommendations", params={"productIds": ["L9ECAV7KIM"], "currencyCode": "ISK"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "L9ECAV7KIM" not in [product["id"] for product in products]


def test_h14_2zyfj3gm2n_jpy_0024(api):
    resp = api.get("/api/recommendations", params={"productIds": ["2ZYFJ3GM2N"], "currencyCode": "JPY"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "2ZYFJ3GM2N" not in [product["id"] for product in products]


def test_h14_0puk6v6ev0_krw_0025(api):
    resp = api.get("/api/recommendations", params={"productIds": ["0PUK6V6EV0"], "currencyCode": "KRW"})
    assert resp.status_code == 200
    products = resp.json()
    assert 1 <= len(products) <= 4
    assert "0PUK6V6EV0" not in [product["id"] for product in products]
