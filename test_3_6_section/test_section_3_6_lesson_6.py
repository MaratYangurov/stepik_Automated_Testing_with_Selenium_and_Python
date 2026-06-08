from selenium import webdriver


browser = webdriver.Firefox()
browser.get('https://stepik.org/lesson/25969/step/8')
# browser.implicitly_wait(15)
# print(browser.title)
# browser.quit()

# Запустите файл:
# pytest -rx -v ./test_3_6_section/test_section_3_6_lesson_6.py