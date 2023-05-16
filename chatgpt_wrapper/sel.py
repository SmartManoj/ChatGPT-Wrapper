import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import os,sys
is_linux = os.name == 'posix'
if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    import os
    if is_linux:
        username = os.environ['USER']
        profile_path = f'/home/{username}/.config/google-chrome'
        options.add_argument(f'--user-data-dir={profile_path}')
    else:
        username = os.environ['username']
        options.add_argument(rf"--user-data-dir=C:\Users\{username}\AppData\Local\Google\Chrome\User Data")
    options.add_argument('--disable-popup-blocking')
    # options.add_argument('--headless=new')

    
    options.add_argument(r'--profile-directory=Default')  # e.g. Profile 3
    capabilities = webdriver.DesiredCapabilities().CHROME

    b = driver = uc.Chrome(options=options,version_main=113 ,desired_capabilities=capabilities)

    _x = b.command_executor._url
    _c = b.session_id
    sr = '''
url = '{}'
rmt_con = remote_connection.RemoteConnection(url)
rmt_con._commands.update({{
    Command.UPLOAD_FILE: ("POST", "/session/$sessionId/file")
}})
b = SessionRemote(command_executor=rmt_con,desired_capabilities={{}})
b.session_id="{}"
'''.format(_x, _c)
    import sys
    
    file = './sr'
    with open(file, 'w') as f:
        f.write(sr)
    