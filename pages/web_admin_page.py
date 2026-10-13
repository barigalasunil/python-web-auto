import logging
import random
import string
from pages.base_page import BasePage
from pages.actions.webpage_actions import WebAppActions

logger = logging.getLogger("framework")


locators = {
    "CLIENT_EMAIL_FIELD": (".//input[@name='username']"),
    "INTERNAL_EMAIL_FIELD": (".//input[@name='staff']"),
    "INTERNAL_PASSWORD_FIELD": (".//input[@name='password']"),
    "SIGN_IN": (".//button[contains(@class, 'sign-in-button')]"),
    "APPLICATION_MANAGER": (".//a[contains(@class, 'projects-link') and contains(@class, 'small-blue-button')]")[1],
    "GLOBAL_DESCRIPTION_REDIRECTION": "a[href*=brands]",
    "LAUNCH_APP_EDITOR": ".//span[text()='LAUNCH APP EDITOR']",
    "MANAGE_FEATURED_IMAGES": "b[text()='MANAGE FEATURED IMAGES']",
    "EDIT_ICON": ".//button[contains(@class, 'edit-icon-wrapper') and starts-with(@id, 'edit_swimlane')]",
    "EDIT_SWIMLANE_PROJECT_NAME": ".//div[contains(@class, 'swimlane-wrapper w-')]//span[2]",
    "ENTER_SWIMLANE_NAME": ".//input[@placeholder='Swimlane Name']",
    "SELECT_SEARCH_PROJECT": ".//div[contains(@class, 'swimlane relative m-')]",
    "SELECT_SEARCH_PROJECT_2": ".//div[contains(@class, 'swimlane relative m-4 smallCards')]",
    "IMAGE_UPLOAD": ".//input[@id='feature_image']",
    "CROP": ".//button//span[text()=' CROP ']",
    "NOCTURNAL_PROJECT": ".//div[@data-tippy-content='Nocturnal Animals']",
    "REARRANGE_PROJECTS": ".//div[contains(@class, 'cursor-pointer') and contains(@class, 'text-2xl') and contains(@class, 'p-1')]//span[text()='❮']",
    "DELETE_NEW_IMAGE": ".//div[@id='bannerImageWrapper-0']//span[@id='deleteImg-0']",
    "DELETE_IMAGE": ".//button//p[text()='DELETE FEATURED IMAGE']",
    "DELETE_BUTTON": ".//button//span[text()=' DELETE ']",
    "PROJECTS_SELECTION": ".//a[contains(@class, 'projects-link')]")[1],
    "ADD_NEW_PROJECT": ".//span[@class='icon icon-add-item']",
    "NAME_OF_THE_PROJECT": ".//input[@placeholder='Name of your project']",
    "PROJECT_DESCRIPTION": ".//div[@data-placeholder='Provide a synopsis for your project']",
    "GENRES_CONTENT": ".//input[@class='search-input']",
    "SUBMIT_PROJECT_DETAILS": ".//button[contains(@class, 'i-button large-button animated')]",
    "VIDEO_NAME": ".//input[@id='videoname-input']",
    "VIDEO_UPLOAD": ".//input[@type='file' and @name='video']",
    "UPLOAD_BUTTON": ".//button[@type='submit' and @name='submit']",
    "COMEDY_DROP_DOWN": ".//div[contains(text(),'Action')]")[1],
    "SAVE_AND_NEXT": ".//button[@type='button' and @name='SAVE']",
    "FINISH_UPLOAD": ".//button[contains(@class, 'i-button large-button animated')]",
    "SEND_SCREENERS": ".//li[@class='send-screener-item']",
    "GD_SEND_SCREENERS": ".//div[contains(text(),'GLOBAL DISTRIBUTION')]",
    "SELECT_ALL": ".//input[@type='checkbox']")[2],
    "PROCEED_UPLOAD": ".//button[@class='btn btn-proceed']",
    "SEARCH_FOR_THE_PROJECT": ".//input[@placeholder='Search for a project']",
    "PROJECT_SEARCH_RESULTS": '//a[@data-tippy-content="{project_name}"]',
    "EDIT_PROJECT": ".//a[contains(text(),'Edit Project')]",
    "DELETE_PROJECT": ".//p[@class='error-text delete-button pointer']",
    "CONTINUE_DELETE": ".//span[text()='Continue']",
    "NO_SEARCH_RESULTS": ".//h3[text()='NO SEARCH RESULTS FOUND']",
    "REORDER": ".//p[text()='REORDER']",
    "REARRANGE_IMAGE": ".//div[@id='moveImgRight-0' and @title='Move Image To Right']",
    "SAVE_CHANGES": ".//button[@class='save-button']",
    "ADD_SWIMLANE": ".//input[@id='add_swimlane']",
    "ADD_SWIMLANE_SECTION_ICON": ".//input[@id='edit_swimlane_116']",
    "AUTOMATION_GD_PROJECT": ".//div[@data-tippy-content='AutomationGD']",
    "SEARCH_PROJECT": ".//input[@placeholder='Search for a project']",
    "REMOVE_PROJECT": ".//div[@data-tippy-content='{}']//following::span[@title='Remove Project']",  # noqa:E501
    "SAVE_SWIMLANE_PROJECT": ".//button[contains(@class, 'save-btn-bg')]",  # noqa:E501
    "RE_ARRANGE_SWIMLANE_ICON": ".//id='reArrangeSwimlaneImage'",
    "MOVE_SWIMELANE_UP": ".//div[@title='Move Swimlane Up']",
    "SAVE_SWIMLANE_REARRANGE": ".//button[@class='save-button']",
    "CANCEL_SWIMLANE_REARRANGE": ".//button[@class='cancel-button']",
    "DELETE_SWIMLANE": ".//button[contains(@class, 'delete-icon')]",
    "WATCH_ON_TV": ".//button[@class='tv-btn']",
    "ACCESS_CODE": ".//div//span[@class='code']",
    "DELETE_CAROUSEL_IMAGE": ".//button[.//p[text()='DELETE FEATURED IMAGE']]",
    "DELETE_POPUP_HEADER": ".//p[contains(text(), 'Deleting will remove all the featured images')]",
    "CONFIRM_DELETE_POPUP": ".//button[.//span[text()=' DELETE ']]",
    "NEXT_CAROUSEL_IMAGE": '(//*[@data-icon="angle-right"])[2]',
    "PROJECT_NAME": ".//div[contains(@data-tippy-content, '{project_name}')]",
    "CAROUSAL_IMAGE_SAVE": ".//button[contains(text(), 'SAVE') and contains(text(), 'EXIT')]",
    "TRANSCODING_PROGRESS": ".//p[normalize-space()='Transcoding in Progress']",
    "VIDEO_ID": ".//span[contains(normalize-space(),'ID:')]",
    "SWIMLANE_TEXT": "./preceding-sibling::span[contains(@class, 'font-bold')]",
    "load_more_swimlane_btn": ".//div[@class='swimlane-paginator' and contains(normalize-space(),'Load More Swimlanes')]"
}


