import time
from appium.webdriver.common.appiumby import AppiumBy
from conftest import readConstants
from pages.actions.android_actions import AndroidActions

from pages.actions.ios_actions import iOSActions
from pages.base_page import BasePage



locators_ipad = {
    "MENU_BAR": (AppiumBy.CLASS_NAME, "XCUIElementTypeTabBar"),
    "HOME_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Home"`]'),
    "DOWNLOADS_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Downloads"`]'),
    "HELP_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Help"`]'),
    "SIGN_OUT_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Sign out"`]'),
    "SEARCH_BUTTON": (AppiumBy.ACCESSIBILITY_ID, 'searchIpad'),
    "SAVE_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Back"`]'),
    "BACK_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Save"`]'),
    "HEADER_LOGO": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar[`name == "Home"`]/XCUIElementTypeButton[1]'),
    "SEARCH_BUTTON": (AppiumBy.ACCESSIBILITY_ID, "searchIpad"),
    "CAROUSAL_IMAGE": (AppiumBy.CLASS_NAME, "XCUIElementTypeCollectionView"),
    "CAROUSAL_IMAGE_CHANGE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypePageIndicator[`value == "page {num} of 5"`]'),
    "GENRES_TAB": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name contains "All Genres"`][1]'),
    "GENRES_CATEGORY_SELECT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "{genre}"`]'),
    "GENRES_SELECT_DISPLAYED_CONTENT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name contains "{project_name}"`]'),
    "SWIMLANES_LIST": (AppiumBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeOther'),
    "PROJECTS_FIRST_SWIMLANES": (AppiumBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]'),
    "PROJECTS_IN_FIRST_SWIMlANES": (AppiumBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText'),
    "PROJECT_START_WATCHING_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == " Start Watching"`]'),
    "VIDEO_CONTROLLER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Play/Pause"`]'),   
    "PAGINATION_PROJECT_LISTING_PAGE": (AppiumBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell'),
    "SWIMLANE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "{swimlane_name}"`]'),
    "SWIMLANE_FIRST": (AppiumBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeOther[1]')
}


class HomePageScreener(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        package_name = readConstants("current_app_package")
        locators_temp = {
            "HOME_NAVIGATION": (AppiumBy.ID, f'{package_name}:id/navHome'),
            "USER_EMAIL": (AppiumBy.ID, f'{package_name}:id/emailId'),
            "COLLAPSED_MENU": (AppiumBy.ID, f'{package_name}:id/layout_menu_collapse'),
            "MENU_SEARCH_COLLAPSED_ICON": (AppiumBy.ID, "com.indee.gd:id/bSearch_collapse"),  # Assuming this locator remains static
            "MENU_SEARCH_ICON": (AppiumBy.ID, f'{package_name}:id/img_search'),
            "MENU_HOME_ICON": (AppiumBy.ID, f'{package_name}:id/img_home'),
            "MENU_HELP_ICON": (AppiumBy.ID, f'{package_name}:id/btn_help'),
            "MENU_SIGNOUT": (AppiumBy.ID, f'{package_name}:id/txt_signout'),
            "SIGNOUT_BUTTON": (AppiumBy.ID, f'{package_name}:id/btn_signout'),
            "PROJECT_BANNER": (AppiumBy.ID, f'{package_name}:id/ivBanner'),
            "PROJECT_TITLE": (AppiumBy.ID, f'{package_name}:id/tvTitle'),
            "LOGIN_HEADER": (AppiumBy.ID, f'{package_name}:id/ivLogo'),
            "PROJECT_VIDEO_BTN": (AppiumBy.ID, f'{package_name}:id/btn_videos'),
            "PROJECT_DETAILS_BTN": (AppiumBy.ID, f'{package_name}:id/btn_details'),
            "SWIMLANES_LIST": (AppiumBy.ID, f'{package_name}:id/row_header'),
            "SWIMLANE_FIRST": (AppiumBy.XPATH, f"(//android.widget.TextView[@resource-id='{package_name}:id/row_header'])[1]"),
            "PROJECTS_FIRST_SWIMLANES": (AppiumBy.XPATH, f"(//*[@resource-id='{package_name}:id/row_content'])[2]"),
            "FIRST_PROJECT_POSTER": (AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@content-desc="Search Results"]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView'),
            "FIRST_PROJECT_INFO": (AppiumBy.XPATH, f"(//android.widget.TextView[@resource-id='{package_name}:id/title_text'])[1]"),
            "PROJECT_START_WATCHING_BUTTON": (AppiumBy.ID, f'{package_name}:id/rv_seemore'),
            "VIDEO_CONTROLLER": (AppiumBy.ID, f'{package_name}:id/llController'),
            "GENRES_TAB": (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView'),
            "GENRES_CATEGORY_SELECT": (AppiumBy.XPATH, "//android.widget.TextView[@text='{}']"),
            "GENRES_SELECT_DISPLAYED_CONTENT": (AppiumBy.ID, f'{package_name}:id/title_text'),
            "CAROUSEL_IMAGE": (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView"),
            "HEADER_LOGO": (AppiumBy.ID, f"{package_name}:id/header_logo"),
            "PAGINATION_PROJECT_LISTING_PAGE": (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]"),
            "VERIFY_MAIL_ID": (AppiumBy.ID, f"{package_name}:id/emailId"),
        }
        self.locators = locators_temp
        print("modied locator ====", self.locators)
    
    def verify_home_screen_navigation(self):
        if isinstance(self.actions, AndroidActions):
            Home_Navigation = self.actions.is_element_displayed(*self.locators["HOME_NAVIGATION"])
            print(Home_Navigation)
            return Home_Navigation
        elif isinstance(self.actions, iOSActions):
            Home_Navigation = self.actions.is_element_displayed(*locators_ipad['MENU_BAR'])
            print(Home_Navigation)
            return Home_Navigation
        else:
            time.sleep(6)
            self.actions.screenshotAttachment("home.jpeg")
            Home_Navigation = self.actions.is_element_displayed("name", "Paramount Global Screeners", "")
            return Home_Navigation

    def validate_logged_in_and_home_page_visible_within_timeframe(self, duration):
        print("in page object time out calculated for ===", duration)
        elementedLoaded = self.actions.validate_element_visitbilty_within_time(*self.locators["COLLAPSED_MENU"], duration)
        print("elementedLoaded   ", elementedLoaded)
        return elementedLoaded
    
    def verify_email_in_menu_bar(self):
        if isinstance(self.actions, AndroidActions):
            print("Android activity")
        elif isinstance(self.actions, iOSActions):
            print("Email Address Display In Menu Feature Is Not Feasible For iPad")
            return True
        else:
            time.sleep(3)
            self.actions.click_button("Down")
            self.actions.click_button("Left")
            return True
        
    def verify_menu_bar(self):
        if isinstance(self.actions, AndroidActions): 
            self.driver.press_keycode(self.keys['KEYCODE_MENU'])
            User_Email = self.actions.is_element_displayed(*self.locators["VERIFY_MAIL_ID"])
            Search_Icon = self.actions.is_element_displayed(*self.locators["MENU_SEARCH_ICON"])
            Menu_Icon = self.actions.is_element_displayed(*self.locators["MENU_HOME_ICON"])
            Help_Icon = self.actions.is_element_displayed(*self.locators["MENU_HELP_ICON"])
            Signout_icon = self.actions.is_element_displayed(*self.locators["MENU_SIGNOUT"])
            Menu_Bar_items = [User_Email, Search_Icon, Menu_Icon, Help_Icon, Signout_icon]
            if all(Menu_Bar_items):
                return True
            else:
                return False
        elif isinstance(self.actions, iOSActions):
            Download_Icon = self.actions.is_element_displayed(*locators_ipad["DOWNLOADS_BUTTON"])
            Home_Icon = self.actions.is_element_displayed(*locators_ipad["HOME_BUTTON"])
            Help_Icon = self.actions.is_element_displayed(*locators_ipad["HELP_BUTTON"])
            Signout_icon = self.actions.is_element_displayed(*locators_ipad["SIGN_OUT_BUTTON"])
            Menu_Bar_items = [Download_Icon, Home_Icon, Help_Icon, Signout_icon]
            if all(Menu_Bar_items):
                return True
            else:
                return False
        else:    
            time.sleep(20)
            self.actions.click_button("Down")
            self.actions.click_button("Left")
            time.sleep(4)
            # element_Name = "lLoggedInLastname"
            # text_Value = "Test-GSOADUBCFX@gmail.com"
            # element_Data = self.actions.fetchRokuCurrentPageSourceUsingName(element_Name, text_Value)
            # attrs = element_Data.get('value', {}).get('Attrs', [])
            # text_attr = next((attr['Value'] for attr in attrs if attr['Name']['Local'] == 'text'), None)
            # print("The text present is :" + text_attr)
            # return text_attr
            # Home_Text = self.actions.fetch_element_with_parent_name_arrtributes("name", "focusTitle", "text", "Search")
            # print("fetched element", Home_Text)
            # Help_Text = self.actions.fetch_Data("lHelp", "HELP")
            # print("fetched element", Help_Text)
            # logout_Text = self.actions.fetch_Data("lLogout", "LOGOUT")
            # print("fetched element", logout_Text)
            # Menu_Bar_items_Roku = [Home_Text, Help_Text, logout_Text]
            # if all(Menu_Bar_items_Roku):
            #     return True
            # else:
            #     return False
            currentElement = self.actions.fetch_element_with_parent_name_arrtributes("text", "Search", "index", "1")
            Search_Text = self.actions.fetch_data_from_json(currentElement)
            print("fetched element", Search_Text)
            currentElement = self.actions.fetch_element_with_parent_name_arrtributes("text", "Home", "index", "1")
            Home_Text = self.actions.fetch_data_from_json(currentElement)
            print("fetched element", Home_Text)
            currentElement = self.actions.fetch_element_with_parent_name_arrtributes("text", "Help", "index", "1")
            Help_Text = self.actions.fetch_data_from_json(currentElement)
            print("fetched element", Help_Text)
            currentElement = self.actions.fetch_element_with_parent_name_arrtributes("text", "Get Support", "index", "1")
            Get_support = self.actions.fetch_data_from_json(currentElement)
            print("fetched element", Get_support)
            currentElement = self.actions.fetch_element_with_parent_name_arrtributes("text", "Sign out", "index", "1")
            SignOut_Text = self.actions.fetch_data_from_json(currentElement)
            print("fetched element", SignOut_Text)
            Menu_Bar_items_Roku = [Search_Text, Home_Text, Help_Text, Get_support, SignOut_Text]
            if all(Menu_Bar_items_Roku):
                self.actions.screenshotAttachment("menu.jpeg")
                return True
            else:
                return False
            # self.actions.click_button("Down")
            # currentElement = self.actions.fetch_element_with_parent_name_arrtributes("name", "unFocusTitle", "index", "1")
            # Search_Text = self.actions.fetch_element(currentElement)
            # print("fetched element----", Search_Text)
            # currentElement = self.actions.fetch_element_with_parent_name_arrtributes("name", "unFocusTitle", "index", "1")
            # Search_Text = self.actions.fetch_element(currentElement)
            # print("fetched element", Search_Text)
            # currentElement = self.actions.fetch_element_with_parent_name_arrtributes("name", "unFocusTitle", "index", "1")
            # Search_Text = self.actions.fetch_element(currentElement)
            # print("fetched element", Search_Text)

    def click_on_search_button(self):
        if isinstance(self.actions, AndroidActions):
            print("Verify search field")
            self.driver.press_keycode(self.keys['KEYCODE_MENU'])
            self.actions.click_button(*self.locators["MENU_SEARCH_ICON"])
            self.actions.click_button(*self.locators["MENU_SEARCH_ICON"])
            try:
                self.actions.click_button(*self.locators["MENU_SEARCH_ICON"])
            except Exception:
                pass
            print("Search icon is displayed in Homepage")
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad["SEARCH_BUTTON"])
        else:
            time.sleep(3)
            print("Click on search=====")
            self.actions.click_button("Down")
            self.actions.click_button("Left")
            self.actions.click_button("Up")
            time.sleep(1)
            self.actions.click_button("Select") 
            self.actions.screenshotAttachment("search.jpeg")
                      
    def verify_swimlanes_list_in_homescreen(self):
        if isinstance(self.actions, AndroidActions):
            try:
                self.actions.wait_for_element(*self.locators["VIDEO_CONTROLLER"], timeout=10)
            except Exception:
                pass
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            return self.actions.is_element_displayed(*self.locators["SWIMLANES_LIST"])
        elif isinstance(self.actions, iOSActions):
            self.actions.swipe()
            return self.actions.is_element_displayed(*locators_ipad['SWIMLANES_LIST'])

    def verify_swimlanes_respective_project(self):
        if isinstance(self.actions, AndroidActions):
            return self.actions.is_element_displayed(*self.locators["PROJECTS_FIRST_SWIMLANES"])
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad["PROJECTS_FIRST_SWIMLANES"])

    def play_first_project_in_swimlanes(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators["FIRST_PROJECT_POSTER"])
            try:
                self.actions.click_button(*self.locators["FIRST_PROJECT_INFO"])
            except Exception:
                pass
            self.actions.click_button(*self.locators["PROJECT_START_WATCHING_BUTTON"])
            try:
                self.actions.click_button(*self.locators["PROJECT_START_WATCHING_BUTTON"])
            except Exception:
                pass
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            return self.actions.is_element_displayed(*self.locators["VIDEO_CONTROLLER"])
        elif isinstance(self.actions, iOSActions):
            Projects_list = self.actions.wait_for_elements(*locators_ipad['PROJECTS_IN_FIRST_SWIMlANES'])
            if Projects_list:
                First_project = Projects_list[-1]
                Project_name = First_project.get_attribute('value')
                print(Project_name)
                First_project.click()
                print('First Project In Swimlane Is Clicked')
                self.actions.click_button(*locators_ipad['PROJECT_START_WATCHING_BUTTON'])
                return self.actions.is_element_displayed(*locators_ipad["VIDEO_CONTROLLER"])
            else:
                print('Projects Are Not Displayed In First Swimlanes')
                return False

    def play_video_for_selected_project(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators["PROJECT_START_WATCHING_BUTTON"])
            try:
                self.actions.click_button(*self.locators["PROJECT_START_WATCHING_BUTTON"])
            except Exception:
                pass
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            return self.actions.is_element_displayed(*self.locators["VIDEO_CONTROLLER"])
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad["PROJECT_START_WATCHING_BUTTON"])
            return self.actions.is_element_displayed(*locators_ipad["VIDEO_CONTROLLER"])
        else:
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            start_watching_button = self.actions.fetch_Data("lButtonText", "Start Watching")
            print("Start watch button -------" + start_watching_button)
            self.actions.screenshotAttachment("playback.jpeg")
            self.actions.click_button("Select")
            time.sleep(7)
            return start_watching_button

    def genres_Dropdown(self): 
        if isinstance(self.actions, AndroidActions):
            Genre = False
            for i in range(20):
                try:
                    self.actions.wait_for_element(*self.locators["GENRES_TAB"], timeout=1)
                    print("Genres Tab is displayed in Homepage")
                    Genre = True
                    break
                except Exception:
                    self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            return Genre
        elif isinstance(self.actions, iOSActions):
            Genre = False
            for i in range(20):
                try:
                    self.actions.wait_for_element(*locators_ipad["GENRES_TAB"], timeout=1)
                    print("Genres Tab is displayed in Homepage")
                    Genre = True
                    break
                except Exception:
                    self.actions.swipe(direction="up")
            print(Genre)
            return Genre
        else:
            time.sleep(5)
            print("Verify generes dropdown")
            self.actions.click_button("Up")
            self.actions.click_button("Select") 
            self.actions.screenshotAttachment("generes.jpeg")
            time.sleep(2)
            Genre_Text = self.actions.is_element_displayed("name", "lButtonText", "All Genres")
            return Genre_Text

    def project_listing_page(self):
        if isinstance(self.actions, AndroidActions):
            return self.actions.is_element_displayed(*self.locators["PAGINATION_PROJECT_LISTING_PAGE"])
        elif isinstance(self.actions, iOSActions):
            Projects = self.actions.wait_for_elements(*locators_ipad['PAGINATION_PROJECT_LISTING_PAGE'])
            if Projects:
                if len(Projects) > 1:
                    print('Multiple projects are displayed under multiple swimlanes')
                else:
                    print('Projects are displayed for only one swimlane')
                return True
            else:
                return False 
        else:
            time.sleep(2)
            time.sleep(2)
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "posterImage", False, "")
            posterImage = self.actions.is_text_available(data, "posterImage")
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "focusedBackgroundImage", False, "")
            image = self.actions.is_text_available(data, "focusedBackgroundImage")
            projectList = [posterImage, image]
            self.actions.screenshotAttachment("projectlisiting.jpeg")
            if all(projectList):
                return True
            else:
                return False    

    def click_on_project(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators["PAGINATION_PROJECT_LISTING_PAGE"])            

    def genres_Dropdown_Select(self, genre):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators["GENRES_TAB"])
            try:
                self.actions.click_button(*self.locators["GENRES_TAB"])
            except Exception:
                pass
            Genre_Selection = False
            by, value = self.locators['GENRES_CATEGORY_SELECT']
            format_value = value.format(genre)
            for i in range(30):
                try:
                    self.actions.wait_for_element(by, format_value, timeout=0.5)
                    self.actions.click_button(by, format_value)
                    Genre_Selection = True
                    print("Genres Tab is displayed in Homepage")
                    break
                except Exception:
                    self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            return Genre_Selection
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad["GENRES_TAB"])
            Genre_Selection = False
            for i in range(30):
                by, value = locators_ipad["GENRES_CATEGORY_SELECT"]
                format_value = value.format(genre=genre)
                Element = self.actions.wait_for_element(by, format_value)
                if Element:
                    Element.click()
                    Genre_Selection = True
                    print("Genres Tab is displayed in Homepage")
                    break
                else:
                    self.actions.swipe(direction="up_right")
            return Genre_Selection
        else:
            time.sleep(3)
            print("Click on Genres===") 
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            time.sleep(2)

    def select_genre_content(self, expectedContent):
        if isinstance(self.actions, AndroidActions):  
            by, value = self.locators["GENRES_SELECT_DISPLAYED_CONTENT"]
            format_value = value.format(project_name=expectedContent)
            Display_Content = self.actions.is_element_displayed(by, format_value)
            self.actions.click_button(by, format_value)
            return Display_Content
        elif isinstance(self.actions, iOSActions):
            self.actions.swipe(direction="up")
            by, value = locators_ipad["GENRES_SELECT_DISPLAYED_CONTENT"]
            format_value = value.format(project_name=expectedContent)
            Display_Content = self.actions.validate_text_contains(by, format_value, expectedContent)
            self.actions.wait_for_element(by, format_value).click()
            return Display_Content
        else: 
            time.sleep(3)
            self.actions.click_button("Select")
            time.sleep(2)
            Generes_content = self.actions.is_element_displayed("name", "lButtonText", "Action")
            self.actions.click_button("Left")
            return Generes_content
                
    def click_logout_button(self):
        if isinstance(self.actions, AndroidActions):
            self.driver.press_keycode(self.keys['KEYCODE_MENU'])
            for i in range(3):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            for i in range(10):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_LEFT'])
            self.actions.click_button(*self.locators["MENU_SIGNOUT"])
            self.actions.click_button(*self.locators["MENU_SIGNOUT"])
            # self.actions.click_button(*self.locators["SIGNOUT_BUTTON"])
            # self.actions.click_button(*self.locators["SIGNOUT_BUTTON"])
            # time.sleep(4)
            return self.actions.is_element_displayed(*self.locators["LOGIN_HEADER"])
        elif isinstance(self.actions, iOSActions):
            print('Inside  sign out click function')
            self.actions.click_button(*locators_ipad["SIGN_OUT_BUTTON"])
        else:
            time.sleep(9)
            print("Click on sign out")
            # self.actions.click_button("Back")
            time.sleep(4)
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Left")
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Down")
            time.sleep(3)
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Select")
            self.actions.click_button("Up")
            self.actions.screenshotAttachment("logout.jpeg")
            self.actions.click_button("Select")
                    
    def click_on_help_button(self):
        if isinstance(self.actions, AndroidActions):    
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_LEFT'])
            self.actions.click_button(*self.locators["MENU_HELP_ICON"])
            try:
                self.actions.click_button(*self.locators["MENU_HELP_ICON"])
            except Exception:
                pass
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad["HELP_BUTTON"])
        else:
            time.sleep(3)
            self.actions.click_button("Down")
            self.actions.click_button("Left")
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            time.sleep(3)
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            self.actions.screenshotAttachment("help.jpeg")
            
    def select_project_from_homepage(self):
        if isinstance(self.actions, AndroidActions):    
            try:
                self.actions.wait_for_element(*self.locators["VIDEO_CONTROLLER"], timeout=15)
            except Exception:
                pass
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.actions.click_button(*self.locators["FIRST_PROJECT_POSTER"])
            return self.actions.is_element_displayed(*self.locators["PROJECT_START_WATCHING_BUTTON"])
        else:
            time.sleep(3)
            self.actions.click_button("Down")
            self.actions.click_button("Left")
            self.actions.click_button("Up")
            time.sleep(1)
            self.actions.click_button("Select")  
            self.actions.click_button("Select")
            time.sleep(1)
            self.actions.doRokuSendKeys("automation")
            time.sleep(3)
            for i in range(4):
                self.actions.click_button("Down")
                time.sleep(3)
            time.sleep(3)    
            self.actions.click_button("Select") 
            time.sleep(3) 
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            time.sleep(7)
            self.actions.click_button("Down")
            time.sleep(7)
            self.actions.click_button("Select")
            # self.actions.click_button("Down")
            # self.actions.click_button("Select")
            
    def verify_Carousel_view(self):
        if isinstance(self.actions, AndroidActions):
            return self.actions.is_element_displayed(*self.locators["CAROUSEL_IMAGE"])
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad["CAROUSAL_IMAGE"])
        else:
            time.sleep(5)
            return self.actions.is_element_displayed("name", "pSliderImage", "")
        
    def verify_carousel_autoscroll_functionality(self):
        if isinstance(self.actions, iOSActions):
            Carousal_Images = []
            for i in range(1, 6):
                by, value = locators_ipad["CAROUSAL_IMAGE_CHANGE"]
                format_value = value.format(num=i)
                Element = self.actions.is_element_displayed(by, format_value)
                Carousal_Images.append(Element)
            if all(Carousal_Images):
                print("Carousal image autoscroll functionality is verified")
                return True
            else:
                return False

    def click_on_carousel_image(self):
        if isinstance(self.actions, iOSActions):
            time.sleep(5)
            self.actions.click_button(*locators_ipad["CAROUSAL_IMAGE"])
            try:
                self.actions.tap(*locators_ipad['CAROUSAL_IMAGE'])
            except Exception:
                pass
   
    def verify_linked_project_in_carousel_image(self):
        if isinstance(self.actions, iOSActions):
            for i in range(5):
                Project_Page = self.actions.is_element_displayed(*locators_ipad["PROJECT_START_WATCHING_BUTTON"])
                print(Project_Page)
                if Project_Page:
                    return True
                else:
                    self.actions.click_button(*locators_ipad["CAROUSAL_IMAGE"])
            return False
        
    def verify_header_logo_in_homepage_screen(self):
        if isinstance(self.actions, AndroidActions):    
            return self.actions.is_element_displayed(*self.locators["HEADER_LOGO"])
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad["HEADER_LOGO"])
        else:
            time.sleep(2)
            # self.actions.click_button("Down")
            # self.actions.click_button("Left")
            return self.actions.is_element_displayed("name", "Paramount Global Screeners", "")
        
    def click_on_header_logo(self):
        if isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad["HEADER_LOGO"])
        else:
            pass

    def click_on_downloads_button(self):
        if isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad["DOWNLOADS_BUTTON"])
        else:
            pass

    def click_on_home_button(self):
        if isinstance(self.actions, AndroidActions):
            time.sleep(10)
            for i in range(4):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            for i in range(2):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_LEFT'])
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad["HOME_BUTTON"])
       
    def verify_deleted_swimlane_is_not_displayed_in_app(self, swimlane):
        if isinstance(self.actions, AndroidActions):
            by, value = self.locators["SWIMLANE"]
            format_value = value.format(swimlane_name=swimlane)
            Deleted_Swimlane = True
            for i in range(20):
                try:
                    self.actions.wait_for_element(by, format_value, timeout=2)
                    Deleted_Swimlane = False
                except Exception:
                    self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            return Deleted_Swimlane
        elif isinstance(self.actions, iOSActions):
            by, value = locators_ipad["SWIMLANE"]
            format_value = value.format(swimlane_name=swimlane)
            Deleted_Swimlane = True
            for i in range(20):
                try:
                    self.actions.get_element_visibility(by, format_value, timeout=2)
                    Deleted_Swimlane = False
                except Exception:
                    self.actions.swipe()
            return Deleted_Swimlane
        else:
            swimlane_name = self.actions.fetch_element(True, "", "", True, "name", "rlHomePage", False, "", True, "Test_Swimlane", False, "", "", False, "")
            fetch_swimlane_name = self.actions.fetch_data_from_json(swimlane_name)
            print("QR code ----" + fetch_swimlane_name)
            return not fetch_swimlane_name

    def verify_added_swimlane_is_displayed_in_app(self, swimlane):
        if isinstance(self.actions, AndroidActions):
            by, value = locators["SWIMLANE"]
            format_value = value.format(swimlane_name=swimlane)
            Added_Swimlane = False
            for i in range(20):
                try:
                    self.actions.wait_for_element(by, format_value, timeout=2)
                    Added_Swimlane = True
                except Exception:
                    self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            return Added_Swimlane
        elif isinstance(self.actions, iOSActions):
            by, value = locators_ipad["SWIMLANE"]
            format_value = value.format(swimlane_name=swimlane)
            Added_Swimlane = False
            for i in range(20):
                try:
                    self.actions.get_element_visibility(by, format_value, timeout=2)
                    Added_Swimlane = True
                except Exception:
                    self.actions.swipe()
            return Added_Swimlane
        else:
            swimlane_name = self.actions.fetch_element(True, "", "", True, "name", "rlHomePage", False, "", True, "Test_Swimlane", False, "", "", False, "")
            fetch_swimlane_name = self.actions.fetch_data_from_json(swimlane_name)
            print("QR code ----" + fetch_swimlane_name)
            return fetch_swimlane_name

    def verify_rearranged_swimlane_is_displayed_in_app(self, swimlane):
        if isinstance(self.actions, AndroidActions):
            Swimlane_name = self.actions.get_text(*self.locators['SWIMLANE_FIRST'])
            if Swimlane_name == swimlane:
                return True
            else:
                return False
        elif isinstance(self.actions, iOSActions):
            Swimlane_name = self.actions.get_text(*locators_ipad['SWIMLANE_FIRST'])
            if Swimlane_name == swimlane:
                return True
            else:
                return False
        else:
            swimlane_name = self.actions.fetch_element(True, "", "", True, "name", "rlHomePage", False, "", True, "Test_Swimlane", False, "", "", False, "")
            fetch_swimlane_name = self.actions.fetch_data_from_json(swimlane_name)
            print("QR code ----" + fetch_swimlane_name)
            return fetch_swimlane_name    
