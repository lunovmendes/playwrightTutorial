class ShopWomen:

    def __init__(self, page):
        self.celebrating_beauty_header = page.locator ("text=Celebrating Beauty and Style")
        self.celebrating_beauty_body = page.locator("playwright-practice was founded by a group of like-minded fashion devotees")
        self.celebrating_beauty_hdr = page.locator("te3xt=Celebrating Beauty and Style")
        self.profile_arrow = page.locator('._1hHt1')
        self.profile_icon = page.locator('#defaultAvatar-comp-kqx7o7qv')
        self.cart_icon = page.locator('.bQgup')
        self.my_orders = page.locator('text=My Orders')
        self.my_orders_profile_box = page.locator('#SOSP_CONTAINER_CUSTMOM_ID >> :nth-match(div, 4)')