from selene import browser, be, have


# Позитивный поиск текста на странице яндекс
def test_positive_find_text(open_url):
    # Ввод текста в поисковую строку
    browser.element('[name="text"]').should(be.blank).type('yashaka/selene').press_enter()
    # Поиск текста на странице
    browser.element('[class="RequestMeta-Message"]').should(have.text('Добавлены результаты по запросу «'))
    browser.element('//span[contains(text(), "GitHub")]').should(have.text('yashaka'))


# Негативный поиск текста на странице яндекс
def test_negative_find_text(open_url):
    # Ввод текста в поисковую строку
    browser.element('[name="text"]').should(be.blank).type('кокшгшо№;%"!:%"*(*(').press_enter()
    # Поиск текста на странице
    browser.element('[class="RequestMeta-Message"]').should(have.text('Точного совпадения не нашлось. Показаны результаты по запросу без кавычек.'))
