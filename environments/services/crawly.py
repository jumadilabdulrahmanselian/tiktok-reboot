from playwright.sync_api import sync_playwright
import time, os

class Crawl:
    browser = None
    context = None
    username = None

    def crawl(self, username) -> None:
        self.username = username
        with sync_playwright() as pw:
            # create browser instance
            bw = pw.chromium.launch(
                # we can choose either a Headful (With GUI) or Headless mode:
                headless=False,
                handle_sigint=True,
                handle_sigterm=True,
                handle_sighup=True
            )
            # create context
            # using context we can define page properties like viewport dimensions
            self.context = bw.new_context(
                # most common desktop viewport is 1920x1080
                viewport={"width": 480, "height": 480},
                extra_http_headers={
                    # 'Cookie': 'ttwid=1%7CwZE-y7-NY6JL2QvapodYb0bOIq8QR88jk1eRGxEzzMw%7C1675735358%7C40870a2d2240e8edb79273bab824843ef043ea4b4054d9287a9eb68d5c32bbc4; tiktok_webapp_theme=light; passport_csrf_token=c4c11c67c5aee05bae74c84786942492; passport_csrf_token_default=c4c11c67c5aee05bae74c84786942492; cmpl_token=AgQQAPNSF-RO0o_TNdsEOZ08-ax9eYyav4ArYMpMHA; uid_tt=da387a0caf7a6edee04cf7caf9af5b114fb1916ebead5378c720dabe8c2f5034; uid_tt_ss=da387a0caf7a6edee04cf7caf9af5b114fb1916ebead5378c720dabe8c2f5034; sid_tt=1e3881095e1500019224eb1b0474873f; sessionid=1e3881095e1500019224eb1b0474873f; sessionid_ss=1e3881095e1500019224eb1b0474873f; store-idc=useast5; store-country-code=us; store-country-code-src=uid; tt-target-idc=useast5; tt-target-idc-sign=YqVSz3wouud1yF_OeOljIWUrdWe506Ja53WCYyPhOnBrm58CJcIPkBLsc8CcnpjZX0HgVh_w87bC7BendErBnPYfUDguQBXnlSbVmdYCMJIULC1ynw7oN_oE5-BXL5oNjPwglCGnhuiDyeK2yfshpNutX9Z5zOLJVnmCJQ5OLNLaS17mDz7LcCd2pPBIiePiL55DmDkZ4RtnSHqpG34-mtPdEzrbWMZvlFPNsTALlzjQzkhHCOnHg4ji0S_tL46K-4lbQpcNDbF-znGlCEGvjhK1wbqcN_d2UY2YXauFDpUN8PS_t2m5P6KnhncPaT5VOJ0GXCBrDqz8h7dYqJIy52jky7GsPep8TMDygo4kdEPPEC5tUa1SlmmNjRARaqfH-f9ovYehMB7bjzi7gspyRjXy6YiiWQhgPcmdl1Vq6-E0kSTcUo6cAJGFhtOgpXVtKcAHoVa2nsPEqrixD-Gqr7VIm6YuxMYZfYzIxOyCJ-0Viwg052WR8zC92UkAIAxh; odin_tt=9de3c5ea2e4bcd4ff23c95d69674378ec83b344cf587acccc88f4cc8ab1491ce670fd8228202e0079b21ef30a97aa1dfc9ac403bdd072f8d594f6f61b0195ed5; ssid_ucp_v1=1.0.0-KGI3ODY2NjVmMDBhMTc5MDU0ZmM3YmI2NjRlNzJlYzE5NThjYThkZjkKGAiFiK3gyO_29l8QoM23ngYYsws4B0D0BxAEGgd1c2Vhc3Q1IiAxZTM4ODEwOTVlMTUwMDAxOTIyNGViMWIwNDc0ODczZg; msToken=Ccvc31FFApbQuH0xV8ffArGgvjMaeR3DNrAWrRyyABS1uDVhZ3nucT-i-VQhKjK48oznILSHxWCs2fobWfRMC3cAniykXswn7mf8MZtK0Xb4Uhb2CyLgBPgVXWF-IPRadedk4VZCsXogfrVrB5E=; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227197228477766338049%22%2C%22timestamp%22:1675735355836}; sid_guard=1e3881095e1500019224eb1b0474873f%7C1676514866%7C5184000%7CMon%2C+17-Apr-2023+02%3A34%3A26+GMT; sid_ucp_v1=1.0.0-KDVkMGZiMjExMmU5YjVjNjlkMTExY2Y2M2NhZmExZWRiZjEzNjcxNjIKGAiFiK3gyO_29l8Qsqy2nwYYsws4B0D0BxAEGgd1c2Vhc3Q1IiAxZTM4ODEwOTVlMTUwMDAxOTIyNGViMWIwNDc0ODczZg; ssid_ucp_v1=1.0.0-KDVkMGZiMjExMmU5YjVjNjlkMTExY2Y2M2NhZmExZWRiZjEzNjcxNjIKGAiFiK3gyO_29l8Qsqy2nwYYsws4B0D0BxAEGgd1c2Vhc3Q1IiAxZTM4ODEwOTVlMTUwMDAxOTIyNGViMWIwNDc0ODczZg; tt_csrf_token=o6mzgltO-O3KiaiCfQ-L1fYyF-BCdxhQPOH4; tt_chain_token=obRM3zgDNNGhMnQhyYOuaA==; _abck=D879C3138A8B22DC026BCA56FFB3E2C0~0~YAAQRR5DJItgdC+GAQAA/9jpeAmR7MbkTA8VVUiJtgzjPz7nLtxCFXn03l3ZF2wkPkoem7fDqC7ZZ5pnYlHemORXAkkTgkwO8MKVAAUbag5ZB/n4cBGCYKiypLAL0ouxjeFr78QRnTKqHjUpHR7tq16ry0CGCzhga/iceRcESkfUNukG4GTp/GQ9UQq9MFq2U8f4/mRvkZsDtHr+25MNySxj4OVKGw6IFXMEmDF0U6PPuvj3IilYiuhFRxUfpX9J3IPK+opK8l3jeYCxwPY2JR6tVr8aQbbfZo6ndIna5SvJTIZBSM8UtYD4xOfROhu9XpzMSHjlht7GBtzltBxaYXK7MXIkOaWLQSpXkucLmZDSf/hVv48t21Y2e4XFGS2IE6H6nGPYwO2b0ebW0rbWr8rBYcQETjom~-1~-1~-1; bm_sz=75A520DC464B440C8BFB694E2201B01C~YAAQZx5DJOOBgDeGAQAAA92xeRI+jy82KTaloncOVCmSzFYq/8RCRAR3sX75b0msxfG4NRiE9cpa2PqQAkqA1C7kUTa9P+HoocwSB5MBdm0yL6Xjjhi1Uajb7PS+i2+MPKsgWmMID4lAIPr7x0yMgGTtzngHAASMIv0/AR2yURmyEPLpkEcE1U8XeS1479CmoDmksEDmByQ7wzYwMG0bv/kVNu+jEdHBZC5W+IwJV7Q9hCtqn56CJ/9EBPtS0jnFgN7vKFU1manSyaFMFBEqAXGT5A4BwSOdstmkXnif/hbhIAHYgDlEiY8O4LngdB/yBMOj+AfeNL6OifY=~3356723~4539714; ttwid=1%7C-4jaDjnRGPdSmSk0_pUptAJUH3Fm29kLb2FhMN7W1FM%7C1677078950%7C6bb45a4b51228c8bef34240031bf459147f1f61a6e54fda8d0739e71beeb413e; ak_bmsc=31AC1181ED03E50E3E3AA86D7855BEEA~000000000000000000000000000000~YAAQZx5DJAeDgDeGAQAApvWxeRJN35Qzzk60TSAi0oGdpqW5Y7gmBB35HB1JeEavtI6MvCqfPFp1B5XQZmOEjxFQewTTJ1qIOeCx2gdDeOwm+fmO+mqDZnsN7g1MvgGCRZZqKbbFFN3/uY7G3eSPb9o54bU6NhAZZH+zfGUNPIlcGAld8hM6YJq6/hmsePiKSIod3GrElRMQn4NXcKDCuyPzZuCZe3F6XAKFdJapkyjiLFaqYVjC8jmqwD+ZClAzdoJJCKwJQ3NGGakeJaSTd/agL7HoPKZga4gm+szQMLPoslV81mMh+ywev1gb5uJVsTbifgK9R1QtYTzhB/rjDoktGswWGKv9rWV2AyMqF0XSbSwdOsdXMfA9ialbuNN2JRVNJRNpjH19R7kRkeBcX35ANaSbaJTk0GhQnWjccEAz8vNQUxnN7VdMwYsi6u1PR6DauxXQV0KvjbKFMFatV/SN0rD5GXFitAa0zAtdprHca5b9gowPIKDN; bm_sv=853D0E285CA617F65E320C5AB5EA27F8~YAAQZx5DJPODgDeGAQAACgCyeRJGXFvJXRhp/W543QZnQvPQ6xsKXUAi6yPvTDwH0dsW0kjilwdSDOzLZZb+4MHmj7Maw0rC6rgTP0FurtdO95G5qwpbD0aDzjyg4PZj9vfjT0AakgDcizkOGNGz0HRDx58x7NDxU//cXbPO2OI38vL4FwxKsFVbPPuofv4pjZx40aeWlLsUh/fCWg9LyScu/hZTChCYRgEMijypAKm4DgZ3GTF2w7/x8vPq7wmC~1; msToken=cNkFqf01Xzc5Mg7R-hBtpe3FTkLO05jbVg8n8QcG8NcO7_1w3Gu13gqchCH2_zxbs7apaSIKYWBlHRIfKWUvc1FWLa3Ok2jxLJPfocByP0adoMHX8eGW88H6lFkQaWVOVNYafiH1rayh8Ds=; msToken=cNkFqf01Xzc5Mg7R-hBtpe3FTkLO05jbVg8n8QcG8NcO7_1w3Gu13gqchCH2_zxbs7apaSIKYWBlHRIfKWUvc1FWLa3Ok2jxLJPfocByP0adoMHX8eGW88H6lFkQaWVOVNYafiH1rayh8Ds=; passport_fe_beating_status=false'
                    # 'Cookie': 'ttwid=1%7CwZE-y7-NY6JL2QvapodYb0bOIq8QR88jk1eRGxEzzMw%7C1675735358%7C40870a2d2240e8edb79273bab824843ef043ea4b4054d9287a9eb68d5c32bbc4; tiktok_webapp_theme=light; passport_csrf_token=c4c11c67c5aee05bae74c84786942492; passport_csrf_token_default=c4c11c67c5aee05bae74c84786942492; cmpl_token=AgQQAPNSF-RO0o_TNdsEOZ08-ax9eYyav4ArYMpMHA; uid_tt=da387a0caf7a6edee04cf7caf9af5b114fb1916ebead5378c720dabe8c2f5034; uid_tt_ss=da387a0caf7a6edee04cf7caf9af5b114fb1916ebead5378c720dabe8c2f5034; sid_tt=1e3881095e1500019224eb1b0474873f; sessionid=1e3881095e1500019224eb1b0474873f; sessionid_ss=1e3881095e1500019224eb1b0474873f; store-idc=useast5; store-country-code=us; store-country-code-src=uid; tt-target-idc=useast5; tt-target-idc-sign=YqVSz3wouud1yF_OeOljIWUrdWe506Ja53WCYyPhOnBrm58CJcIPkBLsc8CcnpjZX0HgVh_w87bC7BendErBnPYfUDguQBXnlSbVmdYCMJIULC1ynw7oN_oE5-BXL5oNjPwglCGnhuiDyeK2yfshpNutX9Z5zOLJVnmCJQ5OLNLaS17mDz7LcCd2pPBIiePiL55DmDkZ4RtnSHqpG34-mtPdEzrbWMZvlFPNsTALlzjQzkhHCOnHg4ji0S_tL46K-4lbQpcNDbF-znGlCEGvjhK1wbqcN_d2UY2YXauFDpUN8PS_t2m5P6KnhncPaT5VOJ0GXCBrDqz8h7dYqJIy52jky7GsPep8TMDygo4kdEPPEC5tUa1SlmmNjRARaqfH-f9ovYehMB7bjzi7gspyRjXy6YiiWQhgPcmdl1Vq6-E0kSTcUo6cAJGFhtOgpXVtKcAHoVa2nsPEqrixD-Gqr7VIm6YuxMYZfYzIxOyCJ-0Viwg052WR8zC92UkAIAxh; odin_tt=9de3c5ea2e4bcd4ff23c95d69674378ec83b344cf587acccc88f4cc8ab1491ce670fd8228202e0079b21ef30a97aa1dfc9ac403bdd072f8d594f6f61b0195ed5; ssid_ucp_v1=1.0.0-KGI3ODY2NjVmMDBhMTc5MDU0ZmM3YmI2NjRlNzJlYzE5NThjYThkZjkKGAiFiK3gyO_29l8QoM23ngYYsws4B0D0BxAEGgd1c2Vhc3Q1IiAxZTM4ODEwOTVlMTUwMDAxOTIyNGViMWIwNDc0ODczZg; msToken=Ccvc31FFApbQuH0xV8ffArGgvjMaeR3DNrAWrRyyABS1uDVhZ3nucT-i-VQhKjK48oznILSHxWCs2fobWfRMC3cAniykXswn7mf8MZtK0Xb4Uhb2CyLgBPgVXWF-IPRadedk4VZCsXogfrVrB5E=; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227197228477766338049%22%2C%22timestamp%22:1675735355836}; sid_guard=1e3881095e1500019224eb1b0474873f%7C1676514866%7C5184000%7CMon%2C+17-Apr-2023+02%3A34%3A26+GMT; sid_ucp_v1=1.0.0-KDVkMGZiMjExMmU5YjVjNjlkMTExY2Y2M2NhZmExZWRiZjEzNjcxNjIKGAiFiK3gyO_29l8Qsqy2nwYYsws4B0D0BxAEGgd1c2Vhc3Q1IiAxZTM4ODEwOTVlMTUwMDAxOTIyNGViMWIwNDc0ODczZg; ssid_ucp_v1=1.0.0-KDVkMGZiMjExMmU5YjVjNjlkMTExY2Y2M2NhZmExZWRiZjEzNjcxNjIKGAiFiK3gyO_29l8Qsqy2nwYYsws4B0D0BxAEGgd1c2Vhc3Q1IiAxZTM4ODEwOTVlMTUwMDAxOTIyNGViMWIwNDc0ODczZg; tt_csrf_token=o6mzgltO-O3KiaiCfQ-L1fYyF-BCdxhQPOH4; tt_chain_token=obRM3zgDNNGhMnQhyYOuaA==; bm_sz=75A520DC464B440C8BFB694E2201B01C~YAAQZx5DJOOBgDeGAQAAA92xeRI+jy82KTaloncOVCmSzFYq/8RCRAR3sX75b0msxfG4NRiE9cpa2PqQAkqA1C7kUTa9P+HoocwSB5MBdm0yL6Xjjhi1Uajb7PS+i2+MPKsgWmMID4lAIPr7x0yMgGTtzngHAASMIv0/AR2yURmyEPLpkEcE1U8XeS1479CmoDmksEDmByQ7wzYwMG0bv/kVNu+jEdHBZC5W+IwJV7Q9hCtqn56CJ/9EBPtS0jnFgN7vKFU1manSyaFMFBEqAXGT5A4BwSOdstmkXnif/hbhIAHYgDlEiY8O4LngdB/yBMOj+AfeNL6OifY=~3356723~4539714; ak_bmsc=31AC1181ED03E50E3E3AA86D7855BEEA~000000000000000000000000000000~YAAQZx5DJAeDgDeGAQAApvWxeRJN35Qzzk60TSAi0oGdpqW5Y7gmBB35HB1JeEavtI6MvCqfPFp1B5XQZmOEjxFQewTTJ1qIOeCx2gdDeOwm+fmO+mqDZnsN7g1MvgGCRZZqKbbFFN3/uY7G3eSPb9o54bU6NhAZZH+zfGUNPIlcGAld8hM6YJq6/hmsePiKSIod3GrElRMQn4NXcKDCuyPzZuCZe3F6XAKFdJapkyjiLFaqYVjC8jmqwD+ZClAzdoJJCKwJQ3NGGakeJaSTd/agL7HoPKZga4gm+szQMLPoslV81mMh+ywev1gb5uJVsTbifgK9R1QtYTzhB/rjDoktGswWGKv9rWV2AyMqF0XSbSwdOsdXMfA9ialbuNN2JRVNJRNpjH19R7kRkeBcX35ANaSbaJTk0GhQnWjccEAz8vNQUxnN7VdMwYsi6u1PR6DauxXQV0KvjbKFMFatV/SN0rD5GXFitAa0zAtdprHca5b9gowPIKDN; bm_sv=853D0E285CA617F65E320C5AB5EA27F8~YAAQZx5DJHqhgDeGAQAAXHizeRJ5JXKVSMT/aTncDWzcvFzZVs7Kr7Dyj35Vlz+nSzMFX4LM2+1mmOWT8IYisBerJwpb8ejucciUSNGyGSS0q91SZuwk6tIpk3BMs1OCSyLESt26iiPH2hqWxWwbf6+OqUUgAawSaOQKNSK7rYdjwe6RMVPfBcuLb1stH3dXMcwOw3+xQ8Dv8HXwh4I/ddij15koGdmlRD9flTpT0XxopAzBsuqd/RfSsArRU/Lm~1; ttwid=1%7CBW5roAL3hf9ZCceg8LRFCtpyiEUkxNWXpvPHrS_IOBg%7C1677079056%7C60716457009ef4fb3556728277ac4b4d3618dba7430f29632220dc68c1ec15da; msToken=9sb66hdUg6klZ1WIMs-NE47FPPe3dY5Yrx0H9ITpuewzmUNMiFKaBQqfaNDpTA8seJ9nHhdHNWwkQf8_ftsq2cKjSHO11sI6TtMZuNtRo-W-ffYpKrD_Qx7ZIZ897UODe4ij1B9fO9of6Ig=; msToken=9sb66hdUg6klZ1WIMs-NE47FPPe3dY5Yrx0H9ITpuewzmUNMiFKaBQqfaNDpTA8seJ9nHhdHNWwkQf8_ftsq2cKjSHO11sI6TtMZuNtRo-W-ffYpKrD_Qx7ZIZ897UODe4ij1B9fO9of6Ig=; _abck=D879C3138A8B22DC026BCA56FFB3E2C0~0~YAAQdR5DJBpzMDKGAQAAR7jPeQlYm2NJjxUp/gTAWRvUew/PP2tQ/mfVgibteG3V22zsPEqv3w7s3+AhxSiALks3B30vJMGIbiFcD7TcYvu/bT+7/Ut4XehcA3OKjylKdp+7zLY1CL/rYR1qH3dolnM6aVxcC/7nHRa8nEK4IPp8x8T1/pQP3QbECnosgmIrQ7aZSrzCH6m054pXi+fSaGNhSvLY/280XWLkdaFbEQOU802vmOdXj9yrIBwBvDnpQg2qvSrz8N3LESC22IChoBohBlj9/cCPEnq169GHgrl8d7p/wod/IbuB3VMrF7BCgoGkRMwdhsCwSKfbsuIZp8pf3SeeoOjBnZ49i1lpk2/TI4c+W6rIjubX8qFllQ==~-1~-1~-1; passport_fe_beating_status=false'
                }
            )
            # create page aka browser tab which we'll be using to do everything
            self.browser = self.context.new_page()
            print("Checking is ID Found...")
            # self.browser.goto("https://www.tiktok.com/@imyourebabyy")
            self.browser.goto("https://www.tiktok.com/@{}".format(self.username))
            time.sleep(5)
            # print(self.context.cookies())
            self.setCookie('cookiesx.txt')
            self.scroll_bottom()
            print("Collecting Video...")

            links = self.browser.locator('a')
            # no = 1
            data = []
            for link in links.element_handles():
                if "@"+self.username+"/video/" in link.get_attribute("href"):
                    # print("{}. {}".format(no, link.get_attribute("href")))
                    # no+=1
                    data.append(link.get_attribute("href"))
            # bw.close()
            self.terminate("chrome.exe")
            return data

    def terminate(self, ProcessName):
        os.system('taskkill /IM "' + ProcessName + '" /F')

    def scroll_bottom(self,):
            # self.check_captcha()
        self.browser.evaluate(
            """
            var intervalID = setInterval(function () {
                var scrollingElement = (document.scrollingElement || document.body);
                scrollingElement.scrollTop = scrollingElement.scrollHeight;
            }, 4000);

            """
        )
        prev_height = None
        while True:
            print("Loading Videos...")
            curr_height = self.browser.evaluate('(window.innerHeight + window.scrollY)')
            # print(curr_height)
            if not prev_height:
                prev_height = curr_height
                time.sleep(5)
            elif prev_height == curr_height:
                self.browser.evaluate('clearInterval(intervalID)')
                break
            else:
                prev_height = curr_height
                time.sleep(5)
            time.sleep(5)

    def read_cookies(self, p='cookies.txt'):
        cookies = []
        with open(p, 'r') as f:
            for e in f:
                e = e.strip()
                if e.startswith('#'):
                    continue
                k = e.split('\t')
                if len(k) < 3:
                    continue  # not enough data
                # with expiry
                # if k[-2] == 'ssid_ucp_v1':
                #     cookies.append({'name': k[-2], 'value': k[-1], 'sameSite': 'None',
                #                    'secure': True, 'httpOnly': True, 'expiry': int(k[4]), 'path': '/'})
                # else:
                cookies.append(
                        {'name': k[-2], 'value': k[-1], 'domain': k[-7], 'expiry': int(k[4]), 'path': '/'})
        return cookies

    def setCookie(self, cookies="cookies.txt"):
        cookies = self.read_cookies(p=os.path.join(os.path.dirname(os.path.abspath(__file__)), cookies))
        # print(cookies)
        self.context.clear_cookies()
        self.context.add_cookies(cookies)

        time.sleep(3)
        self.browser.reload()