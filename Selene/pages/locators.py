from selenium.webdriver.common.by import By


class SalePageLocators:
    GEAR_DEALS_TITLE = "//*[text()='Gear Deals']"
    BAGS_LINK = "//a[text()='Bags']"
    FITNESS_EQUIPMENT_LINK = "//a[text()='Fitness Equipment']"
    LINK_SALE = "https://magento.softwaretestingboard.com/sale.html"
    LINK_WOMEN_SALE = "https://magento.softwaretestingboard.com/promotions/women-sale.html"
    LINK_TEES_WOMEN = "https://magento.softwaretestingboard.com/women/tops-women/tees-women.html"

    BREADCRUMBS_LINKS_ON_PAGE_TEES = ['https://magento.softwaretestingboard.com/',
                                      'https://magento.softwaretestingboard.com/women.html',
                                      'https://magento.softwaretestingboard.com/women/tops-women.html']
    BREADCRUMBS_LINKS_ON_PAGE_WOMEN_SALE = ['https://magento.softwaretestingboard.com/',
                                            'https://magento.softwaretestingboard.com/sale.html']


class ProductLocators:

    ADD_TO_CART_BUTTON = '#product-addtocart-button'

    ARGUS_All_WEATHER_TANK = '[alt="Argus All-Weather Tank"]'
    ARGUS_All_WEATHER_TANK_SIZE = '//*[@title="Argus All-Weather Tank"]/../..//*[@option-label="M"]'
    ARGUS_All_WEATHER_TANK_COLOR = '//*[@title="Argus All-Weather Tank"]/../..//*[@option-label="Gray"]'
    ARGUS_All_WEATHER_TANK_ADD_TO_CARD = '//*[@title="Argus All-Weather Tank"]/../..//*[@title="Add to Cart"]'
    MINI_BASKET_WINDOW = '.action.showcart'
    VIEW_AND_EDIT_CART_LINK = "//*[text()='View and Edit Cart']"
    VIEW_AND_EDIT_CART_HREF = "[class='action viewcart']"
    SEE_DETAILS = '[data-role="title"]'
    SIZE_M = '//*[@class="product options list"]//*[text()="M"]'
    COLOR_GRAY = '//*[@class="product options list"]//*[text()="Gray"]'
    NAME_ITEM = '//*[text()="Argus All-Weather Tank"]'
    PRICE_ITEM = '//*[@class="minicart-price"]//*[@class="price"]'
    CART_SUBTOTAL = '.subtotal .price'
    QTY_FIELD = ".details-qty input"
    UPDATE = '[title="Update"]'
    SIZE_XS = '#option-label-size-143-item-166'
    COLOR_BLUE = '#option-label-color-93-item-50'
    SHOULD_CHOOSE_SIZE_AND_COLOR = '.swatch-input super-attribute-select'
    TEXT_REQUIRED_FIELD = 'This is a required field.'

    NAME_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART = '//*[@id="shopping-cart-table"] //*[text()="Argus All-Weather Tank"]'
    SIZE_M_ARGUS_ALL_WEATHER_TANK_CHECKOUT_CART = '//*[contains(text(),"M")]/../..//*[@id="shopping-cart-table"]'
    COLOR_GRAY_ARGUS_CHECKOUT_CART = '//*[@id="shopping-cart-table"]//*[contains(text(),"Gray")]'
    PRICE_ITEM_CHECKOUT_CART = '//*[@class="col price"] //*[text()="$22.00"]'
    CART_SUBTOTAL_CHECKOUT_CART = '//*[@class="col subtotal"] //*[text()="$22.00"]'
    QTY_FIELD_CHECKOUT_CART = '[class="field qty"] input'
    MINICART_COUNTER = '.counter-label'


class ShoppingCart:
    ESTIMATE_SHIPPING = '//*[@id="block-shipping"]//*[@class="title"]'
    COUNTRY_SELECT_DROP = '//*[@class="field"]//*[@name="country_id"]'
    STATE_REGION_SELECT = '//*[@class="field"]//*[@name="region_id"]'

    FLAT_RATE = '[data-bind="text: $data"]'
    SUBTOTAL_VAlUE = '[class="price"][data-th="Subtotal"]'
    ORDER_TOTAL_VALUE = '[data-bind="text: getValue()"]'
    PROCESEED_TO_CHECKOUT_BUTTON = '[data-role="proceed-to-checkout"]'



