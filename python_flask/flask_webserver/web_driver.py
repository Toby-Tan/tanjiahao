import requests
from selenium import webdriver


driver = webdriver.Chrome(port=7000)
url = 'http://www.baidu.com'
# driver.get(url)
#
#
# # selenium原理，web服务器通过/session/session_id/url--调用Post方法，传入url
server_url = 'http://localhost:7000/session/{}/url'.format(driver.session_id)
res = requests.post(server_url, json={'url': url})
print(res)



