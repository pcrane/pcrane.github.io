#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Download a webpage as a PDF."""
from selenium import webdriver
import os

def download(driver, target_path):

    """Download the currently displayed page to target_path."""

    def execute(script, args):
        driver.execute('executePhantomScript',
                       {'script': script, 'args': args})

    # hack while the python interface lags
    driver.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')
    
    # set page format
    # inside the execution script, webpage is "this"
    page_format = 'this.paperSize = {format: "A4", orientation: "portrait", margin: "1.5cm" };'
    execute(page_format, [])

    # dirty hack -- we replace the 1st 'link' tag's href with print.css
    jsres = driver.execute_script(
    """
        document.getElementsByTagName("link").item(1).href='print.css';
    """);

    # render current page
    render = '''this.render("{}")'''.format(target_path)
    execute(render, [])

if __name__ == '__main__':
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.abspath(os.path.join(path, os.pardir))

    driver = webdriver.PhantomJS('phantomjs')
    
    driver.get("file://" + os.path.join(path, 'index.html'))
    download(driver, os.path.join(path, "paul_crane_resume.pdf"))
    driver.close()
