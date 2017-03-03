class Student(object):
    def ge_score(self):
        return self._score

    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('Score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0~100')
        self._score = value


D:\PythonProjects\learnPythonProject02\calssSetValueEx01.py