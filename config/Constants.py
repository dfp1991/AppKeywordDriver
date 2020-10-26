

class Contains:
    def __init__(self):
        self.Path_TestData = ".\\src\\dataEngine\\dataEngine.xlsx"
        self.File_TestData = "dataEngine.xlsx"
        self.objectMap_Path = ".\\src\\config\\objectMap.properties"

        #dataEngine.xlsx列值
        self.Col_TestCaseID = 0
        self.Col_TestScenarioID = 1
        self.Col_PageObject = 3
        self.Col_ActionKeyword = 4
        self.Col_RunMode = 2
        self.Col_Result = 3
        self.Col_TestStepResult = 6
        self.Col_DataSet = 5

        self.KEYWORD_FAIL = "FILE"
        self.KEYWORD_PASS = "PASS"

        #dataEngine.xlsx中sheet
        self.Sheet_TestSteps = "TestSteps"
        self.Sheet_TestCases = "TestCases"


