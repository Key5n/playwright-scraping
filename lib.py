def get_title(page):
    """
    サイトのタイトルを取得する関数

    Args:
        page(Page): context.new_page()した結果
    """
    return page.title()

def number_of_h2_element(page):
    """
    h2要素の数を取得する関数

    Args:
        page(Page): context.new_page()した結果
    
    Returns:
        int: h2要素の数
    """
    return len(page.query_selector_all("h2"))

def get_h1_text(page):
    """
    h1要素のテキストを取得する関数

    Args:
        page(Page): context.new_page()した結果
    
    Returns:
        string: h1要素のテキスト
    """
    return page.inner_text("h1")