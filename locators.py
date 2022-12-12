from selenium.webdriver.common.by import By


# common
MAIN_TOP = (By.CSS_SELECTOR, "#top")
MAIN_TOP_CURRENCY = (By.CSS_SELECTOR, "#form-currency button[data-toggle='dropdown']")
SEARCH_INPUT = (By.CSS_SELECTOR, "#search input")
SEARCH_BTN = (By.CSS_SELECTOR, "#search button")
PRODUCT_MENU = (By.CSS_SELECTOR, "#menu")
CART_BTN = (By.CSS_SELECTOR, "#cart")
CART_TOTAL = (By.CSS_SELECTOR, "#cart-total")
FOOTER = (By.CSS_SELECTOR, "footer")
CONTENT = (By.CSS_SELECTOR, "div#content")

# main page
MAIN_SLIDER = (By.CSS_SELECTOR, "#slideshow0")
MAIN_CAROUSEL = (By.CSS_SELECTOR, "#carousel0")
PRODUCTS = (By.CSS_SELECTOR, "div.product-thumb")

# catalog page
BREADCRUMB = (By.CSS_SELECTOR, "ul.breadcrumb")
CATEGORY_TITLE = (By.CSS_SELECTOR, "#content h2")
LEFT_PANEL = (By.CSS_SELECTOR, "#column-left")
SORT_TYPE = (By.CSS_SELECTOR, "#input-sort")
SHOW_LIMIT = (By.CSS_SELECTOR, "#input-limit")
LIST_VIEW_BTN = (By.CSS_SELECTOR, "#list-view")
GRID_VIEW_BTN = (By.CSS_SELECTOR, "#grid-view")
LIST_PRODUCTS = (By.CSS_SELECTOR, "div.product-list")
GRID_PRODUCTS = (By.CSS_SELECTOR, "div.product-grid")

# product card page
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "button#button-cart")
QUANTITY_INPUT = (By.CSS_SELECTOR, "input#input-quantity")
PRODUCT_IMGS = (By.CSS_SELECTOR, "ul.thumbnails img")
ACTIVE_TAB = (By.CSS_SELECTOR, "ul.nav-tabs li.active")

# admin login page
OPENCART_IMG = (By.CSS_SELECTOR, "img[alt='OpenCart']")
USERNAME_INPUT = (By.CSS_SELECTOR, "input#input-username")
PASSWORD_INPUT = (By.CSS_SELECTOR, "input#input-password")
USERNAME_LBL = (By.CSS_SELECTOR, "label[for='input-username']")
PASSWORD_LBL = (By.CSS_SELECTOR, "label[for='input-password']")
LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
FORGOTTEN_PASSWORD_LINK = (By.CSS_SELECTOR, "span.help-block a")

# user registration page
PRIVACY_POLICY_CHB = (By.CSS_SELECTOR, "input[name='agree']")
CONTINUE_BTN = (By.CSS_SELECTOR, "input[type='submit']")
RIGHT_COLUMN = (By.CSS_SELECTOR, "aside#column-right")
REGISTER_TITLE = (By.CSS_SELECTOR, "#content h1")
ACCOUNT_BLOCK = (By.CSS_SELECTOR, "fieldset#account")
