from playwright.sync_api import sync_playwright
from lib import get_h1_text,get_title,number_of_h2_element

def run(playwright):
    # ブラウザ（ここではchromium）のインスタンスを起動
    browser = playwright.chromium.launch()

    # 新しいブラウザページのコンテキストを作成
    context = browser.new_context()

    # ページを開く
    page = context.new_page()
    page.goto("https://60thkoudaisai-app.vercel.app/faq")
    page.screenshot();

    # ページのタイトルを取得
    print(f"Page title: {get_title(page)}")

    # h1 要素のテキストコンテントを取得
    print(f"H1 content: {get_h1_text(page)}")

    # h2 要素を全て取得し、その数を出力
    print(f"Number of H2 elements: {number_of_h2_element(page)}")

    # ブラウザを閉じる
    browser.close()


with sync_playwright() as playwright:
    run(playwright)