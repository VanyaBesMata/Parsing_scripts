import requests
import json


def main():
    products_id, cookies, headers = get_products_id()
    info_items(products_id, cookies, headers)
    response = get_prices(products_id, cookies, headers)
    compare_items_prices(response)
    get_result()


# Получение id товара.
def get_products_id():
    cookies = {
        '_ga_BNX5WPP3YK': 'GS1.1.1668959131.1.1.1668959847.60.0.0',
        '_ga_CFMZTSS5FM': 'GS1.1.1668959131.1.1.1668959847.0.0.0',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'JSESSIONID': '8h2Qj6TGJzyRH3Mjcb2cc6Nyb2mQvH3PC8yn6df2kKpBrHCpJDg1!-1711692893',
        'MVID_CITY_ID': 'CityCZ_974',
        'MVID_KLADR_ID': '5200000100000',
        'MVID_REGION_ID': '118',
        'MVID_REGION_SHOP': 'S902',
        'MVID_TIMEZONE_OFFSET': '3',
        'bIPs': '-1707567431',
        'flacktory': 'no',
        'MVID_ENVCLOUD': 'prod1',
        'tmr_reqNum': '24',
        '_sp_id.d61c': '9e92613a-8afd-4d8a-a353-d82638cfd428.1668959131.1.1668959539..484910e0-70e8-4f8a-bb15-e163e9848c8f..711a377b-f77c-445a-833b-235790ec517c.1668959130964.28',
        '_sp_ses.d61c': '*',
        '__lhash_': '690ea19b8fb952a2650c609203954f4e',
        'uxs_uid': '71a38050-68ea-11ed-9160-83d32d0ccf91',
        'partnerSrc': 'yandex',
        'tmr_detect': '0%7C1668959136534',
        'AF_SYNC': '1668959135093',
        'afUserId': '3cffd128-e15e-46cb-89cf-a2ceda64744f-p',
        'advcake_click_id': '',
        'advcake_session_id': 'feb53195-b6a6-9d96-fe5f-717a3d503f24',
        'advcake_track_id': 'cda63779-075d-94d7-a7a8-145ea017c9e1',
        'advcake_track_url': 'https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dipr_Nn_Image_Name_Pure_search_desktop%26utm_content%3Dpid%7C21914417751_21914417751%7Ccid%7C54501827%7Cgid%7C4285491394%7Caid%7C9547803829%7Cpos%7Cpremium1%7Ckey%7C%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C47%7Cregion_name%7C%25D0%259D%25D0%25B8%25D0%25B6%25D0%25BD%25D0%25B8%25D0%25B9%2520%25D0%259D%25D0%25BE%25D0%25B2%25D0%25B3%25D0%25BE%25D1%2580%25D0%25BE%25D0%25B4%7Ccoef_goal%7C0%7Cdesktop%26utm_term%3D%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%26reff%3Dyandex_cpc_ipr_Nn_Image_Name_Pure_Search%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs1NDUwMTgyNzs5NTQ3ODAzODI5O3lhbmRleC5ydTpwcmVtaXVt%26yclid%3D16679260242218057727',
        'advcake_utm_partner': 'ipr_Nn_Image_Name_Pure_search_desktop',
        'advcake_utm_webmaster': 'pid%7C21914417751_21914417751%7Ccid%7C54501827%7Cgid%7C4285491394%7Caid%7C9547803829%7Cpos%7Cpremium1%7Ckey%7C%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C47%7Cregion_name%7C%25D0%259D%25D0%25B8%25D0%25B6%25D0%25BD%25D0%25B8%25D0%25B9%2520%25D0%259D%25D0%25BE%25D0%25B2%25D0%25B3%25D0%25BE%25D1%2580%25D0%25BE%25D0%25B4%7Ccoef_goal%7C0%7Cdesktop',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': 'e6e1b2b3-cc48-4b95-9a80-bda7ba383261',
        'tmr_lvid': '78e9cbc6daa16fd5051eef28ec1a6d2f',
        'tmr_lvidTS': '1668959134259',
        'flocktory-uuid': 'cc574ca3-260e-4bbc-915e-50df241791bf-2',
        '__SourceTracker': 'yandex__cpc',
        '__allsource': 'yandex',
        '__cpatrack': 'yandex_cpc',
        '__sourceid': 'yandex',
        '_ga': 'GA1.2.1337426488.1668959131',
        '_gid': 'GA1.2.1859510357.1668959131',
        'admitad_deduplication_cookie': 'yandex__cpc',
        'admitad_uid': '%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BC',
        'utm_term': '%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BC',
        'SMSError': '',
        'authError': '',
        '_ym_d': '1668959132',
        '_ym_isad': '1',
        '_ym_uid': '1668959132120367847',
        'MVID_GLC': 'true',
        'MVID_AB_TOP_SERVICES': '0',
        'MVID_GTM_ENABLED': '011',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOmZhbHNlLCJjb21wYXJpc29uIjpmYWxzZX0=',
        'MVID_AB_PDP_CHAR': '2',
        'MVID_GLP': 'true',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjpmYWxzZSwiZmF2b3JpdGUiOmZhbHNlLCJjYXJ0Ijp0cnVlfQ==',
        'cfidsgib-w-mvideo': '1QOat337yWtU74BJQug3gzuPYsxf9klhRf87YR8PPEnA/rMp2x+9r87aPwCZw77EKw71+z/Xhq3J3K8WL243BbuS75RXRUN1azvmyGXx6lIBiOmoqWLz254OVDpPI22uHFIbP2uyk2Qy3L13UeJdDk48ZpSilhUZQRcxjA==',
        'MVID_GUEST_ID': '21549339358',
        'MVID_SHOPPING_CART': '8dc818e9-918e-4dc1-92b0-9aae6fb4ff88',
        'MVID_CRM_ID': '0051102206',
        'MVID_GEOLOCATION_NEEDED': 'false',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_CART_AVAILABILITY': 'true',
        'MVID_CREDIT_AVAILABILITY': 'true',
        'MVID_HANDOVER_SUMMARY': 'true',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_MOBILE_FILTERS': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_WEBP_ENABLED': 'true',
        'HINTS_FIO_COOKIE_NAME': '1',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
        'MVID_CART_MULTI_DELETE': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'old',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'searchType2': '3',
    }

    headers = {
        'Accept': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_ga_BNX5WPP3YK=GS1.1.1668959131.1.1.1668959847.60.0.0; _ga_CFMZTSS5FM=GS1.1.1668959131.1.1.1668959847.0.0.0; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; JSESSIONID=8h2Qj6TGJzyRH3Mjcb2cc6Nyb2mQvH3PC8yn6df2kKpBrHCpJDg1!-1711692893; MVID_CITY_ID=CityCZ_974; MVID_KLADR_ID=5200000100000; MVID_REGION_ID=118; MVID_REGION_SHOP=S902; MVID_TIMEZONE_OFFSET=3; bIPs=-1707567431; flacktory=no; MVID_ENVCLOUD=prod1; tmr_reqNum=24; _sp_id.d61c=9e92613a-8afd-4d8a-a353-d82638cfd428.1668959131.1.1668959539..484910e0-70e8-4f8a-bb15-e163e9848c8f..711a377b-f77c-445a-833b-235790ec517c.1668959130964.28; _sp_ses.d61c=*; __lhash_=690ea19b8fb952a2650c609203954f4e; uxs_uid=71a38050-68ea-11ed-9160-83d32d0ccf91; partnerSrc=yandex; tmr_detect=0%7C1668959136534; AF_SYNC=1668959135093; afUserId=3cffd128-e15e-46cb-89cf-a2ceda64744f-p; advcake_click_id=; advcake_session_id=feb53195-b6a6-9d96-fe5f-717a3d503f24; advcake_track_id=cda63779-075d-94d7-a7a8-145ea017c9e1; advcake_track_url=https%3A%2F%2Fwww.mvideo.ru%2F%3Futm_source%3Dyandex%26utm_medium%3Dcpc%26utm_campaign%3Dipr_Nn_Image_Name_Pure_search_desktop%26utm_content%3Dpid%7C21914417751_21914417751%7Ccid%7C54501827%7Cgid%7C4285491394%7Caid%7C9547803829%7Cpos%7Cpremium1%7Ckey%7C%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C47%7Cregion_name%7C%25D0%259D%25D0%25B8%25D0%25B6%25D0%25BD%25D0%25B8%25D0%25B9%2520%25D0%259D%25D0%25BE%25D0%25B2%25D0%25B3%25D0%25BE%25D1%2580%25D0%25BE%25D0%25B4%7Ccoef_goal%7C0%7Cdesktop%26utm_term%3D%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%26reff%3Dyandex_cpc_ipr_Nn_Image_Name_Pure_Search%26_openstat%3DZGlyZWN0LnlhbmRleC5ydTs1NDUwMTgyNzs5NTQ3ODAzODI5O3lhbmRleC5ydTpwcmVtaXVt%26yclid%3D16679260242218057727; advcake_utm_partner=ipr_Nn_Image_Name_Pure_search_desktop; advcake_utm_webmaster=pid%7C21914417751_21914417751%7Ccid%7C54501827%7Cgid%7C4285491394%7Caid%7C9547803829%7Cpos%7Cpremium1%7Ckey%7C%25D0%25B2%25D0%25B8%25D0%25B4%25D0%25B5%25D0%25BE%2520%25D0%25BC%7Caddphrases%7Cno%7Cdvc%7Cdesktop%7Cregion%7C47%7Cregion_name%7C%25D0%259D%25D0%25B8%25D0%25B6%25D0%25BD%25D0%25B8%25D0%25B9%2520%25D0%259D%25D0%25BE%25D0%25B2%25D0%25B3%25D0%25BE%25D1%2580%25D0%25BE%25D0%25B4%7Ccoef_goal%7C0%7Cdesktop; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=e6e1b2b3-cc48-4b95-9a80-bda7ba383261; tmr_lvid=78e9cbc6daa16fd5051eef28ec1a6d2f; tmr_lvidTS=1668959134259; flocktory-uuid=cc574ca3-260e-4bbc-915e-50df241791bf-2; __SourceTracker=yandex__cpc; __allsource=yandex; __cpatrack=yandex_cpc; __sourceid=yandex; _ga=GA1.2.1337426488.1668959131; _gid=GA1.2.1859510357.1668959131; admitad_deduplication_cookie=yandex__cpc; admitad_uid=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BC; utm_term=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%20%D0%BC; SMSError=; authError=; _ym_d=1668959132; _ym_isad=1; _ym_uid=1668959132120367847; MVID_GLC=true; MVID_AB_TOP_SERVICES=0; MVID_GTM_ENABLED=011; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOmZhbHNlLCJjb21wYXJpc29uIjpmYWxzZX0=; MVID_AB_PDP_CHAR=2; MVID_GLP=true; MVID_OLD_NEW=eyJjb21wYXJpc29uIjpmYWxzZSwiZmF2b3JpdGUiOmZhbHNlLCJjYXJ0Ijp0cnVlfQ==; cfidsgib-w-mvideo=1QOat337yWtU74BJQug3gzuPYsxf9klhRf87YR8PPEnA/rMp2x+9r87aPwCZw77EKw71+z/Xhq3J3K8WL243BbuS75RXRUN1azvmyGXx6lIBiOmoqWLz254OVDpPI22uHFIbP2uyk2Qy3L13UeJdDk48ZpSilhUZQRcxjA==; MVID_GUEST_ID=21549339358; MVID_SHOPPING_CART=8dc818e9-918e-4dc1-92b0-9aae6fb4ff88; MVID_CRM_ID=0051102206; MVID_GEOLOCATION_NEEDED=false; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_MINDBOX_DYNAMICALLY=true; MVID_CART_AVAILABILITY=true; MVID_CREDIT_AVAILABILITY=true; MVID_HANDOVER_SUMMARY=true; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINI_PDP=true; MVID_MOBILE_FILTERS=true; MVID_PROMO_CATALOG_ON=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; wurfl_device_id=generic_web_browser; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CATALOG_STATE=1; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GIFT_KIT=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_WEBP_ENABLED=true; HINTS_FIO_COOKIE_NAME=1; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_TAXI_DELIVERY_INTERVALS_VIEW=old; NEED_REQUIRE_APPLY_DISCOUNT=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; searchType2=3',
        'Connection': 'keep-alive',
        'Accept-Language': 'ru',
        'Host': 'www.mvideo.ru',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
        'Referer': 'https://www.mvideo.ru/smartfony-i-svyaz-10/smartfony-205/f/skidka=da/tolko-v-nalichii=da',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'x-set-application-id': '7111af73-c4d2-4ac5-a1f3-ecbc38323c94',
        'baggage': 'sentry-transaction=%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=1f21e6e62b21457a86842f43be4f6958,sentry-sample_rate=0%2C5',
        'sentry-trace': '1f21e6e62b21457a86842f43be4f6958-b4d7a6ee92826fcf-0',
    }

    params = {
        'categoryId': '205',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing',
                            params=params, cookies=cookies,
                            headers=headers).json()
    products_id = response.get('body').get('products')
    with open('1_products_id.json', 'w') as f:
        json.dump(products_id, f, indent=4, ensure_ascii=False)

    return products_id, cookies, headers


