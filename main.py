from Gorgon import Gorgon
from Argus import Argus
from Ladon import Ladon
from urllib.parse import urlencode
import time
def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "v04.04.05-ov-android", sdk_version: int = 134744640, platform: int = 0, unix: int = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        if not unix: unix = int(time.time())
    
        return Gorgon(params, unix, payload, cookie).get_value() | { 
            "x-ladon"   : Ladon.encrypt(unix, license_id, aid),
            "x-argus"   : Argus.get_sign(params, x_ss_stub, unix,
                platform        = platform,
                aid             = aid,
                license_id      = license_id,
                sec_device_id   = sec_device_id,
                sdk_version     = sdk_version_str, 
                sdk_version_int = sdk_version
            )
        }
def base_params():
        return {
            "passport-sdk-version": "19",
            "iid": '7318518857994389254',
            "device_id": '7318517321748022790',
            "ac": "wifi",
            "channel": "googleplay",
            "aid": "1233",
            "app_name": "musical_ly",
            "version_code": "300904",
            "version_name": "30.9.4",
            "device_platform": "android",
            "os": "android",
            "ab_version": "30.9.4",
            "ssmix": "a",
            "device_type": "ASUS_Z01QD",
            "device_brand": "Asus",
            "language": "en",
            "os_api": "28",
            "os_version": "9",
            "openudid": "704713c0da01388a",
            "manifest_version_code": "2023009040",
            "resolution": "1600*900",
            "dpi": "300",
            "update_version_code": "2023009040",
            "_rticket": "1692845349183",
            "is_pad": "0",
            "current_region": "BE",
            "app_type": "normal",
            "sys_region": "US",
            "mcc_mnc": "20610",
            "timezone_name": "Asia/Shanghai",
            "residence": "BE",
            "app_language": "en",
            "carrier_region": "BE",
            "ac2": "wifi",
            "uoo": "0",
            "op_region": "BE",
            "timezone_offset": "28800",
            "build_number": "30.9.4",
            "host_abi": "arm64-v8a",
            "locale": "en",
            "region": "US",
            "ts": "1692845349",
            "cdid": "60c2140f-c112-491a-8c93-183fd1ea8acf",
            "support_webview": "1",
            "okhttp_version": "4.1.120.34-tiktok",
            "use_store_region_cookie": "1"
        }
print(sign(urlencode(base_params())))