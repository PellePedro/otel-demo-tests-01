import json  # noqa: F401


def test_h01_cur_dkk_0001(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "DKK" in codes


def test_h01_cur_eur_0002(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "EUR" in codes


def test_h01_cur_gbp_0003(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "GBP" in codes


def test_h01_cur_hkd_0004(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HKD" in codes


def test_h01_cur_hrk_0005(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HRK" in codes


def test_h01_cur_huf_0006(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HUF" in codes


def test_h01_cur_idr_0007(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "IDR" in codes


def test_h01_cur_ils_0008(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ILS" in codes


def test_h01_cur_inr_0009(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "INR" in codes


def test_h01_cur_isk_0010(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ISK" in codes


def test_h01_cur_jpy_0011(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "JPY" in codes


def test_h01_cur_krw_0012(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "KRW" in codes


def test_h01_cur_mxn_0013(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MXN" in codes


def test_h01_cur_myr_0014(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MYR" in codes


def test_h01_cur_nok_0015(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NOK" in codes


def test_h01_cur_nzd_0016(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NZD" in codes


def test_h01_cur_php_0017(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PHP" in codes


def test_h01_cur_pln_0018(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PLN" in codes


def test_h01_cur_ron_0019(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RON" in codes


def test_h01_cur_rub_0020(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RUB" in codes


def test_h01_cur_sek_0021(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SEK" in codes


def test_h01_cur_sgd_0022(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SGD" in codes


def test_h01_cur_thb_0023(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "THB" in codes


def test_h01_cur_try_0024(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "TRY" in codes


def test_h01_cur_usd_0025(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "USD" in codes


def test_h01_cur_zar_0026(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ZAR" in codes


def test_h01_cur_aud_0027(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "AUD" in codes


def test_h01_cur_bgn_0028(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BGN" in codes


def test_h01_cur_brl_0029(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BRL" in codes


def test_h01_cur_cad_0030(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CAD" in codes


def test_h01_cur_chf_0031(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CHF" in codes


def test_h01_cur_cny_0032(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CNY" in codes


def test_h01_cur_czk_0033(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CZK" in codes


def test_h01_cur_dkk_0034(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "DKK" in codes


def test_h01_cur_eur_0035(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "EUR" in codes


def test_h01_cur_gbp_0036(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "GBP" in codes


def test_h01_cur_hkd_0037(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HKD" in codes


def test_h01_cur_hrk_0038(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HRK" in codes


def test_h01_cur_huf_0039(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HUF" in codes


def test_h01_cur_idr_0040(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "IDR" in codes


def test_h01_cur_ils_0041(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ILS" in codes


def test_h01_cur_inr_0042(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "INR" in codes


def test_h01_cur_isk_0043(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ISK" in codes


def test_h01_cur_jpy_0044(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "JPY" in codes


def test_h01_cur_krw_0045(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "KRW" in codes


def test_h01_cur_mxn_0046(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MXN" in codes


def test_h01_cur_myr_0047(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MYR" in codes


def test_h01_cur_nok_0048(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NOK" in codes


def test_h01_cur_nzd_0049(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NZD" in codes


def test_h01_cur_php_0050(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PHP" in codes


def test_h01_cur_pln_0051(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PLN" in codes


def test_h01_cur_ron_0052(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RON" in codes


def test_h01_cur_rub_0053(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RUB" in codes


def test_h01_cur_sek_0054(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SEK" in codes


def test_h01_cur_sgd_0055(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SGD" in codes


def test_h01_cur_thb_0056(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "THB" in codes


def test_h01_cur_try_0057(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "TRY" in codes


def test_h01_cur_usd_0058(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "USD" in codes


def test_h01_cur_zar_0059(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ZAR" in codes


def test_h01_cur_aud_0060(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "AUD" in codes


def test_h01_cur_bgn_0061(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BGN" in codes


def test_h01_cur_brl_0062(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BRL" in codes


def test_h01_cur_cad_0063(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CAD" in codes


def test_h01_cur_chf_0064(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CHF" in codes


def test_h01_cur_cny_0065(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CNY" in codes


def test_h01_cur_czk_0066(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CZK" in codes


def test_h01_cur_dkk_0067(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "DKK" in codes


def test_h01_cur_eur_0068(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "EUR" in codes


def test_h01_cur_gbp_0069(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "GBP" in codes


def test_h01_cur_hkd_0070(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HKD" in codes


def test_h01_cur_hrk_0071(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HRK" in codes


def test_h01_cur_huf_0072(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HUF" in codes


def test_h01_cur_idr_0073(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "IDR" in codes


def test_h01_cur_ils_0074(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ILS" in codes


def test_h01_cur_inr_0075(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "INR" in codes


def test_h01_cur_isk_0076(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ISK" in codes


def test_h01_cur_jpy_0077(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "JPY" in codes


def test_h01_cur_krw_0078(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "KRW" in codes


def test_h01_cur_mxn_0079(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MXN" in codes


def test_h01_cur_myr_0080(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MYR" in codes


def test_h01_cur_nok_0081(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NOK" in codes


def test_h01_cur_nzd_0082(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NZD" in codes


def test_h01_cur_php_0083(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PHP" in codes


def test_h01_cur_pln_0084(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PLN" in codes


def test_h01_cur_ron_0085(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RON" in codes


def test_h01_cur_rub_0086(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RUB" in codes


def test_h01_cur_sek_0087(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SEK" in codes


def test_h01_cur_sgd_0088(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SGD" in codes


def test_h01_cur_thb_0089(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "THB" in codes


def test_h01_cur_try_0090(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "TRY" in codes


def test_h01_cur_usd_0091(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "USD" in codes


def test_h01_cur_zar_0092(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ZAR" in codes


def test_h01_cur_aud_0093(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "AUD" in codes


def test_h01_cur_bgn_0094(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BGN" in codes


def test_h01_cur_brl_0095(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BRL" in codes


def test_h01_cur_cad_0096(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CAD" in codes


def test_h01_cur_chf_0097(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CHF" in codes


def test_h01_cur_cny_0098(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CNY" in codes


def test_h01_cur_czk_0099(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CZK" in codes


def test_h01_cur_dkk_0100(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "DKK" in codes


def test_h01_cur_eur_0101(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "EUR" in codes


def test_h01_cur_gbp_0102(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "GBP" in codes


def test_h01_cur_hkd_0103(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HKD" in codes


def test_h01_cur_hrk_0104(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HRK" in codes


def test_h01_cur_huf_0105(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HUF" in codes


def test_h01_cur_idr_0106(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "IDR" in codes


def test_h01_cur_ils_0107(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ILS" in codes


def test_h01_cur_inr_0108(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "INR" in codes


def test_h01_cur_isk_0109(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ISK" in codes


def test_h01_cur_jpy_0110(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "JPY" in codes


def test_h01_cur_krw_0111(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "KRW" in codes


def test_h01_cur_mxn_0112(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MXN" in codes


def test_h01_cur_myr_0113(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MYR" in codes


def test_h01_cur_nok_0114(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NOK" in codes


def test_h01_cur_nzd_0115(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NZD" in codes


def test_h01_cur_php_0116(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PHP" in codes


def test_h01_cur_pln_0117(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PLN" in codes


def test_h01_cur_ron_0118(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RON" in codes


def test_h01_cur_rub_0119(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RUB" in codes


def test_h01_cur_sek_0120(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SEK" in codes


def test_h01_cur_sgd_0121(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SGD" in codes


def test_h01_cur_thb_0122(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "THB" in codes


def test_h01_cur_try_0123(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "TRY" in codes


def test_h01_cur_usd_0124(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "USD" in codes


def test_h01_cur_zar_0125(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ZAR" in codes


def test_h01_cur_aud_0126(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "AUD" in codes


def test_h01_cur_bgn_0127(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BGN" in codes


def test_h01_cur_brl_0128(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BRL" in codes


def test_h01_cur_cad_0129(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CAD" in codes


def test_h01_cur_chf_0130(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CHF" in codes


def test_h01_cur_cny_0131(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CNY" in codes


def test_h01_cur_czk_0132(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CZK" in codes


def test_h01_cur_dkk_0133(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "DKK" in codes


def test_h01_cur_eur_0134(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "EUR" in codes


def test_h01_cur_gbp_0135(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "GBP" in codes


def test_h01_cur_hkd_0136(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HKD" in codes


def test_h01_cur_hrk_0137(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HRK" in codes


def test_h01_cur_huf_0138(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HUF" in codes


def test_h01_cur_idr_0139(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "IDR" in codes


def test_h01_cur_ils_0140(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ILS" in codes


def test_h01_cur_inr_0141(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "INR" in codes


def test_h01_cur_isk_0142(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ISK" in codes


def test_h01_cur_jpy_0143(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "JPY" in codes


def test_h01_cur_krw_0144(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "KRW" in codes


def test_h01_cur_mxn_0145(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MXN" in codes


def test_h01_cur_myr_0146(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MYR" in codes


def test_h01_cur_nok_0147(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NOK" in codes


def test_h01_cur_nzd_0148(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NZD" in codes


def test_h01_cur_php_0149(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PHP" in codes


def test_h01_cur_pln_0150(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PLN" in codes


def test_h01_cur_ron_0151(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RON" in codes


def test_h01_cur_rub_0152(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RUB" in codes


def test_h01_cur_sek_0153(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SEK" in codes


def test_h01_cur_sgd_0154(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SGD" in codes


def test_h01_cur_thb_0155(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "THB" in codes


def test_h01_cur_try_0156(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "TRY" in codes


def test_h01_cur_usd_0157(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "USD" in codes


def test_h01_cur_zar_0158(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ZAR" in codes


def test_h01_cur_aud_0159(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "AUD" in codes


def test_h01_cur_bgn_0160(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BGN" in codes


def test_h01_cur_brl_0161(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BRL" in codes


def test_h01_cur_cad_0162(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CAD" in codes


def test_h01_cur_chf_0163(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CHF" in codes


def test_h01_cur_cny_0164(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CNY" in codes


def test_h01_cur_czk_0165(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CZK" in codes


def test_h01_cur_dkk_0166(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "DKK" in codes


def test_h01_cur_eur_0167(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "EUR" in codes


def test_h01_cur_gbp_0168(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "GBP" in codes


def test_h01_cur_hkd_0169(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HKD" in codes


def test_h01_cur_hrk_0170(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HRK" in codes


def test_h01_cur_huf_0171(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HUF" in codes


def test_h01_cur_idr_0172(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "IDR" in codes


def test_h01_cur_ils_0173(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ILS" in codes


def test_h01_cur_inr_0174(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "INR" in codes


def test_h01_cur_isk_0175(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ISK" in codes


def test_h01_cur_jpy_0176(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "JPY" in codes


def test_h01_cur_krw_0177(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "KRW" in codes


def test_h01_cur_mxn_0178(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MXN" in codes


def test_h01_cur_myr_0179(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MYR" in codes


def test_h01_cur_nok_0180(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NOK" in codes


def test_h01_cur_nzd_0181(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NZD" in codes


def test_h01_cur_php_0182(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PHP" in codes


def test_h01_cur_pln_0183(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PLN" in codes


def test_h01_cur_ron_0184(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RON" in codes


def test_h01_cur_rub_0185(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RUB" in codes


def test_h01_cur_sek_0186(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SEK" in codes


def test_h01_cur_sgd_0187(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SGD" in codes


def test_h01_cur_thb_0188(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "THB" in codes


def test_h01_cur_try_0189(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "TRY" in codes


def test_h01_cur_usd_0190(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "USD" in codes


def test_h01_cur_zar_0191(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ZAR" in codes


def test_h01_cur_aud_0192(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "AUD" in codes


def test_h01_cur_bgn_0193(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BGN" in codes


def test_h01_cur_brl_0194(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BRL" in codes


def test_h01_cur_cad_0195(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CAD" in codes


def test_h01_cur_chf_0196(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CHF" in codes


def test_h01_cur_cny_0197(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CNY" in codes


def test_h01_cur_czk_0198(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CZK" in codes


def test_h01_cur_dkk_0199(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "DKK" in codes


def test_h01_cur_eur_0200(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "EUR" in codes


def test_h01_cur_gbp_0201(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "GBP" in codes


def test_h01_cur_hkd_0202(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HKD" in codes


def test_h01_cur_hrk_0203(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HRK" in codes


def test_h01_cur_huf_0204(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HUF" in codes


def test_h01_cur_idr_0205(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "IDR" in codes


def test_h01_cur_ils_0206(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ILS" in codes


def test_h01_cur_inr_0207(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "INR" in codes


def test_h01_cur_isk_0208(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ISK" in codes


def test_h01_cur_jpy_0209(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "JPY" in codes


def test_h01_cur_krw_0210(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "KRW" in codes


def test_h01_cur_mxn_0211(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MXN" in codes


def test_h01_cur_myr_0212(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MYR" in codes


def test_h01_cur_nok_0213(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NOK" in codes


def test_h01_cur_nzd_0214(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NZD" in codes


def test_h01_cur_php_0215(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PHP" in codes


def test_h01_cur_pln_0216(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PLN" in codes


def test_h01_cur_ron_0217(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RON" in codes


def test_h01_cur_rub_0218(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RUB" in codes


def test_h01_cur_sek_0219(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SEK" in codes


def test_h01_cur_sgd_0220(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SGD" in codes


def test_h01_cur_thb_0221(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "THB" in codes


def test_h01_cur_try_0222(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "TRY" in codes


def test_h01_cur_usd_0223(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "USD" in codes


def test_h01_cur_zar_0224(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ZAR" in codes


def test_h01_cur_aud_0225(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "AUD" in codes


def test_h01_cur_bgn_0226(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BGN" in codes


def test_h01_cur_brl_0227(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BRL" in codes


def test_h01_cur_cad_0228(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CAD" in codes


def test_h01_cur_chf_0229(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CHF" in codes


def test_h01_cur_cny_0230(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CNY" in codes


def test_h01_cur_czk_0231(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CZK" in codes


def test_h01_cur_dkk_0232(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "DKK" in codes


def test_h01_cur_eur_0233(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "EUR" in codes


def test_h01_cur_gbp_0234(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "GBP" in codes


def test_h01_cur_hkd_0235(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HKD" in codes


def test_h01_cur_hrk_0236(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HRK" in codes


def test_h01_cur_huf_0237(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HUF" in codes


def test_h01_cur_idr_0238(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "IDR" in codes


def test_h01_cur_ils_0239(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ILS" in codes


def test_h01_cur_inr_0240(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "INR" in codes


def test_h01_cur_isk_0241(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ISK" in codes


def test_h01_cur_jpy_0242(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "JPY" in codes


def test_h01_cur_krw_0243(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "KRW" in codes


def test_h01_cur_mxn_0244(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MXN" in codes


def test_h01_cur_myr_0245(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MYR" in codes


def test_h01_cur_nok_0246(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NOK" in codes


def test_h01_cur_nzd_0247(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NZD" in codes


def test_h01_cur_php_0248(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PHP" in codes


def test_h01_cur_pln_0249(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PLN" in codes


def test_h01_cur_ron_0250(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RON" in codes


def test_h01_cur_rub_0251(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RUB" in codes


def test_h01_cur_sek_0252(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SEK" in codes


def test_h01_cur_sgd_0253(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SGD" in codes


def test_h01_cur_thb_0254(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "THB" in codes


def test_h01_cur_try_0255(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "TRY" in codes


def test_h01_cur_usd_0256(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "USD" in codes


def test_h01_cur_zar_0257(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ZAR" in codes


def test_h01_cur_aud_0258(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "AUD" in codes


def test_h01_cur_bgn_0259(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BGN" in codes


def test_h01_cur_brl_0260(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BRL" in codes


def test_h01_cur_cad_0261(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CAD" in codes


def test_h01_cur_chf_0262(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CHF" in codes


def test_h01_cur_cny_0263(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CNY" in codes


def test_h01_cur_czk_0264(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CZK" in codes


def test_h01_cur_dkk_0265(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "DKK" in codes


def test_h01_cur_eur_0266(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "EUR" in codes


def test_h01_cur_gbp_0267(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "GBP" in codes


def test_h01_cur_hkd_0268(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HKD" in codes


def test_h01_cur_hrk_0269(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HRK" in codes


def test_h01_cur_huf_0270(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HUF" in codes


def test_h01_cur_idr_0271(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "IDR" in codes


def test_h01_cur_ils_0272(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ILS" in codes


def test_h01_cur_inr_0273(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "INR" in codes


def test_h01_cur_isk_0274(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ISK" in codes


def test_h01_cur_jpy_0275(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "JPY" in codes


def test_h01_cur_krw_0276(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "KRW" in codes


def test_h01_cur_mxn_0277(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MXN" in codes


def test_h01_cur_myr_0278(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MYR" in codes


def test_h01_cur_nok_0279(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NOK" in codes


def test_h01_cur_nzd_0280(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NZD" in codes


def test_h01_cur_php_0281(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PHP" in codes


def test_h01_cur_pln_0282(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PLN" in codes


def test_h01_cur_ron_0283(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RON" in codes


def test_h01_cur_rub_0284(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RUB" in codes


def test_h01_cur_sek_0285(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SEK" in codes


def test_h01_cur_sgd_0286(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SGD" in codes


def test_h01_cur_thb_0287(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "THB" in codes


def test_h01_cur_try_0288(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "TRY" in codes


def test_h01_cur_usd_0289(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "USD" in codes


def test_h01_cur_zar_0290(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ZAR" in codes


def test_h01_cur_aud_0291(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "AUD" in codes


def test_h01_cur_bgn_0292(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BGN" in codes


def test_h01_cur_brl_0293(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BRL" in codes


def test_h01_cur_cad_0294(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CAD" in codes


def test_h01_cur_chf_0295(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CHF" in codes


def test_h01_cur_cny_0296(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CNY" in codes


def test_h01_cur_czk_0297(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CZK" in codes


def test_h01_cur_dkk_0298(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "DKK" in codes


def test_h01_cur_eur_0299(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "EUR" in codes


def test_h01_cur_gbp_0300(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "GBP" in codes


def test_h01_cur_hkd_0301(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HKD" in codes


def test_h01_cur_hrk_0302(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HRK" in codes


def test_h01_cur_huf_0303(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HUF" in codes


def test_h01_cur_idr_0304(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "IDR" in codes


def test_h01_cur_ils_0305(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ILS" in codes


def test_h01_cur_inr_0306(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "INR" in codes


def test_h01_cur_isk_0307(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ISK" in codes


def test_h01_cur_jpy_0308(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "JPY" in codes


def test_h01_cur_krw_0309(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "KRW" in codes


def test_h01_cur_mxn_0310(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MXN" in codes


def test_h01_cur_myr_0311(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MYR" in codes


def test_h01_cur_nok_0312(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NOK" in codes


def test_h01_cur_nzd_0313(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NZD" in codes


def test_h01_cur_php_0314(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PHP" in codes


def test_h01_cur_pln_0315(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PLN" in codes


def test_h01_cur_ron_0316(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RON" in codes


def test_h01_cur_rub_0317(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RUB" in codes


def test_h01_cur_sek_0318(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SEK" in codes


def test_h01_cur_sgd_0319(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SGD" in codes


def test_h01_cur_thb_0320(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "THB" in codes


def test_h01_cur_try_0321(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "TRY" in codes


def test_h01_cur_usd_0322(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "USD" in codes


def test_h01_cur_zar_0323(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ZAR" in codes


def test_h01_cur_aud_0324(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "AUD" in codes


def test_h01_cur_bgn_0325(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BGN" in codes


def test_h01_cur_brl_0326(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BRL" in codes


def test_h01_cur_cad_0327(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CAD" in codes


def test_h01_cur_chf_0328(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CHF" in codes


def test_h01_cur_cny_0329(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CNY" in codes


def test_h01_cur_czk_0330(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CZK" in codes


def test_h01_cur_dkk_0331(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "DKK" in codes


def test_h01_cur_eur_0332(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "EUR" in codes


def test_h01_cur_gbp_0333(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "GBP" in codes


def test_h01_cur_hkd_0334(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HKD" in codes


def test_h01_cur_hrk_0335(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HRK" in codes


def test_h01_cur_huf_0336(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HUF" in codes


def test_h01_cur_idr_0337(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "IDR" in codes


def test_h01_cur_ils_0338(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ILS" in codes


def test_h01_cur_inr_0339(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "INR" in codes


def test_h01_cur_isk_0340(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ISK" in codes


def test_h01_cur_jpy_0341(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "JPY" in codes


def test_h01_cur_krw_0342(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "KRW" in codes


def test_h01_cur_mxn_0343(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MXN" in codes


def test_h01_cur_myr_0344(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MYR" in codes


def test_h01_cur_nok_0345(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NOK" in codes


def test_h01_cur_nzd_0346(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NZD" in codes


def test_h01_cur_php_0347(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PHP" in codes


def test_h01_cur_pln_0348(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PLN" in codes


def test_h01_cur_ron_0349(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RON" in codes


def test_h01_cur_rub_0350(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RUB" in codes


def test_h01_cur_sek_0351(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SEK" in codes


def test_h01_cur_sgd_0352(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SGD" in codes


def test_h01_cur_thb_0353(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "THB" in codes


def test_h01_cur_try_0354(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "TRY" in codes


def test_h01_cur_usd_0355(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "USD" in codes


def test_h01_cur_zar_0356(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ZAR" in codes


def test_h01_cur_aud_0357(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "AUD" in codes


def test_h01_cur_bgn_0358(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BGN" in codes


def test_h01_cur_brl_0359(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BRL" in codes


def test_h01_cur_cad_0360(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CAD" in codes


def test_h01_cur_chf_0361(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CHF" in codes


def test_h01_cur_cny_0362(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CNY" in codes


def test_h01_cur_czk_0363(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CZK" in codes


def test_h01_cur_dkk_0364(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "DKK" in codes


def test_h01_cur_eur_0365(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "EUR" in codes


def test_h01_cur_gbp_0366(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "GBP" in codes


def test_h01_cur_hkd_0367(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HKD" in codes


def test_h01_cur_hrk_0368(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HRK" in codes


def test_h01_cur_huf_0369(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HUF" in codes


def test_h01_cur_idr_0370(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "IDR" in codes


def test_h01_cur_ils_0371(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ILS" in codes


def test_h01_cur_inr_0372(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "INR" in codes


def test_h01_cur_isk_0373(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ISK" in codes


def test_h01_cur_jpy_0374(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "JPY" in codes


def test_h01_cur_krw_0375(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "KRW" in codes


def test_h01_cur_mxn_0376(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MXN" in codes


def test_h01_cur_myr_0377(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MYR" in codes


def test_h01_cur_nok_0378(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NOK" in codes


def test_h01_cur_nzd_0379(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NZD" in codes


def test_h01_cur_php_0380(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PHP" in codes


def test_h01_cur_pln_0381(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PLN" in codes


def test_h01_cur_ron_0382(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RON" in codes


def test_h01_cur_rub_0383(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "RUB" in codes


def test_h01_cur_sek_0384(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SEK" in codes


def test_h01_cur_sgd_0385(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "SGD" in codes


def test_h01_cur_thb_0386(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "THB" in codes


def test_h01_cur_try_0387(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "TRY" in codes


def test_h01_cur_usd_0388(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "USD" in codes


def test_h01_cur_zar_0389(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ZAR" in codes


def test_h01_cur_aud_0390(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "AUD" in codes


def test_h01_cur_bgn_0391(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BGN" in codes


def test_h01_cur_brl_0392(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "BRL" in codes


def test_h01_cur_cad_0393(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CAD" in codes


def test_h01_cur_chf_0394(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CHF" in codes


def test_h01_cur_cny_0395(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CNY" in codes


def test_h01_cur_czk_0396(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "CZK" in codes


def test_h01_cur_dkk_0397(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "DKK" in codes


def test_h01_cur_eur_0398(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "EUR" in codes


def test_h01_cur_gbp_0399(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "GBP" in codes


def test_h01_cur_hkd_0400(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "HKD" in codes