# Получение информации о товаре.
def info_items(products_id, cookies, headers):
    json_data = {
        'productIds': products_id,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list',
                             cookies=cookies, headers=headers,
                             json=json_data).json()
    with open('2_items.json', 'w') as f:
        json.dump(response, f, indent=4, ensure_ascii=False)


# Получение ценника товара.
def get_prices(products_id, cookies, headers):
    products_id_str = ','.join(products_id)
    params = {
        'productIds': products_id_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices',
                            params=params, cookies=cookies,
                            headers=headers).json()
    with open('3_prices.json', 'w') as f:
        json.dump(response, f, indent=4, ensure_ascii=False)

    return response


# Сопоставление ценников и id товара.
def compare_items_prices(response):
    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_BasePrice': item_base_price,
            'item_SalePrice': item_sale_price,
            'item_Bonus': item_bonus
        }

    with open('4_items_prices.json', 'w') as f:
        json.dump(items_prices, f, indent=4, ensure_ascii=False)


# Сопоставление и получение готового файла.
def get_result():
    with open('2_items.json') as f:
        products_data = json.load(f)

    with open('4_items_prices.json') as f:
        products_price = json.load(f)

    products_data = products_data.get('body').get('products')
    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_price:
            prices = products_price[product_id]

        item['item_BasePrice'] = prices.get('item_BasePrice')
        item['item_SalePrice'] = prices.get('item_SalePrice')
        item['item_Bonus'] = prices.get('item_Bonus')

    with open('5_result.json', 'w') as f:
        json.dump(products_data, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
