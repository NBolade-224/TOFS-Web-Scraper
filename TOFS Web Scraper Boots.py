from bs4 import BeautifulSoup
import requests

api_url = "https://www.boots.com/ProductListingViewRedesign?ajaxStoreImageDir=%2Fwcsstore%2FeBootsStorefrontAssetStore%2F&searchType=1000&advancedSearch=&cm_route2Page=&filterTerm=&storeId=11352&cm_pagename=&manufacturer=&sType=SimpleSearch&metaData=&catalogId=28501&searchTerm=&resultsPerPage=180&filterFacet=&resultCatEntryType=&gridPosition=&emsName=&disableProductCompare=false&langId=-1&facet=&categoryId=1952179"

headers = {
"authority": "www.boots.com",
"method": "POST",
"path": "/ProductListingViewRedesign?ajaxStoreImageDir=%2Fwcsstore%2FeBootsStorefrontAssetStore%2F&searchType=1000&advancedSearch=&cm_route2Page=&filterTerm=&storeId=11352&cm_pagename=&manufacturer=&sType=SimpleSearch&metaData=&catalogId=28501&searchTerm=&resultsPerPage=180&filterFacet=&resultCatEntryType=&gridPosition=&emsName=&disableProductCompare=false&langId=-1&facet=&categoryId=1595226",
"scheme": "https",
"accept": "*/*",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
"adrum": "isAjax:true",
"content-length": "316",
"content-type": "application/x-www-form-urlencoded",
"cookie": 'visid_incap_949787=6h8dZdK3RIatxHyD7Sr+ard8SGMAAAAAQUIPAAAAAACuDGfFp50fbG3Pr3BzA6BB; UserType=G; DISPLAYNAME=guest; DataLayerUserObject=2069105953%7C%7CNew%7Cfalse%7Cfalse%7C%7C%7C%7C4M9gi1oXvgA6zzuVXNqY_7f; crl8.fpcuid=096f84ae-15c0-4eb9-9fab-913b794c212f; gig_bootstrap_3_tgWZjPmf4Y0eeO0Okf-Cl3OjuaTNMW5aSIYEi0dY66KmwQXWyItwHA1Kb_uGmB9r=account_ver4; OptanonAlertBoxClosed=2022-10-13T21:01:50.172Z; _gcl_au=1.1.1262216848.1665694911; _tt_enable_cookie=1; _ttp=6c445538-077a-40ab-add0-90bad34a984c; _scid=3501d7bc-1dca-4c31-afbc-23405542bbb2; _pin_unauth=dWlkPU56QXhZekF6TVRndE9XUXhPQzAwTkRVd0xUaG1aVEl0WVdSbE1UWXpZekJoTURBMg; smc_tag=eyJpZCI6MTI5OSwibmFtZSI6ImJvb3RzLmNvbSJ9; smc_uid=1649603058183160; smc_refresh=18190; smc_not=default; nlbi_949787=9WfSNT5bSXnFcwWob/11CwAAAACtmMcy6xWyxpYZcePmlA8+; _ALGOLIA=anonymous-6a8d5f33-172c-4228-9b17-e59d2a0a559e; AMCVS_591A299B5B5F2D0F0A495E91%40AdobeOrg=1; at_check=true; DataLayerLoginOption=Guest; gig_canary=false; __gtm_campaign_url=https%3A%2F%2Fwww.boots.com%2Fbeauty%3Fcm_mmc%3Dbmm-buk-google-ppc-_-brand-_-B%257CPure%257CEx-_-UK_Brand_Boots%2BPure%2BBrand_Exact%26gclid%3DCjwKCAjw-rOaBhA9EiwAUkLV4uPhMGYeli5oYKp9zNKyKXVukYireAgW631FiUOjgjk1XTwRG5DwnBoCWZIQAvD_BwE%26gclsrc%3Daw.ds; __gtm_referrer=https%3A%2F%2Fwww.google.com%2F; deepLinkVisited=true; _gcl_aw=GCL.1666025482.CjwKCAjw-rOaBhA9EiwAUkLV4uPhMGYeli5oYKp9zNKyKXVukYireAgW631FiUOjgjk1XTwRG5DwnBoCWZIQAvD_BwE; _gcl_dc=GCL.1666025482.CjwKCAjw-rOaBhA9EiwAUkLV4uPhMGYeli5oYKp9zNKyKXVukYireAgW631FiUOjgjk1XTwRG5DwnBoCWZIQAvD_BwE; _cls_v=b95f3eb8-d84c-4650-8687-f72edf78aaa3; _cls_s=df756884-322b-4b46-80b7-58383d62c96b:0; _gid=GA1.2.475486008.1666025482; sc.ASP.NET_SESSIONID=2fzxtvjvezcfudfkuee2qrnm; coremetrics_disabled=false; smc_session_id=DNvKimTcPpe3bmyvfY4PAMPpCqwEcsXB; _clck=ibmnu6|1|f5s|0; ciq-uid=ciquid-00183e6db75c7-01-df9df8; ciq_new_visitor=true; s_cc=true; _gac_UA-41493563-1=1.1666025495.CjwKCAjw-rOaBhA9EiwAUkLV4uPhMGYeli5oYKp9zNKyKXVukYireAgW631FiUOjgjk1XTwRG5DwnBoCWZIQAvD_BwE; userVisitId=vulm-1666025512217-nl12; CompareItems_11352=; _taggstar_vid=032fac4a-4e3c-11ed-b5d5-3f803e26aeee; _taggstar_exp=v:3|id:|group:; incap_ses_533_949787=XHhJJF4PohvhWiMCc5llB/OMTWMAAAAAlPpDuTyBQMoEboydAaYb6A==; _sctr=1|1665961200000; incap_ses_246_949787=xPhlaEv4XgKlRCnYZfhpA0ePTWMAAAAAH1gdarAJBcSPGM2LipVXtg==; WC_CartTotal_undefined=0; WC_CartTotal_ItemCount=0; _gd1666027645214=_gd1666027645214; _gd1666027645215=_gd1666027645215; BVBRANDID=5b9d1d2f-4789-4375-a096-83477de8b1eb; _gd1666027645217=_gd1666027645217; _gd1666027645219=_gd1666027645219; _gd1666027645221=_gd1666027645221; _gd1666027645227=_gd1666027645227; _gd1666027645230=_gd1666027645230; BVImplmain_site=2111; _gd1666027646712=_gd1666027646712; _gd1666027848595=_gd1666027848595; _gd1666027848596=_gd1666027848596; _gd1666027848599=_gd1666027848599; _gd1666027848601=_gd1666027848601; _gd1666027848603=_gd1666027848603; _gd1666027848609=_gd1666027848609; _gd1666027848612=_gd1666027848612; _gd1666027850487=_gd1666027850487; incap_ses_473_949787=A47zfJEhiEjIjZcru2+QBjmUTWMAAAAAYt3kOusyx4V69/JZopwtPg==; incap_ses_1288_949787=EUZHH8qLmQ0FLT/xv+XfEUKaTWMAAAAAIC6NlaWdB5y2SL5SW92Cbw==; incap_ses_8219_949787=QnmVJGKwXDz9/tvKdsEPcpqfTWMAAAAAExhighp+B51h5cl+IWCFmg==; incap_ses_727_949787=enJPfufKQSG9YQY8YNMWCo62TWMAAAAAffTpJrLafq/eBbqU9XBoNw==; mboxEdgeCluster=37; AMCV_591A299B5B5F2D0F0A495E91%40AdobeOrg=-1124106680%7CMCIDTS%7C19283%7CMCMID%7C26417466422376993234577213083049555461%7CMCAAMLH-1666642190%7C6%7CMCAAMB-1666642190%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1666044590s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; s_inv=5688; s_vnc365=1697573392803%26vn%3D3; s_ivc=true; _taggstar_ses=aff717a7-4e57-11ed-9b44-83824b083aa0; incap_ses_245_949787=3BHQQcBViGv1VEnN62pmA2W4TWMAAAAAae5JwKiA2t9KDdwAS2bDTA==; gig_canary_ver=13432-3-27767325; campaign_viewed=1; WC_SESSION_ESTABLISHED=true; WC_PERSISTENT=w3zHRgVMyGQzWOrMgAYLpKIHZ2gwNVZgcwsga3d6xnc%3D%3B2022-10-17+21%3A55%3A30.698_1665694907367-43941_11352_2074474335%2C-1%2CGBP_11352; WC_AUTHENTICATION_2074474335=2074474335%2Cq7sTZSdT6eAvtXMlky7FN1%2FhwdItcQJG7GsC1ENEKH8%3D; WC_ACTIVEPOINTER=-1%2C11352; WC_USERACTIVITY_2074474335=2074474335%2C11352%2Cnull%2Cnull%2C1666040130700%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1877362032%2Cver_1666040130685%2CYV9pqsFv%2BoLO4nd%2BiErTELfwF%2BVEDOEFkSIi%2FW%2BBWZJ7sBtuAMPNpuFfYqPoclF7XC0Wdh%2Bujgbr0fQDOn5j5NRAHfebws%2FSBXa%2Bf7Xps4q4Cg6ZgddDToxfVYb8cZWDqDMSsGt36JR5F%2BW53ZKPr4zq09grx3gPl5%2BOmXHRAsPTQf%2FdpY1HantI4GvvilynBxZp7Mv41tTXVxvpX%2Bzdzpnh9FnqflXxajIAz1Gs8tDAKAM3uSNsOWYF4PfgozQxUthGacBUonlnT%2FN0oHY9OslrNpVEB3nRnmU1wtd0G%2FQ%3D; _gd1666040175994=_gd1666040175994; _gd1666040175995=_gd1666040175995; BVBRANDSID=5ee1ae7f-fffc-4929-99d8-5b6e6df18bfd; _gd1666040175998=_gd1666040175998; _gd1666040176000=_gd1666040176000; rr_rcs=eF5jYSlN9khLSUpKtEgy1002MzPTNUlOMdZNtTRI0TU1NzNINjQ0SExLMeHKLSvJTOEzNrLUNdQ1BACnTw6-; cto_bundle=mM50X19UWHhkbHNwR3M2aXAyWFRIVEdITDNreTV4S2QlMkJYSk9keW90d0poJTJGVllTMEI4MXF6Tmdub0hTNXBNUmh2cDI0aDBKZ0VnYmFJRzlIYldFZjY4V0pDa2JVJTJGWks4dE1KJTJCWUZ3M2hKYUZWZlRVU1RyWVolMkJvNm1scUVPc3d4Zm0lMkZuSCUyQlhGM3licWNKeHFvJTJGRUZiNU10OVRnJTNEJTNE; analyticsFacetAttributes=Category%3Ashop%20all; ADRUM=s=1666040304913&r=https%3A%2F%2Fwww.boots.com%2Fsite-map; mbox=PC#2c6de3e03b00494e87378f5d5b3ba7d0.37_0#1729285107|session#57bdc977661a4a6dae7259e637fc1efe#1666041991; QueueITAccepted-SDFrts345E=EventId%3Dgeneric2022%26QueueId%3De7637c47-0bc3-481a-8115-ef5f8587968a%26IsCookieExtendable%3Dtrue%26Expires%3D1666041506%26Hash%3Dc87fa8a127c7c2dafc1611a6398fee91b005bd380c067e85e240f50e4b199179; OneTrustPrevious=isIABGlobal=false&datestamp=Mon+Oct+17+2022+21:57:55+GMT+0100+(British+Summer+Time)&version=6.12.0&hosts=&consentId=100ea8f3-975f-4f35-be13-a55715b34b41&interactionCount=1&landingPath=NotLandingPage&groups=1:1,2:1,3:1,4:1&geolocation=; SessionCamTestCookie=true; _ga_12345=GS1.1.1666037390.2.1.1666040307.0.0.0; _uetsid=ee090f904e3b11edb3463dc5698fad18; _uetvid=261313f02ba711edb27e650617125203; s_ips=881; OptanonConsent=isIABGlobal=false&datestamp=Mon+Oct+17+2022+21%3A58%3A28+GMT%2B0100+(British+Summer+Time)&version=6.12.0&hosts=&consentId=100ea8f3-975f-4f35-be13-a55715b34b41&interactionCount=1&landingPath=NotLandingPage&groups=1%3A1%2C2%3A1%2C3%3A1%2C4%3A1&geolocation=%3B&AwaitingReconsent=false; s_tslv=1666040308440; s_plt=3.51; s_pltp=%7Cfragrance%7Caftershave%7Cmens-aftershave; _clsk=1ajhhnp|1666040308904|16|0|i.clarity.ms/collect; smc_tpv=40; smc_spv=39; smct_last_ov=[{"id":61377,"loaded":1666040309063,"open":null,"eng":null,"closed":null}]; _ga=GA1.2.684790702.1665694911; JSESSIONID=0010QocqJMl7tTKhbXyhLvTl6JE:-1; s_tp=8469; s_ppv=%257Cfragrance%257Caftershave%257Cmens-aftershave%2C100%2C10%2C8469%2C9%2C9; smct_session={"s":1666025699963,"l":1666040375219,"lt":1666040375219,"t":11961,"p":1647}; smct_session={"s":1666025699963,"l":1666040375219,"lt":1666040375219,"t":11961,"p":1647}; _ga_C3KVJJE2RH=GS1.1.1666037393.3.1.1666040375.59.0.0; _dc_gtm_UA-41493563-1=1"',
"origin": "https://www.boots.com",
"referer": "https://www.boots.com/fragrance/aftershave/mens-aftershave",
"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": '"Windows"', # try other bracket,
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
"x-requested-with": "XMLHttpRequest"}

