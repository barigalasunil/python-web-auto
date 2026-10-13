from selenium.webdriver.common.by import By
import time
# from pages.actions.webpage_actions import WebAppActions
from pages.actions.android_actions import AndroidActions
from selenium.webdriver.common.keys import Keys
from conftest import readConstants, readPreReqJsonValue
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import pyautogui
import os
import random
import string

locators = {
    "CLIENT_EMAIL_FIELD": (By.NAME, 'username'),
    "INTERNAL_EMAIL_FIELD": (By.NAME, 'staff'),
    "INTERNAL_PASSWORD_FIELD": (By.NAME, 'password'),
    "SIGN_IN": (By.XPATH, "//div[@class='sign-in-button']//button"),
    "PROJECTS": (By.XPATH, "(//a[contains(@class,'projects-link small-blue-button-')])[1]"),
    "APPLICATION_MANAGER": (By.XPATH, "(//a[contains(@class,'projects-link small-blue-button-')])[2]"),  # noqa:E501
    "FYC_REDIRECTION": (By.XPATH, "//div[contains(@class, 'FYC')]"),  # noqa:E501
    "WATCH_REBUILD": (By.XPATH, "//button[@name='Valid_Ext_VLKFPUYEPIAC_2025']"),
    "START_FRESH": (By.XPATH, "//button//span[text()='START AFRESH']"),
    "PARAMOUNT_TELEVISION": (By.XPATH, "(//img[@class='division-logo box-border p-4'])[2]"),
    "LAUNCH_APP_EDITOR": (By.XPATH, "//span[text()='LAUNCH APP EDITOR']"),
    "MANAGE_FEATURED_IMAGES": (By.XPATH, "//b[text()='MANAGE FEATURED IMAGES']"),
    "IMAGE_UPLOAD": (By.XPATH, "//input[@id='feature_image']"),
    "CROP": (By.XPATH, "//button//span[text()=' CROP ']"),
    "DELETE_IMAGE": (By.XPATH, "//button//p[text()='DELETE FEATURED IMAGE']"),
    "DELETE_BUTTON": (By.XPATH, "//button//span[text()=' DELETE ']"),
    "PROJECTS_SELECTION": (By.XPATH, "(//a[contains(@class,'projects-link')])[1]"),
    "ADD_NEW_PROJECT": (By.XPATH, "//span[@class='icon icon-add-item']"),
    "NAME_OF_THE_PROJECT": (By.XPATH, "//input[@placeholder='Name of your project']"),
    "PROJECT_DESCRIPTION": (By.XPATH, "//div[@data-placeholder='Provide a synopsis for your project']"),
    "GENRES_CONTENT": (By.XPATH, "//input[@class='search-input']"),
    "SUBMIT_PROJECT_DETAILS": (By.XPATH, "//button[contains(@class,'i-button large-button animated')]"),
    "VIDEO_NAME": (By.ID, "videoname-input"),
    "VIDEO_UPLOAD": (By.XPATH, "//input[@type='file' and @name='video']"),
    "UPLOAD_BUTTON": (By.XPATH, "//button[@type='submit' and @name='submit']"),
    "COMEDY_DROP_DOWN": (By.XPATH, "(//div[contains(text(),'Action')])[1]"),
    "SAVE_AND_NEXT": (By.XPATH, "//button[@type='button' and @name='SAVE']"),
    "FINISH_UPLOAD": (By.XPATH, "//button[contains(@class,'i-button large-button animated')]"),
    "SEND_SCREENERS": (By.XPATH, "//li[@class='send-screener-item']"),
    "FYC_SEND_SCREENERS": (By.XPATH, "//div[contains(text(),'FYC')]"),
    "SELECT_ALL": (By.XPATH, "(//input[@type='checkbox'])[2]"),
    "PROCEED_UPLOAD": (By.XPATH, "//button[@class='btn btn-proceed']"),
    "SEARCH_FOR_THE_PROJECT": (By.XPATH, "//input[@placeholder='Search for a project']"),
    "PROJECT_SEARCH_RESULTS": (By.XPATH, '//a[@data-tippy-content="{project_name}"]'),
    "EDIT_PROJECT": (By.XPATH, "//a[contains(text(),'Edit Project')]"),
    "DELETE_PROJECT": (By.XPATH, "//p[@class='error-text delete-button pointer']"),
    "CONTINUE_DELETE": (By.XPATH, "//span[text()='Continue']"),
    "NO_SEARCH_RESULTS": (By.XPATH, "//h3[text()='NO SEARCH RESULTS FOUND']"),
    "REORDER": (By.XPATH, "//p[text()='REORDER']"),
    "REARRANGE_IMAGE": (By.ID, "moveImgRight-0"),
    "SAVE_CHANGES": (By.XPATH, "//button[@class='save-button']"),
    "ADD_SWIMLANE": (By.XPATH, "//button[@id='add_swimlane']"),
    "ADD_SWIMLANE_SECTION_ICON": (By.ID, "edit_swimlane_582"),
    "AUTOMATION_GD_PROJECT": (By.XPATH, "//div[@data-tippy-content='RIVERDALE']"),
    "SEARCH_PROJECT": (By.XPATH, "//input[@placeholder='Search for a project']"),
    "REMOVE_PROJECT": (By.XPATH, "(//div[contains(@class, 'cross-holder')]//span[@title='Remove Project'])[2]"),  # noqa:E501
    "EDIT_SWIMLANE_PROJECT_NAME": (By.XPATH, "(//div[contains(@class,'swimlane-wrapper w-')]//span)[2]"),  # noqa:E501
    "ENTER_SWIMLANE_NAME": (By.XPATH, "//input[@placeholder='Swimlane Name']"),
    "SELECT_SEARCH_PROJECT": (By.XPATH, "//div[contains(@class,'swimlane relative m-')]"),  # noqa:E501
    "SELECT_SEARCH_PROJECT_2": (By.XPATH, "//div[contains(@class, 'swimlane relative m-4 smallCards')]"),
    "SAVE_SWIMLANE_PROJECT": (By.XPATH, "//button[contains(@class,'save-btn-bg')]"),  # noqa:E501
    "RE_ARRANGE_SWIMLANE_ICON": (By.XPATH, "//div[@id='reArrangeSwimlaneImage']"),
    "API_KEY_SECTION": (By.XPATH, "//a[text()='API keys']"),
    "USERNAME_NIMAAD": (By.NAME, "username"),
    "PASSWORD_NIMAAD": (By.NAME, "password"),
    "SIGN_IN_NIMAAD": (By.XPATH, "//input[@value='Log in']"),
    "API_KEY": (By.XPATH, "(//td[@class='field-name' and text()='{field_name}']/preceding-sibling::th)[1]"),
    "EXPIRY_DATE": (By.NAME, "expiry_date_0"),
    "SAVE_DATE": (By.XPATH, "//input[@value='Save']"),
    "WATCHLIST_PRODUCT": (By.XPATH, "//a[text()='Watch products']"),
    "PARAMOUNT_WATCHLIST": (By.XPATH, "//tr[td[text()='FYC']]/th[@class='field-enterprise nowrap']/a[text()='paramount']"),
    "WATCHLIST_CHECKBOX": (By.ID, "id_watchlist_enabled"),
    "RESUME_PLAYBACK": (By.ID, "id_resume_playback_enabled"),
    "MOVE_SWIMELANE_UP": (By.XPATH, "//div[@title='Move Swimlane Up']"),
    "BUILD_SELECTION": (By.XPATH, "//button[@name='{pin_value}']"),
    "SECURITY_SELECTION": (By.XPATH, "//p[contains(text(), 'No Security')]"),
    "MANAGE": (By.XPATH, "//button//span[contains(text(), 'MANAGE')]"),
    "SAVE_BUTTON": (By.XPATH, "//button//span[contains(text(), 'SAVE')]"),
    "PROJECT_SEARCH_DROPDOWN": (By.XPATH, "//p[contains(text(), '{}')]"),
    "SEARCH_RESULTS": (By.XPATH, "//div[contains(text(), '{}')]"),
    "EDIT_ICON": (By.XPATH, "//button[contains(@class, 'edit-icon-wrapper') and starts-with(@id, 'edit_swimlane')]"),
    "SAVE_SWIMLANE_REARRANGE": (By.XPATH, "//button[@class='save-button']"),
    "CANCEL_SWIMLANE_REARRANGE": (By.XPATH, "//button[@class='cancel-button']"),
    "DELETE_SWIMLANE": (By.XPATH, "//button[contains(@class, 'delete-icon')]"),
    "PROJECT_NAME": (By.XPATH, "//div[contains(@data-tippy-content, '{project_name}')]"),
    "REARRANGE_PROJECTS": (By.XPATH, "//div[contains(@class, 'cursor-pointer') and contains(@class, 'text-2xl') and contains(@class, 'p-1')]//span[text()='❮']"),
    "VIDEO_DELETE": (By.XPATH, "//i[contains(@class, 'icon-trash-icon')]"),
    "DELETE_VIDEO_POPUP_HEADER": (By.XPATH, "//div[@class='modal-header']//p[text()='Delete Video from Project']"),
    "DELETE_VIDEO_CONTINUE": (By.XPATH, "//button[.//span[text()='Continue']]"),
    "NO_VIDEOS_IN_PROJECT": (By.XPATH, "//p[@class='regular-text' and text()='Total Videos - 0']"),
    "UNPUBLISH": (By.XPATH, "//button[contains(text(), 'Unpublish')]"),
    "UNPUBLISH_SELECT_ALL": (By.XPATH, "//input[@type='checkbox']"),
    "BUTTON_UNPUBLISH": (By.XPATH, "//button[@class='btn btn-proceed']"),
    "UNPUBLISH_SUCCESS_TICK": (By.XPATH, "//div[@class='success-tick-icon']"),
    "UNPUBLISH_SUCCESS_MESSAGE": (By.XPATH, "//div[contains(@class, 'mt-4')]"),
    "NIMAAD_SAVE_BUTTON": (By.NAME, '_save'),
    "DELETE_API": (By.XPATH, "//a[@class='deletelink']"),
    "CONFIRM_DELETE": (By.XPATH, "//input[@value='Yes, I’m sure']"),
    "ADD_API_KEY": (By.XPATH, "//a[@class='addlink' and contains(text(), 'Add API Key')]"),
    "TIME": (By.CLASS_NAME, "vTimeField"),
    "API_NAME": (By.XPATH, "//input[@name='name' and @id='id_name']"),
    "API_WATCH_PRODUCT": (By.XPATH, "//select[@id='id_watch_product']"),
    "WATCH_PRODUCT_FYC": (By.XPATH, "//option[text()='FYC | paramount']"),
    "PERMISSIONS": (By.ID, 'id_permissions'),
    "WATCH_DOMAIN": (By.XPATH, "//select[@id='id_watch_domain']"),
    "WATCH_DOMAIN_FYC": (By.XPATH, "//option[text()='{}-paramount-fyc.watch.devtest.indee.tv | FYC | paramount']"),
    "INTENDED_CLIENT": (By.XPATH, "//select[@id='id_watch_domain']"),
    "INTENDED_CLIENT_VALUE": (By.XPATH, "//option[text()='{intended_client}']"),
    "ENTERPRISE": (By.XPATH, "//select[@id='id_enterprise']"),
    "ENTERPRISE_PARAMOUNT": (By.XPATH, "//option[text()='paramount']"),
    "API_SAVE_BUTTON": (By.XPATH, "//input[@value='Save']"),
    "NEW_BUTTON": (By.XPATH, "//div[contains(text(),'+ New')]"),
    "SEARCH_AUDIENCE": (By.XPATH, "//input[@placeholder='Search for an audience']"),
    "PIN_SELECTION": (By.XPATH, "//div[@class='cms-tile w-full h-full flex justify-center items-center font-bold  p-2 box-border break-all text-sm text-center {pin_value}']"),
    "PIN_EXECUTION": (By.XPATH, "//div[contains(@class, 'cms-tile') and contains(text(), '{pin_value}')]"),
    "BRAND_EXECUTION": (By.XPATH, "//span[@class='division-name-text' and text()='{brand_value}']"),
    "BRAND_NEXT_PAGE": (By.XPATH, "//span[@class='icon icon-right-arrow']"),
    "CAROUSAL_IMAGE_SAVE": (By.XPATH, "//button[contains(text(), 'SAVE') and contains(text(), 'EXIT')]"),
    "DELETE_CAROUSEL_IMAGE": (By.XPATH, "//button[.//p[text()='DELETE FEATURED IMAGE']]"),
    "DELETE_POPUP_HEADER": (By.XPATH, "//p[contains(text(), 'Deleting will remove all the featured images')]"),
    "CONFIRM_DELETE_POPUP": (By.XPATH, "//button[.//span[text()=' DELETE ']]"),
    "SELECT_BRAND": (By.XPATH, "//div[@class='cms-subtitle-text' and text()='Select a brand to manage']"),
    "TRANSCODING_PROGRESS": (By.XPATH, "//p[normalize-space()='Transcoding in Progress']"),
    "VIDEO_ID": (By.XPATH, "//span[contains(normalize-space(),'ID:')]"),
    "NO_SECURITY": (By.XPATH, "//div[@class='security flex flex-col justify-center items-center']/p[@class='security-name' and text()='No Security']"),
    "SWIMLANE_TEXT": (By.XPATH, "./preceding-sibling::span[contains(@class, 'font-bold')]")
}


