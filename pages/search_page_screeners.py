from appium.webdriver.common.appiumby import AppiumBy

from pages.actions.android_actions import AndroidActions
from pages.actions.ios_actions import iOSActions
from pages.actions.roku_actions import RokuActions
from pages.homepage_screener import HomePageScreener
from datetime import datetime
import time
from pages.base_page import BasePage
from conftest import readPreReqJsonValue,  readConstants


locators_ipad = {
    "SEARCH_BOX_FIELD": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "{search_content}"`]'),
    "KEYBOARD_SEARCH_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Search"`]'),
    "SEARCH_RESULTS_HEADER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "SEARCH RESULTS"`]'),
    "SEARCH_RESULTS_PAGINATION": (AppiumBy.CLASS_NAME, 'XCUIElementTypeCell'),
    "SEARCH_RESULTS_PROJECT_INFO": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name contains "{project_name}"`]'),
    "NO_RESULT_ICON": (AppiumBy.ACCESSIBILITY_ID, 'warning'),
    "NO_RESULT_FOUND_HEADER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "No Titles Available"`]'),
    "NO_RESULT_TEXT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "No titles are available in this genre."`]'),
    "SEARCH_RESULTS_FIRST_PROJECT": (AppiumBy.XPATH, '//XCUIElementTypeCell/XCUIElementTypeStaticText'),
    "DETAILS_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Details"`]'),
    "VIDEOS_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Videos"`]'),
    "PROJECT_SYNOPSIS": (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]'),
    "CASTANDCREW_TITLE_PROJECT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "Cast and Crew"`]'),
    "CAST_VALUE": (AppiumBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]'),
    "CREW_VALUE": (AppiumBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[2]'),
    "FIRST_VIDEO": (AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]'),
    "VIDOE_SYNOPSIS": (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[2]'),
    "AIR_DATE_TITLE": (AppiumBy.ACCESSIBILITY_ID, 'Airdate'),
    "AIR_DATE_VALUE": (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[4]'),
    "VIDEOS_PAGINATION": (AppiumBy.CLASS_NAME, 'XCUIElementTypeCollectionView'),
    "VIDEO_POSTER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage[1]'),   # noqa:E501
    "VIDEO_TAB_2FA_LABEL": (AppiumBy.ACCESSIBILITY_ID, '2FA_img'),
    "VIDEO_NAME": (AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[1]'),  # noqa:E501
    "EXPIRY_LABEL": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Expires on: "`][1]'),
    "REMAINING_VIEWS_CONTENT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Remaining Views:"`][1]'),
    "DETAILS_POSTER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage'),   # noqa:E501
    "DETAILS_LAYOUT": (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]'),
    "DETAILS_TAB_PROJECT": (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[1]'),
    "REMAINING_VIEWS_COUNT": (AppiumBy.XPATH, '//XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[5]'),
    "PROJECT_START_WATCHING_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == " Start Watching"`]'),
    "VIDEO_CONTROLLER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[4]'),   # noqa:E501
    "DOWNLOAD_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "  Download"`]'),
    "DOWNLOADING_TEXT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Downloading...0.0%"`]'),
    "VIDEO_POSTER_IMAGE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage'),  # noqa:E501
    "VIDEO_PLAY_BUTTON": (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton'),
    "EXPIRES_ON": (AppiumBy.ACCESSIBILITY_ID, 'Expires On:'),
    "REMAINING_VIEWS": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Remaining Views:"`][3]'),
    "CLOSE_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "closeMenu"`]'),
    "VIDEO_DETAILS_POSTER": (AppiumBy.XPATH, "//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeImage"),
    "VIDEO_DETAILS_VIDEO_NAME": (AppiumBy.XPATH, "//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText"),
    "SEASON_SELECTION_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name contains "Season"`]'),
    "SEASON_SELECTION_NUMBER": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name contains "{season}"`]'),
    "PROJECT_NAME": (AppiumBy.ID, 'com.indee.indeestaffsc:id/tvScName'),  # noqa:E501
    "PROJECT_VIDEO": (AppiumBy.XPATH, "//XCUIElementTypeCollectionView/XCUIElementTypeCell[{index_number}]"),
    "EXPIRED_VIDEOS": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "{}"`]'),
    "EXPIRY_VALUE": (AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[3]'),   # noqa:E501
    "PROJECT_VIDEO_NAME": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "{}"`]'),
    "SEARCH_PROJECT_NAME": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "{project_name}"`]')
}


