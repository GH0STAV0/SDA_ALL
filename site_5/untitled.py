def blogger(driver):
	try:

		ain_button=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.top-banner')))
		ain_button.click()
		print('ok click')
		time.sleep(25)
	except Exception as e:
		print("error scrol 1")
#####################################################################################
	driver.get(url_6)
	time.sleep(5)
	# input("")
	try:
		accept_coockies=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'cookieChoiceDismiss')))
		accept_coockies.click()
		time.sleep(5)
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	except Exception as e:
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	time.sleep(3)
	try:
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML4'))))
		time.sleep(5)
		# driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'PopularPosts1'))))
		# time.sleep(3)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML2'))))
		time.sleep(5)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML3'))))
		time.sleep(10)
	except Exception as e:
		print("error scrol 1")
	try:
		post1_coockies=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PopularPosts1"]/div/ul/li[1]/div[1]/div[2]/a')))
		post1_coockies.click()
		print("1111111111111111111111111")
		time.sleep(5)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML4'))))
		time.sleep(3)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'PopularPosts1'))))
		time.sleep(3)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML2'))))
		time.sleep(3)
		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML3'))))
		time.sleep(10)

		# time.sleep(5)
		post2_coockies=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PopularPosts1"]/div/ul/li[2]/div[1]/div[2]/a')))
		post2_coockies.click()
		print("22222222222222222222222222222222")
		time.sleep(5)

		driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'HTML3'))))
		time.sleep(5)
		#time.sleep(4)

		post3_coockies=WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, '//*[@id="PopularPosts1"]/div/ul/li[3]/div[1]/div[2]/a')))
		post3_coockies.click()
		print("X3333333333333333333")
		# input('')
		time.sleep(3)
		time.sleep(5)
	except Exception as e:
		print("error scrol 1")
	# time.sleep(1)
	# driver.execute_script("window.open('');")
	# time.sleep(3)
	# driver.switch_to.window(driver.window_handles[1])
	# time.sleep(3)




# p0st_phase()
######################USER AGENT ###################################################