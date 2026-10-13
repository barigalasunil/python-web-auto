
import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.actions.android_actions import AndroidActions
from pages.actions.ios_actions import iOSActions 
from pages.base_page import BasePage
from pages.actions.roku_actions import RokuActions
from conftest import readPreReqJsonValue
from conftest import readConstants

locators_ipad = {
    "MENU_BAR": (AppiumBy.ACCESSIBILITY_ID, "Tab Bar"),
    "MENU_HOME_ICON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Home"`]'),
    "MENU_BRAND_ICON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Brands"`]'),
    "MENU_WATCHLIST_ICON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Watchlist"`]'),
    "MENU_HELP_ICON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Help"`]'),
    "MENU_SIGNOUT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Sign out"`]'),
    "HEADER_LOGO": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeNavigationBar[`name == "Home"`]/XCUIElementTypeButton[1]'),
    "SEARCH_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "searchIpad"`]'),
    "CAROUSAL_IMAGE": (AppiumBy.CLASS_NAME, "XCUIElementTypeCollectionView"),
    "CAROUSAL_IMAGE_CHANGE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypePageIndicator[`value == "page {num} of 4"`]'),
    "GENRES_TAB": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "All Genres     "`][2]'),
    "GENRES_CATEGORY_SELECT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "{genre}}"`]'),
    "GENRES_SELECT_DISPLAYED_CONTENT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "{project_name}"`]'),
    "SEARCH_BOX_FIELD": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "Search for a title..."`]') 
}


class HomePageCinema(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        package_name = readConstants("current_app_package")
        locators_temp = {
            "HOME_NAVIGATION": (AppiumBy.ID, f"{package_name}:id/navHome"),
            "MENU_SEARCH_ICON": (AppiumBy.ID, f"{package_name}:id/btn_search"),
            "MENU_HOME_ICON": (AppiumBy.ID, f"{package_name}:id/btn_home"),
            "MENU_BRAND_ICON": (AppiumBy.ID, f"{package_name}:id/btn_brand"),
            "MENU_WATCHLIST_ICON": (AppiumBy.ID, f"{package_name}:id/btn_watchlist"),
            "MENU_HELP_ICON": (AppiumBy.ID, f"{package_name}:id/btn_help"),
            "MENU_SIGNOUT": (AppiumBy.ID, f"{package_name}:id/btn_signout"),
            "PROJECT_BANNER": (AppiumBy.ID, f"{package_name}:id/ivBanner"),
            "PROJECT_TITLE": (AppiumBy.ID, f"{package_name}:id/tvTitle"),
            "PROJECT_VIDEO_BTN": (AppiumBy.ID, f"{package_name}:id/btn_videos"),
            "PROJECT_DETAILS_BTN": (AppiumBy.ID, f"{package_name}:id/btn_details"),
            "SEASON_NUMBER1": (AppiumBy.ID, f"{package_name}:id/tvSeason"),
            "SWIMLANES_LIST": (AppiumBy.ID, f"{package_name}:id/row_header"),
            "SWIMLANE_FIRST": (AppiumBy.XPATH, f"(//android.widget.TextView[@resource-id='{package_name}:id/row_header'])[1]"),
            "PROJECTS_FIRST_SWIMLANES": (AppiumBy.XPATH, f"(//*[@resource-id='{package_name}:id/row_content'])[2]"),
            "FIRST_PROJECT_POSTER": (AppiumBy.XPATH, f"(//*[@resource-id='{package_name}:id/main_image'])[2]"),
            "FIRST_PROJECT_INFO": (AppiumBy.XPATH, f"(//android.widget.TextView[@resource-id='{package_name}:id/title_text'])[1]"),
            "WATCH_LIST": (AppiumBy.ID, f"{package_name}:id/txt_watchlist"),
            "VIDEO_CONTROLLER": (AppiumBy.ID, f"{package_name}:id/llController"),
            "GENRES_TAB": (AppiumBy.ID, f"{package_name}:id/dy_txt_genre"),
            "GENRES_CATEGORY_SELECT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Action']"),
            "GENRES_SELECT_DISPLAYED_CONTENT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Episodic04VCZFABPVDC']"),
            "CAROUSEL_IMAGE": (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView"),
            "HEADER_LOGO": (AppiumBy.ID, f"{package_name}:id/header_logo"),
            "PAGINATION_PROJECT_LISTING_PAGE": (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[2]"),
            "SEARCH_BOX_FIELD": (AppiumBy.ID, f"{package_name}:id/txt_search"),
            "PROJECT_VIDEO": (AppiumBy.ID, f"{package_name}:id/ivScImage"),
            "REMAINING_VIEW": (AppiumBy.ID, f"{package_name}:id/btnRemainingDate"),
            "EXPIRY_ON": (AppiumBy.ID, f"{package_name}:id/btnExpiryDate"),
            "PROJECTPOSTER": (AppiumBy.ID, f"{package_name}:id/ivPoster"),
            "PROJECTBANNER": (AppiumBy.ID, f"{package_name}:id/ivBanner"),
            "SEEMOREBUTTON": (AppiumBy.ID, f"{package_name}:id/rv_seemore"),
            "PROJECTDISCRIPTION": (AppiumBy.ID, f"{package_name}:id/rmTvEpisodeDescription"),
            "PPOJECTSYSNOPSIS": (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout"),
            "SEASON_NUMBER": (AppiumBy.ID, f"{package_name}:id/row_header"),
            "MULTIPLE_EPISODES": (AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@content-desc="SEASON 01"]'),
            "EPISODE_1": (AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@content-desc="SEASON 01"]/android.view.ViewGroup[1]/android.widget.TextView[2]'),
            "EPISODE_2": (AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@content-desc="SEASON 01"]/android.view.ViewGroup[2]/android.widget.TextView[2]'),
            "WATCH_BUTTON": (AppiumBy.ID, f"{package_name}:id/btPlayNow"),
            "SETTINGS_BUTTON": (AppiumBy.ID, f"{package_name}:id/exo_audio"),
            "VIDEO_DURATION": (AppiumBy.ID, f"{package_name}:id/tvScTime"),
            "AUTHEN_PLAYBUTTON": (AppiumBy.ID, f"{package_name}:id/btPlayNow"),
            "ENTER_PASSWORD": (AppiumBy.ID, f"{package_name}:id/etPhoneNumber"),
            "ENTER_PASSWORD_BUTTON": (AppiumBy.ID, f"{package_name}:id/btnControl"),
            "FARWARD_BUTTON": (AppiumBy.ID, f"{package_name}:id/exo_ffwd"),
            "TITLE": (AppiumBy.ID, f"{package_name}:id/tvTitle"),
            "INVALID_ERROR_MESSAGE": (AppiumBy.ID, f"{package_name}:id/tvError"),
            "OPT_NUMBER": (AppiumBy.ID, f"{package_name}:id/etVerificationCode"),
            "ENTER_OTP": (AppiumBy.ID, f"{package_name}:id/btnControl"),
            "EXPIRE": (AppiumBy.ID, f"{package_name}:id/btnExpiryDate"),
            "EPISODE_NUMBER": (AppiumBy.ID, f"{package_name}:id/tvEpisodeTitle")

        }
        self.locators = locators_temp
        print("modied locator ====", self.locators)

    def verify_home_screen_navigation(self):
        Home_Navigation = self.actions.is_element_displayed(*self.locators["HOME_NAVIGATION"])
        return Home_Navigation

    def validate_logged_in_and_home_page_visible_within_timeframe(self, duration):
        print("in page object time out calculated for ===", duration)
        elementedLoaded = self.actions.validate_element_visitbilty_within_time(*self.locators["COLLAPSED_MENU"], duration)
        print("elementedLoaded   ", elementedLoaded)
        return elementedLoaded
    
    def verify_menu_bar(self):
        if isinstance(self.actions, AndroidActions):
            try:
                
                self.actions.wait_for_element(*self.locators["VIDEO_CONTROLLER"], timeout=8)
            except Exception:
                pass
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_LEFT'])
            Home_Icon = self.actions.is_element_displayed(*self.locators["MENU_HOME_ICON"])
            Search_Icon = self.actions.is_element_displayed(*self.locators["MENU_SEARCH_ICON"])
            Brand_Icon = self.actions.is_element_displayed(*self.locators["MENU_BRAND_ICON"])
            Watchlist_icon = self.actions.is_element_displayed(*self.locators["MENU_WATCHLIST_ICON"])
            Help_icon = self.actions.is_element_displayed(*self.locators["MENU_HELP_ICON"])
            Signout_icon = self.actions.is_element_displayed(*self.locators["MENU_SIGNOUT"])
            Menu_Bar_items = [Home_Icon, Search_Icon, Brand_Icon, Watchlist_icon, Help_icon, Signout_icon]
           
            if all(Menu_Bar_items):
                return True
            else:
                return False
        elif isinstance(self.actions, iOSActions):
            Home_Icon = self.actions.is_element_displayed(*locators_ipad["MENU_HOME_ICON"])
            Brand_Icon = self.actions.is_element_displayed(*locators_ipad["MENU_BRAND_ICON"])
            Watchlist_icon = self.actions.is_element_displayed(*locators_ipad["MENU_WATCHLIST_ICON"])
            Help_icon = self.actions.is_element_displayed(*locators_ipad["MENU_HELP_ICON"])
            Signout_icon = self.actions.is_element_displayed(*locators_ipad["MENU_SIGNOUT"])
            Menu_Bar_items = [Home_Icon, Brand_Icon, Watchlist_icon, Help_icon, Signout_icon]
            if all(Menu_Bar_items):
                return True
            else:
                return False
        elif isinstance(self.actions, RokuActions):
            self.actions.screenshotAttachment("menu_bar.jpeg")
            self.actions.click_button("Down")
            self.actions.click_button("Left")
            self.actions.click_button("Down")
            # self.actions.is_element_displayed("name", "lSignIn", "Sign in")
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Home", False, "", "", False, "")
            Home_Icon = self.actions.is_text_available(data, "Home")
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Search", False, "", "", False, "")
            Search_Icon = self.actions.is_text_available(data, "Search")
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Brand", False, "", "", False, "")
            Brand_Icon = self.actions.is_text_available(data, "Brand")
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Watchlist", False, "", "", False, "")
            Watch_list = self.actions.is_text_available(data, "Watchlist")
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Help", False, "", "", False, "")
            Help_icon = self.actions.is_text_available(data, "Help")
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Sign out", False, "", "", False, "")
            Signout_icon = self.actions.is_text_available(data, "Sign out")
            self.actions.screenshotAttachment("Signout_icon.jpeg")
            print("Home_Icon", Home_Icon)
            print("Search_Icon", Search_Icon)
            print("Brand_Icon", Brand_Icon)
            print("Help_icon", Help_icon)
            Menu_Bar_items = [Home_Icon, Search_Icon, Brand_Icon, Watch_list, Help_icon, Signout_icon]
            self.actions.screenshotAttachment("Menu_Bar_items.jpeg")
            if all(Menu_Bar_items):
                return True
            else:
                return False
               
    def verify_Search_Field(self):
        if isinstance(self.actions, AndroidActions):  
            print("Verify search field")
            try:
                self.actions.wait_for_element(*self.locators["VIDEO_CONTROLLER"], timeout=15)
            except Exception:
                pass
            for i in range(3):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_LEFT'])
            self.actions.click_button(*self.locators["MENU_SEARCH_ICON"])
            try:
                self.actions.click_button(*self.locators["MENU_SEARCH_ICON"])
            except Exception:
                pass
            print("Search icon is displayed in Homepage")
            return self.actions.is_element_displayed(*self.locators['SEARCH_BOX_FIELD'])
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad["SEARCH_BUTTON"])
            return self.actions.is_element_displayed(*locators_ipad['SEARCH_BOX_FIELD'])
        elif isinstance(self.actions, RokuActions):
            self.actions.screenshotAttachment("Search_Field.jpeg")
            time.sleep(8)
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Left")
            time.sleep(2)
            self.actions.click_button("Up")
            time.sleep(2)
            self.actions.click_button("Up")
            time.sleep(2)
            self.actions.click_button("Up")

            time.sleep(4)
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Search", False, "", "", False, "")
            Search_Icon = self.actions.is_text_available(data, "Search")
            self.actions.screenshotAttachment("Search_Icon.jpeg")
            self.actions.click_button("Select")
            time.sleep(4)
            return Search_Icon
            
    def verify_swimlanes_list_in_homescreen(self):
        try:
            self.actions.wait_for_element(*self.locators["VIDEO_CONTROLLER"], timeout=10)
        except Exception:
            pass
        self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
        Swimlanes_List = self.actions.is_element_displayeds(*self.locators["SWIMLANES_LIST"])
        if Swimlanes_List:
            return self.actions.is_element_displayed(*self.locators['SWIMLANE_FIRST'])
        else:
            return False

    def verify_swimlanes_respective_project(self):
        if isinstance(self.actions, AndroidActions):
            Swimlanes = self.verify_swimlanes_list_in_homescreen()
            if Swimlanes:
                return self.actions.is_element_displayed(*self.locators["PROJECTS_FIRST_SWIMLANES"])
            else:
                return False
        if isinstance(self.actions, str):
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "SWIMLANE 5", False, "", "", False, "")
            swimLane1 = self.actions.is_text_available(data, "SWIMLANE 5")
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "SWIMLANE 6", False, "", "", False, "")
            swimLane2 = self.actions.is_text_available(data, "SWIMLANE 6")
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "SWIMLANE 7", False, "", "", False, "")
            swimLane3 = self.actions.is_text_available(data, "SWIMLANE 7")
            swimLanesSection = [swimLane1, swimLane2, swimLane3]
            if all(swimLanesSection):
                return True
            else:
                return False           
                
    def play_video_for_selected_project(self):
        self.actions.click_button(*self.locators["FIRST_PROJECT_POSTER"])
        self.actions.click_button(*self.locators["PROJECT_START_WATCHING_BUTTON"])
        try:
            self.actions.click_button(*self.locators["PROJECT_START_WATCHING_BUTTON"])
        except Exception:
            pass
        return self.actions.is_element_displayed(*self.locators["VIDEO_CONTROLLER"])

    # def genres_Dropdown(self):
    #     Genre = False
    #     for i in range(20):
    #         try:
    #             self.actions.wait_for_element(*self.locators["GENRES_TAB"], timeout=1)
    #             print("Genres Tab is displayed in Homepage")
    #             Genre = True
    #             break
    #         except Exception:
    #             self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
    #     return Genre

    # def genres_Dropdown_Select(self):
    #     self.actions.click_button(*self.locators["GENRES_TAB"])
    #     try:
    #         self.actions.click_button(*self.locators["GENRES_TAB"])
    #     except Exception:
    #         pass
    #     Genre_Selection = False
    #     for i in range(30):
    #         try:
    #             self.actions.wait_for_element(*self.locators["GENRES_CATEGORY_SELECT"], timeout=0.5)
    #             self.actions.click_button(*self.locators["GENRES_CATEGORY_SELECT"])
    #             Genre_Selection = True
    #             print("Genres Tab is displayed in Homepage")
    #             break
    #         except Exception:
    #             self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
    #     return Genre_Selection

    # def select_genre_content(self, expectedContent):
    #     for i in range(5):
    #         Display_Content = self.actions.validate_text(*self.locators["GENRES_SELECT_DISPLAYED_CONTENT"], expectedContent)
    #         if Display_Content:
    #             self.actions.click_button(*self.locators["GENRES_SELECT_DISPLAYED_CONTENT"])
    #             return Display_Content
    #         else:
    #             self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
    #     return Display_Content

    def click_logout_button(self):
        if isinstance(self.actions, AndroidActions):  
            try:
                self.actions.wait_for_element(*self.locators["VIDEO_CONTROLLER"], timeout=15)
            except Exception:
                pass
            print('what is my driver to do press_keycode===', type(self.driver))
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            time.sleep(2)
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_LEFT'])
            self.actions.click_button(*self.locators["MENU_SIGNOUT"])
            for i in range(2):
                try:
                    self.actions.click_button(*self.locators["MENU_SIGNOUT"])
                except Exception:
                    pass
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad["MENU_SIGNOUT"])
        elif isinstance(self.actions, RokuActions):
            self.actions.screenshotAttachment("click_logout_button.jpeg")
            self.actions.click_button("Down")
            self.actions.click_button("Left")
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            self.actions.click_button("Up")
            self.actions.click_button("Select")
            self.actions.screenshotAttachment("after_ogout_button.jpeg")
                    
    def click_on_help_button(self):
        if isinstance(self.actions, AndroidActions):    
            try:
                self.actions.wait_for_element(*self.locators["VIDEO_CONTROLLER"], timeout=15)
            except Exception:
                pass
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_LEFT'])
            self.actions.click_button(*self.locators["MENU_HELP_ICON"])
            try:
                self.actions.click_button(*self.locators["MENU_HELP_ICON"])
            except Exception:
                pass
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad["MENU_HELP_ICON"])
        elif isinstance(self.actions, RokuActions):
            self.actions.click_button("Left")
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            self.actions.screenshotAttachment("click_help_button.jpeg")
            self.actions.click_button("Select")
            
    def click_on_Brand_button(self):
        if isinstance(self.actions, AndroidActions):    
            try:
                self.actions.wait_for_element(*self.locators["VIDEO_CONTROLLER"], timeout=15)
            except Exception:
                pass
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_LEFT'])
            self.actions.click_button(*self.locators["MENU_BRAND_ICON"])
            try:
                self.actions.click_button(*self.locators["MENU_BRAND_ICON"])
            except Exception:
                pass
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['MENU_BRAND_ICON'])
        elif isinstance(self.actions, RokuActions):
            time.sleep(5)
            self.actions.click_button("Left")
            self.actions.click_button("Down")
            self.actions.click_button("Select")  
            
    def select_project_from_homepage(self):
        try:
            self.actions.wait_for_element(*self.locators["VIDEO_CONTROLLER"], timeout=15)
        except Exception:
            pass
        for i in range(3):
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
        self.actions.click_button(*self.locators["FIRST_PROJECT_POSTER"])
        try:
            self.actions.click_button(*self.locators["FIRST_PROJECT_POSTER"])
        except Exception:
            pass
        return self.actions.is_element_displayed(*self.locators["WATCH_LIST"])

    def verify_Carousel_view(self):
        if isinstance(self.actions, AndroidActions):  
            return self.actions.is_element_displayed(*self.locators["CAROUSEL_IMAGE"])
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad["CAROUSAL_IMAGE"])
        else:
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "pSliderImage", False, "")
            carouselImage = self.actions.is_text_available(data, "pSliderImage")
            return carouselImage

    def verify_header_logo_in_homepage_screen(self, project_description):
        if isinstance(self.actions, AndroidActions):
            self.actions.is_element_displayed(*self.locators["HEADER_LOGO"])
            self.actions.is_element_displayed(*self.locators["PROJECTPOSTER"])
            self.actions.is_element_displayed(*self.locators["PROJECTBANNER"])
            self.actions.is_element_displayed(*self.locators["SEEMOREBUTTON"])
            time.sleep(3)
            project_description = readPreReqJsonValue("prereq", "episode_synopsis")
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
            return self.actions.validate_text_contains(*self.locators["PROJECTDISCRIPTION"], project_description)
        
        else:
            time.sleep(6)
            print("Verify project poster")
            project_poster = self.actions.is_element_displayed("name", "pProjectPoster", "")
            project_banner = self.actions.is_element_displayed("name", "pProjectBanner", "")
            see_more_button = self.actions.is_element_displayed("name", "lSeeMore", "SEE MORE")
            self.actions.click_button("Select")
            time.sleep(2)
            project_description = self.actions.fetch_element_with_parent_name_arrtributes("name", "lEpisodeDescription", "text", readPreReqJsonValue("prereq", "episode_synopsis"))
            self.actions.click_button("Back")
            time.sleep(2)
            Homepage_projects = [project_poster, project_banner, see_more_button, project_description]
            if all(Homepage_projects):
                return True
            else:
                return False

    def verify_pagination_project_listing_page(self):
        if isinstance(self.actions, AndroidActions):
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            return self.actions.is_element_displayed(*self.locators["PAGINATION_PROJECT_LISTING_PAGE"])
        else:
            time.sleep(2)
            time.sleep(2)
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "posterImage", False, "")
            posterImage = self.actions.is_text_available(data, "posterImage")
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "focusedBackgroundImage", False, "")
            image = self.actions.is_text_available(data, "focusedBackgroundImage")
            projectList = [posterImage, image]
            if all(projectList):
                return True
            else:
                return False
            
    def watchList_MenuNotDisplayed(self):
        if isinstance(self.actions, AndroidActions):
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            return self.actions.is_element_displayed(*self.locators["PAGINATION_PROJECT_LISTING_PAGE"])
        else:
            time.sleep(5)
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Left")
            time.sleep(5)
            statusValue = False
            try:
                data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Watchlist", False, "", "", False, "")
                Watch_list = self.actions.is_text_available(data, "Watchlist")
                statusValue = Watch_list
                statusValue = True
            except Exception:
                statusValue = False
            return statusValue
        
    def watchList_ShouldDisplay(self):
        if isinstance(self.actions, AndroidActions):
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            return self.actions.is_element_displayed(*self.locators["PAGINATION_PROJECT_LISTING_PAGE"])
        else:
            time.sleep(5)
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Down")
            time.sleep(2)
            self.actions.click_button("Left")
            time.sleep(5)
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Watchlist", False, "", "", False, "")
            Watch_list = self.actions.is_text_available(data, "Watchlist")
            return Watch_list
        
    def click_first_project(self, brandIndex):
        if isinstance(self.actions, AndroidActions):
            time.sleep(5)
            for i in range(3):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
        elif isinstance(self.actions, RokuActions):
            time.sleep(6)
            brandto_select = int(brandIndex) - 1  # Chosing second brand .. cannot click using brand 
            for i in range(brandto_select):
                self.actions.click_button("Right")  # Chosing second brand .. cannot click using brand 
            self.actions.screenshotAttachment("Brands.jpeg")
            self.actions.click_button("Select")
            print("brand selction doen")
            self.actions.screenshotAttachment("PostBrands.jpeg")
            time.sleep(6)

    def click_second_project(self):
        if isinstance(self.actions, AndroidActions):
            time.sleep(5)
            for i in range(3):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
        else:
            time.sleep(2)
            self.actions.click_button("Right")
            time.sleep(2)
            self.actions.click_button("Select")           
        
    def expiry_date_time(self, Expiry_date_and_time):
        if isinstance(self.actions, AndroidActions):
            return self.actions.validate_text_contains(*self.locators["EXPIRY_ON"], Expiry_date_and_time)
        else:
            time.sleep(6)
            print("Verify expiry date and time")
            expire_date = self.actions.fetch_element(True, "", "", True, "name", "pExpiresBorder", False, "", False, "", True, "name", "lExpiresText", False, "")
            time.sleep(4)
            fetched_expiry_date = self.actions.fetch_data_from_json(expire_date)
            print("access code ----" + fetched_expiry_date) 
            # fetched_expiry_date = self.actions.is_element_displayed("name", "lExpiresText", "EXPIRES ON FEBRUARY 27, 06:00 PM")
            if fetched_expiry_date == readPreReqJsonValue("prereq", "Expiry_date_and_time"):
                self.actions.click_button("Back")
                return True
            else:
                return False
            # return fetched_expiry_date
        
    def remaining_views(self, Expirelabel):
        if isinstance(self.actions, AndroidActions):
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
            return self.actions.validate_text_contains(*self.locators["EXPIRY_ON"], Expirelabel)
        else:
            time.sleep(6)
            print("Verify expiry views")
            # remaining_views = self.actions.fetch_element(True, "", "", True, "name", "pRemainingViewsBorder", False, "", False, "", True, "name", "lRemainingViewsText", False, "")
            # time.sleep(4)
            # fetch_remaining_views = self.actions.fetch_data_from_json(remaining_views)
            # print("access code ----" + fetch_remaining_views) 
            fetch_expiry = self.actions.is_element_displayed("name", "lExpiresText", "")
            self.actions.click_button("Back")
            return fetch_expiry  

    def remaining_views_project(self, Remainingviews):
        if isinstance(self.actions, AndroidActions):
            # self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            # self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            # # self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
            return self.actions.validate_text_contains(*self.locators["REMAINING_VIEW"], Remainingviews)
        else:
            time.sleep(6)
            print("Verify remaining views")
            # remaining_views = self.actions.fetch_element(True, "", "", True, "name", "pRemainingViewsBorder", False, "", False, "", True, "name", "lRemainingViewsText", False, "")
            # time.sleep(4)
            # fetch_remaining_views = self.actions.fetch_data_from_json(remaining_views)
            # print("access code ----" + fetch_remaining_views) 
            fetch_remaining_views = self.actions.is_element_displayed("name", "lRemainingViewsText", "")
            self.actions.click_button("Back")  
            return fetch_remaining_views  

    def watch_now_button(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators["WATCH_BUTTON"])
            for i in range(20):
                time.sleep(20)
            return self.actions.is_element_displayed(*self.locators["REMAINING_VIEW"])
        else:
            time.sleep(6)
            watch_now_button = self.actions.is_element_displayed("name", "titleHidden", "PLAY NOW") 
            return watch_now_button

    def episodic_synopsis(self):
        if isinstance(self.actions, AndroidActions):
            episode_synopsis = readPreReqJsonValue("prereq", "episode_synopsis")
            return self.actions.validate_text_contains(*self.locators["PROJECTDISCRIPTION"], episode_synopsis)
        else:
            time.sleep(6)
            synospys = readPreReqJsonValue("prereq", "Episodic_description")
            synopsis = self.actions.fetch_element(True, "", "", True, "name", "lProjectDescription", False, "", True, synospys, False, "", "", False, "")
            fetch_synopsis = self.actions.fetch_data_from_json(synopsis)
            print("Fetch synopsis===" + fetch_synopsis)
            if fetch_synopsis:
                self.actions.click_button("Back")
                return True
            else:
                return False   

    # def project_poster(self):
    #     if isinstance(self.actions, AndroidActions):
    #         print("Android actions")
    #     else:
    #         time.sleep(6)
    #         print("Verify project poster")
    #         project_poster = self.actions.is_element_displayed("name", "pProjectPoster", "")
    #         return project_poster
        
    def project_banner(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.wait_for_element(*self.locators["VIDEO_CONTROLLER"])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            
        else:
            time.sleep(2)
            print("Verify project banner")
            project_poster = self.actions.is_element_displayed("name", "pProjectBanner", "")
            return project_poster  

    def see_more(self):
        if isinstance(self.actions, AndroidActions):
            print("Android actions")
        else:
            time.sleep(2)
            print("Verify see more button")
            see_more_button = self.actions.is_element_displayed("name", "lSeeMore", "SEE MORE")
            return see_more_button  

    def project_description(self):
        if isinstance(self.actions, AndroidActions):
            print("Android actions")
        else:
            time.sleep(2)
            print("Verify project description")
            self.actions.click_button("Up")
            self.actions.click_button("Select")
            time.sleep(1)
            see_more_button = self.actions.is_element_displayed("name", "lProjectDescription", "This is some project desription")
            return see_more_button  

    def season_number(self):
        if isinstance(self.actions, AndroidActions):
            season = readPreReqJsonValue("prereq", "season_number")
            # seasons = self.actions.wait_for_elements(*self.locators["SEASON_NUMBER"])
            # print('Number of seasons present in the given project :' + str(len(seasons)))
            season_number = self.actions.get_text(*self.locators["SEASON_NUMBER1"])
            if season_number == season:
                return True
            else:
                return False
        else:
            time.sleep(3)
            return True

    def duration_video(self):
        if isinstance(self.actions, AndroidActions):
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            return self.actions.is_element_displayed(*self.locators["VIDEO_DURATION"])
        else:
            time.sleep(2)
            video_duration = self.actions.is_element_displayed("name", "lEpisodeTime", "min")    
            return video_duration   
        
    def episodic_number(self):
        if isinstance(self.actions, AndroidActions):
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            episodic_number = readPreReqJsonValue("prereq", "episodic_name")
            episodic_number = episodic_number.split()[-1]
            Epi_1 = self.actions.get_text(*self.locators["EPISODE_NUMBER"])
            time.sleep(3)
            if Epi_1 == episodic_number:
                return True
            else:
                return False
        else:
            time.sleep(2)
            season_number = self.actions.is_element_displayed("name", "lSeasonNumberStr", readPreReqJsonValue("prereq", "season_number"))
            episodic_number = self.actions.is_element_displayed("name", "lEpisodeTitle", readPreReqJsonValue("prereq", "episodic_name"))
            self.actions.click_button("Back") 
            all_data = [season_number, episodic_number]
            if all(all_data):
                return True
            else:
                return False     

    def mulitiple_episodes(self):
        if isinstance(self.actions, AndroidActions):
            return self.actions.is_element_displayed(*self.locators["MULTIPLE_EPISODES"])
        else:
            time.sleep(6)
            first_episode = self.actions.fetch_element(True, "", "", True, "name", "episodeTitle", False, "", True, readPreReqJsonValue("prereq", "multiple_episodic_one"), True, "index", "1", False, "") 
            fetch_first_episode = self.actions.fetch_data_from_json(first_episode)
            # print("Fetch synopsis===" + fetch_first_episode)
            second_episode = self.actions.fetch_element(True, "", "", True, "name", "episodeTitle", False, "", True, readPreReqJsonValue("prereq", "multiple_episodic_two"), True, "index", "1", False, "") 
            fetch_second_episode = self.actions.fetch_data_from_json(second_episode)
            # print("Fetch synopsis===" + fetch_second_episode)
            mulitiple_episodes = [fetch_first_episode, fetch_second_episode]
            if all(mulitiple_episodes):
                return True
            else:
                return False
            
    def remaining_views_count(self):
        if isinstance(self.actions, AndroidActions):
            print("Android actions")
        else:
            time.sleep(2)
            remaining_views = self.actions.fetch_element_with_parent_name_arrtributes("name", "pRemainingViewsBorder", "name", "lRemainingViewsText")
            fetch_element = self.actions.fetch_data_from_json(remaining_views)
            print("fetched element==" + fetch_element)
            out_string = ""
            for i in fetch_element:
                if i.isdigit():
                    out_string += i
            print("Number==" + out_string)
            return out_string
            
    def click_authenticate_button(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators["AUTHEN_PLAYBUTTON"])
        else:
            time.sleep(2)
            self.actions.click_button("Select")
            
    def enter_password_and_authenticate(self, password):
        if isinstance(self.actions, AndroidActions):
            print('Inside enter pass fn')
            Enter_element = self.actions.wait_for_element(*self.locators["ENTER_PASSWORD"])
            print(Enter_element)
            time.sleep(3)
            self.actions.enter_text(*self.locators["ENTER_PASSWORD"], password)
            time.sleep(2)
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.actions.click_button(*self.locators["ENTER_PASSWORD_BUTTON"])     
        else:   
            time.sleep(2)
            print("Enter password")
            self.actions.click_button("Select")
            time.sleep(2)
            self.actions.doRokuSendKeys(password)
            self.actions.click_button("Enter")
            time.sleep(2)
            self.actions.click_button("Select")

    def enter_invalid_password_and_authenticate(self, invalid_password):
        if isinstance(self.actions, AndroidActions):
            self.actions.is_element_displayed(*self.locators["ENTER_PASSWORD"])
            self.actions.enter_text(*self.locators["ENTER_PASSWORD"], invalid_password)
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
        else:   
            time.sleep(2)
            print("Enter password")
            self.actions.click_button("Select")
            time.sleep(2)
            self.actions.doRokuSendKeys(invalid_password)
            self.actions.click_button("Enter")
            time.sleep(10)
            self.actions.click_button("Select")
            time.sleep(1)
            self.actions.click_button("Back")
            time.sleep(1)
            self.actions.click_button("Select")
            time.sleep(2)
            self.actions.click_button("Select")
            time.sleep(2)
            self.actions.doRokuSendKeys(invalid_password)
            self.actions.click_button("Enter")
            time.sleep(10)
            self.actions.click_button("Select")
            time.sleep(2)

    def enter_invalid_password_and_authenticate_OTP(self, invalid_password_error_message):
        if isinstance(self.actions, AndroidActions):
            return self.actions.validate_text_contains(*self.locators["INVALID_ERROR_MESSAGE"], invalid_password_error_message)
            
        else:   
            time.sleep(2)
            print("Enter password")
            self.actions.click_button("Select")
            time.sleep(2)
            self.actions.doRokuSendKeys(readPreReqJsonValue("prereq", "invalid_pin"))
            self.actions.click_button("Enter")
            time.sleep(2)
            self.actions.click_button("Select")
            time.sleep(2)
            remaining_views = self.actions.fetch_element_with_parent_name_arrtributes("name", "lErrorMessage", "text", "Authentication failed. The verification code that you entered is incorrect.")
            fetch_element = self.actions.fetch_data_from_json(remaining_views)
            print("fetched element==" + fetch_element)   
            self.actions.click_button("Back")
            self.actions.click_button("Back")
            return fetch_element     
                
    def verify_successfull_playback(self, remaining_views):
        if isinstance(self.actions, AndroidActions):
            print('inside play function')
            self.actions.wait_for_element(*self.locators["VIDEO_CONTROLLER"], timeout=8)
            for i in range(20):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
                # self.actions.click_button(*self.locators['"BTN_FORWARD"'])
                time.sleep(20)
                project_discription = readPreReqJsonValue("prereq", "episode_synopsis")
                Home_page = self.actions.validate_text_contains(*self.locators["PROJECTDISCRIPTION"], project_discription)
                print(Home_page)
                if Home_page:
                    return True
                else:
                    pass
            return False
        if isinstance(self.actions, RokuActions): 
            time.sleep(6) 
            self.actions.screenshotAttachment("cinema_video_paying.jpeg")
            self.actions.click_button("Back")
            time.sleep(4)
            self.actions.screenshotAttachment("cinema_video_back.jpeg")
            # remaining_views = self.actions.fetch_element_with_parent_name_arrtributes("name", "pRemainingViewsBorder", "name", "lRemainingViewsText")
            # fetch_element = self.actions.fetch_data_from_json(remaining_views)
            fetch_element = self.actions.fetch_Data("lRemainingViewsText", "REMAINING VIEWS")
            print("fetched element==" + fetch_element)
            out_string = ""
            for i in fetch_element:
                if i.isdigit():
                    out_string += i
            print("Number==" + out_string)
            remaining_views_after_playback = int(out_string)
            remaining_views_before_playback = int(remaining_views)
            print(remaining_views_after_playback)
            print(remaining_views_before_playback)
            self.actions.screenshotAttachment("remainignCount_chek.jpeg")
            if remaining_views_before_playback > remaining_views_after_playback:
                print('Remaining view count is decreased as expected')
                self.actions.click_button("Back")
                return True
            else:
                print('Remaining view count is not decreased after playback')
                return False
            
    def verify_error_message_playback(self, invalid_password_error_message):
        if isinstance(self.actions, AndroidActions):
            return self.actions.validate_text_contains(*self.locators['INVALID_ERROR_MESSAGE'], invalid_password_error_message)
        elif isinstance(self.actions, RokuActions):  
            self.actions.screenshotAttachment("error_message.jpeg")
            error_message = self.actions.fetch_element(True, "", "", True, "name", "gPasswordGrp", False, "", True, "incorrect_password", True, "index", "1", False, "")
            self.actions.is_text_available(error_message, invalid_password_error_message)
            # remaining_views = self.actions.fetch_element_with_parent_name_arrtributes("name", "lErrorMessage", "index", "1")
            # fetch_element = self.actions.fetch_data_from_json(remaining_views)
            self.actions.click_button("Back")
            return True
        
    def enter_phone_number(self, phone_number):
        if isinstance(self.actions, AndroidActions):
            self.actions.enter_text(*self.locators["ENTER_PASSWORD"], phone_number)
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
        elif isinstance(self.actions, RokuActions):  
            self.actions.screenshotAttachment("enter_phone_number.jpeg")
            # self.actions.click_button("Select")
            # time.sleep(3)
            # print("Select country")
            # for i in range(110):
            #     self.actions.click_button("Down")
            # time.sleep(2)        
            # self.actions.click_button("Select")
            time.sleep(2)
            self.actions.click_button("Right")
            print("Select country")
            time.sleep(2)
            self.actions.click_button("Select")
            time.sleep(1)
            self.actions.doRokuSendKeys(phone_number)
            time.sleep(2)
            self.actions.click_button("Enter")  

    def enter_otp(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.enter_text(*self.locators["OPT_NUMBER"], "1234")
            self.actions.click_button(*self.locators["ENTER_OTP"])
            
        else: 
            self.actions.click_button("Down")
            time.sleep(3)
            self.actions.doRokuSendKeys("1234")
            self.actions.click_button("Enter")
            self.actions.click_button("Select")

    def verify_error_message_invalid_otp(self, invalid_password_error_message):
        if isinstance(self.actions, AndroidActions):
            print("Android actions")
        else:   
            error_message = self.actions.fetch_element(True, "", "", True, "name", "lErrorMessage", False, "", True, "Authentication failed. The verification code that you entered is incorrect.", True, "index", "1", False, "")
            fetched_element = self.actions.is_text_available(error_message, invalid_password_error_message)
            return fetched_element        