class AdminPortalPageFYC(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    
    # Client_Email_FIELD = (By.NAME, 'username')
    # Internal_Email_Field = (By.NAME, 'staff')
    # Internal_Password_Field = (By.NAME, 'password')
    # Sign_In = (By.XPATH, "//div[@class='sign-in-button']//button")
    # Application_Manager = (By.XPATH, "(//a[contains(@class,'projects-link small-blue-button-')])[2]")
    # Global_Description_Redirection = (By.XPATH, "(//div[@class='application-manager-wrapper']//a//div//div)[2]")
    # Launch_App_Editor = (By.XPATH, "//span[text()='LAUNCH APP EDITOR']")
    # Manage_Featured_Images = (By.XPATH, "//b[text()='MANAGE FEATURED IMAGES']")
    # Image_Upload = (By.XPATH, "//div[@class='flex items-center justify-center']")
    # Reorder = (By.XPATH, "//p[text()='REORDER']")
    # ReArrange_Image = (By.ID, "moveImgRight-0")
    # Save_Changes = (By.XPATH, "//button[@class='save-button']")
    # Add_Swimlane = (By.ID, "add_swimlane")
    # Add_Swimlane_Section_Icon = (By.ID, "edit_swimlane_116")
    # Automation_GD_Project = (By.XPATH, "//div[@data-tippy-content='AutomationGD']")
    # Search_Project = (By.XPATH, "//input[@placeholder='Search for a project']")
    # Remove_Project = (By.XPATH, "//div[@data-tippy-content='AutomationGD']//following::span[@title='Remove Project']")

    # def launch_browser_url(self, driver, url):
    #     # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    #     driver.get(url)
      
    def login_to_admin_portal(self, clientemail, internalemail, password):
        time.sleep(15)
        AndroidActions(self.driver).enter_text(*locators['CLIENT_EMAIL_FIELD'], clientemail)   # noqa:E501
        AndroidActions(self.driver).enter_text(*locators['INTERNAL_EMAIL_FIELD'], internalemail)  # noqa:E501
        AndroidActions(self.driver).enter_text(*locators['INTERNAL_PASSWORD_FIELD'], password)  # noqa:E501
        AndroidActions(self.driver).click_button(*locators['SIGN_IN'])

    def navigate_To_FYC_Portal(self, driver):
        pin = readPreReqJsonValue("prereq", "fyc_execution_id")
        time.sleep(10)
        AndroidActions(driver).wait_for_element(*locators['APPLICATION_MANAGER'])
        AndroidActions(driver).click_button(*locators['APPLICATION_MANAGER'])
        time.sleep(10)
        AndroidActions(driver).wait_for_element(*locators['FYC_REDIRECTION'])  # noqa:E501
        AndroidActions(driver).click_button(*locators['FYC_REDIRECTION'])  # noqa:E501
        time.sleep(10)
        try:
            pin_selection = readPreReqJsonValue("prereq", "fyc_admin_pin") 
            by, value = locators["PIN_SELECTION"]
            format_value = value.format(pin_value=pin_selection)
            for i in range(5):
                audience_selection = AndroidActions(driver).is_element_displayed(by, format_value)
                if audience_selection:
                    break
                else:
                    AndroidActions(driver).click_button(*locators['BRAND_NEXT_PAGE'])
            AndroidActions(driver).click_button(by, format_value)
            AndroidActions(driver).wait_for_element(*locators['SELECT_BRAND'])
        except Exception:
            AndroidActions(driver).wait_for_element(*locators['NEW_BUTTON'])  # noqa:E501
            AndroidActions(driver).click_button(*locators['NEW_BUTTON'])  # noqa:E501
            time.sleep(5)
            pin = readPreReqJsonValue("prereq", "fyc_execution_id")
            Search_field = AndroidActions(driver).wait_for_element(*locators['SEARCH_AUDIENCE']) 
            AndroidActions(driver).enter_text(*locators['SEARCH_AUDIENCE'], pin)
            Search_field.send_keys(Keys.ENTER)
            time.sleep(5)
            pin_selection = readPreReqJsonValue("prereq", "fyc_admin_pin") 
            by, value = locators["PIN_EXECUTION"]
            format_value = value.format(pin_value=pin_selection)
            AndroidActions(driver).click_button(by, format_value)
        time.sleep(10)
        brand_selection = readPreReqJsonValue("prereq", "fyc_brand_to_replace") 
        by, value = locators["BRAND_EXECUTION"]
        format_value = value.format(brand_value=brand_selection)
        for i in range(50):
            print('Inside loop')
            Brand = AndroidActions(driver).is_element_displayed(by, format_value)  # noqa:E501
            if Brand:
                break
            else:
                AndroidActions(driver).click_button(*locators['BRAND_NEXT_PAGE']) 
        AndroidActions(driver).wait_for_element(by, format_value)
        AndroidActions(driver).click_button(by, format_value)
        for i in range(2):
            try:
                AndroidActions(driver).click_button(by, format_value)
            except Exception:
                pass
        time.sleep(20)
        brand_value = readPreReqJsonValue("prereq", "fyc_pin_to_replace_in_url") 
        brand_to_replace = readPreReqJsonValue("prereq", "fyc_admin_brand_pin_value") 
        current_url = self.driver.current_url
        print(current_url)
        updated_url = current_url.replace(brand_value, brand_to_replace)
        print(updated_url)
        self.driver.get(updated_url)  
        # current_url = self.driver.current_url
        # updated_url = current_url.replace('%2F', '/').replace('?page=34', '')
        # self.driver.get(updated_url)
        time.sleep(10)
        try:
            AndroidActions(driver).wait_for_element(*locators['START_FRESH'])
            AndroidActions(driver).click_button(*locators['START_FRESH'])
        except Exception:
            pass
        time.sleep(10)
        pyautogui.scroll(300)
        AndroidActions(driver).wait_for_element(*locators['LAUNCH_APP_EDITOR'])  # noqa:E501
        AndroidActions(driver).click_button(*locators['LAUNCH_APP_EDITOR'])
        time.sleep(30)
        
    def upload_carousel_Image(self, driver):
        AndroidActions(driver).wait_for_element(*locators['MANAGE_FEATURED_IMAGES'])
        AndroidActions(driver).click_button(*locators['MANAGE_FEATURED_IMAGES'])
        user_directory = os.getcwd()
        image_path = os.path.join(user_directory, 'AdminData', 'pexels-vlasceanu-1403653.jpg').replace('\\', '/')
        # image_path = "D:\latest\Indee_App_Automation\AdminData"  # noqa:E501
        AndroidActions(driver).wait_for_element(*locators['IMAGE_UPLOAD'])
        print("Uploading image===")
        # UserActions(driver).click_button(*self.Image_Upload)
        Image_upload = AndroidActions(driver).wait_for_element(*locators['IMAGE_UPLOAD'])
        print(Image_upload)
        if Image_upload:
            Image_upload.send_keys(image_path)
        AndroidActions(driver).click_button(*locators["CROP"])    
        time.sleep(5)
        AndroidActions(driver).wait_for_element(*locators['CAROUSAL_IMAGE_SAVE'])
        AndroidActions(driver).click_button(*locators['CAROUSAL_IMAGE_SAVE'])
        time.sleep(10)

    def delete_carousel_image(self, driver):
        AndroidActions(driver).wait_for_element(*locators['MANAGE_FEATURED_IMAGES'])
        AndroidActions(driver).click_button(*locators['MANAGE_FEATURED_IMAGES'])
        time.sleep(5)
        AndroidActions(driver).wait_for_element(*locators['DELETE_CAROUSEL_IMAGE'])
        AndroidActions(driver).click_button(*locators['DELETE_CAROUSEL_IMAGE'])
        time.sleep(5)
        AndroidActions(driver).wait_for_element(*locators['DELETE_POPUP_HEADER'])
        AndroidActions(driver).wait_for_element(*locators['CONFIRM_DELETE_POPUP'])
        AndroidActions(driver).click_button(*locators['CONFIRM_DELETE_POPUP'])
        time.sleep(10)
        AndroidActions(driver).wait_for_element(*locators['CAROUSAL_IMAGE_SAVE'])
        AndroidActions(driver).click_button(*locators['CAROUSAL_IMAGE_SAVE'])
        time.sleep(10)

    def re_Arranging_Image(self, driver):
        AndroidActions(driver).wait_for_element(*locators['MANAGE_FEATURED_IMAGES'])
        AndroidActions(driver).click_button(*locators['MANAGE_FEATURED_IMAGES'])
        AndroidActions(driver).wait_for_element(*locators['REORDER'])
        AndroidActions(driver).click_button(*locators['REORDER'])  
        time.sleep(10)
        Rearrange = AndroidActions(driver).wait_for_element(*locators['REARRANGE_IMAGE'])
        if Rearrange:
            self.driver.execute_script("arguments[0].click();", Rearrange)
        AndroidActions(driver).wait_for_element(*locators['SAVE_CHANGES'])
        AndroidActions(driver).click_button(*locators['SAVE_CHANGES'])

    def add_Swimlane(self, driver, swimlanename, projectname):
        try:
            AndroidActions(driver).wait_for_element(*locators['ADD_SWIMLANE'])
        except Exception:
            pass
        AndroidActions(driver).click_button(*locators['ADD_SWIMLANE'])
        time.sleep(10)
        Swimlanes = AndroidActions(driver).wait_for_elements(*locators['EDIT_ICON'])
        Last_Element = None
        for swimlane in Swimlanes:
            preceding_text = swimlane.find_element(*locators['SWIMLANE_TEXT']).text
            if "SWIMLANE" in preceding_text:
                Last_Element = swimlane 
        time.sleep(10) 
        Last_Element.click()
        time.sleep(10)
        time.sleep(10)
        AndroidActions(driver).wait_for_element(*locators["EDIT_SWIMLANE_PROJECT_NAME"])
        AndroidActions(driver).click_button(*locators["EDIT_SWIMLANE_PROJECT_NAME"])
        time.sleep(10)
        time.sleep(10)
        AndroidActions(driver).enter_text(*locators["ENTER_SWIMLANE_NAME"], swimlanename)
        time.sleep(10)
        AndroidActions(driver).wait_for_element(*locators["SEARCH_PROJECT"])
        AndroidActions(driver).enter_text(*locators["SEARCH_PROJECT"], projectname)
        AndroidActions(driver).wait_for_element(*locators["SELECT_SEARCH_PROJECT"])
        AndroidActions(driver).click_button(*locators["SELECT_SEARCH_PROJECT"])
        time.sleep(10)
        AndroidActions(driver).click_button(*locators["SAVE_SWIMLANE_PROJECT"])
        time.sleep(10)
        time.sleep(10)

    def edit_swimlane(self, driver, swimlanename, projectname):
        AndroidActions(driver).wait_for_element(*locators['ADD_SWIMLANE'])
        time.sleep(10)
        Swimlanes = AndroidActions(driver).wait_for_elements(*locators['EDIT_ICON'])
        Last_Element = None
        swimlanename_before_editing = readPreReqJsonValue("prereq", "new_admin_swimlane_name")
        for swimlane in Swimlanes:
            preceding_text = swimlane.find_element(*locators['SWIMLANE_TEXT']).text
            if swimlanename_before_editing in preceding_text:
                Last_Element = swimlane 
        time.sleep(10)  
        Last_Element.click()
        time.sleep(10)
        time.sleep(10)
        self.actions.wait_for_element(*locators["EDIT_SWIMLANE_PROJECT_NAME"])
        AndroidActions(driver).click_button(*locators["EDIT_SWIMLANE_PROJECT_NAME"])
        time.sleep(10)
        time.sleep(10)
        AndroidActions(driver).enter_text(*locators["ENTER_SWIMLANE_NAME"], swimlanename)
        time.sleep(10)
        self.actions.wait_for_element(*locators["SEARCH_PROJECT"])
        AndroidActions(driver).enter_text(*locators["SEARCH_PROJECT"], projectname)
        self.actions.wait_for_element(*locators["SELECT_SEARCH_PROJECT"])
        AndroidActions(driver).click_button(*locators["SELECT_SEARCH_PROJECT"])
        time.sleep(10)
        AndroidActions(driver).click_button(*locators["SAVE_SWIMLANE_PROJECT"])
        time.sleep(10)

    def remove_project_from_swimlane(self, driver, projectname):
        AndroidActions(driver).wait_for_element(*locators['ADD_SWIMLANE'])
        time.sleep(10)
        Swimlanes = AndroidActions(driver).wait_for_elements(*locators['EDIT_ICON'])
        First_Element = None
        swimlanename_after_editing = readPreReqJsonValue("prereq", "fyc_admin_edited_swimlane_name")
        for swimlane in Swimlanes:
            preceding_text = swimlane.find_element(*locators['SWIMLANE_TEXT']).text
            if swimlanename_after_editing in preceding_text:
                First_Element = swimlane
        time.sleep(10)  
        First_Element.click()
        time.sleep(10)
        time.sleep(10)
        AndroidActions(driver).wait_for_element(*locators["REMOVE_PROJECT"])
        AndroidActions(driver).click_button(*locators["REMOVE_PROJECT"])
        time.sleep(10)
        AndroidActions(driver).click_button(*locators["SAVE_SWIMLANE_PROJECT"])
        time.sleep(10)
        time.sleep(10)
        
    def delete_swimlane(self, driver):
        Swimlanes = AndroidActions(driver).wait_for_elements(*locators['EDIT_ICON'])
        First_Element = None
        swimlanename_after_editing = readPreReqJsonValue("prereq", "fyc_admin_edited_swimlane_name")
        for swimlane in Swimlanes:
            preceding_text = swimlane.find_element(*locators['SWIMLANE_TEXT']).text
            if swimlanename_after_editing in preceding_text:
                First_Element = swimlane
        time.sleep(10)  
        First_Element.click()
        time.sleep(10)
        time.sleep(10)
        AndroidActions(driver).wait_for_element(*locators['DELETE_SWIMLANE'])
        AndroidActions(driver).click_button(*locators['DELETE_SWIMLANE'])
        try:
            AndroidActions(driver).click_button(*locators['DELETE_SWIMLANE'])
        except Exception:
            pass

    def rearranging_projects_within_swimlanes(self, driver, projectname):
        AndroidActions(driver).wait_for_element(*locators['ADD_SWIMLANE'])
        time.sleep(10)
        Swimlanes = AndroidActions(driver).wait_for_elements(*locators['EDIT_ICON'])
        Last_Element = None
        swimlanename_after_editing = readPreReqJsonValue("prereq", "fyc_admin_edited_swimlane_name")
        for swimlane in Swimlanes:
            preceding_text = swimlane.find_element(*locators['SWIMLANE_TEXT']).text
            if swimlanename_after_editing in preceding_text:
                Last_Element = swimlane
        time.sleep(10)  
        Last_Element.click()
        time.sleep(10)
        time.sleep(10)
        AndroidActions(driver).wait_for_element(*locators["SEARCH_PROJECT"])
        AndroidActions(driver).enter_text(*locators["SEARCH_PROJECT"], projectname)
        AndroidActions(driver).wait_for_element(*locators["SELECT_SEARCH_PROJECT_2"])
        AndroidActions(driver).click_button(*locators["SELECT_SEARCH_PROJECT_2"])
        time.sleep(10)
        by, value = locators["PROJECT_NAME"]
        format_value = value.format(project_name=projectname)
        AndroidActions(driver).click_button(by, format_value)
        AndroidActions(driver).wait_for_element(*locators["REARRANGE_PROJECTS"])
        AndroidActions(driver).click_button(*locators["REARRANGE_PROJECTS"])
        time.sleep(10)
        AndroidActions(driver).click_button(*locators["SAVE_SWIMLANE_PROJECT"])
        time.sleep(10)
        time.sleep(10)

    def reorder_Swimlanes(self, driver):
        time.sleep(10)
        Rearrange = AndroidActions(driver).wait_for_element(*locators['RE_ARRANGE_SWIMLANE_ICON'])
        self.driver.execute_script("arguments[0].click();", Rearrange)
        time.sleep(10)
        Swimlanes = AndroidActions(driver).wait_for_elements(*locators["MOVE_SWIMELANE_UP"])
        Length_Of_Swimlanes = len(Swimlanes)
        if Length_Of_Swimlanes > 0:
            for i in range(Length_Of_Swimlanes):
                if i != Length_Of_Swimlanes:
                    Swimlane_last = Swimlanes[Length_Of_Swimlanes - 1]
                    self.driver.execute_script("arguments[0].click();", Swimlane_last)
                    print('button clicked')
                    time.sleep(8) 
            Save_button = AndroidActions(driver).wait_for_element(*locators["SAVE_SWIMLANE_REARRANGE"]) 
            if Save_button:
                self.driver.execute_script("arguments[0].click();", Save_button)
                try:
                    AndroidActions(driver).click_button(*locators["SAVE_SWIMLANE_REARRANGE"])
                except Exception:
                    pass
            print('save button clicked')
            AndroidActions(driver).click_button(*locators["CANCEL_SWIMLANE_REARRANGE"])
            try:
                AndroidActions(driver).click_button(*locators["CANCEL_SWIMLANE_REARRANGE"])
            except Exception:
                pass
            time.sleep(10)
        else:
            print("No swimlanes to move.")
        time.sleep(10)

    def launch_nimaad_link(self):
        print("I launch nimaad URL")

    def enter_credentials(self, driver, username, password):
        AndroidActions(driver).enter_text(*locators["USERNAME_NIMAAD"], username) 
        AndroidActions(driver).enter_text(*locators["PASSWORD_NIMAAD"], password)   
        AndroidActions(driver).click_button(*locators["SIGN_IN_NIMAAD"])
  
    def navigate_to_api_section(self, driver):
        AndroidActions(driver).wait_for_element(*locators["API_KEY_SECTION"])
        AndroidActions(driver).click_button(*locators["API_KEY_SECTION"])

    def navigate_to_api_Key(self, driver, request):
        platform = request.config.getoption("--platform")
        field_fire_tv = readPreReqJsonValue("prereq", "fyc_api_fire_tv").format(readConstants("QA_SERVER"))
        field_ipad = readPreReqJsonValue("prereq", "fyc_api_ipad").format(readConstants("QA_SERVER"))
        field_roku = readPreReqJsonValue("prereq", "fyc_api_roku").format(readConstants("QA_SERVER"))
        if platform == "fire_tv":
            by, value = locators["API_KEY"]
            format_value = value.format(field_name=field_fire_tv)
            Element = AndroidActions(driver).wait_for_element(by, format_value)
            Element.click()
        elif platform == "ipad":
            by, value = locators["API_KEY"]
            format_value = value.format(field_name=field_ipad)
            Element = AndroidActions(driver).wait_for_element(by, format_value)
            Element.click()
        else:
            by, value = locators["API_KEY"]
            format_value = value.format(field_name=field_roku)
            Element = AndroidActions(driver).wait_for_element(by, format_value)
            Element.click()

    def modify_expiry_date(self, driver, Api_expiry_date):
        AndroidActions(driver).wait_for_element(*locators["EXPIRY_DATE"])
        AndroidActions(driver).enter_text(*locators["EXPIRY_DATE"], Api_expiry_date) 
        Expiry_Date = self.driver.find_element(*locators["EXPIRY_DATE"])  
        Expiry = Expiry_Date.get_attribute("value")
        time.sleep(3)
        AndroidActions(driver).click_button(*locators["SAVE_DATE"])
        return Expiry
    
    def delete_api_key(self, driver):
        AndroidActions(driver).wait_for_element(*locators["DELETE_API"])
        AndroidActions(driver).click_button(*locators["DELETE_API"]) 
        AndroidActions(driver).click_button(*locators['CONFIRM_DELETE'])

    def navigate_to_add_api(self, driver):
        AndroidActions(driver).wait_for_element(*locators['ADD_API_KEY'])
        AndroidActions(driver).click_button(*locators['ADD_API_KEY'])

    def add_api_key(self, driver, request):
        platform = request.config.getoption("--platform")
        new_api_expiry = readPreReqJsonValue("prereq", "fyc_new_api_expiry_date")
        new_api_time = readPreReqJsonValue("prereq", "fyc_new_api_time")
        field_fire_tv = readPreReqJsonValue("prereq", "fyc_api_fire_tv").format(readConstants("QA_SERVER"))
        field_ipad = readPreReqJsonValue("prereq", "fyc_api_ipad").format(readConstants("QA_SERVER"))
        field_roku = readPreReqJsonValue("prereq", "fyc_api_roku").format(readConstants("QA_SERVER"))
        AndroidActions(driver).wait_for_element(*locators["EXPIRY_DATE"])
        AndroidActions(driver).enter_text(*locators["EXPIRY_DATE"], new_api_expiry)
        AndroidActions(driver).enter_text(*locators['TIME'], new_api_time)
        if platform == "fire_tv":
            AndroidActions(driver).enter_text(*locators['API_NAME'], field_fire_tv)
        elif platform == "ipad":
            AndroidActions(driver).enter_text(*locators['API_NAME'], field_ipad)
        else:
            AndroidActions(driver).enter_text(*locators['API_NAME'], field_roku)
        AndroidActions(driver).click_button(*locators["API_WATCH_PRODUCT"])
        AndroidActions(driver).click_button(*locators['WATCH_PRODUCT_FYC'])
        permissions = Select(AndroidActions(driver).wait_for_element(*locators["PERMISSIONS"]))
        permissions.select_by_visible_text("content_access")
        permissions.select_by_visible_text("app_config_access")
        permissions.select_by_visible_text("account_creation_access")
        permissions.select_by_visible_text("password_reset_access")
        AndroidActions(driver).click_button(*locators["WATCH_DOMAIN"])
        waytchDomainValue = locators['WATCH_DOMAIN_FYC'][1].format(readConstants("QA_SERVER"))
       
        AndroidActions(driver).click_button(locators['WATCH_DOMAIN_FYC'][0], waytchDomainValue)
        AndroidActions(driver).click_button(*locators["INTENDED_CLIENT"])
        by, value = locators["INTENDED_CLIENT_VALUE"]
        client_fire_tv = "Amazon Firestick"
        client_ipad = "iPad"
        client_roku = "Roku"
        if platform == "fire_tv":
            format_value = value.format(intended_client=client_fire_tv)
            Element = AndroidActions(driver).wait_for_element(by, format_value)
            Element.click()
        elif platform == "ipad":
            format_value = value.format(intended_client=client_ipad)
            Element = AndroidActions(driver).wait_for_element(by, format_value)
            Element.click()
        else:
            format_value = value.format(intended_client=client_roku)
            Element = AndroidActions(driver).wait_for_element(by, format_value)
            Element.click()
        AndroidActions(driver).click_button(*locators["ENTERPRISE"])
        AndroidActions(driver).click_button(*locators['ENTERPRISE_PARAMOUNT'])
        time.sleep(5)
        AndroidActions(driver).click_button(*locators['API_SAVE_BUTTON'])
        time.sleep(5)

    def navigate_to_watclist_product(self, driver):
        # AndroidActions(driver).wait_for_element(*locators["Expiry_date"])
        time.sleep(9)
        AndroidActions(driver).click_button(*locators["WATCHLIST_PRODUCT"])
        AndroidActions(driver).wait_for_element(*locators["PARAMOUNT_WATCHLIST"])
        AndroidActions(driver).click_button(*locators["PARAMOUNT_WATCHLIST"])

    # def navigate_to_watclist_product(self, driver):
    #    AndroidActions(driver).wait_for_element(*locators["Expiry_date"])
    #    AndroidActions(driver).click_button(*locators["WatchList_Product"])
    #    AndroidActions(driver).wait_for_element(*locators["Blackreelawards_Watclist"])
    #   AndroidActions(driver).click_button(*locators["Blackreelawards_Watclist"])

    def navigate_to_project_section(self, driver):
        AndroidActions(driver).wait_for_element(*locators["PROJECTS_SELECTION"])
        AndroidActions(driver).click_button(*locators["PROJECTS_SELECTION"])
        AndroidActions(driver).wait_for_element(*locators["ADD_NEW_PROJECT"])
        AndroidActions(driver).click_button(*locators["ADD_NEW_PROJECT"])
        time.sleep(5)

    def enter_details_in_project_section(self, driver, Project_Name, Description, Generes_Content):   
        time.sleep(5)
        print("Entering project details=====") 
        random_characters = random.choice(string.ascii_letters) + random.choice(string.digits)
        Project_Name = Project_Name + random_characters
        AndroidActions(driver).wait_for_element(*locators["NAME_OF_THE_PROJECT"])
        AndroidActions(driver).enter_text(*locators["NAME_OF_THE_PROJECT"], Project_Name)
        AndroidActions(driver).wait_for_element(*locators["PROJECT_DESCRIPTION"])
        AndroidActions(driver).enter_text(*locators["PROJECT_DESCRIPTION"], Description)
        AndroidActions(driver).wait_for_element(*locators["GENRES_CONTENT"])
        AndroidActions(driver).enter_text(*locators["GENRES_CONTENT"], Generes_Content)
        AndroidActions(driver).wait_for_element(*locators["COMEDY_DROP_DOWN"])
        AndroidActions(driver).click_button(*locators["COMEDY_DROP_DOWN"])
        AndroidActions(driver).wait_for_element(*locators["SUBMIT_PROJECT_DETAILS"])
        AndroidActions(driver).click_button(*locators["SUBMIT_PROJECT_DETAILS"])
        return Project_Name

    def enter_details_in_video_section(self, driver, video_name):
        AndroidActions(driver).wait_for_element(*locators["VIDEO_NAME"])
        AndroidActions(driver).enter_text(*locators["VIDEO_NAME"], video_name)
        video_upload = AndroidActions(driver).wait_for_element(*locators["VIDEO_UPLOAD"])
        user_directory = os.getcwd()
        video_path = os.path.join(user_directory, 'AdminData', 'publish', 'video.mp4').replace('\\', '/')
        # video_path = "D:\Latest-code\Indee_App_Automation\AdminData\publish\video"
        video_upload.send_keys(video_path)
        AndroidActions(driver).wait_for_element(*locators["UPLOAD_BUTTON"])
        AndroidActions(driver).click_button(*locators["UPLOAD_BUTTON"])
        time.sleep(80)
        AndroidActions(driver).wait_for_element(*locators["SAVE_AND_NEXT"])
        AndroidActions(driver).click_button(*locators["SAVE_AND_NEXT"])
        AndroidActions(driver).wait_for_element(*locators["FINISH_UPLOAD"])
        AndroidActions(driver).click_button(*locators["FINISH_UPLOAD"])
        time.sleep(5)
        print("Finish the upload")
        self.wait_for_trancoding(driver)

    def send_screeners_to_publish(self, driver):
        pin_selection = readPreReqJsonValue("prereq", "fyc_admin_pin") 
        AndroidActions(driver).wait_for_element(*locators["SEND_SCREENERS"])
        AndroidActions(driver).click_button(*locators["SEND_SCREENERS"])
        AndroidActions(driver).wait_for_element(*locators["FYC_SEND_SCREENERS"])
        AndroidActions(driver).click_button(*locators["FYC_SEND_SCREENERS"])
        time.sleep(20)
        by, value = locators["BUILD_SELECTION"]
        format_value = value.format(pin_value=pin_selection)
        AndroidActions(driver).click_button(by, format_value)
        AndroidActions(driver).wait_for_element(*locators["SELECT_ALL"], timeout=120)
        AndroidActions(driver).click_button(*locators["SELECT_ALL"])
        AndroidActions(driver).wait_for_element(*locators["PROCEED_UPLOAD"])
        AndroidActions(driver).click_button(*locators["PROCEED_UPLOAD"])
        AndroidActions(driver).wait_for_element(*locators["NO_SECURITY"])
        AndroidActions(driver).click_button(*locators["NO_SECURITY"])
        time.sleep(5)
        AndroidActions(driver).wait_for_element(*locators["PROCEED_UPLOAD"])
        AndroidActions(driver).click_button(*locators["PROCEED_UPLOAD"])
        time.sleep(5)
        Upload_button = AndroidActions(driver).wait_for_element(*locators["PROCEED_UPLOAD"])
        if Upload_button:
            AndroidActions(driver).click_button(*locators["PROCEED_UPLOAD"])
            time.sleep(10)
        else:
            pass

    def select_brand_to_publish(self, driver, Project_Name):
        time.sleep(10)
        pyautogui.scroll(-300)
        AndroidActions(driver).wait_for_element(*locators['APPLICATION_MANAGER'])
        AndroidActions(driver).click_button(*locators['APPLICATION_MANAGER'])
        time.sleep(10)
        AndroidActions(driver).wait_for_element(*locators['FYC_REDIRECTION'])
        AndroidActions(driver).click_button(*locators['FYC_REDIRECTION'])
        time.sleep(10)
        try:
            pin_selection = readPreReqJsonValue("prereq", "fyc_admin_pin") 
            by, value = locators["PIN_SELECTION"]
            format_value = value.format(pin_value=pin_selection)
            print(format_value)
            for i in range(5):
                audience_selection = AndroidActions(driver).is_element_displayed(by, format_value)
                print(audience_selection)
                if audience_selection:
                    break
                else:
                    AndroidActions(driver).click_button(*locators['BRAND_NEXT_PAGE'])
            AndroidActions(driver).click_button(by, format_value)
            AndroidActions(driver).wait_for_element(*locators['SELECT_BRAND'])
        except Exception:
            AndroidActions(driver).wait_for_element(*locators['NEW_BUTTON'])  # noqa:E501
            AndroidActions(driver).click_button(*locators['NEW_BUTTON'])  # noqa:E501
            time.sleep(5)
            pin = readPreReqJsonValue("prereq", "fyc_execution_id")
            Search_field = AndroidActions(driver).wait_for_element(*locators['SEARCH_AUDIENCE']) 
            AndroidActions(driver).enter_text(*locators['SEARCH_AUDIENCE'], pin)
            Search_field.send_keys(Keys.ENTER)
            time.sleep(5)
            pin_selection = readPreReqJsonValue("prereq", "fyc_admin_pin") 
            by, value = locators["PIN_EXECUTION"]
            format_value = value.format(pin_value=pin_selection)
            AndroidActions(driver).click_button(by, format_value)
        time.sleep(10)
        brand_selection = readPreReqJsonValue("prereq", "fyc_brand_to_replace") 
        by, value = locators["BRAND_EXECUTION"]
        format_value = value.format(brand_value=brand_selection)
        for i in range(50):
            print('Inside loop')
            Brand = AndroidActions(driver).is_element_displayed(by, format_value)  # noqa:E501
            if Brand:
                break
            else:
                AndroidActions(driver).click_button(*locators['BRAND_NEXT_PAGE'])
        AndroidActions(driver).wait_for_element(by, format_value)
        AndroidActions(driver).click_button(by, format_value)
        for i in range(2):
            try:
                AndroidActions(driver).click_button(by, format_value)
            except Exception:
                pass
        time.sleep(20)
        brand_value = readPreReqJsonValue("prereq", "fyc_pin_to_replace_in_url") 
        brand_to_replace = readPreReqJsonValue("prereq", "fyc_admin_brand_pin_value") 
        current_url = self.driver.current_url
        print(current_url)
        updated_url = current_url.replace(brand_value, brand_to_replace)
        print(updated_url)
        self.driver.get(updated_url)  
        # current_url = self.driver.current_url
        # updated_url = current_url.replace('%2F', '/').replace('?page=34', '')
        # self.driver.get(updated_url)
        time.sleep(10)
        try:
            AndroidActions(driver).wait_for_element(*locators['START_FRESH'])
            AndroidActions(driver).click_button(*locators['START_FRESH'])
        except Exception:
            pass
        time.sleep(10)
        AndroidActions(driver).wait_for_element(*locators['MANAGE'])
        AndroidActions(driver).click_button(*locators['MANAGE'])
        Search_field = AndroidActions(driver).wait_for_element(*locators["SEARCH_FOR_THE_PROJECT"])
        AndroidActions(driver).enter_text(*locators["SEARCH_FOR_THE_PROJECT"], Project_Name)
        Search_field.send_keys(Keys.ENTER)
        by, value = locators['PROJECT_SEARCH_DROPDOWN']
        format_value = value.format(Project_Name)
        AndroidActions(driver).wait_for_element(by, format_value)
        AndroidActions(driver).click_button(by, format_value)
        by, value = locators['SEARCH_RESULTS']
        format_value = value.format(Project_Name)
        AndroidActions(driver).wait_for_element(by, format_value)
        AndroidActions(driver).click_button(by, format_value)
        AndroidActions(driver).wait_for_element(*locators['SAVE_BUTTON'])
        AndroidActions(driver).click_button(*locators['SAVE_BUTTON'])
        time.sleep(20)

    def search_project_to_delete(self, driver, Project_Name):
        Search_field = AndroidActions(driver).wait_for_element(*locators["SEARCH_FOR_THE_PROJECT"])
        AndroidActions(driver).enter_text(*locators["SEARCH_FOR_THE_PROJECT"], Project_Name)
        Search_field.send_keys(Keys.ENTER)

    def navigate_to_project_to_delete(self, driver, Project_Name):
        AndroidActions(driver).wait_for_element(locators["PROJECT_SEARCH_RESULTS"][0], locators["PROJECT_SEARCH_RESULTS"][1].format(project_name=Project_Name))
        AndroidActions(driver).click_button(locators["PROJECT_SEARCH_RESULTS"][0], locators["PROJECT_SEARCH_RESULTS"][1].format(project_name=Project_Name))
        AndroidActions(driver).wait_for_element(*locators["EDIT_PROJECT"])
        AndroidActions(driver).click_button(*locators["EDIT_PROJECT"])
        AndroidActions(driver).wait_for_element(*locators["DELETE_PROJECT"])
        AndroidActions(driver).click_button(*locators["DELETE_PROJECT"])
        AndroidActions(driver).wait_for_element(*locators["CONTINUE_DELETE"])
        AndroidActions(driver).click_button(*locators["CONTINUE_DELETE"])

    def search_project_to_publish(self, driver, Project_Name):
        Search_field = AndroidActions(driver).wait_for_element(*locators["SEARCH_FOR_THE_PROJECT"])
        AndroidActions(driver).enter_text(*locators["SEARCH_FOR_THE_PROJECT"], Project_Name)
        Search_field.send_keys(Keys.ENTER)

    def navigate_to_project_to_publish(self, driver, Project_Name):
        AndroidActions(driver).wait_for_element(locators["PROJECT_SEARCH_RESULTS"][0], locators["PROJECT_SEARCH_RESULTS"][1].format(project_name=Project_Name))
        AndroidActions(driver).click_button(locators["PROJECT_SEARCH_RESULTS"][0], locators["PROJECT_SEARCH_RESULTS"][1].format(project_name=Project_Name))

    def navigate_to_project_to_delete_the_video(self, driver, Project_Name):
        AndroidActions(driver).wait_for_element(locators["PROJECT_SEARCH_RESULTS"][0], locators["PROJECT_SEARCH_RESULTS"][1].format(project_name=Project_Name))
        AndroidActions(driver).click_button(locators["PROJECT_SEARCH_RESULTS"][0], locators["PROJECT_SEARCH_RESULTS"][1].format(project_name=Project_Name))
        AndroidActions(driver).wait_for_element(*locators["VIDEO_DELETE"])
        AndroidActions(driver).click_button(*locators["VIDEO_DELETE"])
        AndroidActions(driver).wait_for_element(*locators["DELETE_VIDEO_POPUP_HEADER"])
        AndroidActions(driver).click_button(*locators["DELETE_VIDEO_POPUP_HEADER"])
        AndroidActions(driver).wait_for_element(*locators["DELETE_VIDEO_CONTINUE"])
        AndroidActions(driver).click_button(*locators["DELETE_VIDEO_CONTINUE"])

    def navigate_to_project_to_unpublish(self, driver, Project_Name):
        pin_selection = readPreReqJsonValue("prereq", "fyc_admin_pin") 
        AndroidActions(driver).wait_for_element(locators["PROJECT_SEARCH_RESULTS"][0], locators["PROJECT_SEARCH_RESULTS"][1].format(project_name=Project_Name))
        AndroidActions(driver).click_button(locators["PROJECT_SEARCH_RESULTS"][0], locators["PROJECT_SEARCH_RESULTS"][1].format(project_name=Project_Name))
        AndroidActions(driver).wait_for_element(*locators["SEND_SCREENERS"])
        AndroidActions(driver).click_button(*locators["SEND_SCREENERS"])
        AndroidActions(driver).wait_for_element(*locators["FYC_SEND_SCREENERS"])
        AndroidActions(driver).click_button(*locators["FYC_SEND_SCREENERS"])
        time.sleep(10)
        AndroidActions(driver).wait_for_element(*locators['UNPUBLISH'])
        AndroidActions(driver).click_button(*locators["UNPUBLISH"])
        by, value = locators["BUILD_SELECTION"]
        format_value = value.format(pin_value=pin_selection)
        AndroidActions(driver).click_button(by, format_value)
        AndroidActions(driver).wait_for_element(*locators["UNPUBLISH_SELECT_ALL"], timeout=120)
        AndroidActions(driver).click_button(*locators["UNPUBLISH_SELECT_ALL"])
        AndroidActions(driver).wait_for_element(*locators["PROCEED_UPLOAD"])
        AndroidActions(driver).click_button(*locators["PROCEED_UPLOAD"])
        print('clickedd proceed')
        AndroidActions(driver).wait_for_element(*locators["NO_SECURITY"])
        AndroidActions(driver).click_button(*locators["NO_SECURITY"])
        time.sleep(5)
        AndroidActions(driver).wait_for_element(*locators["BUTTON_UNPUBLISH"])
        AndroidActions(driver).click_button(*locators["BUTTON_UNPUBLISH"])
        time.sleep(5)
        unpublish = AndroidActions(driver).wait_for_element(*locators["BUTTON_UNPUBLISH"])
        if unpublish:
            AndroidActions(driver).click_button(*locators["BUTTON_UNPUBLISH"])
            time.sleep(10)
        print('clicked unpublish')

    def verify_project_unpublished_in_admin(self, driver):
        time.sleep(10)
        print('unpuublished')
        success_icon = AndroidActions(driver).wait_for_element(*locators['UNPUBLISH_SUCCESS_TICK'])
        time.sleep(10)
        success_message = AndroidActions(driver).wait_for_element(*locators["UNPUBLISH_SUCCESS_MESSAGE"])
        if all([success_icon, success_message]):
            return True
        else:
            return False

    def verify_deleted_project(self, driver, Project_Name):
        Search_field = AndroidActions(driver).wait_for_element(*locators["SEARCH_FOR_THE_PROJECT"])
        AndroidActions(driver).enter_text(*locators["SEARCH_FOR_THE_PROJECT"], Project_Name)
        Search_field.send_keys(Keys.ENTER)
        unpublished_project = AndroidActions(driver).get_text(*locators["NO_SEARCH_RESULTS"])
        return unpublished_project
    
    def verify_video_inside_the_project_is_deleted(self, driver, Project_Name):
        AndroidActions(driver).wait_for_element(*locators['PROJECTS'])
        AndroidActions(driver).click_button(*locators['PROJECTS'])
        Search_field = AndroidActions(driver).wait_for_element(*locators["SEARCH_FOR_THE_PROJECT"])
        AndroidActions(driver).enter_text(*locators["SEARCH_FOR_THE_PROJECT"], Project_Name)
        Search_field.send_keys(Keys.ENTER)
        return self.actions.is_element_displayed(*locators['NO_VIDEOS_IN_PROJECT'])
    
    def disable_checkbox_watchlist(self, driver):
        time.sleep(8)
        Watchlist = self.driver.find_element(*locators["WATCHLIST_CHECKBOX"])
        watchlist_enabled = Watchlist.is_selected()
        if watchlist_enabled:
            AndroidActions(driver).click_button(*locators["WATCHLIST_CHECKBOX"])
            time.sleep(8)
        AndroidActions(driver).click_button(*locators["NIMAAD_SAVE_BUTTON"])
        time.sleep(3)
        return True
    
    def enable_checkbox_watchlist(self, driver):
        time.sleep(8)
        Watchlist = self.driver.find_element(*locators["WATCHLIST_CHECKBOX"])
        watchlist_enabled = Watchlist.is_selected()
        if not watchlist_enabled:
            AndroidActions(driver).click_button(*locators["WATCHLIST_CHECKBOX"])
            time.sleep(8)
        AndroidActions(driver).click_button(*locators["NIMAAD_SAVE_BUTTON"])
        time.sleep(3)
        return True

    def disable_checkbox_resume_playback(self, driver):
        time.sleep(8)
        Watchlist = self.driver.find_element(*locators["RESUME_PLAYBACK"])
        watchlist_enabled = Watchlist.is_selected()
        print(watchlist_enabled)
        if watchlist_enabled:
            AndroidActions(driver).click_button(*locators["RESUME_PLAYBACK"])
            time.sleep(8)
        AndroidActions(driver).click_button(*locators["NIMAAD_SAVE_BUTTON"])
        time.sleep(3)
        return True
    
    def enable_checkbox_resume_playback(self, driver):
        time.sleep(8)
        Watchlist = self.driver.find_element(*locators["RESUME_PLAYBACK"])
        watchlist_enabled = Watchlist.is_selected()
        print(watchlist_enabled)
        if not watchlist_enabled:
            AndroidActions(driver).click_button(*locators["RESUME_PLAYBACK"])
            time.sleep(8)
        AndroidActions(driver).click_button(*locators["NIMAAD_SAVE_BUTTON"])
        time.sleep(3)
        return True
    
    def wait_for_trancoding(self, driver):
        AndroidActions(driver).is_element_displayed(*locators["VIDEO_ID"])
        print("status of the tanscoding")
        Status = AndroidActions(driver).is_element_displayed(*locators["TRANSCODING_PROGRESS"])
        print(Status)
        while (Status):
            print("Waiting for transcoding")
            time.sleep(20)
            self.driver.refresh()
            Status = AndroidActions(driver).is_element_displayed(*locators["TRANSCODING_PROGRESS"])       
        print("Transcoding completed")
