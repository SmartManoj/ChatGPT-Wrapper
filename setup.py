from setuptools import setup

setup(
    name='ChatGPT Wrapper',
    version='0.1.0',    
    description='ChatGPT Wrapper using Selenium and PyAutoGUI',
    url='',
    author='மனோஜ்குமார் பழனிச்சாமி',
    author_email='smartmanoj42857@gmail.com',
    license='BSD 2-clause',
    packages=['chatgpt_wrapper'],
    requires=[
        'selenium',
        'undetected_chromedriver',
        'pyautogui',
        'pyperclip',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    
)