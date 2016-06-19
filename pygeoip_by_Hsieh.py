#encoding: utf-8
import pygeoip
import webbrowser

lite = pygeoip.GeoIP('./GeoLiteCity.dat')
asnum = pygeoip.GeoIP('./GeoIPASNum.dat')

def Pygeoip_ip(target):
        rec = lite.record_by_name(target)
        city = rec['city']
        region = rec['region_code']
        country = rec['country_name']
        long = rec['longitude']
        lat = rec['latitude']
	area = rec['area_code']
	pos = rec['postal_code']
	isp = asnum.isp_by_addr(target)
        print '- 偵測目標 - ' + target
        print '- 偵測位置 - '
	print ' 國家 : '+str(country)+' , 城市 : '+str(city)+' , 地區 : '+str(region)
	print ' ISP : '+str(isp)
        print ' 經度 : '+str(lat)+ ' , 緯度 : '+ str(long)
	print ' 地區代碼 :'+str(area)+' , 郵遞區號 : '+str(pos)
	
	f = open("geoip_history.txt","a")
        f.write('- 偵測目標 - ' +str(target))
        f.write('\n')
        f.write('- 偵測位置 - ')
        f.write('\n')
        f.write(' 國家 : '+ str(country) +' , 城市 : '+ str(city) +' , 地區 : ' +str(region))
        f.write('\n')
        f.write(' ISP : ' + str(isp))
        f.write('\n')
        f.write(' 經度 : '+str(lat)+ ' , 緯度 : '+ str(long))
        f.write('\n')
        f.write(' 地區代碼 : '+str(area)+' , 郵遞區號 : '+str(pos))
        f.write('\n')
        f.write('----------------------------------------------\n')
        f.close

def Pygeoip_dn(target):
	rec = lite.record_by_name(target)
        city = rec['city']
        region = rec['region_code']
        country = rec['country_name']
        long = rec['longitude']
        lat = rec['latitude']
        pos = rec['postal_code']
	area = rec['area_code']
	isp = asnum.isp_by_name(target)
        print '- 偵測目標 - ' + target
        print '- 偵測位置 - '
        print ' 國家 : '+ str(country) +' , 城市 : '+ str(city) +' , 地區 : ' +str(region)
	print ' ISP : ' + str(isp)
        print ' 經度 : '+str(lat)+ ' , 緯度 : '+ str(long)
        print ' 地區代碼 : '+str(area)+' , 郵遞區號 : '+str(pos)
	
	f = open("geoip_history.txt","a")
	f.write('- 偵測目標 - ' +str(target))
	f.write('\n')
	f.write('- 偵測位置 - ')
	f.write('\n')
	f.write(' 國家 : '+ str(country) +' , 城市 : '+ str(city) +' , 地區 : ' +str(region))
	f.write('\n')
	f.write(' ISP : ' + str(isp))
	f.write('\n')
	f.write(' 經度 : '+str(lat)+ ' , 緯度 : '+ str(long))
	f.write('\n')
	f.write(' 地區代碼 : '+str(area)+' , 郵遞區號 : '+str(pos))
	f.write('\n')
	f.write('----------------------------------------------\n')
	f.close

select = input('請選擇查詢方法 →[1]網域 [2]IP address : ')

if select == 1:
  dn = raw_input('鎖定目標 :')
  Pygeoip_dn(dn)

elif select == 2:
  ip = raw_input('鎖定目標 :')
  Pygeoip_ip(ip)