class SearchPageScreener(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        package_name = readConstants("current_app_package")
        locators_temp = {
            "SEARCH_BOX_FIELD": (AppiumBy.ID, f'{package_name}:id/txt_search'),
            "SEARCH_RESULTS_HEADER": (AppiumBy.ID, f'{package_name}:id/row_header'),
            "SEARCH_RESULTS_PAGINATION": (AppiumBy.ID, f'{package_name}:id/row_content'),
            "SEARCH_RESULTS_PROJECT_INFO": (AppiumBy.ID, f'{package_name}:id/title_text'),
            "NO_RESULT_ICON": (AppiumBy.ID, f'{package_name}:id/iv_es'),
            "NO_RESULT_FOUND_HEADER": (AppiumBy.ID, f'{package_name}:id/txt_title'),
            "SEARCH_RESULTS_FIRST_PROJECT": (AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@content-desc="Search Results"]/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.TextView'),
            "NO_RESULT_TEXT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").textContains("Please select another genre")'),
            "REMAINING_VIEWS_CONTENT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Remaining Views:")'),
            "REMAINING_VIEWS_COUNT": (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[2]"),
            "PROJECT_START_WATCHING_BUTTON": (AppiumBy.ID, f'{package_name}:id/btn_detail_playnow'),
            "AIR_DATE_TITLE": (AppiumBy.ID, f'{package_name}:id/txt_air_date_title'),
            "AIR_DATE_VALUE": (AppiumBy.ID, f'{package_name}:id/txt_air_date'),
            "AIR_DATE_NOTDISPLAY": (AppiumBy.ID, f'{package_name}:id/txt_air_date_title'),
            "FIRST_VIDEO": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("{}")'),
            "PROJECT_SYNOPSIS": (AppiumBy.ID, f'{package_name}:id/txt_detail_btn_desc'),
            "DETAILS_TAB_PROJECT": (AppiumBy.ID, f'{package_name}:id/txt_detail_btn_title'),
            "CASTANDCREW_TITLE_PROJECT": (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.TextView[3]"),
            "CAST_VALUE": (AppiumBy.ID, f'{package_name}:id/sm_tv_character'),
            "CAST_VALUE2": (AppiumBy.ID, f'{package_name}:id/sm_tv_original'),
            "VIDOE_SYNOPSIS": (AppiumBy.ID, f'{package_name}:id/txt_detail_desc'),
            "DETAILS_BTN": (AppiumBy.ID, f'{package_name}:id/btn_details'),
            "VIDEOS_BTN": (AppiumBy.ID, f'{package_name}:id/btn_videos'),
            "VIDEOS_PAGINATION": (AppiumBy.ID, f'{package_name}:id/row_content'),
            "VIDEO_POSTER": (AppiumBy.ID, f'{package_name}:id/ivScImage'),
            "PLAY_BUTTON": (AppiumBy.ID, f'{package_name}:id/ivScPlay'),
            "VIDEO_NAME": (AppiumBy.ID, f'{package_name}:id/tvScName'),
            "EXPIRY_LABEL": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Expires on:")'),
            "DETAILS_POSTER": (AppiumBy.ID, f'{package_name}:id/img_detail_poster'),
            "DETAILS_LAYOUT": (AppiumBy.ID, f'{package_name}:id/layout_scroll'),
            "VIDEO_CONTROLLER": (AppiumBy.ID, f'{package_name}:id/llController'),
            "PROJECT_LISTING_PAGE": (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]'),
            "PROJECT_NAME": (AppiumBy.ID, f'{package_name}:id/tvScName'),
            "PROJECT_VIDEO": (AppiumBy.ID, f'{package_name}:id/scHolder'),
            "EXPIRED_VIDEOS": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("{}")'),
            "EXPIRY_VALUE": (AppiumBy.ID, f'{package_name}:id/txt_detail_card_expiry')
        }
        self.locators = locators_temp
        print("modied locator ====", self.locators)
            



    def verify_search_page_reached(self):
        if isinstance(self.actions, AndroidActions):
            return self.actions.is_element_displayed(*self.locators['SEARCH_BOX_FIELD'])          
        elif isinstance(self.actions, iOSActions):
            enter_text = "Search for a title..."
            by, value = locators_ipad["SEARCH_BOX_FIELD"]
            default_format_value = value.format(search_content=enter_text)
            Search_box = self.actions.is_element_displayed(by, default_format_value)
            return Search_box
        else:
            return True

    def enter_Text_In_Search_Field(self, Searchcontent):
        sub_string = readPreReqJsonValue("prereq", "search_string_project")
        japanese_project = readPreReqJsonValue("prereq", "forensic_burned_watermark_no_security_project")
        if Searchcontent == japanese_project:
            Searchcontent = Searchcontent.replace("。", '')
        elif Searchcontent != sub_string:
            Searchcontent = Searchcontent + readPreReqJsonValue("prereq", "publicity_execution_id")
        print(Searchcontent)
        if isinstance(self.actions, AndroidActions):
            self.actions.enter_text(*self.locators['SEARCH_BOX_FIELD'], Searchcontent)
            Text_Entered = self.actions.validate_text_contains(*self.locators['SEARCH_BOX_FIELD'], Searchcontent)
            return Text_Entered
        elif isinstance(self.actions, iOSActions):
            enter_text = "Search for a title..."
            by, value = locators_ipad["SEARCH_BOX_FIELD"]
            default_format_value = value.format(search_content=enter_text)
            search_content_validation = value.format(search_content=Searchcontent)
            Search_box = self.driver.find_element(by, default_format_value)
            Search_box.clear()
            Search_box.send_keys(Searchcontent)
            Text_Entered = self.actions.validate_text_contains(by, search_content_validation, Searchcontent)
            return Text_Entered
        else:
            self.actions.click_button("Select")
            time.sleep(1)
            self.actions.doRokuSendKeys(Searchcontent)
            time.sleep(2)
            self.actions.screenshotAttachment("searchcontent.jpeg")
            time.sleep(3)
            for i in range(4):
                self.actions.click_button("Down")
                time.sleep(3)
            time.sleep(3)    
            self.actions.click_button("Select") 
            time.sleep(3) 
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            # self.actions.is_element_displayed("name", "lButtonText", Searchcontent)
            return True
            
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
            print("Submit the search")
            return True
            
    def search_Results(self):
        self.actions.is_element_displayed(*self.locators['SEARCH_RESULTS_FIRST_PROJECT'])

    def verify_Search_Content(self, searchContent):
        if isinstance(self.actions, AndroidActions):
            by, value = self.locators["SEARCH_RESULTS_FIRST_PROJECT"]
            format_value = value.format(searchContent)
            Search_Project = self.actions.is_element_displayed(by, format_value)
            return Search_Project
        elif isinstance(self.actions, iOSActions):
            by, value = locators_ipad["SEARCH_RESULTS_PROJECT_INFO"]
            format_value = value.format(project_name=searchContent)
            Search_Project = self.actions.validate_text_contains(by, format_value, searchContent)
            return Search_Project
        else:
            time.sleep(3)
            # element_Name = "lProjectTitle"
            # Project_Name = "Automation_Test_Project"
            # element_Data = self.actions.fetchRokuCurrentPageSourceUsingName(element_Name, Project_Name)
            # attrs = element_Data.get('value', {}).get('Attrs', [])
            # text_attr = next((attr['Value'] for attr in attrs if attr['Name']['Local'] == 'text'), None)
            # print("The text present is :" + text_attr)
            text_attr = self.actions.is_element_displayed("name", "lButtonText", "")
            text_attr = self.actions.is_element_displayed("name", "lButtonText", "")
            return text_attr

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
            time.sleep(4)
            self.actions.click_button("Back")
            time.sleep(4)
            self.actions.screenshotAttachment("paginaton.jpeg")
            return self.actions.is_element_displayed("name", "lPosterTitle", "")
            #API call to fetch by tag using 'VideosRowListItem' and fetch results
            #In that result validate videos row list items is present
            # #Json node present greater than zero 
            # pass

    def maximum_Count_Verification(self, Searchcontent):
        self.actions.enter_text(*self.locators['MENU_SEARCH_ICON'], Searchcontent)
        self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
        return self.actions.is_element_displayed(*self.locators['REMAINING_VIEWS_CONTENT'])

    def maximum_Count_Video_Redirection(self, Count, video_name):
        if isinstance(self.actions, AndroidActions):
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
        elif isinstance(self.actions, iOSActions):
            for i in range(2):
                self.actions.swipe()
            Element = self.driver.find_element(*locators_ipad['REMAINING_VIEWS_COUNT'])
            ViewsCount = Element.get_attribute("value")
            if int(ViewsCount) > int(Count):
                by, value = locators_ipad['PROJECT_VIDEO_NAME']
                format_value = value.format(video_name)
                self.actions.click_button(by, format_value)
                return True
            else:
                return False

        else:
            time.sleep(3)
            element_Name = "mslRemainingViews"
            text_Value = "Remaining Views:"
            element_Data = self.actions.fetchRokuCurrentPageSourceUsingName(element_Name, text_Value)
            # print("The value is " + json.dumps(element_Data, indent=4))
            attrs = element_Data.get('value', {}).get('Attrs', [])
            text_attr = next((attr['Value'] for attr in attrs if attr['Name']['Local'] == 'text'), None)
            print("The text present is :" + text_attr)
            str1 = text_attr 
            num = ''.join(i for i in str1 if i.isdigit())
            print(num)
            self.actions.screenshotAttachment("remainingviews.jpeg")
            if int(num) > int(Count):
                time.sleep(3)
                self.actions.click_button("Select")
                return True
            else:
                return False  

    def click_OnProjectResult(self, project_name):
        sub_string = readPreReqJsonValue("prereq", "search_string_project")
        if project_name != sub_string:
            project_name = "  " + project_name + readPreReqJsonValue("prereq", "publicity_execution_id")
        print(project_name)
        if isinstance(self.actions, AndroidActions):
            by, value = self.locators["SEARCH_RESULTS_FIRST_PROJECT"]
            format_value = value.format(project_name)
            self.actions.click_button(by, format_value)
            time.sleep(2)
            Project_navigation = self.actions.is_element_displayed(*self.locators['VIDEOS_BTN'])
            if Project_navigation:
                pass
            else:
                self.actions.click_button(by, format_value)
        elif isinstance(self.actions, iOSActions):
            by, value = locators_ipad["SEARCH_PROJECT_NAME"]
            format_value = value.format(project_name=project_name)
            self.actions.click_button(by, format_value)
            time.sleep(5)
        else:
            time.sleep(7)
            self.actions.click_button("Down")
            time.sleep(7)
            self.actions.screenshotAttachment("projectselection.jpeg")
            self.actions.click_button("Select")
            # self.actions.click_button("Down")
            # self.actions.click_button("Select")
            print("Click on project list")

    def click_OnVideoInsideProject(self, video_name):
        if isinstance(self.actions, AndroidActions):
            for i in range(4):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            by, value = self.locators["FIRST_VIDEO"]
            format_value = value.format(video_name)
            self.actions.click_button(by, format_value)
            try:
                self.actions.click_button(by, format_value)
            except Exception:
                pass
        elif isinstance(self.actions, iOSActions):
            by, value = locators_ipad['PROJECT_VIDEO_NAME']
            format_value = value.format(video_name)
            self.actions.click_button(by, format_value)
        else:
            print("In videos page")
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            time.sleep(2)

    def do_remote_activity(self):
        if isinstance(self.actions, AndroidActions):
            print("This function is only for roku")
            pass
        elif isinstance(self.actions, iOSActions):
            print("This function is only for roku")
            pass
        else:
            time.sleep(3)
            self.actions.click_button("Back")
            time.sleep(3)
            self.actions.click_button("Right")
            self.actions.click_button("Select")            
            
    def airDate_Should_Not_Display(self):
        if isinstance(self.actions, AndroidActions):
            statusValue = self.actions.is_element_displayed(*self.locators['AIR_DATE_NOTDISPLAY'])
            return not statusValue
        elif isinstance(self.actions, iOSActions):
            self.actions.swipe()
            statusValue = self.actions.is_element_displayed(*self.locators['AIR_DATE_TITLE'])
            return not statusValue
        else:
            #def fetch_element_with_parent_name_arrtributes(self, parent_attibuteName, parent_attributeValue, attibuteName, attributeValue):
            # currentElement = self.actions.fetch_element_with_parent_name_arrtributes("children", "2", "text", "Jul 25, 2024")
            current_element = self.actions.fetch_element(False, False, "", False, "", "", False, "", False, "", True, "name", "rightSection", False, "")
            Air_Date = self.actions.is_text_available(current_element, "Original Air Date")
            self.actions.screenshotAttachment("airdatenot.jpeg")
            return not Air_Date

    def verify_AirDate_Value(self, searchContent):
        if isinstance(self.actions, AndroidActions):
            self.actions.is_element_displayed(*self.locators['AIR_DATE_TITLE'])
            return self.actions.validate_text(*self.locators['AIR_DATE_VALUE'], searchContent)
        elif isinstance(self.actions, iOSActions):
            self.actions.swipe()
            air_date_value = searchContent.split(' ')
            month = []
            for i, j in enumerate(air_date_value[0]):
                if i < 3:
                    month.append(j)
            month_value = ''.join(month)
            air_date_value[0] = month_value
            air_date_value.pop()
            air_date = ' '.join(air_date_value)
            print(air_date)
            Air_date_title = self.actions.is_element_displayed(*locators_ipad['AIR_DATE_TITLE'])
            Air_date_value = self.actions.validate_text(*locators_ipad['AIR_DATE_VALUE'], air_date)
            print(Air_date_title)
            print(Air_date_value)
            if all([Air_date_title, Air_date_value]):
                return True
            else:
                return False   
        else:
            # time.sleep(3)
            # element_Name = "lSignIn"
            # text_Value = "SIGN IN"
            # element_Data = self.actions.fetchRokuCurrentPageSourceUsingName(element_Name, text_Value)
            # # print("The value is " + json.dumps(element_Data, indent=4))
            # attrs = element_Data.get('value', {}).get('Attrs', [])
            # text_attr = next((attr['Value'] for attr in attrs if attr['Name']['Local'] == 'text'), None)
            # print("The text present is :" + text_attr)
            # return text_attr
            time.sleep(10)
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            currentElement = self.actions.fetch_element_with_parent_name_arrtributes("children", "2", "text", "Jul 25, 2024")
            Air_Date = self.actions.fetch_data_from_json(currentElement)
            self.actions.screenshotAttachment("airdate.jpeg")
            print("element", Air_Date)
            return Air_Date

    def click_DetailsTab_Project(self):
        if isinstance(self.actions, AndroidActions):
            for i in range(4):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            try:
                self.actions.wait_for_element(*self.locators['REMAINING_VIEWS_COUNT'], timeout=3)
            except Exception:
                pass
            self.actions.click_button(*self.locators['DETAILS_BTN'])
            try:
                self.actions.click_button(*self.locators['DETAILS_BTN'])
                Details_Poster = self.actions.is_element_displayed(*self.locators['DETAILS_POSTER'])
                if Details_Poster:
                    pass
            except Exception:
                for i in range(2):
                    self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['DETAILS_BUTTON'])
        else:
            # self.actions.click_button("Down") 
            self.actions.click_button("Right")       
            # self.actions.click_button("Down")

    def click_videos_tab_project(self):
        if isinstance(self.actions, AndroidActions):
            for i in range(2):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.actions.click_button(*self.locators['VIDEOS_BTN'])
            try:
                self.actions.click_button(*self.locators['VIDEOS_BTN'])
            except Exception:
                pass
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['VIDEOS_BUTTON'])
        else:
            time.sleep(2)
            print("Navigating to project")
            self.actions.click_button("Left")
            self.actions.screenshotAttachment("videostab.jpeg")
            print("stop")

    def verify_Cast_Crew_Title_Displayed(self, castValue1, castValue2, crew_ipad):
        if isinstance(self.actions, AndroidActions):
            castValue1 = castValue1.replace(', ', '\n')
            print(castValue1)
            self.actions.is_element_displayed(*self.locators['CASTANDCREW_TITLE_PROJECT'])  
            cast = self.actions.validate_text_contains(*self.locators['CAST_VALUE'], castValue2)
            print(cast)
            crew = self.actions.validate_text_contains(*self.locators['CAST_VALUE2'], castValue1)
            print(crew)
            Cast_And_Crew_Details = [cast, crew]
            if all(Cast_And_Crew_Details):
                return True
            else:
                return False
        elif isinstance(self.actions, iOSActions):
            self.actions.swipe()
            crew_ipad = crew_ipad.replace(',', '')
            Cast_And_Crew_Title = self.actions.is_element_displayed(*locators_ipad['CASTANDCREW_TITLE_PROJECT'])
            Cast = self.actions.validate_text(*locators_ipad['CAST_VALUE'], crew_ipad)
            Crew = self.actions.validate_text(*locators_ipad['CREW_VALUE'], castValue2)
            Cast_And_Crew_Details = [Cast_And_Crew_Title, Cast, Crew]
            if all(Cast_And_Crew_Details):
                return True
            else:
                return False
        elif isinstance(self.actions, RokuActions):
            cast_and_crew = self.actions.fetch_element_with_parent_name_arrtributes("name", "rightSection", "index", "2")
            cast_and_crew_data = self.actions.fetch_data_from_json(cast_and_crew)
            print("Cast and crew =====" + cast_and_crew_data)
            # cast_one = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Prince Daemon Targaryen", False, "", "", False, "")
            # cast_one_data = self.actions.fetch_data_from_json(cast_one)
            # print("Cast one  ====" + cast_one_data)
            time.sleep(3)
            self.actions.screenshotAttachment("castandcrew.jpeg")
            cast_and_crew_details = [cast_and_crew_data] 
            if all(cast_and_crew_details):
                return True
            else:
                return False

    def verify_Project_Synopsis_Information(self, synopsis):
        if isinstance(self.actions, AndroidActions):
            for i in range(2):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            statusValue = self.actions.validate_text_contains(*self.locators['PROJECT_SYNOPSIS'], synopsis)
            return statusValue
        elif isinstance(self.actions, iOSActions):
            return self.actions.validate_text_contains(*locators_ipad['PROJECT_SYNOPSIS'], synopsis)
        elif isinstance(self.actions, RokuActions):
            project_synopsis = self.actions.fetch_element_with_parent_name_arrtributes("name", "rightSection", "index", "1")
            project_synopsis_data = self.actions.fetch_data_from_json(project_synopsis)
            print("Project synopsis=====" , project_synopsis_data)
            self.actions.screenshotAttachment("projectsysnopsis.jpeg")
            time.sleep(3)
            expectedData = readPreReqJsonValue("prereq", synopsis)
        if project_synopsis_data in expectedData:
            return True
        else:
            return False 

    def verify_Video_Synopsis_Information(self, synopsis):
        if isinstance(self.actions, AndroidActions):
            statusValue = self.actions.validate_text_contains(*self.locators['VIDOE_SYNOPSIS'], synopsis)
            return statusValue
        elif isinstance(self.actions, iOSActions):
            self.actions.swipe()
            return self.actions.validate_text_contains(*locators_ipad['VIDOE_SYNOPSIS'], synopsis)
        else:
            time.sleep(4)
            video_synopsis = self.actions.fetch_element_with_parent_name_arrtributes("name", "rightSection", "index", "1")
            video_synopsis_data = self.actions.fetch_data_from_json(video_synopsis)
            print("Video Synopsis" + video_synopsis_data)
            self.actions.screenshotAttachment("videosynopsis.jpeg")
        if video_synopsis_data == readPreReqJsonValue("prereq", synopsis):
            return True
        else:
            return False 
           
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
            Play_Button = self.actions.is_element_displayed(*self.locators['PLAY_BUTTON'])
            Name = self.actions.is_element_displayed(*self.locators['VIDEO_NAME'])
            Expiry = self.actions.is_element_displayed(*self.locators['EXPIRY_LABEL'])
            Remaining_Views = self.actions.is_element_displayed(*self.locators['REMAINING_VIEWS_CONTENT'])
            Video_Tab_Elements = [Videos_Pagination, Video_Poster, Play_Button, Name, Expiry, Remaining_Views]
            if all(Video_Tab_Elements):
                return True
            else:
                return False
        elif isinstance(self.actions, iOSActions):
            self.actions.swipe()
            Videos_Pagination = self.actions.is_element_displayed(*locators_ipad['VIDEOS_PAGINATION'])
            Video_Poster = self.actions.is_element_displayed(*locators_ipad['VIDEO_POSTER'])
            Name = self.actions.is_element_displayed(*locators_ipad['VIDEO_NAME'])
            Expiry = self.actions.is_element_displayed(*locators_ipad['EXPIRY_LABEL'])
            Remaining_Views = self.actions.is_element_displayed(*locators_ipad['REMAINING_VIEWS_CONTENT'])
            Video_Tab_Elements = [Videos_Pagination, Video_Poster, Name, Expiry, Remaining_Views]
            print(Video_Tab_Elements)
            if all(Video_Tab_Elements):
                return True
            else:
                return False
        else:
            time.sleep(3)
            Season_Number = self.actions.fetch_Data("lButtonText", "Season 1")
            print("Season Number ====" + Season_Number)
            season1 = readPreReqJsonValue("prereq", "automation_season1")
            season2 = readPreReqJsonValue("prereq", "automation_season1")
            Video_Project_Title = self.actions.fetch_Data("lVideoTitle", season1)
            print("Video Project_Title ====" + Video_Project_Title)
            self.actions.screenshotAttachment("video.jpeg")
            Video_Project_Title_Two = self.actions.fetch_Data("lVideoTitle", season2)
            Videos_Tab_Elements = [Season_Number, Video_Project_Title, Video_Project_Title_Two]
            if all(Videos_Tab_Elements):
                return True
            else:
                return False

    def verify_details_tab_contents_in_project(self):
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
            Details_Poster = self.actions.is_element_displayed(*locators_ipad['VIDEO_POSTER_IMAGE'])
            Details_Layout = self.actions.is_element_displayed(*locators_ipad['DETAILS_LAYOUT'])
            Synopses = self.actions.is_element_displayed(*locators_ipad['PROJECT_SYNOPSIS'])
            Header_Text = self.actions.wait_for_element(*locators_ipad['DETAILS_TAB_PROJECT'])    #is_element_displayed returns false
            if Header_Text is not None:
                Header_Text = True
            else:
                Header_Text = False
            self.actions.swipe()
            Cast_And_Crew = self.actions.is_element_displayed(*locators_ipad['CASTANDCREW_TITLE_PROJECT'])
            Details_Tab_Elements = [Details_Poster, Details_Layout, Synopses, Header_Text, Cast_And_Crew]
            print(Details_Tab_Elements)
            if all(Details_Tab_Elements):
                return True
            else:
                return False
        else:
            print("Verifying details tab")
            cast_and_crew = self.actions.fetch_element_with_parent_name_arrtributes("name", "rightSection", "index", "2")
            cast_and_crew_data = self.actions.fetch_data_from_json(cast_and_crew)
            print("Cast and crew =====" + cast_and_crew_data)
            self.actions.screenshotAttachment("detailstab.jpeg")
            cast_one = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "", False, "", "", False, "")
            cast_one_data = self.actions.fetch_data_from_json(cast_one)
            print("Cast one  ====" + cast_one_data)
            time.sleep(3)
            cast_and_crew_details = [cast_and_crew_data] 
            if all(cast_and_crew_details):
                return True
            else:
                return False
            
    def verify_auto_playback(self):
        if isinstance(self.actions, AndroidActions):
            try:
                self.actions.wait_for_element(*self.locators['SEARCH_RESULTS_HEADER'], timeout=3)
            except Exception:
                pass
            for i in range(2):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            Videos_Pagination = self.actions.is_element_displayed(*self.locators['VIDEOS_PAGINATION'])
            Video_Poster = self.actions.is_element_displayed(*self.locators['VIDEO_POSTER'])
            Play_Button = self.actions.is_element_displayed(*self.locators['PLAY_BUTTON'])
            Name = self.actions.is_element_displayed(*self.locators['VIDEO_NAME'])
            Expiry = self.actions.is_element_displayed(*self.locators['EXPIRY_LABEL'])
            Remaining_Views = self.actions.is_element_displayed(*self.locators['REMAINING_VIEWS_CONTENT'])
            Video_Tab_Elements = [Videos_Pagination, Video_Poster, Play_Button, Name, Expiry, Remaining_Views]
            if all(Video_Tab_Elements):
                return True
            else:
                return False
        elif isinstance(self.actions, iOSActions):
            try:
                self.actions.click_button(*locators_ipad['CLOSE_BUTTON'])
            except Exception:
                pass
            Video_Poster = self.actions.is_element_displayed(*locators_ipad['VIDEO_DETAILS_POSTER'])
            Play_Button = self.actions.is_element_displayed(*locators_ipad['VIDEO_PLAY_BUTTON'])
            Expiry = self.actions.is_element_displayed(*locators_ipad['EXPIRES_ON'])
            Remaining_Views = self.actions.is_element_displayed(*locators_ipad['REMAINING_VIEWS_CONTENT'])
            Video_name = self.actions.is_element_displayed(*locators_ipad['VIDEO_DETAILS_VIDEO_NAME'])
            Video_Tab_Elements = [Video_Poster, Play_Button, Expiry, Remaining_Views, Video_name]
            print(Video_Tab_Elements)
            if all(Video_Tab_Elements):
                return True
            else:
                return False
        else:  
            self.actions.screenshotAttachment("autoplayback.jpeg")
            time.sleep(5)
            Expires_on = self.actions.fetch_Data("mslExpiresOn", "")
            print("Expiry on ====" , Expires_on)
            remaining_view_text = self.actions.fetch_Data("mslRemainingViews", "Remaining Views")
            print("Remaining views ====" + remaining_view_text)
            # cast_one = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Queen Rhaenyra Targaryen", False, "", "", False, "")
            # cast_one_data = self.actions.fetch_data_from_json(cast_one)
            # print("Cast one  ====" + cast_one_data)  
            self.actions.screenshotAttachment("autoplayback.jpeg")
            video_page_elements = [Expires_on, remaining_view_text]
            if all(video_page_elements):
                return True
            else:
                return False        

    def click_on_start_watching_button(self):
        if isinstance(self.actions, AndroidActions):
            try:
                self.actions.wait_for_element(*self.locators['SEARCH_RESULTS_HEADER'], timeout=3)
            except Exception:
                pass
            self.actions.click_button(*self.locators['PROJECT_START_WATCHING_BUTTON'])
            for i in range(4):
                try:
                    self.actions.tap(*self.locators['PROJECT_START_WATCHING_BUTTON'])
                    Video_Controller = self.actions.is_element_displayed(*self.locators['VIDEO_CONTROLLER'])
                    if Video_Controller:
                        return True
                except Exception:
                    pass
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
                try:
                    Video_Controller = self.actions.is_element_displayed(*self.locators['VIDEO_CONTROLLER'])
                    if Video_Controller:
                        return True
                except Exception:
                    pass
            return False
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['VIDEO_PLAY_BUTTON'])
            Video_Controller = self.actions.is_element_displayed(*locators_ipad['VIDEO_CONTROLLER'])
            if Video_Controller:
                return True
            else:
                return False
        else: 
            time.sleep(2)
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            print("Select the project")
            self.actions.click_button("Select")
            print("project got selected")
            time.sleep(2)
            # self.actions.is_element_displayed("name", "lButtonText", "Start Watching")
            self.actions.click_button("Select")
            time.sleep(7)
            self.actions.click_button("Left")
            time.sleep(2)
            self.actions.is_element_displayed("name", "mslVideoDescription", "")
            self.actions.screenshotAttachment("pause.jpeg")
            self.actions.click_button("Select")
            time.sleep(3)
            # self.actions.click_button("Back")
            return True
        
    def click_on_start_watching_button_authentication(self):
        if isinstance(self.actions, AndroidActions):
            try:
                self.actions.wait_for_element(*self.locators['SEARCH_RESULTS_HEADER'], timeout=3)
            except Exception:
                pass
            self.actions.click_button(*self.locators['PROJECT_START_WATCHING_BUTTON'])
            for i in range(5):
                try:
                    self.actions.tap(*self.locators['PROJECT_START_WATCHING_BUTTON'])
                    Video_Controller = self.actions.is_element_displayed(*self.locators['VIDEO_CONTROLLER'])
                    if Video_Controller:
                        return True
                except Exception:
                    pass
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
                try:
                    Video_Controller = self.actions.is_element_displayed(*self.locators['VIDEO_CONTROLLER'])
                    if Video_Controller:
                        return True
                except Exception:
                    pass
            return False
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['VIDEO_PLAY_BUTTON'])
            Video_Controller = self.actions.is_element_displayed(*locators_ipad['VIDEO_CONTROLLER'])
            if Video_Controller:
                return True
            else:
                return False
        else: 
            time.sleep(2)
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            
            self.actions.click_button("Down")
            self.actions.click_button("Down")
            print("Select the project")
            self.actions.click_button("Select")
            print("project got selected")
            time.sleep(2)
            # self.actions.is_element_displayed("name", "lButtonText", "Start Watching")
            self.actions.click_button("Select")
            time.sleep(3)
            # self.actions.click_button("Back")
            return True    
        
    def roku_back_button(self):
        if isinstance(self.actions, AndroidActions):
            print("pass")
        elif isinstance(self.actions, RokuActions):
            time.sleep(2)
            self.actions.click_button("Back")        
           
    def click_on_download_button_in_video_details_page(self):
        if isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['DOWNLOAD_BUTTON'])
            time.sleep(15)
            Download_started = self.actions.is_element_displayed(*locators_ipad['DOWNLOADING_TEXT'])
            return Download_started
        else:
            return True
        
    def enter_Text_In_Search_Input_Field(self, search_content, search_content_ipad):
        if isinstance(self.actions, AndroidActions):
            try:
                self.actions.wait_for_element(*self.locators['REMAINING_VIEWS_COUNT'], timeout=2)
            except Exception:
                pass
            self.actions.enter_text(*self.locators['SEARCH_BOX_FIELD'], search_content)
            Text_Entered = self.actions.validate_text_contains(*self.locators['SEARCH_BOX_FIELD'], search_content)
            return Text_Entered
        elif isinstance(self.actions, iOSActions):
            enter_text = "Search for a title..."
            by, value = locators_ipad["SEARCH_BOX_FIELD"]
            default_format_value = value.format(search_content=enter_text)
            search_content_validation = value.format(search_content=search_content_ipad)
            Search_box = self.driver.find_element(by, default_format_value)
            Search_box.clear()
            Search_box.send_keys(search_content_ipad)
            Text_Entered = self.actions.validate_text_contains(by, search_content_validation, search_content_ipad)
            return Text_Entered
        else:
            self.actions.click_button("Select")
            time.sleep(1)
            Search_Text = self.actions.doRokuSendKeys(search_content)
            time.sleep(2)
            return Search_Text

    def verify_no_results_in_search_page(self):
        if isinstance(self.actions, AndroidActions):
            no_results_icon = self.actions.is_element_displayed(*self.locators['NO_RESULT_ICON'])
            no_results_text = self.actions.is_element_displayed(*self.locators['NO_RESULT_TEXT'])
            if all([no_results_icon, no_results_text]):
                return True
            else:
                return False
        elif isinstance(self.actions, iOSActions):
            no_results_icon = self.actions.is_element_displayed(*locators_ipad['NO_RESULT_ICON'])
            no_results_text = self.actions.is_element_displayed(*locators_ipad['NO_RESULT_TEXT'])
            if all([no_results_icon, no_results_text]):
                return True
            else:
                return False
        else:
            time.sleep(3)
            element_Name = "lProjectTitle"
            Project_Name = "Automation_Test_Project"
            element_Data = self.actions.fetchRokuCurrentPageSourceUsingName(element_Name, Project_Name)
            # print("The value is " + json.dumps(element_Data, indent=4))
            attrs = element_Data.get('value', {}).get('Attrs', [])
            text_attr = next((attr['Value'] for attr in attrs if attr['Name']['Local'] == 'text'), None)
            print("The text present is :" + text_attr)
            return not text_attr    

    def select_season_with_multiple_audio_andd_subtitle_playback(self, season_number):
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['SEASON_SELECTION_BUTTON'])
            by, value = self.locators["SEASON_SELECTION_NUMBER"]
            format_value = value.format(season=season_number)
            self.actions.click_button(by, format_value)
        if isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['SEASON_SELECTION_BUTTON'])
            by, value = locators_ipad["SEASON_SELECTION_NUMBER"]
            format_value = value.format(season=season_number)
            self.actions.click_button(by, format_value)

    def verify_download_button_is_not_displayed(self):
        if isinstance(self.actions, AndroidActions):
            return self.actions.is_element_displayed(*self.locators['DOWNLOAD_BUTTON'])
        if isinstance(self.actions, iOSActions):
            return self.actions.is_element_displayed(*locators_ipad['DOWNLOAD_BUTTON'])
        else:
            return False
        
    def select_project_video_with_multiple_audio(self, multiple_audio_name):
        if isinstance(self.actions, AndroidActions):
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            Videos = self.actions.wait_for_elements(*self.locators['PROJECT_NAME'])
            print("Videos: ", Videos)
            for index, element in enumerate(Videos):
                video_name = element.get_attribute('text')
                if multiple_audio_name in video_name:
                    index_number = index + 1
                    # by, value = self.locators["PROJECT_VIDEO"]
                    # format_value = value.format(index_number=index_number)
                    element.click()
                    break
        elif isinstance(self.actions, iOSActions):
            self.actions.swipe()
            Videos = self.actions.wait_for_elements(*locators_ipad['PROJECT_NAME'])
            for index, element in enumerate(Videos):
                video_name = element.get_attribute('value')
                if multiple_audio_name in video_name:
                    index_number = index + 1
                    by, value = locators_ipad["PROJECT_VIDEO"]
                    format_value = value.format(index_number=index_number)
                    self.actions.click_button(by, format_value)
                    break
        else:
            return True
       
    def enter_Text_In_Search_Field_To_Verify_Different_Screeneers(self, no_security, forensic, overlay):
        if isinstance(self.actions, AndroidActions):
            projects = [no_security, forensic, overlay]
            project_status = []
            for index, search_content in enumerate(projects):
                print(index)
                self.enter_Text_In_Search_Field(search_content)
                self.submit_Search_Button()
                project_presence = self.verify_Search_Content(search_content)
                project_status.append(project_presence)
                time.sleep(5)
                if index != len(projects) - 1:
                    print('new_search')
                    HomePageScreener.click_on_search_button(self)
            if all(project_status):
                return True
            else:
                return False
        if isinstance(self.actions, iOSActions):
            projects = [no_security, forensic, overlay]
            project_status = []
            for index, search_content in enumerate(projects):
                print(index)
                self.enter_Text_In_Search_Field(search_content)
                self.submit_Search_Button()
                project_presence = self.verify_Search_Content(search_content)
                project_status.append(project_presence)
                time.sleep(5)
                if index != len(projects) - 1:
                    print('new_search')
                    HomePageScreener.click_on_search_button(self)
            if all(project_status):
                return True
            else:
                return False
        else:
            projects = [no_security, forensic, overlay]
            project_status = []
            for index, search_content in enumerate(projects):
                print(index)
                self.enter_Text_In_Search_Field(search_content)
                self.submit_Search_Button()
                project_presence = self.verify_Search_Content(search_content)
                project_status.append(project_presence)
                time.sleep(5)
                if index != len(projects) - 1:
                    print('new_search')
                    HomePageScreener.click_on_search_button(self)
            if all(project_status):
                return True    

    def verify_views_exhausted_error_message_in_project_video(self, expired_message):
        if isinstance(self.actions, AndroidActions):
            for i in range(4):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            expired_message = readPreReqJsonValue("prereq", "Screener_expired_project_message")
            by, value = self.locators['EXPIRED_VIDEOS']
            format_value = value.format(expired_message)
            return self.actions.validate_text_contains(by, format_value, expired_message)
        if isinstance(self.actions, iOSActions):
            by, value = locators_ipad['EXPIRED_VIDEOS']
            format_value = value.format(expired_message)
            return self.actions.is_element_displayed(by, format_value)
        else:
            self.actions.screenshotAttachment
            return self.actions.is_element_displayed("name", "lExpired", readPreReqJsonValue("prereq", "Screener_expired_project_message"))

    def verify_expire_on_text_is_future_dated(self):
        if isinstance(self.actions, AndroidActions):
            for i in range(4):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            expires_on = self.actions.wait_for_element(*self.locators['EXPIRY_LABEL'])
            print(expires_on)
            if expires_on:
                expiry_date = self.actions.get_text(*self.locators['EXPIRY_VALUE'])
                print(expiry_date)
                expiry_date = datetime.strptime(expiry_date, "%B %d, %Y %H:%M")
                print(expiry_date)
                current_date = datetime.now()
                print(current_date)
                if expiry_date > current_date:
                    print('Expiry Date For The Screeners Is Future Dated')
                    return True
                else:
                    return False
            else:
                return False
        if isinstance(self.actions, iOSActions):
            self.actions.swipe()
            expires_on = self.actions.wait_for_element(*locators_ipad['EXPIRY_LABEL'])
            if expires_on:
                expiry_date = self.actions.get_text(*locators_ipad['EXPIRY_VALUE'])
                expiry_date = datetime.strptime(expiry_date, "%b %d, %Y %H:%M")
                current_date = datetime.now()
                if expiry_date > current_date:
                    print('Expiry Date For The Screeners Is Future Dated')
                    return True
                else:
                    return False
            else:
                return False
        else:
            expire_date = self.actions.fetch_Data("mslExpiresOn", "")
            expire = expire_date[19:23]
            self.actions.screenshotAttachment("futuredated.jpeg") 
            print("Expire===" + expire)
            if expire > "2024":
                return True
            else:
                return False   
            
    def validate_expiry_date_and_remaining_views_count(self):
        if isinstance(self.actions, AndroidActions):
            for i in range(4):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            remaining_views_count = self.actions.get_text(*self.locators['REMAINING_VIEWS_COUNT'])
            print(remaining_views_count)
            expiry_date = self.actions.get_text(*self.locators['EXPIRY_VALUE'])
            print(expiry_date)
            return remaining_views_count, expiry_date
        if isinstance(self.actions, iOSActions):
            remaining_views_count = self.actions.get_text(*locators_ipad['REMAINING_VIEWS_COUNT'])
            print(remaining_views_count)
            expiry_date = self.actions.get_text(*locators_ipad['EXPIRY_VALUE'])
            print(expiry_date)
            return remaining_views_count, expiry_date
        else:
            remaining_views_count = self.actions.fetch_Data("mslRemainingViews", "Remaining Views: 540")
            text = remaining_views_count
            remaining_views = text[17:20]  
            print("Remaining views count ===" + remaining_views)
            return remaining_views, None
        
    def verify_the_remaining_views_an_expiry_date_is_updated(self, remaining_views, expiry_date):
        if isinstance(self.actions, AndroidActions):
            remaining_views_count_1 = remaining_views
            expiry_date_1 = expiry_date
            remaining_views_count_2, expiry_date_2 = self.validate_expiry_date_and_remaining_views_count()
            if (remaining_views_count_1 != remaining_views_count_2) and (expiry_date_1 != expiry_date_2):
                return True
            else:
                return False
        if isinstance(self.actions, iOSActions):
            remaining_views_count_1 = remaining_views
            expiry_date_1 = expiry_date
            remaining_views_count_2, expiry_date_2 = self.validate_expiry_date_and_remaining_views_count()
            if (remaining_views_count_1 != remaining_views_count_2) and (expiry_date_1 != expiry_date_2):
                return True
            else:
                return False
        else:
            remaining_views_count_1 = remaining_views
            expiry_date_1 = expiry_date
            remaining_views_count_2, expiry_date_2 = self.validate_expiry_date_and_remaining_views_count()
            if (remaining_views_count_1 != remaining_views_count_2):
                return True
            else:
                return False   
        
