"doc string"
import unittest
import json
from selenium import webdriver


class Tester(unittest.TestCase):
    "doc string"

    def setUp(self):
        "doc string"
        self.driver = webdriver.Chrome("D:\\Downloads\\"
                                       "Compressed\\Selenium-Test-master\\Files\\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.verification_errors = []
        self.accept_next_alert = True

    def test_er(self):
        "doc string"
        driver = self.driver
        total = {}
        with open("text.txt", "w") as txt_file:
            for result in range(10):
                driver.get("https://en.wikipedia.org/wiki/Software_metric")
                result = driver.execute_script("return window.performance.getEntries()")
                for current in result:
                    url = current["name"]
                    current_list = total.get(url, [])
                    current_list.append(current["duration"])
                    total[url] = current_list
                    txt_file.write(f"{current['name']}, {current['duration']}\n")

        with open("excel.csv", "w") as csv_file:
            for key, value in total.items():
                average = sum(value) / len(total)
                print("Sum : " + str(average))
                csv_file.write(f"{key}, {average}\n")

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(result, json_file, ensure_ascii=False, indent=4)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verification_errors)


if __name__ == "__main__":
    unittest.main()
