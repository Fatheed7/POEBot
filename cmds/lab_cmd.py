from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import nextcord


async def lab_cmd(interaction, difficulty):  # sourcery skip
    searching = await interaction.send("Searching...",)
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument("--log-level=3")
    user_agent = (
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,'
        'like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    )
    options.add_argument("--window-size=1920,1200")
    options.add_argument('user-agent={0}'.format(user_agent))

    # sourcery skip: avoid-builtin-shadow
    # for char in char_list:
    driver = webdriver.Chrome(
        options=options,
        service=ChromeService(ChromeDriverManager().install()))
    URL = "https://www.poelab.com/"
    driver.get(URL)
    lab = driver.find_elements(By.CLASS_NAME, 'redLink')
    if difficulty == "normal":
        lab[3].click()
    elif difficulty == "cruel":
        lab[2].click()
    elif difficulty == "merciless":
        lab[1].click()
    elif difficulty == "uber":
        lab[0].click()
    sleep(1)
    img = driver.find_element(By.ID, 'notesImg')
    print(img.get_attribute('src'))
    text = difficulty.capitalize() + " Lab"
    embed = nextcord.Embed(
        title=text,
        color=nextcord.Color.red())
    embed.set_image(url=img.get_attribute('src'))
    embed.add_field(
        name="Click me if the image doesn't load",
        value=f'[{text}]({img.get_attribute("src")})',
        inline=False)
    await searching.delete()
    await interaction.send(embed=embed)

    driver.quit()
