import pyautogui
import time
import json


class Edge:
    def __init__(self):
        self.current_user = None

        # get json data
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

        self.sooriya_searches = int(data["sooriya"])
        self.kamalantha_searches = int(data["kamalantha"])
        self.pcgatelanka_searches = int(data["pcgatelanka"])
        self.amadiravisha_searches = int(data["amadiraveesha"])

        self.seconds_between_searches = data["seconds_between_searches"]

        self.search_list = data["search_list"]
    
    def open_browser(self):
        pyautogui.hotkey('win', 'r')
        pyautogui.write("microsoft-edge:")
        pyautogui.press("enter")


    def open_browser_with_visuals(self):
        pyautogui.click("edge.png")


    def create_array(self, length):
        return list(map(str, self.search_list[0:length]))

    def search(self, time_delay, what_to_search):
        
        time.sleep(time_delay * 0.5)

        for i in what_to_search:
            pyautogui.hotkey('ctrl', 't')
            pyautogui.write(i)
            time.sleep(.2)
            pyautogui.press('enter')
            time.sleep(self.seconds_between_searches)

        time.sleep(time_delay * 2)



    def close_tabs(self, count_of_tabs):
        for i in range(count_of_tabs):
            pyautogui.hotkey('ctrl', 'f4')
            time.sleep(.5)


    def select_user(self, profile_image_name):
        time.sleep(.5)
        pyautogui.hotkey("ctrl", "shift", "m")
        time.sleep(2)
        location_search_result = pyautogui.locateOnScreen(profile_image_name, confidence=0.8)

        if location_search_result:
            self.current_user = profile_image_name
        else:
            print(f"couldnt find {profile_image_name}")
        pyautogui.click(location_search_result)
        time.sleep(3)

    def close_browser(self):
        pyautogui.hotkey('alt', 'f4')


    def see_if_is_on_screen(self, image):
        image_search_result = pyautogui.locateOnScreen(image, confidence=0.8)
        if image_search_result:
            return True
        else:
            return False

    def primary_procedure(self): # full searches

        self.open_browser()
        time.sleep(1)

        self.search(1, self.create_array(self.sooriya_searches))
        self.close_tabs(self.sooriya_searches)

        time.sleep(1)
        self.select_user("profile_images/kamalantha_profile.png")
        time.sleep(1)
        self.search(1, self.create_array(self.kamalantha_searches))
        self.close_browser()

        pyautogui.moveTo(500, 500)

        time.sleep(1)
        self.select_user("profile_images/pcgatelanka_profile.png")
        self.search(1, self.create_array(self.pcgatelanka_searches))
        self.close_browser()

        pyautogui.moveTo(500, 500)

        time.sleep(1)
        self.select_user("profile_images/amadiravisha_profile.png")
        self.search(1, self.create_array(self.amadiravisha_searches))
        self.close_browser()


edge = Edge()
edge.primary_procedure()