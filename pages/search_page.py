from appium.webdriver.common.appiumby import AppiumBy

from pages.actions.android_actions import AndroidActions
from pages.actions.ios_actions import iOSActions
from pages.actions.roku_actions import RokuActions
import time
from conftest import readConstants, readPreReqJsonValue
from pages.base_page import BasePage


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
    "DETAILS_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Details"`]'),
    "VIDEOS_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Videos"`]'),
    "PROJECT_SYNOPSIS": (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther[1]/XCUIElementTypeStaticText[2]'),
    "CASTANDCREW_TITLE_PROJECT": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "Cast and Crew"`]'),
    "CAST_VALUE": (AppiumBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[2]'),
    "CREW_VALUE": (AppiumBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]'),
    "FIRST_VIDEO": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name contains "{}"`]'),
    "VIDOE_SYNOPSIS": (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[2]'),
    "AIR_DATE_TITLE": (AppiumBy.ACCESSIBILITY_ID, 'Airdate'),
    "AIR_DATE_VALUE": (AppiumBy.XPATH, '//XCUIElementTypeScrollView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeStaticText[4]'),
    "VIDEOS_PAGINATION": (AppiumBy.CLASS_NAME, 'XCUIElementTypeCollectionView'),
    "VIDEO_POSTER": (AppiumBy.XPATH, '//XCUIElementTypeCollectionView/XCUIElementTypeCell[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage[1]'),  # noqa:E501
    "VIDEO_TAB_DOWNLOAD_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "downloadable_img"`][1]'),
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
    "DOWNLOADED_BUTTON": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Downloaded"`]'),
    "VIDEO_POSTER_IMAGE": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeImage'),  # noqa:E501
    "VIDEO_PLAY_BUTTON": (AppiumBy.IOS_PREDICATE, 'name contains "seconds" AND type == "XCUIElementTypeButton"'),
    "EXPIRES_ON": (AppiumBy.ACCESSIBILITY_ID, 'Expires On:'),
    "REMAINING_VIEWS": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Remaining Views:"`][3]'),
    "SEARCH_PROJECT_NAME": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "{project_name}"`]'),
    "PROJECT_CLOSE_BUTTON": (AppiumBy.ACCESSIBILITY_ID, 'Close Button'),
    "POPUP_CLOSE_BUTTON": (AppiumBy.ACCESSIBILITY_ID, "closeMenu"),
    "APPLICATION": (AppiumBy.CLASS_NAME, 'XCUIElementTypeApplication'),
    "RATE_THE_VIDEO": (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "emptyStar"`][5]')
}


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        package_name = readConstants("current_app_package")
        locators_temp = {
            "SEARCH_BOX_FIELD": (AppiumBy.ID, f'{package_name}:id/txt_search'),
            "SEARCH_RESULTS_HEADER": (AppiumBy.ID, f'{package_name}:id/row_header'),
            "SEARCH_RESULTS_PAGINATION": (AppiumBy.ACCESSIBILITY_ID, 'Search Results'),
            "SEARCH_RESULTS_PROJECT_INFO": (AppiumBy.ID, f'{package_name}:id/title_text'),
            "NO_RESULT_ICON": (AppiumBy.ID, f'{package_name}:id/iv_es'),
            "NO_RESULT_FOUND_HEADER": (AppiumBy.ID, f'{package_name}:id/txt_title'),
            "SEARCH_RESULTS_FIRST_PROJECT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.indee.gd:id/title_text").textContains("{}")'),
            "NO_RESULT_TEXT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").textContains("Please select another genre")'),
            "REMAINING_VIEWS_CONTENT": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Remaining Views:")'),
            "REMAINING_VIEWS_COUNT": (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[2]"),
            "PROJECT_START_WATCHING_BUTTON": (AppiumBy.ID, f'{package_name}:id/rv_seemore'),
            "AIR_DATE_TITLE": (AppiumBy.ID, f'{package_name}:id/txt_air_date_title'),
            "AIR_DATE_VALUE": (AppiumBy.ID, f'{package_name}:id/txt_air_date'),
            "AIR_DATE_NOTDISPLAY": (AppiumBy.ID, f'{package_name}:id/txt_air_date_title'),
            "FIRST_VIDEO": (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("{}")'),
            "PROJECT_SYNOPSIS": (AppiumBy.ID, f'{package_name}:id/txt_detail_btn_desc'),
            "DETAILS_TAB_PROJECT": (AppiumBy.ID, f'{package_name}:id/txt_detail_btn_title'),
            "CASTANDCREW_TITLE_PROJECT": (AppiumBy.XPATH, "//android.widget.TextView[@text='Cast and Crew']"),
            "CAST_VALUE": (AppiumBy.ID, f'{package_name}:id/sm_tv_character'),
            "CAST_VALUE2": (AppiumBy.ID, f'{package_name}:id/sm_tv_original'),
            "VIDOE_SYNOPSIS": (AppiumBy.ID, f'{package_name}:id/ivScImage'),
            "DETAILS_BTN": (AppiumBy.ID, f'{package_name}:id/btn_details'),
            "VIDEOS_BTN": (AppiumBy.ID, f'{package_name}:id/btn_videos'),
            "VIDEOS_PAGINATION": (AppiumBy.ID, f'{package_name}:id/row_content'),
            "VIDEO_POSTER": (AppiumBy.ID, f'{package_name}:id/ivScImage'),
            "PLAY_BUTTON": (AppiumBy.ID, f'{package_name}:id/ivScPlay'),
            "VIDEO_NAME": (AppiumBy.ID, f'{package_name}:id/tvScName'),
            "EXPIRY_LABEL": (AppiumBy.ID, f'{package_name}:id/txt_detail_card_expiry'),
            "DETAILS_POSTER": (AppiumBy.ID, f'{package_name}:id/img_detail_poster'),
            "DETAILS_LAYOUT": (AppiumBy.ID, f'{package_name}:id/layout_scroll'),
            "VIDEO_CONTROLLER": (AppiumBy.ID, f'{package_name}:id/llController')
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

    def enter_Text_In_Search_Field(self, Searchcontent):
        automation_projects = readPreReqJsonValue("prereq", "gd_admin_project_name")
        if automation_projects not in Searchcontent:
            print("Inside if project is not created by app automation")
            Searchcontent = Searchcontent + readPreReqJsonValue("prereq", "app_pre_req_execution_id")
        if isinstance(self.actions, AndroidActions):
            time.sleep(5)
            # self.driver.press_keycode(self.keys['KEYCODE_DPAD_CENTER'])
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
        elif isinstance(self.actions, RokuActions):
            self.actions.screenshotAttachment("searchcontent.jpeg")
            self.actions.click_button("Select")
            time.sleep(1)
            print("Search field=====")
            self.actions.doRokuSendKeys(Searchcontent)
            time.sleep(2)
            self.actions.screenshotAttachment("aftersearchcontent.jpeg")
            time.sleep(2)
            return True
            
    def submit_Search_Button(self):
        if isinstance(self.actions, AndroidActions):
            time.sleep(3)
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_CENTER'])
            for i in range(4):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_RIGHT'])
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
            print("Enter the search")
        elif isinstance(self.actions, iOSActions):
            try:
                self.actions.click_button(*locators_ipad['KEYBOARD_SEARCH_BUTTON'])
            except Exception:
                pass
        elif isinstance(self.actions, RokuActions):
            self.actions.screenshotAttachment("beforesearch.jpeg")
            time.sleep(3)
            for i in range(10):
                self.actions.click_button("Down")
                time.sleep(3)
            # time.sleep(3)    
            # self.actions.click_button("Select") 
            # time.sleep(6) 
            self.actions.click_button("Up")
            time.sleep(2) 
            self.actions.click_button("Select")
            time.sleep(10) 
            self.actions.screenshotAttachment("aftersearch.jpeg")
            
    def search_Results(self):
        self.actions.is_element_displayed(*self.locators['SEARCH_RESULTS_FIRST_PROJECT'])

    def verify_Search_Content(self, searchContent):
        automation_projects = readPreReqJsonValue("prereq", "gd_admin_project_name")
        if automation_projects not in searchContent:
            searchContent = searchContent + readPreReqJsonValue("prereq", "app_pre_req_execution_id")
        if isinstance(self.actions, AndroidActions):
            by, value = self.locators["SEARCH_RESULTS_FIRST_PROJECT"]
            format_value = value.format(searchContent)
            Search_Project = self.actions.validate_text_contains(by, format_value, searchContent)
            return Search_Project
        elif isinstance(self.actions, iOSActions):
            by, value = locators_ipad["SEARCH_RESULTS_PROJECT_INFO"]
            format_value = value.format(project_name=searchContent)
            Search_Project = self.actions.validate_text_contains(by, format_value, searchContent)
            return Search_Project
        elif isinstance(self.actions, RokuActions):
            time.sleep(3)
            self.actions.screenshotAttachment("searchresult.jpeg")
            element_Name = "lProjectTitle"
            Project_Name = ""
            element_Data = self.actions.fetchRokuCurrentPageSourceUsingName(element_Name, Project_Name)
            if element_Data is not None:
                attrs = element_Data.get('value', {}).get('Attrs', [])
                Project_Name = next((attr['Value'] for attr in attrs if attr['Name']['Local'] == 'text'), None)
                print("The text present is :", Project_Name)
                if Project_Name in searchContent:
                    return True
                else:
                    return False
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
            #API call to fetch by tag using 'VideosRowListItem' and fetch results
            #In that result validate videos row list items is present
            # #Json node present greater than zero 
            return True

    def maximum_Count_Verification(self, Searchcontent):
        self.actions.enter_text(*self.locators['MENU_SEARCH_ICON'], Searchcontent)
        self.driver.press_keycode(self.keys['KEYCODE_DPAD_ENTER'])
        return self.actions.is_element_displayed(*self.locators['REMAINING_VIEWS_CONTENT'])

    def maximum_Count_Video_Redirection(self, Count):
        if isinstance(self.actions, AndroidActions):
            for i in range(1):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            Element = self.actions.wait_for_element(*self.locators['REMAINING_VIEWS_COUNT'])
            print
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
                self.actions.click_button(*locators_ipad['PROJECT_START_WATCHING_BUTTON'])
                return True
            else:
                return False

        else:
            time.sleep(3)
            self.actions.screenshotAttachment("remainigcoutncheck.jpeg")
            element_Name = "mslRemainingViews"
            text_Value = "Remaining Views:"
            element_Data = self.actions.fetchRokuCurrentPageSourceUsingName(element_Name, text_Value)
            # print("The value is " + json.dumps(element_Data, indent=4))
            attrs = element_Data.get('value', {}).get('Attrs', [])
            text_attr = next((attr['Value'] for attr in attrs if attr['Name']['Local'] == 'text'), None)
            print("The text present is :", text_attr)
            str1 = text_attr 
            num = ''.join(i for i in str1 if i.isdigit())
            print(num)
            if int(num) > int(Count):
                time.sleep(3)
                self.actions.click_button("Select")
                self.actions.click_button("Down")
                self.actions.click_button("Select")
                time.sleep(3)
                self.actions.click_button("Back")
                self.actions.click_button("Back")
                return True
            else:
                return False  

    def roku_back_button(self):
        if isinstance(self.actions, RokuActions):
            time.sleep(6)
            self.actions.click_button("Back")
        elif isinstance(self.actions, iOSActions):
            for i in range(2):
                try:
                    try:
                        self.actions.click_button(*locators_ipad['PROJECT_CLOSE_BUTTON'])
                    except Exception:
                        pass
                    self.actions.click_button(*locators_ipad['POPUP_CLOSE_BUTTON'])
                    try:
                        self.actions.click_button(*locators_ipad['RATE_THE_VIDEO'])
                    except Exception:
                        pass
                except Exception:
                    self.actions.click_button(*locators_ipad['APPLICATION'])
        else:
            pass   
        
    def click_OnProjectResult(self, project_name):
        automation_projects = readPreReqJsonValue("prereq", "gd_admin_project_name")
        if automation_projects not in project_name:
            project_name = project_name + readPreReqJsonValue("prereq", "app_pre_req_execution_id")
        print(" click_OnProjectResult   project_name  ===",project_name)
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
            time.sleep(10)
            by, value = locators_ipad["SEARCH_PROJECT_NAME"]
            format_value = value.format(project_name=project_name)
            self.actions.click_button(by, format_value)
            time.sleep(5)
        elif isinstance(self.actions, RokuActions):
            self.actions.screenshotAttachment("beforeclickproject.jpeg")
            time.sleep(7)
            self.actions.click_button("Down")
            time.sleep(7)
            self.actions.click_button("Select")
            time.sleep(3)
            self.actions.screenshotAttachment("afterclickproject.jpeg")
            time.sleep(7)
           
            print("Click on project list")
            
    def roku_left(self):
        if isinstance(self.actions, RokuActions):
            time.sleep(2)
            self.actions.click_button("Left")
        else:
            return True

    def click_OnVideoInsideProject(self, video_name):
        if isinstance(self.actions, AndroidActions):
            for i in range(2):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
            by, value = self.locators["FIRST_VIDEO"]
            format_value = value.format(video_name)
            self.actions.click_button(by, format_value)
            try:
                self.actions.click_button(by, format_value)
            except Exception:
                pass
        elif isinstance(self.actions, iOSActions):
            by, value = locators_ipad['FIRST_VIDEO']
            format_value = value.format(video_name)
            self.actions.click_button(by, format_value)
        elif isinstance(self.actions, RokuActions):
            print("In videos page")
            self.actions.screenshotAttachment("beforeonvideo.jpeg")
            self.actions.click_button("Down")
            time.sleep(1)
            self.actions.click_button("Down")
            time.sleep(1)
            self.actions.click_button("Down")
            time.sleep(1)
            self.actions.screenshotAttachment("focusVideo.jpeg")
            self.actions.click_button("Select")
            self.actions.screenshotAttachment("afteronvideo.jpeg")
            
    def airDate_Should_Not_Display(self):
        if isinstance(self.actions, AndroidActions):
            statusValue = self.actions.is_element_displayed(*self.locators['AIR_DATE_NOTDISPLAY'])
            return not statusValue
        elif isinstance(self.actions, iOSActions):
            self.actions.swipe()
            statusValue = self.actions.is_element_displayed(*self.locators['AIR_DATE_TITLE'])
            return not statusValue
        else:
            self.actions.screenshotAttachment("airdate.jpeg")
            #def fetch_element_with_parent_name_arrtributes(self, parent_attibuteName, parent_attributeValue, attibuteName, attributeValue):
            # currentElement = self.actions.fetch_element_with_parent_name_arrtributes("children", "2", "text", "Jul 25, 2024")
            current_element = self.actions.fetch_element(False, False, "", False, "", "", False, "", False, "", True, "name", "rightSection", False, "")
            Air_Date = self.actions.is_text_available(current_element, "Original Air Date")
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
            Air_date_value = self.actions.validate_text_contains(*locators_ipad['AIR_DATE_VALUE'], air_date)
            print(Air_date_title)
            print(Air_date_value)
            if all([Air_date_title, Air_date_value]):
                return True
            else:
                return False   
        elif isinstance(self.actions, RokuActions):
            # time.sleep(3)
            # element_Name = "lSignIn"
            # text_Value = "SIGN IN"
            # element_Data = self.actions.fetchRokuCurrentPageSourceUsingName(element_Name, text_Value)
            # # print("The value is " + json.dumps(element_Data, indent=4))
            # attrs = element_Data.get('value', {}).get('Attrs', [])
            # text_attr = next((attr['Value'] for attr in attrs if attr['Name']['Local'] == 'text'), None)
            # print("The text present is :" + text_attr)
            # return text_attr
            time.sleep(5)
            # air_date_value = searchContent.split(' ')
            currentElement = self.actions.fetch_element_with_parent_name_arrtributes("children", "2", "text", searchContent)
            Air_Date = self.actions.fetch_data_from_json(currentElement)
            print("airdate===", Air_Date)
            if Air_Date in readPreReqJsonValue("prereq", "gd_airdate"):
                return True
            else:
                return False
            
    def click_DetailsTab_Project(self):
        if isinstance(self.actions, AndroidActions):
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
        elif isinstance(self.actions, RokuActions):
            time.sleep(5)
            self.actions.screenshotAttachment("before_videostab_button.jpeg")
            self.actions.click_button("Down") 
            self.actions.screenshotAttachment("aftr_videostab__button.jpeg")
            time.sleep(5)
            for i in range(3):
                self.actions.click_button("Right")
                time.sleep(1)  
            self.actions.screenshotAttachment("aftrDetails_button.jpeg")   
            #focus comes to details tab 
            self.actions.click_button("Down")
            self.actions.screenshotAttachment("focusonDetails_data.jpeg")  

    def click_videos_tab_project(self, click_video_tab=True):
        print("am i goign to click project videotab?",click_video_tab)
        if isinstance(self.actions, AndroidActions):
            self.actions.click_button(*self.locators['VIDEOS_BTN'])
            try:
                self.actions.click_button(*self.locators['VIDEOS_BTN'])
            except Exception:
                pass
        elif isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['VIDEOS_BUTTON'])
        elif isinstance(self.actions, RokuActions):
            print("am i goign to click project videotab?")
            if click_video_tab:
                time.sleep(2)
                if click_video_tab:
                    self.actions.screenshotAttachment("inproject_videos.jpeg")
                    time.sleep(2)
                    print("Navigating to project")
                    self.actions.click_button("Down")
                    time.sleep(2)
                    self.actions.screenshotAttachment("inproject_videos_focus.jpeg")
                    print("stop")

    def verify_Cast_Crew_Title_Displayed(self, castValue1, castValue2):
        if isinstance(self.actions, AndroidActions):
            castValue2 = castValue2.replace(', ', '\n')
            for i in range(2):
                self.driver.press_keycode(self.keys['KEYCODE_DPAD_DOWN'])
                self.actions.is_element_displayed(*self.locators['CASTANDCREW_TITLE_PROJECT'])       
                cast = self.actions.validate_text_contains(*self.locators['CAST_VALUE'], castValue1)
                crew = self.actions.validate_text_contains(*self.locators['CAST_VALUE2'], castValue2)
                Cast_And_Crew_Details = [cast, crew]
                if all(Cast_And_Crew_Details):
                    return True
                else:
                    return False
        elif isinstance(self.actions, iOSActions):
            self.actions.swipe()
            Cast_And_Crew_Title = self.actions.is_element_displayed(*locators_ipad['CASTANDCREW_TITLE_PROJECT'])
            Cast = self.actions.validate_text(*locators_ipad['CAST_VALUE'], castValue1)
            Crew = self.actions.validate_text(*locators_ipad['CREW_VALUE'], castValue2)
            Cast_And_Crew_Details = [Cast_And_Crew_Title, Cast, Crew]
            if all(Cast_And_Crew_Details):
                return True
            else:
                return False
        elif isinstance(self.actions, RokuActions):
            cast_crew_details = readPreReqJsonValue("prereq", "project_crew_lengthy")
            cast_and_crew = self.actions.fetch_element_with_parent_name_arrtributes("name", "rightSection", "text", cast_crew_details)
            cast_and_crew_data = self.actions.fetch_data_from_json(cast_and_crew)
            print("Cast and crew =====" + cast_and_crew_data)
            print("nagigate back after cast and crew verification")
            # cast_one = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Prince Daemon Targaryen", False, "", "", False, "")
            # cast_one_data = self.actions.fetch_data_from_json(cast_one)
            # print("Cast one  ====" + cast_one_data)
            
            time.sleep(3)
            self.actions.click_button("Up")
            time.sleep(1)
            self.actions.click_button("Left")
            time.sleep(1)
            self.actions.click_button("Up")
            self.actions.click_button("Up")
            self.actions.screenshotAttachment("backtoprjectcarousalview.jpeg")
            # cast_and_crew_details = [cast_and_crew_data] 
            if cast_and_crew_data:
                
                return True
            else:
                return False

    def verify_Project_Synopsis_Information(self, project_synopsis):
        if isinstance(self.actions, AndroidActions):
            
            statusValue = self.actions.validate_text_contains(*self.locators['PROJECT_SYNOPSIS'], project_synopsis)
            return statusValue
        elif isinstance(self.actions, iOSActions):
            return self.actions.validate_text_contains(*locators_ipad['PROJECT_SYNOPSIS'], project_synopsis)
        elif isinstance(self.actions, RokuActions):
            project_synopsis_element = self.actions.fetch_element_with_parent_name_arrtributes("name", "rightSection", "index", "1")
            project_synopsis_data = self.actions.fetch_data_from_json(project_synopsis_element)
            print("Project synopsis=====" , project_synopsis_data)
            time.sleep(3)
            
            if project_synopsis in project_synopsis_data:
                self.actions.click_button("Up")
                time.sleep(1)
                self.actions.click_button("Right")
                time.sleep(1)
                self.actions.click_button("Up")
                return True
            else:
                return False
            

    def verify_Video_Synopsis_Information(self):
        if isinstance(self.actions, AndroidActions):
            statusValue = self.actions.is_element_displayed(*self.locators['VIDOE_SYNOPSIS'])
            return statusValue
        elif isinstance(self.actions, iOSActions):
            self.actions.swipe()
            return self.actions.is_element_displayed(*locators_ipad['VIDOE_SYNOPSIS'])
        elif isinstance(self.actions, RokuActions):
            time.sleep(4)
            video_synopsis = self.actions.fetch_element_with_parent_name_arrtributes("name", "rightSection", "index", "1")
            video_synopsis_data = self.actions.fetch_data_from_json(video_synopsis)
            print("Video Synopsis" , video_synopsis_data)
            time.sleep(3)
            expectedData = readPreReqJsonValue("prereq", "episode_synopsis")
            if video_synopsis_data in expectedData:
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
            Play_Button = self.actions.is_element_displayed(*locators_ipad['VIDEO_TAB_DOWNLOAD_BUTTON'])
            Name = self.actions.is_element_displayed(*locators_ipad['VIDEO_NAME'])
            Expiry = self.actions.is_element_displayed(*locators_ipad['EXPIRY_LABEL'])
            Remaining_Views = self.actions.is_element_displayed(*locators_ipad['REMAINING_VIEWS_CONTENT'])
            Video_Tab_Elements = [Videos_Pagination, Video_Poster, Play_Button, Name, Expiry, Remaining_Views]
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
            Header_Text = self.actions.is_element_displayed(*locators_ipad['DETAILS_TAB_PROJECT'])
            self.actions.swipe()
            Cast_And_Crew = self.actions.is_element_displayed(*locators_ipad['CASTANDCREW_TITLE_PROJECT'])
            Details_Tab_Elements = [Details_Poster, Details_Layout, Synopses, Header_Text, Cast_And_Crew]
            print(Details_Tab_Elements)
            if all(Details_Tab_Elements):
                return True
            else:
                return False
        elif isinstance(self.actions, RokuActions):
            print("Verifying details tab")
            cast_and_crew = self.actions.fetch_element_with_parent_name_arrtributes("name", "rightSection", "index", "2")
            cast_and_crew_data = self.actions.fetch_data_from_json(cast_and_crew)
            print("Cast and crew =====" + cast_and_crew_data)
            cast_one = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Actor1: Cast1", False, "", "", False, "")
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
            Video_Poster = self.actions.is_element_displayed(*locators_ipad['VIDEOS_PAGINATION'])
            Play_Button = self.actions.is_element_displayed(*locators_ipad['VIDEO_PLAY_BUTTON'])
            Dowload_Button = self.actions.is_element_displayed(*locators_ipad['DOWNLOAD_BUTTON'])
            Expiry = self.actions.is_element_displayed(*locators_ipad['EXPIRES_ON'])
            Remaining_Views = self.actions.is_element_displayed(*locators_ipad['REMAINING_VIEWS'])
            self.actions.swipe()
            Video_syopsis = self.actions.is_element_displayed(*locators_ipad['VIDOE_SYNOPSIS'])
            Air_date = self.actions.is_element_displayed(*locators_ipad['AIR_DATE_TITLE'])
            Cast_and_crew = self.actions.is_element_displayed(*locators_ipad['CASTANDCREW_TITLE_PROJECT'])
            Video_Tab_Elements = [Video_Poster, Play_Button, Dowload_Button, Expiry, Remaining_Views, Video_syopsis, Air_date, Cast_and_crew]
            if all(Video_Tab_Elements):
                return True
            else:
                return False
        elif isinstance(self.actions, RokuActions):
            time.sleep(4)
            expiry_date_text = readPreReqJsonValue("prereq", "gd_expiry_date")
            Expires_on = self.actions.fetch_element_with_parent_name_arrtributes("name", "cbExpiresOn", "text", expiry_date_text)
            fetched_expire = self.actions.fetch_data_from_json(Expires_on)
            print("Expiry on ====" + fetched_expire)
            remaining_view_text = self.actions.fetch_element_with_parent_name_arrtributes("name", "cbRemainingViews", "text", "Remaining Views")
            fetched_remaining = self.actions.fetch_data_from_json(remaining_view_text)
            print("Remaining views ====" + fetched_remaining)
            # cast_one = self.actions.fetch_element(False, "", "", False, "", "", False, "", True, "Queen Rhaenyra Targaryen", False, "", "", False, "")
            # cast_one_data = self.actions.fetch_data_from_json(cast_one)
            # print("Cast one  ====" + cast_one_data)  
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
            self.actions.click_button(*locators_ipad['PROJECT_START_WATCHING_BUTTON'])
            Video_Controller = self.actions.is_element_displayed(*locators_ipad['VIDEO_CONTROLLER'])
            if Video_Controller:
                return True
            else:
                return False
        elif isinstance(self.actions, RokuActions):
            time.sleep(2)
            # start_watching_button = self.actions.fetch_Data("lButtonText", "Start Watching")
            # print("Start watch button -------" + start_watching_button)
            self.actions.click_button("Down")
            self.actions.click_button("Select")
            time.sleep(2)
            return True
           
    def click_on_download_button_in_video_details_page(self):
        if isinstance(self.actions, iOSActions):
            self.actions.click_button(*locators_ipad['DOWNLOAD_BUTTON'])
            time.sleep(15)
            Download_started = self.actions.is_element_displayed(*locators_ipad['DOWNLOADING_TEXT'])
            if not Download_started:
                Download_started = self.actions.is_element_displayed(*locators_ipad['DOWNLOADED_BUTTON'])
            return Download_started
        
    def enter_Text_In_Search_Input_Field(self, search_content, search_content_ipad):
        if isinstance(self.actions, AndroidActions):
            try:
                self.actions.wait_for_element(*self.locators['REMAINING_VIEWS_COUNT'], timeout=2)
            except Exception:
                pass
            self.driver.press_keycode(self.keys['KEYCODE_DPAD_CENTER'])
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
        elif isinstance(self.actions, RokuActions):
            self.actions.click_button("Select")
            time.sleep(1)
            self.actions.doRokuSendKeys(search_content)
            time.sleep(2)
            return True

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
        elif isinstance(self.actions, RokuActions):
            time.sleep(3)
            element_Name = "lProjectTitle"
            Project_Name = readConstants("Admin_Project_Name")
            element_Data = self.actions.fetchRokuCurrentPageSourceUsingName(element_Name, Project_Name)
            # print("The value is " + json.dumps(element_Data, indent=4))
            attrs = element_Data.get('value', {}).get('Attrs', [])
            text_attr = next((attr['Value'] for attr in attrs if attr['Name']['Local'] == 'text'), None)
            print("The text present is :", text_attr)
            return not text_attr

