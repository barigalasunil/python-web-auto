from appium.webdriver.common.appiumby import AppiumBy

from conftest import readConstants
from pages.actions.android_actions import AndroidActions
from pages.actions.ios_actions import iOSActions
from pages.base_page import BasePage
import time


locators_ipad = {
    "SEARCH_BOX_FIELD": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "{search_content}"`]'),
    "KEYBOARD_SEARCH_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Search"`]'),
    "SEARCH_RESULTS_HEADER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "SEARCH RESULTS"`]'),
    "SEARCH_RESULTS_PAGINATION": (AppiumBy.CLASS_NAME, 'XCUIElementTypeCell'),
    "SEARCH_RESULTS_PROJECT_INFO": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name contains "{project_name}"`]'),
    "NO_RESULT_ICON": (AppiumBy.ACCESSIBILITY_ID, 'warning'),
    "NO_RESULT_FOUND_HEADER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "No Titles Available"`]'),
    "NO_RESULT_TEXT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "No titles are available in this genre."`]'),
    "SEARCH_RESULTS_FIRST_PROJECT": (AppiumBy.XPATH, '//XCUIElementTypeCell/XCUIElementTypeStaticText[1]'),
    "VIDEOS_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Videos"`]'),
    "DETAILS_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Details"`]'),
    "ADD_TO_WATCHLIST_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == " Add to Watchlist"`]'),
    "REMOVE_FROM_WATCHLIST": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == " Remove from Watchlist"`]'),
    "PROJECT_SYNOPSIS": (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeStaticText[2]'),
    "VIDEOS_SYNOPSIS": (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[2]'),
    "AIR_DATE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Airdate"`]'),
    "AIR_DATE_VALUE": (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[4]'),
    "VIDEOS_PAGINATION": (AppiumBy.CLASS_NAME, 'XCUIElementTypeCollectionView'),
    "VIDEOS_POSTER_IMAGE": (AppiumBy.XPATH, '//XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage'),
    "EXPIRY_LABEL": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Expires on: "`]'),
    "REMAINING_VIEWS": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Remaining Views:"`]'),
    "VIDEO_NAME": (AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[1]'),  # noqa:E501
    "EXPIRY_VALUE": (AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[3]'),    # noqa:E501
    "REMAINING_VIEWS_VALUE": (AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[5]'),  # noqa:E501
    "DETAILS_POSTER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage'),  # noqa:E501
    "DETAILS_TAB_PROJECT": (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeStaticText[1]'),
    "CASTANDCREW_TITLE_PROJECT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "Cast and Crew"`]'),
    "CAST_VALUE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "{cast_value}"`]'),
    "CREW_VALUE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "{crew_value}"`]'),
    "VIDEO_CONTROLLER": (AppiumBy.ACCESSIBILITY_ID, 'Play/Pause')
}


class SearchPage_Cinema(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        package_name = readConstants("current_app_package")

        locators_temp = {
            "SEARCH_BOX_FIELD": (AppiumBy.ID, f'{package_name}:id/txt_search'),
            "SEARCH_RESULTS_HEADER": (AppiumBy.ID, f'{package_name}:id/row_header'),
            "SEARCH_RESULTS_PAGINATION": (AppiumBy.ACCESSIBILITY_ID, 'Search Results'),
            "SEARCH_RESULTS_PROJECT_INFO": (AppiumBy.ID, 'com.indee.gd:id/title_text'),
            "NO_RESULT_ICON": (AppiumBy.ID, 'com.indee.gd:id/iv_es'),
            "NO_RESULT_FOUND_HEADER": (AppiumBy.ID, 'com.indee.gd:id/txt_title'),
            "SEARCH_RESULTS_FIRST_PROJECT": (AppiumBy.ID, f'{package_name}:id/title_text'),
            "NO_RESULT_TEXT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").textContains("Please select another genre")'),
            "REMAINING_VIEWS_CONTENT": (AppiumBy.ID, f'{package_name}:id/txt_detail_remaining_view'),
            "REMAINING_VIEWS_COUNT": (AppiumBy.ID, f"{package_name}:id/txt_detail_card_views"),
            "PROJECT_START_WATCHING_BUTTON": (AppiumBy.ID, 'com.indee.gd:id/rv_seemore'),
            "AIR_DATE_TITLE": (AppiumBy.ID, f'{package_name}:id/txt_air_date_title'),
            "AIR_DATE_VALUE": (AppiumBy.ID, f'{package_name}:id/txt_air_date'),
            "AIR_DATE_NOTDISPLAY": (AppiumBy.ID, f'{package_name}:id/txt_air_date'),
            "FIRST_VIDEO": (AppiumBy.ID, f'{package_name}:id/ivScImage'),
            "PROJECT_SYNOPSIS": (AppiumBy.ID, f'{package_name}:id/ivScImage'),
            "DETAILS_TAB_PROJECT": (AppiumBy.ID, f'{package_name}:id/txt_detail_title'),
            "CASTANDCREW_TITLE_PROJECT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Cast and Crew']"),
            "CAST_VALUE": (AppiumBy.ID, f'{package_name}:id/sm_tv_character'),
            "CAST_VALUE2": (AppiumBy.ID, f'{package_name}:id/sm_tv_original'),
            "VIDOE_SYNOPSIS": (AppiumBy.ID, f'{package_name}:id/img_playnow_popup'),
            "DETAILS_BTN": (AppiumBy.ID, f'{package_name}:id/btn_details'),
            "VIDEOS_BTN": (AppiumBy.ID, f'{package_name}:id/btn_videos'),
            "VIDEOS_PAGINATION": (AppiumBy.ID, f'{package_name}:id/row_content'),
            "VIDEO_POSTER": (AppiumBy.ID, f'{package_name}:id/scHolder'),
            "PLAY_BUTTON": (AppiumBy.ID, f'{package_name}:id/btn_detail_playnow'),
            "VIDEO_NAME": (AppiumBy.ID, f'{package_name}:id/tvTitle'),
            "EXPIRY_LABEL": (AppiumBy.ID, f'{package_name}:id/txt_detail_expiry'),
            "EXPIRY_DATE_AND_TIME": (AppiumBy.ID, f'{package_name}:id/txt_detail_card_expiry'),
            "DETAILS_POSTER": (AppiumBy.ID, f'{package_name}:id/img_playnow_popup'),
            "DETAILS_LAYOUT": (AppiumBy.ID, f'{package_name}:id/layout_scrollview'),
            "VIDEO_CONTROLLER": (AppiumBy.ID, 'com.indee.gd:id/llController'),
            "PLAY_BUTTON_VERIFY": (AppiumBy.ID, f'{package_name}:id/ivScPlay'),
            "CAST_AND_CREW": (AppiumBy.ID, f'{package_name}:id/tvCastCrew')  
        }
        self.locators = locators_temp
        print("modied locator ====", self.locators)


    def enter_Text_In_Search_Field(self, Searchcontent):
        if isinstance(self.actions, AndroidActions):
            try:
                self.actions.wait_for_element(*self.locators['REMAINING_VIEWS_COUNT'], timeout=2)
            except Exception:
                pass
                self.actions.enter_text(*self.locators['SEARCH_BOX_FIELD'], Searchcontent)
        elif isinstance(self.actions, iOSActions):
            enter_text = "Search for a title..."
            by, value = locators_ipad["SEARCH_BOX_FIELD"]
            default_format_value = value.format(search_content=enter_text)
            search_content_validation = value.format(search_content=Searchcontent)
            Search_box = self.driver.find_element(by, default_format_value)
            print(Search_box)
            Search_box.click()
            Search_box.clear()
            Search_box.send_keys(Searchcontent)
            print('Entered text value')
            Text_Entered = self.actions.validate_text_contains(by, search_content_validation, Searchcontent)
            print(Text_Entered)
            return Text_Entered
        else:
            time.sleep(4)
            self.actions.click_button("Select")
            time.sleep(4)
            print("check name", Searchcontent)
            self.actions.doRokuSendKeys(Searchcontent)
            time.sleep(3)
            for i in range(4):
                self.actions.click_button("Down")
                time.sleep(3)
            time.sleep(3)    
            self.actions.click_button("Select") 
            time.sleep(3) 
            self.actions.click_button("Down")
            self.actions.click_button("Select")
             
    def submit_Search_Button(self):
        if isinstance(self.actions, AndroidActions):
            try:
                self.actions.wait_for_element(*self.locators['REMAINING_VIEWS_COUNT'], timeout=1)
            except Exception:
                pass
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_CENTER'])
                for i in range(4):
                    self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_RIGHT'])
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
        elif isinstance(self.actions, iOSActions):
            try:
                self.actions.click_button(*locators_ipad['KEYBOARD_SEARCH_BUTTON'])
            except Exception:
                pass
        else:
            print("handled in search method itself")
            
    def search_Results(self):
        self.actions.is_element_displayed(*self.locators['SEARCH_RESULTS_FIRST_PROJECT'])

    def verify_Search_Content(self, searchContent):
        if isinstance(self.actions, AndroidActions):
            Search_Project = self.actions.validate_text_contains(*self.locators['SEARCH_RESULTS_FIRST_PROJECT'], searchContent)
            return Search_Project
        elif isinstance(self.actions, iOSActions):
            by, value = locators_ipad["SEARCH_RESULTS_PROJECT_INFO"]
            format_value = value.format(project_name=searchContent)
            Search_Project = self.actions.validate_text_contains(by, format_value, searchContent)
            return Search_Project
        else:
            time.sleep(6)
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "NonEpisodic01ZAEHKBDMOK", False, "", "", False, "")
            content_Name = self.actions.is_text_available(data, "NonEpisodic01ZAEHKBDMOK")
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Add to Watchlist", False, "", "", False, "")
            add_To_WatchList = self.actions.is_text_available(data, "Add to Watchlist")
            content_Items = [content_Name, add_To_WatchList]
            if all(content_Items):
                return True
            else:
                return False
            
    def pagination_Call_Search_Field(self):
        if isinstance(self.actions, AndroidActions):
            return self.actions.is_element_displayed(*self.locators['SEARCH_RESULTS_PAGINATION'])
        elif isinstance(self.actions, iOSActions):
            No_results = self.actions.is_element_displayed(*locators_ipad['NO_RESULT_ICON'])
            print(No_results)
            if No_results:
                print('No Projects Available for the entered seach text')
                return False
            else:
                return self.actions.is_element_displayed(*locators_ipad['SEARCH_RESULTS_PAGINATION'])
        else:
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Add to Watchlist", False, "", "", False, "")
            paginationCall = self.actions.is_text_available(data, "Add to Watchlist")
            return paginationCall

    def maximum_Count_Verification(self, Searchcontent):
        if isinstance(self.actions, AndroidActions):
            self.actions.enter_text(*self.locators['MENU_SEARCH_ICON'], Searchcontent)
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
            return self.actions.is_element_displayed(*self.locators['REMAINING_VIEWS_CONTENT'])
        else:
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "mslRemainingViews", False, "")
            remainingViews = self.actions.is_text_available(data, "mslRemainingViews")
            return remainingViews
    
    def maximum_Count_Video_Redirection(self, Count):
        for i in range(3):
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
        Element = self.driver.find_element(*self.locators['REMAINING_VIEWS_COUNT'])
        ViewsCount = Element.get_attribute("text")
        print(ViewsCount)
        if int(ViewsCount) > int(Count):
            self.actions.click_button(*self.locators['PROJECT_START_WATCHING_BUTTON'])
            return True
        else:
            return False

    def click_OnProjectResult(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['SEARCH_RESULTS_FIRST_PROJECT'])
            time.sleep(2)
            Project_navigation = self.actions.is_element_displayed(*self.locators['VIDEOS_BTN'])
            if Project_navigation:
                pass
            else:
                self.actions.click_button(*self.locators['SEARCH_RESULTS_FIRST_PROJECT'])
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['SEARCH_RESULTS_FIRST_PROJECT'])
        else:
            pass
            #self.doRokuKeyEvents("Down")
            #self.doRokuKeyEvents("Select")

    def click_OnVideoInsideProject(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['FIRST_VIDEO'])
            try:
                self.actions.click_button(*self.locators['FIRST_VIDEO'])
            except Exception:
                pass
        else:
            try:
                time.sleep(3)
                self.actions.click_button("Down")
                self.actions.click_button("Down")
                self.actions.click_button("Down")
                self.actions.click_button("Select")
                time.sleep(3)
            except Exception:
                print("Handled Exception")
             
    def click_on_project_video(self):
        self.actions.click_button(*self.locators['PLAY_BUTTON'])
        try:
            self.actions.click_button(*self.locators['PLAY_BUTTON'])
        except Exception:
            pass

    def airDate_Should_Not_Display(self):
        if isinstance(self.actions, AndroidActions):
            statusValue = False
            try:
                self.actions.is_element_displayed(*self.locators['AIR_DATE_NOTDISPLAY'])
                statusValue = True
            except Exception:
                statusValue = False
            return statusValue
        elif isinstance(self.actions, iOSActions):
            statusValue = False
            try:
                self.actions.is_element_displayed(*locators_ipad['AIR_DATE'])
                statusValue = True
            except Exception:
                statusValue = False
            return statusValue
        else:
            statusValue = False
            try:
                data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Original Air Date", False, "", "", False, "")
                original_AirDateLabel = self.actions.is_text_available(data, "Original Air Date")
                statusValue = original_AirDateLabel
                statusValue = True
            except Exception:
                statusValue = False
            return statusValue
            
    def verify_AirDate_Value(self, air_date_value):
        if isinstance(self.actions, AndroidActions):
            self.actions.is_element_displayed(*self.locators['AIR_DATE_TITLE'])
            return self.actions.validate_text(*self.locators['AIR_DATE_VALUE'], air_date_value)
        elif isinstance(self.actions, iOSActions):
            self.actions.is_element_displayed(*locators_ipad["AIR_DATE"])
            return self.actions.validate_text_contains(*locators_ipad['AIR_DATE_VALUE'], air_date_value)
        else:
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Original Air Date", False, "", "", False, "")
            original_AirDateLabel = self.actions.is_text_available(data, "Original Air Date")
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, air_date_value, False, "", "", False, "")
            air_Date_Value = self.actions.is_text_available(data, air_date_value)
            air_Date_Values = [original_AirDateLabel, air_Date_Value]
            if all(air_Date_Values):
                return True
            else:
                return False

    def click_DetailsTab_Project(self):
        if isinstance(self.actions, AndroidActions):
            try:
                self.actions.is_element_displayed(*self.locators['REMAINING_VIEWS_COUNT'], timeout=3)
            except Exception:
                pass
            self.actions.click_button(*self.locators['DETAILS_BTN'])
            try:
                self.actions.click_button(*self.locators['DETAILS_BTN'])
                Details_Poster = self.actions.is_element_displayed(*self.locators['DETAILS_POSTER'])
                if Details_Poster:
                    print('Details poster reached')
                    pass
            except Exception:
                print("inside exception")
            for i in range(2):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad["DETAILS_BUTTON"])
        else:
            time.sleep(4)
            self.actions.click_button("Down")    
            self.actions.click_button("Right")
            time.sleep(4)
            
    def click_videos_tab_project(self):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['VIDEOS_BTN'])
            try:
                self.actions.click_button(*self.locators['VIDEOS_BTN'])
            except Exception:
                pass
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['VIDEOS_BUTTON'])
        else:
            pass
        
    def verify_Cast_Crew_Title_Displayed(self, Cast, Crew):
        if isinstance(self.actions, AndroidActions):
            # self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            # self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
            # return self.actions.is_element_displayed(*self.locators["CAST_AND_CREW"])
            self.actions.is_element_displayed(*self.locators['CASTANDCREW_TITLE_PROJECT'])       
            cast = self.actions.validate_text_contains(*self.locators['CAST_VALUE'], Cast)
            print(cast)
            crew = self.actions.validate_text_contains(*self.locators['CAST_VALUE2'], Crew)
            print(crew)
            Cast_And_Crew_Details = [cast, crew]
            if all(Cast_And_Crew_Details):
                return True
            else:
                return False
        elif isinstance(self.actions, iOSActions):
            print("ios actions")
            # self.actions.swipe()
            # Cast_And_Crew_Title = self.actions.is_element_displayed(*locators_ipad['CASTANDCREW_TITLE_PROJECT'])
            # by, value = locators_ipad["CAST_VALUE"]
            # format_value = value.format(cast_value=castValue)
            # Cast = self.actions.validate_text(by, format_value, castValue)
            # by, value = locators_ipad["CREW_VALUE"]
            # format_value = value.format(crew_value=crewValue)
            # Crew = self.actions.validate_text(by, format_value, crewValue)
            # Cast_And_Crew_Details = [Cast_And_Crew_Title, Cast, Crew]
            # if all(Cast_And_Crew_Details):
            #     return True
            # else:
            #     return False
        else:
            time.sleep(3)
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, Cast, False, "", "", False, "")
            crew_Details = self.actions.fetch_data_from_json(data) 
            print("cast details===" + crew_Details)  
            data2 = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, Crew, False, "", "", False, "")
            cast_Details = self.actions.fetch_data_from_json(data2)
            print("crew details===" + crew_Details)  
            castAndCrewDetails = [crew_Details, cast_Details]
            if all(castAndCrewDetails):
                self.actions.click_button("Back")
                return True
            else:
                return False
                            
    def verify_Project_Synopsis_Information(self):
        if isinstance(self.actions, AndroidActions):
            statusValue = self.actions.is_element_displayed(*self.locators['PROJECT_SYNOPSIS'])
            return statusValue
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad['PROJECT_SYNOPSIS'])

    def verify_Video_Synopsis_Information(self):
        if isinstance(self.actions, AndroidActions):
            statusValue = self.actions.is_element_displayed(*self.locators['VIDOE_SYNOPSIS'])
            return statusValue
        elif isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad['VIDEOS_SYNOPSIS'])
 
    def verify_video_tab_contents_in_project(self):
        if isinstance(self.actions, AndroidActions):
            try:
                self.actions.wait_for_element(*self.locators['SEARCH_RESULTS_HEADER'], timeout=3)
            except Exception:
                pass
            for i in range(2):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            Videos_Pagination = self.actions.is_element_displayed(*self.locators['VIDEOS_PAGINATION'])
            Video_Poster = self.actions.is_element_displayed(*self.locators['VIDEO_POSTER'])
            Play_Button = self.actions.is_element_displayed(*self.locators['PLAY_BUTTON'],)
            Name = self.actions.is_element_displayed(*self.locators['VIDEO_NAME'],)
            Expiry = self.actions.is_element_displayed(*self.locators['EXPIRY_LABEL'],)
            Remaining_Views = self.actions.is_element_displayed(*self.locators['REMAINING_VIEWS_CONTENT'],)
            Video_Tab_Elements = [Videos_Pagination, Video_Poster, Play_Button, Name, Expiry, Remaining_Views]
            print(Video_Tab_Elements)
            if all(Video_Tab_Elements):
                return True
            else:
                return False
        elif isinstance(self.actions, iOSActions):
            self.actions.swipe()
            Videos_Pagination = self.actions.is_element_displayed(*locators_ipad['VIDEOS_PAGINATION'])
            Video_Poster = self.actions.is_element_displayed(*locators_ipad['VIDEOS_POSTER_IMAGE'])
            Name = self.actions.is_element_displayed(*locators_ipad['VIDEO_NAME'])
            Expiry = self.actions.is_element_displayed(*locators_ipad['EXPIRY_LABEL'])
            Remaining_Views = self.actions.is_element_displayed(*locators_ipad['REMAINING_VIEWS'])
            Video_Tab_Elements = [Videos_Pagination, Video_Poster, Name, Expiry, Remaining_Views]
            if all(Video_Tab_Elements):
                return True
            else:
                return False
        else:
            time.sleep(9)
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "mslExpiresOn", False, "")
            expiresOn = self.actions.is_text_available(data, "mslExpiresOn")
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "mslRemainingViews", False, "")
            remainingViews = self.actions.is_text_available(data, "mslRemainingViews")
            Video_Tab_Elements = [expiresOn, remainingViews]
            if all(Video_Tab_Elements):
                return True
            else:
                return False
            
    def verify_details_tab_contents_in_project(self, projectName, projectDescription):
        if isinstance(self.actions, AndroidActions):
            Details_Poster = self.actions.is_element_displayed(*self.locators['DETAILS_POSTER'])
            Details_Layout = self.actions.is_element_displayed(*self.locators['DETAILS_LAYOUT'])
            Synopses = self.actions.is_element_displayed(*self.locators['PROJECT_SYNOPSIS'])
            Header_Text = self.actions.is_element_displayed(*self.locators['DETAILS_TAB_PROJECT'])
            Cast_And_Crew = self.actions.is_element_displayed(*self.locators['CASTANDCREW_TITLE_PROJECT'])
            Details_Tab_Elements = [Details_Poster, Details_Layout, Synopses, Header_Text, Cast_And_Crew]
            if all(Details_Tab_Elements):
                return True
            else:
                return False
        elif isinstance(self.actions, iOSActions):
            Details_Poster = self.actions.is_element_displayed(*locators_ipad['DETAILS_POSTER'])
            Synopses = self.actions.is_element_displayed(*locators_ipad['PROJECT_SYNOPSIS'])
            Header_Text = self.actions.is_element_displayed(*locators_ipad['DETAILS_TAB_PROJECT'])
            self.actions.swipe()
            Cast_And_Crew = self.actions.is_element_displayed(*locators_ipad['CASTANDCREW_TITLE_PROJECT'])
            Details_Tab_Elements = [Details_Poster, Synopses, Header_Text, Cast_And_Crew]
            if all(Details_Tab_Elements):
                return True
            else:
                return False
        else:
            time.sleep(4)
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, projectDescription, False, "", "", False, "")
            description = self.actions.is_text_available(data, projectDescription)
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, projectName, False, "", "", False, "")
            projectTitle = self.actions.is_text_available(data, projectName)
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Cast and Crew", False, "", "", False, "")
            castAndCrew = self.actions.is_text_available(data, "Cast and Crew")
            Details_Tab_Elements = [description, projectTitle, castAndCrew]
            if all(Details_Tab_Elements):
                return True
            else:
                return False

    # def click_on_start_watching_button(self):
    #     try:
    #         self.actions.wait_for_element(*self.locators['SEARCH_RESULTS_HEADER'], timeout=3)
    #     except Exception:
    #         pass
    #     self.actions.click_button(*self.locators['PROJECT_START_WATCHING_BUTTON'])
    #     for i in range(5):
    #         try:
    #             self.actions.tap(*self.locators['PROJECT_START_WATCHING_BUTTON'])
    #             Video_Controller = self.actions.is_element_displayed(*self.locators['VIDEO_CONTROLLER'])
    #             if Video_Controller:
    #                 return True
    #         except Exception:
    #             pass
    #         self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
    #         try:
    #             Video_Controller = self.actions.is_element_displayed(*self.locators['VIDEO_CONTROLLER'])
    #             if Video_Controller:
    #                 return True
    #         except Exception:
    #             pass
    #     return False
    
    def Expiry_label_with_date_and_time(self, Expiry_label, Remaining_Views):
        if isinstance(self.actions, AndroidActions):
            for i in range(2):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            Expiry_Label = self.actions.is_element_displayed(*self.locators['EXPIRY_LABEL'])
            Expiry_Date_and_time = self.actions.is_element_displayed(*self.locators['EXPIRY_DATE_AND_TIME'])
            if all([Expiry_Label, Expiry_Date_and_time]):
                return True
            else:
                return False
        elif isinstance(self.actions, iOSActions):
            self.actions.swipe()
            Expiry_Label = self.actions.is_element_displayed(*locators_ipad['EXPIRY_LABEL'])
            Expiry_Date_and_time = self.actions.is_element_displayed(*locators_ipad['EXPIRY_VALUE'])
            if all([Expiry_Label, Expiry_Date_and_time]):
                return True
            else:
                return False
        else:
            time.sleep(4)
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            time.sleep(4)
            self.actions.click_button("Select")    
            time.sleep(4)
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, Expiry_label, False, "", "", False, "")
            expireDateAndTime = self.actions.is_text_available(data, Expiry_label)
            data = self.actions.fetch_element(False, "", "", False, "", "", False, "", False, "", True, "name", "mslRemainingViews", False, "")
            remaining_Views = self.actions.is_text_available(data, "mslRemainingViews")
            expiryLabelAndRemainingView = [expireDateAndTime, remaining_Views]
            if all(expiryLabelAndRemainingView):
                return True
            else:
                return False
            
    def verify_no_projects_displayed(self):
        if isinstance(self.actions, AndroidActions):
            no_results_icon = self.actions.is_element_displayed(*self.locators['NO_RESULT_ICON'])
            no_results_text = self.actions.is_element_displayed(*self.locators['NO_RESULT_FOUND_HEADER'])
            if all([no_results_icon, no_results_text]):
                return True
            else:
                return False
        elif isinstance(self.actions, iOSActions):
            no_results_icon = self.actions.is_element_displayed(*locators_ipad['NO_RESULT_ICON'])
            no_results_text = self.actions.is_element_displayed(*locators_ipad['NO_RESULT_FOUND_HEADER'])
            if all([no_results_icon, no_results_text]):
                return True
            else:
                return False
