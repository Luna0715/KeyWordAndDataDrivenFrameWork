#非混合框架时，向163邮箱添加联系人及发邮件测试代码：
#encoding = utf-8
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("启动浏览器...")
#创建Chrome浏览器的实例
driver = webdriver.Chrome(executable_path="D:\driver\chromedriver")
#最大化浏览器窗口
driver.maximize_window()
print("启动浏览器成功")
print("访问163邮箱登录页...")
driver.get("http://mail.163.com")
#暂停5s，以便邮箱登录页面加载完成
time.sleep(5)
assert "163网易免费邮--中文邮箱第一品牌" in driver.title
print("访问163邮箱登录页成功")
#创建显式等待
wait = WebDriverWait(driver,30)
driver.find_element_by_id("switchAccountLogin").click()
#检查xpath为//*[@class="loginForm"]//iframe的frame是否存在，存在则切换进frame控件
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'//*[@class="loginForm"]//iframe')))
#获取用户名输入框
userName = driver.find_element_by_xpath('//*[@data-loginname="loginEmail"]')
#输入用户名
userName.send_keys("Lyazhou715")
#获取密码输入框
pwd = driver.find_element_by_xpath("//input[@name='password']")
#输入密码
pwd.send_keys("xxx")
#发送一个回车键
pwd.send_keys(Keys.RETURN)
print("用户登录...")
#等待5s,以便登录成功后的页面加载完成
time.sleep(5)
assert "网易邮箱" in driver.title
print("登录成功")
print("添加联系人...")
#显示等待通讯录链接页面元素的出现
addressBook = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[text()='通讯录']")))
#单击“通讯录”按钮
addressBook.click()
#显示等待新建联系人按钮出现
newContact = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[text()='新建联系人']")))
#单击“新建联系人”按钮
newContact.click()

#显式等待输入联系人输入框的出现
contactName = wait.until(EC.visibility_of_element_located((By.XPATH,'//a[@title="编辑详细姓名"]/preceding-sibling::div/input')))
#输入联系人姓名
contactName.send_keys("lbb")
#输入联系人电子邮箱
driver.find_element_by_xpath('//*[@id="iaddress_MAIL_wrap"]//input').send_keys("1512663577@qq.com")
driver.find_element_by_xpath("//span[text()='设为星标联系人']/preceding-sibling::span/b").click()
time.sleep(2)
#输入联系人手机号
driver.find_element_by_xpath("//*[@id='iaddress_TEL_wrap']//input").send_keys("16666666666")
time.sleep(2)
#输入备注信息
driver.find_element_by_xpath("//textarea").send_keys("朋友")
time.sleep(2)
#单击“确认”按钮
driver.find_element_by_xpath('//span[text()="确 定"]').click()
time.sleep(5)
assert "1512663577@qq.com" in driver.page_source
print("添加联系人成功")

print("进入首页")
driver.find_element_by_xpath('//div[.="首页"]').click()
print("写信...")
#显式等待写信链接页面元素的出现
element = wait.until(EC.visibility_of_element_located((By.XPATH,'//span[text()="写 信"]')))
#单击写信链接
element.click()
time.sleep(5)
#写入收件人地址
driver.find_element_by_xpath('//div//input[@aria-label="收件人地址输入框，请输入邮件地址，多人时地址请以分号隔开"]').send_keys("Lbinbin715@163.com")
#写入邮件主题
driver.find_element_by_xpath("//div[@aria-label='邮件主题输入框，请输入邮件主题']/input").send_keys("新邮件")
#切换进frame控件
driver.switch_to.frame(driver.find_element_by_class_name("APP-editor-iframe"))
editBox = driver.find_element_by_xpath('/html/body')
editBox.send_keys("发给光荣之路的一封信")
driver.switch_to.default_content()
print("写信完成")
driver.find_element_by_xpath("//header//span[text()='发送']").click()
print("开始发送邮件...")
time.sleep(3)
assert "发送成功" in driver.page_source
print("邮件发送成功")
driver.quit()