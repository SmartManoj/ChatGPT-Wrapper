from .selr import *
text_area_selector = 'textarea'
send_button='#__next > div.overflow-hidden.w-full.h-full.relative.flex.z-0 > div.relative.flex.h-full.max-w-full.flex-1.overflow-hidden > div > main > div.absolute.bottom-0.left-0.w-full.border-t.md\:border-t-0.dark\:border-white\/20.md\:border-transparent.md\:dark\:border-transparent.md\:bg-vert-light-gradient.bg-white.dark\:bg-gray-800.md\:\!bg-transparent.dark\:md\:bg-vert-dark-gradient.pt-2 > form > div > div.flex.flex-col.w-full.py-2.flex-grow.md\:py-3.md\:pl-4.relative.border.border-black\/10.bg-white.dark\:border-gray-900\/50.dark\:text-white.dark\:bg-gray-700.rounded-md.shadow-\[0_0_10px_rgba\(0\,0\,0\,0\.10\)\].dark\:shadow-\[0_0_15px_rgba\(0\,0\,0\,0\.10\)\] > button > svg'
def send_msg(msg):
    text_area = driver.find_element(By.CSS_SELECTOR, text_area_selector)
    from pyperclip import copy, paste
    print()
    copy(str(msg))
    text_area.send_keys(Keys.CONTROL, 'v')
    text_area.send_keys(Keys.ENTER)

    last_msg_selector='#__next > div.overflow-hidden.w-full.h-full.relative.flex.z-0 > div.relative.flex.h-full.max-w-full.flex-1.overflow-hidden > div > main > div.flex-1.overflow-hidden > div > div > div > div:nth-last-child(2) > div > div.relative.flex.w-\[calc\(100\%-50px\)\].flex-col.gap-1.md\:gap-3.lg\:w-\[calc\(100\%-115px\)\] > div.flex.flex-grow.flex-col.gap-3 > div > div > p'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, send_button)))
    last_msg = driver.find_element(By.CSS_SELECTOR, last_msg_selector)
    return (last_msg.text)

if __name__ == '__main__':
    # driver.switch_to.window(driver.window_handles[0])
    print(send_msg(r'5+9'))