class AdminPortalPage(BasePage):
    """Admin portal page using Playwright page object model."""

    def __init__(self, page):
        super().__init__(page)
        self.actions = WebAppActions(page)
        logger.info("AdminPortalPage initialized")

    def login_to_admin_portal(self, client_email, internal_email, password):
        """Login to the admin portal."""
        self.page.goto(self.page.url) if hasattr(self, 'page') and hasattr(self.page, 'url') else None
        self.actions.wait_for_selector(locators["CLIENT_EMAIL_FIELD"])
        self.actions.fill(locators["CLIENT_EMAIL_FIELD"], client_email)
        self.actions.fill(locators["INTERNAL_EMAIL_FIELD"], internal_email)
        self.actions.fill(locators["INTERNAL_PASSWORD_FIELD"], password)
        self.actions.click(locators["SIGN_IN"])
        logger.info("Admin portal login completed")
        self.actions.wait_for_selector(locators["APPLICATION_MANAGER"], timeout=120000)

    def navigate_To_GD_Portal(self):
        """Navigate to the Global Description portal."""
        self.actions.wait_for_selector(locators["APPLICATION_MANAGER"], timeout=120000)
        self.actions.click(locators["APPLICATION_MANAGER"])
        self.actions.wait_for_selector(locators["GLOBAL_DESCRIPTION_REDIRECTION"], timeout=120000)
        self.actions.click(locators["GLOBAL_DESCRIPTION_REDIRECTION"])
        self.actions.wait_for_selector(locators["LAUNCH_APP_EDITOR"], timeout=60000)
        logger.info("Navigated to GD portal")

    def upload_Image(self, image_file):
        """Upload an image to the admin portal."""
        self.actions.wait_for_selector(locators["MANAGE_FEATURED_IMAGES"], timeout=60000)
        self.actions.click(locators["MANAGE_FEATURED_IMAGES"])
        self.actions.wait_for_selector(locators["IMAGE_UPLOAD"], timeout=60000)
        user_directory = os.getcwd()
        image_path = os.path.join(user_directory, 'AdminData', image_file)
        self.actions.upload_file(locators["IMAGE_UPLOAD"], image_path)
        self.actions.click(locators["CROP"])
        self.actions.wait_for_selector(locators["CAROUSAL_IMAGE_SAVE"], timeout=60000)
        self.actions.click(locators["CAROUSAL_IMAGE_SAVE"])
        logger.info("Image uploaded successfully")

    def delete_image(self):
        """Delete the featured image."""
        self.actions.wait_for_selector(locators["MANAGE_FEATURED_IMAGES"], timeout=60000)
        self.actions.click(locators["MANAGE_FEATURED_IMAGES"])
        self.actions.wait_for_selector(locators["DELETE_CAROUSEL_IMAGE"], timeout=30000)
        self.actions.click(locators["DELETE_CAROUSEL_IMAGE"])
        self.actions.wait_for_selector(locators["DELETE_POPUP_HEADER"], timeout=10000)
        self.actions.wait_for_selector(locators["CONFIRM_DELETE_POPUP"], timeout=10000)
        self.actions.click(locators["CONFIRM_DELETE_POPUP"])
        self.actions.wait_for_selector(locators["CAROUSAL_IMAGE_SAVE"], timeout=60000)
        self.actions.click(locators["CAROUSAL_IMAGE_SAVE"])
        logger.info("Image deleted successfully")

    def add_project(self, project_name, description, genres_content):
        """Add a new project."""
        self.actions.click(locators["ADD_NEW_PROJECT"])
        self.actions.fill(locators["NAME_OF_THE_PROJECT"], project_name)
        self.actions.fill(locators["PROJECT_DESCRIPTION"], description)
        self.actions.fill(locators["GENRES_CONTENT"], genres_content)
        self.actions.click(locators["SUBMIT_PROJECT_DETAILS"])
        logger.info(f"Project added: {project_name}")

    def enter_details_in_project_section(self, Project_Name, Description, Generes_Content):
        """Enter details in the project section."""
        random_characters = random.choice(string.ascii_letters) + random.choice(string.digits)
        Project_Name = Project_Name + random_characters
        self.actions.wait_for_selector(locators["NAME_OF_THE_PROJECT"])
        self.actions.fill(locators["NAME_OF_THE_PROJECT"], Project_Name)
        self.actions.wait_for_selector(locators["PROJECT_DESCRIPTION"])
        self.actions.fill(locators["PROJECT_DESCRIPTION"], Description)
        self.actions.wait_for_selector(locators["GENRES_CONTENT"])
        self.actions.fill(locators["GENRES_CONTENT"], Generes_Content)
        self.actions.wait_for_selector(locators["COMEDY_DROP_DOWN"])
        self.actions.click(locators["COMEDY_DROP_DOWN"])
        self.actions.wait_for_selector(locators["SUBMIT_PROJECT_DETAILS"])
        self.actions.click(locators["SUBMIT_PROJECT_DETAILS"])
        return Project_Name

    def navigate_to_access_code_section(self):
        """Navigate to the access code section."""
        self.actions.wait_for_selector(locators["WATCH_ON_TV"])
        self.actions.click(locators["WATCH_ON_TV"])

    def fetch_access_code(self):
        """Fetch the access code from the cinema section."""
        self.actions.wait_for_selector(locators["ACCESS_CODE"])
        Access_code = self.actions.get_text(locators["ACCESS_CODE"])
        logger.info(f"Access code fetched: {Access_code}")
        return Access_code

    def navigate_to_project_section(self):
        """Navigate to the project section."""
        self.actions.wait_for_selector(locators["PROJECTS_SELECTION"])
        self.actions.click(locators["PROJECTS_SELECTION"])
        self.actions.wait_for_selector(locators["ADD_NEW_PROJECT"])
        self.actions.click(locators["ADD_NEW_PROJECT"])

    def enter_details_in_video_section(self, video_name):
        """Enter details in the video section."""
        self.actions.wait_for_selector(locators["VIDEO_NAME"])
        self.actions.fill(locators["VIDEO_NAME"], video_name)
        user_directory = os.getcwd()
        video_path = os.path.join(user_directory, 'AdminData', 'publish', 'video.mp4')
        video_upload = self.page.wait_for_selector(locators["VIDEO_UPLOAD"])
        video_upload.set_input_files(video_path)
        self.actions.wait_for_selector(locators["UPLOAD_BUTTON"])
        self.actions.click(locators["UPLOAD_BUTTON"])
        self.actions.wait_for_selector(locators["SAVE_AND_NEXT"])
        self.actions.click(locators["SAVE_AND_NEXT"])
        self.actions.wait_for_selector(locators["FINISH_UPLOAD"])
        self.actions.click(locators["FINISH_UPLOAD"])
        logger.info("Video upload completed")

    def send_screeners_to_publish(self):
        """Send screeners to publish."""
        self.actions.wait_for_selector(locators["SEND_SCREENERS"])
        self.actions.click(locators["SEND_SCREENERS"])
        self.actions.wait_for_selector(locators["GD_SEND_SCREENERS"])
        self.actions.click(locators["GD_SEND_SCREENERS"])
        self.actions.wait_for_selector(locators["SELECT_ALL"], timeout=120000)
        self.actions.click(locators["SELECT_ALL"])
        self.actions.wait_for_selector(locators["PROCEED_UPLOAD"])
        self.actions.click(locators["PROCEED_UPLOAD"])
        logger.info("Screeners sent to publish")

    def search_project_to_unpublish(self, Project_Name):
        """Search for a project to unpublish."""
        self.actions.wait_for_selector(locators["SEARCH_FOR_THE_PROJECT"])
        self.actions.fill(locators["SEARCH_FOR_THE_PROJECT"], Project_Name)
        self.actions.fill(locators["SEARCH_FOR_THE_PROJECT"], Project_Name)  # send_keys(Keys.ENTER)
        # Playwright fill doesn't send enter, so we press input
        self.page.keyboard.press("Enter")

    def navigate_to_project_to_unpublish(self, Project_Name):
        """Navigate to the project to unpublish."""
        self.actions.wait_for_selector(locators["PROJECT_SEARCH_RESULTS"][0], locators["PROJECT_SEARCH_RESULTS"][1].format(project_name=Project_Name))
        self.actions.click(locators["PROJECT_SEARCH_RESULTS"][0], locators["PROJECT_SEARCH_RESULTS"][1].format(project_name=Project_Name))
        self.actions.wait_for_selector(locators["EDIT_PROJECT"])
        self.actions.click(locators["EDIT_PROJECT"])
        self.actions.wait_for_selector(locators["DELETE_PROJECT"])
        self.actions.click(locators["DELETE_PROJECT"])
        self.actions.wait_for_selector(locators["CONTINUE_DELETE"])
        self.actions.click(locators["CONTINUE_DELETE"])

    def verify_deleted_project(self, Project_Name):
        """Verify a project was deleted."""
        self.actions.wait_for_selector(locators["SEARCH_FOR_THE_PROJECT"])
        self.actions.fill(locators["SEARCH_FOR_THE_PROJECT"], Project_Name)
        unpublished_project = self.actions.get_text(locators["NO_SEARCH_RESULTS"])
        return unpublished_project

    def upload_Image_2(self):
        """Upload a second image."""
        user_directory = os.getcwd()
        image_path = os.path.join(user_directory, 'AdminData', 'pexels-vlasceanu-1403653.jpg')
        self.actions.wait_for_selector(locators["MANAGE_FEATURED_IMAGES"], timeout=60000)
        self.actions.click(locators["MANAGE_FEATURED_IMAGES"])
        self.actions.upload_file(locators["IMAGE_UPLOAD"], image_path)
        self.actions.click(locators["CROP"])
        self.actions.wait_for_selector(locators["CAROUSAL_IMAGE_SAVE"], timeout=60000)
        self.actions.click(locators["CAROUSAL_IMAGE_SAVE"])
        logger.info("Second image uploaded")

    def delete_image_2(self, driver):
        """Delete an image (legacy method - kept for compatibility)."""
        self.actions.wait_for_selector(locators["MANAGE_FEATURED_IMAGES"], timeout=60000)
        self.actions.click(locators["MANAGE_FEATURED_IMAGES"])
        self.actions.wait_for_selector(locators["DELETE_CAROUSEL_IMAGE"], timeout=30000)
        self.actions.click(locators["DELETE_CAROUSEL_IMAGE"])
        self.actions.wait_for_selector(locators["DELETE_POPUP_HEADER"], timeout=10000)
        self.actions.wait_for_selector(locators["CONFIRM_DELETE_POPUP"], timeout=10000)
        self.actions.click(locators["CONFIRM_DELETE_POPUP"])
        self.actions.wait_for_selector(locators["CAROUSAL_IMAGE_SAVE"], timeout=60000)
        self.actions.click(locators["CAROUSAL_IMAGE_SAVE"])
        logger.info("Image deleted (legacy method)")

    def wait_for_trancoding(self, driver):
        """Wait for transcoding to complete."""
        # Playwright equivalent - check for transcoding progress element
        try:
            while self.page.wait_for_selector(locators["TRANSCODING_PROGRESS"], timeout=20000) == True:
                logger.info("Waiting for transcoding...")
                # Playwright doesn't have time.sleep, use page.wait_for_timeout
                self.page.wait_for_timeout(20000)
            logger.info("Transcoding completed")
        except Exception:
            logger.info("Transcoding check completed or element not found")

    def re_Arranging_Image(self, driver):
        """Re-arrange image (legacy method)."""
        self.actions.wait_for_selector(locators["MANAGE_FEATURED_IMAGES"], timeout=60000)
        self.actions.click(locators["MANAGE_FEATURED_IMAGES"])
        self.actions.wait_for_selector(locators["REORDER"])
        self.actions.click(locators["REORDER"])
        logger.info("Image re-arranged")

    def add_Swimlane(self, swimlanename, projectname):
        """Add a swimlane."""
        self.actions.wait_for_selector(locators["ADD_SWIMLANE"])
        self.actions.click(locators["ADD_SWIMLANE"])
        self.actions.wait_for_selector(locators["load_more_swimlane_btn"])
        self.actions.fill(locators["ENTER_SWIMLANE_NAME"], swimlanename)
        self.actions.wait_for_selector(locators["SEARCH_PROJECT"])
        self.actions.fill(locators["SEARCH_PROJECT"], projectname)
        self.actions.wait_for_selector(locators["SELECT_SEARCH_PROJECT"])
        self.actions.click(locators["SELECT_SEARCH_PROJECT"])
        self.actions.click(locators["SAVE_SWIMLANE_PROJECT"])
        logger.info(f"Swimlane added: {swimlanename}")

    def edit_swimlane(self, projectname, new_swimlane):
        """Edit a swimlane."""
        self.actions.wait_for_selector(locators["ADD_SWIMLANE"])
        self.actions.wait_for_selector(locators["load_more_swimlane_btn"])
        self.actions.fill(locators["ENTER_SWIMLANE_NAME"], new_swimlane)
        self.actions.wait_for_selector(locators["SEARCH_PROJECT"])
        self.actions.fill(locators["SEARCH_PROJECT"], projectname)
        self.actions.wait_for_selector(locators["SELECT_SEARCH_PROJECT"])
        self.actions.click(locators["SELECT_SEARCH_PROJECT"])
        self.actions.click(locators["SAVE_SWIMLANE_PROJECT"])
        logger.info(f"Swimlane edited to: {new_swimlane}")

    def rearranging_projects_within_swimlanes(self, projectname):
        """Rearrange projects within swimlanes."""
        # Find and click edit icons
        swimlanes = self.page.query_selector_all(".//button[contains(@id,'edit_swimlane')]")
        Last_Element = None
        for swimlane in swimlanes:
            preceding_text = swimlane.inner_text()
            if "SWIMLANE" in preceding_text:
                Last_Element = swimlane
        if Last_Element:
            Last_Element.click()
            logger.info("Swimlane selected for rearrangement")
        # Enter new swimlane name
        self.actions.wait_for_selector(locators["EDIT_SWIMLANE_PROJECT_NAME"])
        self.actions.fill(locators["EDIT_SWIMLANE_PROJECT_NAME"], projectname)
        logger.info(f"Project name set: {projectname}")

    def reorder_Swimlanes(self):
        """Reorder swimlanes."""
        Rearrange = self.page.query_selector(".//div[@title='Move Swimlane Up']")
        if Rearrange:
            self.page.evaluate("arguments[0].click();", Rearrange)
            logger.info("Swimlane moved up")
        Save_button = self.page.query_selector(".//button[@class='save-button']")
        if Save_button:
            self.page.evaluate("arguments[0].click();", Save_button)
            logger.info("Save button clicked")
        self.page.wait_for_timeout(10000)
        self.page.query_selector(".//button[@class='cancel-button']").click()
        logger.info("Cancel clicked")

    def remove_project_from_swimlane(self, projectname):
        """Remove a project from a swimlane."""
        self.actions.wait_for_selector(locators["ADD_SWIMLANE"], timeout=60000)
        self.actions.click(locators["ADD_SWIMLANE"])
        self.actions.wait_for_selector(locators["load_more_swimlane_btn"])
        self.actions.fill(locators["SEARCH_PROJECT"], projectname)
        self.actions.wait_for_selector(locators["SELECT_SEARCH_PROJECT"])
        self.actions.click(locators["SELECT_SEARCH_PROJECT"])
        self.actions.click(locators["SAVE_SWIMLANE_PROJECT"])
        logger.info(f"Project removed from swimlane: {projectname}")

    def delete_swimlane(self):
        """Delete a swimlane."""
        swimlanes = self.page.query_selector_all(".//button[contains(@class, 'delete-icon')]")
        First_Element = None
        for swimlane in swimlanes:
            preceding_text = swimlane.inner_text()
            if "SWIMLANE" in preceding_text:
                First_Element = swimlane
        if First_Element:
            First_Element.click()
            self.actions.wait_for_selector(locators["DELETE_SWIMLANE"], timeout=10000)
            self.actions.click(locators["DELETE_SWIMLANE"])
            logger.info("Swimlane deleted")

    def reorder_Swimlanes(self):
        """Reorder swimlanes (duplicate - keep one)."""
        Rearrange = self.page.query_selector(".//div[@title='Move Swimlane Up']")
        if Rearrange:
            self.page.evaluate("arguments[0].click();", Rearrange)
            logger.info("Swimlane moved up")
        Save_button = self.page.query_selector(".//button[@class='save-button']")
        if Save_button:
            self.page.evaluate("arguments[0].click();", Save_button)
            logger.info("Save button clicked")
        self.page.wait_for_timeout(10000)
        self.page.query_selector(".//button[@class='cancel-button']").click()
        logger.info("Cancel clicked")