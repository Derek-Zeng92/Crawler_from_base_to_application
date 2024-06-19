cookie = 'GUID=877917ea-ed6a-4f3e-a914-df6f35a7bffd; Hm_lvt_9793f42b498361373512340937deb2a0=1663935071; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F18%252F98%252F90%252F96139098.jpg-88x88%253Fv%253D1650527904000%26id%3D96139098%26nickname%3D%25E4%25B9%25A6%25E5%258F%258BqYx51ZhI1%26e%3D1679488405%26s%3D5fad52324388d0be; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2296139098%22%2C%22%24device_id%22%3A%221836a424247201-028f2e505afa75-9156f2c-1024000-1836a4242485%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22877917ea-ed6a-4f3e-a914-df6f35a7bffd%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1663936406'
# k_v = cookie.split(';')
# print(k_v)
# cookie_dict = {}
# for i in k_v:
#     l = i.split('=')
#     cookie_dict[l[0].strip()] = l[1].strip()

cookie_dict = {i.split('=')[0].strip(): i.split('=')[1].strip() for i in cookie.split(';')}
print(cookie_dict)