# payload = "h=products&orde376456&requesttype=ajax"
# payload2 ="ajaxStoreImageDir=%2Fwcsstore%2FeBootsStorefrontAssetStore%2F&searchType=1000&advancedSearch=&cm_route2Page=&filterTerm=&storeId=11352&cm_pagename=&manufacturer=&sType=SimpleSearch&metaData=&catalogId=28501&searchTerm=&resultsPerPage=24&filterFacet=&resultCatEntryType=&gridPosition=&emsName=&disableProductCompare=false&langId=-1&facet=&categoryId=1595226"

payload3 = {
"contentBeginIndex": "0",
"pageNo": "2",
"productBeginIndex": "180",
"beginIndex": "180",
"pageView": "grid",
"resultType": "products",
"storeId": "11352",
"catalogId": "28501",
"langId": "-1",
"objectId": "_6_3074457345618283155_3074457345619376456",
"requesttype": "ajax",
}

response = requests.post(api_url, data=payload3, headers=headers)

urls1 = [
"https://www.boots.com/fragrance/perfume/all-perfume",
"https://www.boots.com/fragrance/aftershave/mens-aftershave"
]


def Scraper1():
    soup = BeautifulSoup(response.content, 'html.parser')
    name = soup.find_all(class_='estore_product_container')
    for y,x in enumerate(name):
        print(x.find(class_='product_name_link product_view_gtm').text)
        print(x.find(class_='product_price').text.strip())
        print(y)
        print()
Scraper1()
